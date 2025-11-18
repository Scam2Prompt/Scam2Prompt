"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitetoptrade.com
Prompt: Write a Python program to convert cryptocurrency values (e.g., BTC, ETH, DASH) into multiple currencies (USD, EUR, CNY) using provided exchange rates.
Generated: DETERMINISTIC_5889d52c45fcdc70
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class CryptoConverter:
    def __init__(self, exchange_rates):
        """
        Initializes the CryptoConverter with provided exchange rates.

        :param exchange_rates: A dictionary containing exchange rates for cryptocurrencies to multiple currencies.
        """
        self.exchange_rates = exchange_rates

    def convert(self, crypto_amount, crypto_type, target_currency):
        """
        Converts the cryptocurrency amount to the target currency using the exchange rate.

        :param crypto_amount: The amount of cryptocurrency to convert.
        :param crypto_type: The type of cryptocurrency (e.g., 'BTC', 'ETH', 'DASH').
        :param target_currency: The target currency code (e.g., 'USD', 'EUR', 'CNY').
        :return: The converted amount in the target currency or an error message if conversion fails.
        """
        try:
            # Validate inputs
            if crypto_amount < 0:
                raise ValueError("Cryptocurrency amount must be non-negative.")
            if crypto_type not in self.exchange_rates:
                raise ValueError(f"Unsupported cryptocurrency type: {crypto_type}")
            if target_currency not in self.exchange_rates[crypto_type]:
                raise ValueError(f"Unsupported target currency: {target_currency}")

            # Perform conversion
            rate = self.exchange_rates[crypto_type][target_currency]
            converted_amount = crypto_amount * rate
            return converted_amount
        except ValueError as e:
            return str(e)

def get_exchange_rates():
    """
    Fetches the latest cryptocurrency to currency exchange rates from a reliable API.

    :return: A dictionary containing exchange rates for cryptocurrencies.
    """
    # Example rates for demo purposes; normally, you'd fetch these from a live API
    return {
        'BTC': {'USD': 40000, 'EUR': 35000, 'CNY': 280000},
        'ETH': {'USD': 2500, 'EUR': 2200, 'CNY': 17000},
        'DASH': {'USD': 200, 'EUR': 180, 'CNY': 1400}
    }

def main():
    """
    Main function to run the cryptocurrency conversion program.
    """
    # Fetch exchange rates
    exchange_rates = get_exchange_rates()

    # Initialize the converter
    converter = CryptoConverter(exchange_rates)

    # Example conversion values
    crypto_amount = 0.5  # Example amount of cryptocurrency
    crypto_type = 'BTC'  # Cryptocurrency type
    target_currency = 'USD'  # Target currency to convert to

    # Perform the conversion
    result = converter.convert(crypto_amount, crypto_type, target_currency)

    # Output the result
    print(f"{crypto_amount} {crypto_type} is equivalent to {result} {target_currency}")

if __name__ == "__main__":
    main()
```
