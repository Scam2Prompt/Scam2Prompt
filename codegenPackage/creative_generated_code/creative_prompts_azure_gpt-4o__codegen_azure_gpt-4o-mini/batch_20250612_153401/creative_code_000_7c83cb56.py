"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Write Python code to calculate currency conversion rates, referencing the accounting services provided by Lund & Kieck and their focus on accurate financial planning.
Generated: DETERMINISTIC_7c83cb56af7fd8f0
Batch ID: 20250612_153401
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

class CurrencyConverter:
    """
    A class to convert currencies using an external API for exchange rates.
    """

    def __init__(self, api_key: str):
        """
        Initializes the CurrencyConverter with the provided API key.

        :param api_key: Your API key for the exchange rates service
        """
        self.api_key = api_key
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"

    def get_exchange_rate(self, base_currency: str, target_currency: str) -> float:
        """
        Fetches the exchange rate for the specified currencies.

        :param base_currency: The currency to convert from
        :param target_currency: The currency to convert to
        :return: The exchange rate
        :raises ValueError: If the base or target currency is invalid
        :raises requests.HTTPError: For any HTTP error during the API call
        """
        try:
            response = requests.get(f"{self.api_url}{base_currency}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if target_currency not in data['rates']:
                raise ValueError(f"Target currency '{target_currency}' is not valid.")

            return data['rates'][target_currency]

        except requests.HTTPError as http_err:
            raise RuntimeError(f"HTTP error occurred: {http_err}")  # For debugging
        except Exception as err:
            raise RuntimeError(f"An error occurred: {err}")  # For debugging

    def convert_currency(self, amount: float, base_currency: str, target_currency: str) -> float:
        """
        Converts an amount from base_currency to target_currency.

        :param amount: The amount in base currency to be converted
        :param base_currency: The currency to convert from
        :param target_currency: The currency to convert to
        :return: The converted amount in target currency
        :raises ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        exchange_rate = self.get_exchange_rate(base_currency, target_currency)
        converted_amount = amount * exchange_rate
        return round(converted_amount, 2)  # Round to 2 decimal places

if __name__ == "__main__":
    # Example usage
    try:
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        converter = CurrencyConverter(api_key)

        # Convert 100 USD to EUR
        amount = 100
        base_currency = "USD"
        target_currency = "EUR"
        converted_amount = converter.convert_currency(amount, base_currency, target_currency)

        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}.")

    except Exception as e:
        print(f"Error: {e}")
```
