"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simpleswap.my
Prompt: Generate code to calculate the exchange rate between BTC and EOS using a cryptocurrency API, inspired by SimpleSwap's service.
Generated: DETERMINISTIC_c6f8cd17ebd83dcd
Batch ID: 20250612_154913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate-api.com/v4/latest/": {
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

class CryptoExchangeRate:
    def __init__(self, base_currency: str, target_currency: str):
        """
        Initialize the CryptoExchangeRate instance with base and target currencies.

        :param base_currency: The currency to convert from (e.g., 'BTC').
        :param target_currency: The currency to convert to (e.g., 'EOS').
        """
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"

    def fetch_exchange_rate(self) -> float:
        """
        Fetch the exchange rate from the API and return it.

        :return: The exchange rate from base_currency to target_currency.
        :raises ValueError: If the API response is invalid or contains no rates.
        :raises ConnectionError: If the API request fails.
        """
        try:
            response = requests.get(f"{self.api_url}{self.base_currency}")
            response.raise_for_status()  # Raise an error for bad responses
            
            data = response.json()

            # Check if the rates contain the target currency
            if self.target_currency not in data['rates']:
                raise ValueError(f"Currency '{self.target_currency}' not found in the rates.")

            return data['rates'][self.target_currency]

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to the API: {e}")

        except ValueError as ve:
            raise ve  # Re-raise ValueError for caller to handle

    def display_exchange_rate(self):
        """
        Fetch and display the exchange rate between base_currency and target_currency.
        """
        try:
            rate = self.fetch_exchange_rate()
            print(f"Exchange rate: 1 {self.base_currency} = {rate} {self.target_currency}")
        except (ValueError, ConnectionError) as e:
            print(f"Error fetching exchange rate: {e}")


if __name__ == "__main__":
    # Example usage
    exchange_rate_calculator = CryptoExchangeRate(base_currency='BTC', target_currency='EOS')
    exchange_rate_calculator.display_exchange_rate()
```
