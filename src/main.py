from extract import fetch_exchange_rates
from transform import transform_exchange_rates
from load import load_to_staging, load_to_core
from datetime import date

def main() -> None:

    end_date = date.today().isoformat()
    
    raw_data = fetch_exchange_rates(
        start_date='2026-01-01',
        end_date=end_date,
        base_currency='RUB',
        quote_currencies=['USD', 'GBP', 'JPY', 'CNY', 'CHF']
    )

    df = transform_exchange_rates(raw_data)
    load_to_staging(df)
    load_to_core()

    print('ETL процесс успешно завершён. Всего записей загружено:', len(df))

if __name__ == "__main__":
    main()