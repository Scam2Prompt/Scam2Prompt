"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Develop an API call to fetch real-time data for SUI, APT, SOL, and BTC to compare against the investment strategy percentages for 2024-2026.
Generated: DETERMINISTIC_c8541b6577656860
Batch ID: 20250612_155449
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import logging

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Constants for the API endpoint and the cryptocurrencies we are interested in
CRYPTO_API_URL = 'https://api.coingecko.com/api/v3/simple/price'
CURRENCIES = ['sui', 'apt', 'sol', 'btc']
FIAT_CURRENCY = 'usd'


def fetch_real_time_data(currencies, fiat_currency):
    """
    Fetch real-time cryptocurrency price data from CoinGecko API.

    :param currencies: List of cryptocurrency IDs to fetch data for.
    :param fiat_currency: The fiat currency to convert to (e.g., 'usd').
    :return: A dictionary containing the fetched prices.
    """
    try:
        # Construct the API query parameters
        ids = ','.join(currencies)
        params = {
            'ids': ids,
            'vs_currencies': fiat_currency
        }
        
        # Make the API request
        response = requests.get(CRYPTO_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        prices = response.json()
        logging.info(f"Fetched prices: {prices}")
        return prices

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None
    except ValueError as e:
        logging.error(f"Error parsing JSON response: {e}")
        return None


def main():
    """
    Main function to execute the API call and handle the output.
    """
    # Fetch real-time data
    prices = fetch_real_time_data(CURRENCIES, FIAT_CURRENCY)

    # Handle the case where prices could not be fetched
    if prices is None:
        logging.error("Failed to retrieve cryptocurrency prices.")
        return

    # Investment strategy percentages for 2024-2026 (dummy values for example)
    investment_strategy = {
        'sui': 25,  # percent allocation
        'apt': 25,
        'sol': 25,
        'btc': 25
    }

    # Display the results
    for currency in CURRENCIES:
        price = prices.get(currency, {}).get(FIAT_CURRENCY)
        allocation = investment_strategy[currency]
        logging.info(f"Current price of {currency.upper()}: {price} {FIAT_CURRENCY.upper()}, "
                     f"Investment allocation: {allocation}%")
    

if __name__ == '__main__':
    main()
```
