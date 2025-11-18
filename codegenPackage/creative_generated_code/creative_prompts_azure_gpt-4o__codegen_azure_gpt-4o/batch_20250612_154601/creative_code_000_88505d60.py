"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltetradingsacademy.com
Prompt: Write Python code to integrate a currency exchange API that provides real-time exchange rates, similar to the "LIVE EXCHANGE RATES" feature described on the Grand Chase website.
Generated: DETERMINISTIC_88505d60633e6405
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangeratesapi.io": {
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
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

class CurrencyExchangeAPI:
    """
    A class to interact with a currency exchange API to fetch real-time exchange rates.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initializes the CurrencyExchangeAPI instance.

        :param api_key: Your API key for authentication.
        :param base_url: The base URL of the currency exchange API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_exchange_rate(self, base_currency: str, target_currency: str) -> float:
        """
        Fetches the real-time exchange rate between two currencies.

        :param base_currency: The base currency (e.g., 'USD').
        :param target_currency: The target currency (e.g., 'EUR').
        :return: The exchange rate as a float.
        :raises: Exception if the API call fails or returns an error.
        """
        endpoint = f"{self.base_url}/latest"
        params = {
            'access_key': self.api_key,
            'base': base_currency,
            'symbols': target_currency
        }

        try:
            logging.info(f"Requesting exchange rate: {base_currency} -> {target_currency}")
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise HTTP errors if any

            data = response.json()

            # Check for API-specific errors in response data
            if 'error' in data:
                raise Exception(f"API Error: {data['error']['info']}")

            exchange_rate = data['rates'].get(target_currency)
            if exchange_rate is None:
                raise Exception("Failed to fetch the exchange rate for the specified currencies.")

            logging.info(f"Exchange rate {base_currency} -> {target_currency}: {exchange_rate}")
            return exchange_rate

        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request Error: {e}")
            raise Exception("Failed to fetch exchange rates due to a network error.") from e
        except Exception as e:
            logging.error(f"Error: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the CurrencyExchangeAPI class
    try:
        # Replace with your API key and base URL
        API_KEY = "your_api_key_here"
        BASE_URL = "https://api.exchangeratesapi.io"

        api = CurrencyExchangeAPI(api_key=API_KEY, base_url=BASE_URL)

        # Specify the currencies for exchange rate lookup
        BASE_CURRENCY = "USD"
        TARGET_CURRENCY = "EUR"

        # Fetch and print the exchange rate
        exchange_rate = api.get_exchange_rate(BASE_CURRENCY, TARGET_CURRENCY)
        print(f"Exchange Rate ({BASE_CURRENCY} -> {TARGET_CURRENCY}): {exchange_rate}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
