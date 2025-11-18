"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Generate a Python script to calculate Bitcoin value using a converter tool, referencing the Bitcoin calculator functionality described on Ark Capital Markets.
Generated: DETERMINISTIC_5ec16d9051c88514
Batch ID: 20250612_152249
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

class BitcoinConverter:
    """
    A class to handle the conversion of Bitcoin to various currencies.

    Attributes:
        api_url (str): The URL of the API to retrieve Bitcoin conversion rates.
    """

    def __init__(self):
        """
        Initializes the BitcoinConverter with the API URL.
        """
        self.api_url = "https://api.coingecko.com/api/v3/simple/price"

    def get_conversion_rate(self, currency):
        """
        Fetches the current Bitcoin conversion rate to the specified currency.

        Args:
            currency (str): The target currency to convert Bitcoin into.

        Returns:
            float: The conversion rate of 1 Bitcoin to the specified currency.

        Raises:
            ValueError: If the currency is invalid or not supported.
            ConnectionError: If there is an issue connecting to the API.
        """
        try:
            response = requests.get(self.api_url, params={'ids': 'bitcoin', 'vs_currencies': currency})
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            if currency in data['bitcoin']:
                return data['bitcoin'][currency]
            else:
                raise ValueError(f"Currency '{currency}' is not supported.")

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to the API: {e}")

    def convert_bitcoin_to_currency(self, amount_in_btc, currency):
        """
        Converts a given amount of Bitcoin to the specified currency.

        Args:
            amount_in_btc (float): The amount of Bitcoin to convert.
            currency (str): The target currency for conversion.

        Returns:
            float: The equivalent amount in the target currency.

        Raises:
            ValueError: If the amount is negative or conversion rate retrieval fails.
        """
        if amount_in_btc < 0:
            raise ValueError("Amount in Bitcoin must be a non-negative number.")

        conversion_rate = self.get_conversion_rate(currency)
        return amount_in_btc * conversion_rate


def main():
    """
    Main function to execute the Bitcoin conversion process.
    """
    converter = BitcoinConverter()

    # Example: Convert 1 Bitcoin to USD
    try:
        amount_in_btc = 1.0  # Amount of Bitcoin to convert
        target_currency = 'usd'  # Currency to convert to

        result = converter.convert_bitcoin_to_currency(amount_in_btc, target_currency)
        print(f"{amount_in_btc} Bitcoin is equal to {result} {target_currency.upper()}.")

    except (ValueError, ConnectionError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
