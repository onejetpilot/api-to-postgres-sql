import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = "postgresql+psycopg2://etl_user:etl_password@localhost:5434/exchange_rates_db"

def load_to_staging(df: pd.DataFrame) -> None:
    """
    Загружает очищенные данные в staging таблицу в PostgreSQL
    """

    engine = create_engine(DB_URL)

    with engine.begin() as connection:
        df.to_sql(
            name='stg_exchange_rates',
            con=connection,
            if_exists='append',
            index=False,
        )

def load_to_core() -> None:
    """
    Загружает данные из staging таблицы в core таблицу в PostgreSQL
    """

    engine = create_engine(DB_URL)

    query = text("""
        INSERT INTO exchange_rates (
            rate_date,
            base_currency,
            quote_currency,
            rate
        )
        SELECT DISTINCT ON (
            rate_date,
            base_currency,
            quote_currency
            )
            rate_date,
            base_currency,
            quote_currency,
            rate
        FROM stg_exchange_rates
        ON CONFLICT (rate_date, base_currency, quote_currency)
        DO UPDATE SET
            rate = EXCLUDED.rate
    """)

    with engine.begin() as connection:
        connection.execute(query)

if __name__ == '__main__':
    test_df = pd.DataFrame(
        [
            {
                'rate_date': '2024-01-01',
                'base_currency': 'EUR',
                'quote_currency': 'USD',
                'rate': 1.1064,
            }
        ]
    )

    load_to_staging(test_df)
    load_to_core()

    print('Данные успешно загружены в staging и core таблицы')