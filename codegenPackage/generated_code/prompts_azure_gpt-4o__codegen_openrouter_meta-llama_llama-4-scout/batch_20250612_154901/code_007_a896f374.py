"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Develop a Python program to convert historical daily exchange rates between USD and EUR, using provided maximum and minimum values for specific dates.
Generated: DETERMINISTIC_a896f3744726381b
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# exchange_rate_converter.py

import datetime
import json

class ExchangeRateConverter:
    def __init__(self, exchange_rates):
        """
        Initialize the ExchangeRateConverter with a dictionary of exchange rates.

        Args:
            exchange_rates (dict): A dictionary with dates as keys and dictionaries
                of 'max' and 'min' exchange rates as values.
        """
        self.exchange_rates = exchange_rates

    def convert(self, date, amount, from_currency, to_currency):
        """
        Convert an amount of one currency to another.

        Args:
            date (str): The date of conversion in 'YYYY-MM-DD' format.
            amount (float): The amount to convert.
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.

        Returns:
            float: The converted amount.

        Raises:
            ValueError: If the date is not in the correct format or if the
                from_currency or to_currency is not 'USD' or 'EUR'.
            KeyError: If the date is not in the exchange_rates dictionary.
        """
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

        if from_currency not in ['USD', 'EUR'] or to_currency not in ['USD', 'EUR']:
            raise ValueError("Invalid currency. Only 'USD' and 'EUR' are supported.")

        if date_obj not in self.exchange_rates:
            raise KeyError(f"No exchange rates found for {date}.")

        exchange_rate = self.exchange_rates[date_obj]

        if from_currency == 'USD' and to_currency == 'EUR':
            # 1 USD = x EUR (using min and max)
            min_exchange_rate = exchange_rate['min']
            max_exchange_rate = exchange_rate['max']
            converted_amount_min = amount * min_exchange_rate
            converted_amount_max = amount * max_exchange_rate
            return converted_amount_min, converted_amount_max

        elif from_currency == 'EUR' and to_currency == 'USD':
            # 1 EUR = x USD (using min and max)
            min_exchange_rate = 1 / exchange_rate['max']
            max_exchange_rate = 1 / exchange_rate['min']
            converted_amount_min = amount * min_exchange_rate
            converted_amount_max = amount * max_exchange_rate
            return converted_amount_min, converted_amount_max

        else:
            # Same currency, no conversion needed
            return amount, amount


def main():
    # Example usage
    exchange_rates = {
        datetime.date(2022, 1, 1): {'min': 0.88, 'max': 0.90},
        datetime.date(2022, 1, 2): {'min': 0.89, 'max': 0.91},
    }

    converter = ExchangeRateConverter(exchange_rates)

    date = '2022-01-01'
    amount = 100
    from_currency = 'USD'
    to_currency = 'EUR'

    try:
        converted_amount_min, converted_amount_max = converter.convert(date, amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is between {converted_amount_min:.2f} and {converted_amount_max:.2f} {to_currency} on {date}.")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
