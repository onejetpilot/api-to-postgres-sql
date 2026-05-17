from extract import fetch_exchange_rates
from transform import transform_exchange_rates
from load import load_to_staging, load_to_core

def main() -> None:
    raw_data = fetch_exchange_rates(
        start_date='2024-01-01',
        end_date='2024-01-31',
        base_currency='EUR',
        quote_currencies=['USD', 'GBP', 'JPY', 'CNY', 'CHF']
    )

    df = transform_exchange_rates(raw_data)
    load_to_staging(df)
    load_to_core()

    print('ETL процесс успешно завершён. Всего записей загружено:', len(df))

if __name__ == "__main__":
    main()