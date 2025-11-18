"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Generate a Python script to convert currency values between EUR, GBP, and USD using historical exchange rates, similar to the examples provided on the website.
Generated: DETERMINISTIC_ab6cfca886125f16
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class CurrencyConverter:
    """
    A class to convert currency values between EUR, GBP, and USD using historical exchange rates.
    """

    def __init__(self):
        """
        Initializes the CurrencyConverter with hardcoded historical exchange rates.
        Note: Exchange rates are hypothetical and for demonstration purposes only.
        """
        self.exchange_rates = {
            'EUR': {'USD': 1.10, 'GBP': 0.88},
            'USD': {'EUR': 0.91, 'GBP': 0.80},
            'GBP': {'EUR': 1.14, 'USD': 1.25}
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Converts a given amount from one currency to another.

        Args:
            amount (float): The amount to convert.
            from_currency (str): The currency to convert from (e.g., 'EUR').
            to_currency (str): The currency to convert to (e.g., 'USD').

        Returns:
            float: The converted amount.

        Raises:
            ValueError: If an unsupported currency is provided.
        """
        if from_currency not in self.exchange_rates:
            raise ValueError(f"Unsupported currency: {from_currency}")

        if to_currency not in self.exchange_rates.get(from_currency, {}):
            raise ValueError(f"Unsupported currency: {to_currency}")

        exchange_rate = self.exchange_rates[from_currency][to_currency]
        return round(amount * exchange_rate, 2)


def main():
    """
    Main function to demonstrate currency conversion.
    """
    # Instantiate the CurrencyConverter
    converter = CurrencyConverter()

    print("Currency Converter: Convert between EUR, GBP, and USD")
    try:
        # User input for amount and currencies
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency to convert from (EUR, GBP, USD): ").upper()
        to_currency = input("Enter the currency to convert to (EUR, GBP, USD): ").upper()

        # Perform conversion
        converted_amount = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is approximately {converted_amount} {to_currency}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
