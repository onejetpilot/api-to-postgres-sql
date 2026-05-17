import pandas as pd

def transform_exchange_rates(raw_data: list[dict]) -> pd.DataFrame:
    """
    Преобразует данные о курсах валют в DataFrame
    """
    df = pd.DataFrame(raw_data)

    df = df.rename(
        columns={
            'date': 'rate_date',
            'base': 'base_currency',
            'quote': 'quote_currency',
        }
    )

    df['rate_date'] = pd.to_datetime(df['rate_date']).dt.date
    df['base_currency'] = df['base_currency'].astype(str)
    df['quote_currency'] = df['quote_currency'].astype(str)
    df['rate'] = df['rate'].astype(float)

    df = df.drop_duplicates(subset=['rate_date', 'base_currency', 'quote_currency'])

    df = df.sort_values(by=['rate_date', 'base_currency', 'quote_currency']).reset_index(drop=True)

    return df

if __name__ == "__main__":
    test_data = [
        {"date": "2024-01-01", "base": "EUR", "quote": "CHF", "rate": 0.92743},
        {"date": "2024-01-01", "base": "EUR", "quote": "CHF", "rate": 0.92743},
        {"date": "2024-01-01", "base": "EUR", "quote": "USD", "rate": 1.1064},
    ]

    result = transform_exchange_rates(test_data)

    print(result)
    print(result.dtypes)
      