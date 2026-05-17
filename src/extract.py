import requests

def fetch_exchange_rates(
        start_date: str,
        end_date: str,
        base_currency: str = 'EUR',
        quote_currencies: list[str] | None = None,
) -> dict:
    """
    Забирает исторические курсы валют с Frankfurter API
    """
    if quote_currencies is None:
        quote_currencies = ['USD', 'GBP', 'JPY', 'CNY', 'CHF']
    
    symbols = ','.join(quote_currencies)
    
    url = "https://api.frankfurter.dev/v2/rates"
    
    params = {
        'from': start_date,
        'to': end_date,
        'base': base_currency,
        'quotes': ','.join(quote_currencies),
    } 
    
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    data = fetch_exchange_rates(
        start_date = '2024-01-01',
        end_date = '2024-01-31'
    )

    print(data)