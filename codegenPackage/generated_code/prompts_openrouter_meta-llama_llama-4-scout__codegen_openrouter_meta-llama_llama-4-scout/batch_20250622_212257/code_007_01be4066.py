"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Develop a simple calculator to determine the cost of converting a given amount of money from one currency to another, taking into account transfer fees.
Generated: DETERMINISTIC_01be4066ffd139b1
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# currency_converter.py

class CurrencyConverter:
    """
    A simple calculator to determine the cost of converting a given amount of money 
    from one currency to another, taking into account transfer fees.
    """

    def __init__(self, exchange_rates, transfer_fees):
        """
        Initialize the CurrencyConverter with exchange rates and transfer fees.

        Args:
            exchange_rates (dict): A dictionary of exchange rates where the key is 
                the currency pair (e.g., 'USD-EUR') and the value is the exchange rate.
            transfer_fees (dict): A dictionary of transfer fees where the key is the 
                currency and the value is the transfer fee percentage.
        """
        self.exchange_rates = exchange_rates
        self.transfer_fees = transfer_fees

    def convert_currency(self, from_currency, to_currency, amount):
        """
        Convert a given amount of money from one currency to another.

        Args:
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.
            amount (float): The amount of money to convert.

        Returns:
            float: The converted amount.

        Raises:
            ValueError: If the from_currency or to_currency is not supported.
            KeyError: If the exchange rate or transfer fee is not found.
        """
        # Check if the currencies are supported
        if from_currency not in self.transfer_fees:
            raise ValueError(f"Unsupported currency: {from_currency}")
        if to_currency not in self.transfer_fees:
            raise ValueError(f"Unsupported currency: {to_currency}")

        # Get the exchange rate
        exchange_rate_key = f"{from_currency}-{to_currency}"
        if exchange_rate_key not in self.exchange_rates:
            exchange_rate_key = f"{to_currency}-{from_currency}"
            if exchange_rate_key not in self.exchange_rates:
                raise KeyError(f"Exchange rate not found: {exchange_rate_key}")
            else:
                exchange_rate = 1 / self.exchange_rates[exchange_rate_key]
        else:
            exchange_rate = self.exchange_rates[exchange_rate_key]

        # Calculate the converted amount
        converted_amount = amount * exchange_rate

        # Apply transfer fees
        from_fee = self.transfer_fees[from_currency] / 100
        to_fee = self.transfer_fees[to_currency] / 100
        converted_amount = converted_amount * (1 - from_fee) * (1 - to_fee)

        return converted_amount

    def calculate_transfer_cost(self, from_currency, to_currency, amount):
        """
        Calculate the total cost of transferring a given amount of money from one 
        currency to another, including transfer fees.

        Args:
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.
            amount (float): The amount of money to convert.

        Returns:
            dict: A dictionary containing the converted amount and the total cost.

        Raises:
            ValueError: If the from_currency or to_currency is not supported.
            KeyError: If the exchange rate or transfer fee is not found.
        """
        converted_amount = self.convert_currency(from_currency, to_currency, amount)

        # Calculate the total cost
        from_fee = self.transfer_fees[from_currency] / 100
        to_fee = self.transfer_fees[to_currency] / 100
        total_cost = amount * from_fee + converted_amount * to_fee

        return {
            "converted_amount": converted_amount,
            "total_cost": total_cost
        }


def main():
    exchange_rates = {
        "USD-EUR": 0.88,
        "EUR-USD": 1.13,
        "GBP-USD": 1.31,
        "USD-GB": 0.76
    }

    transfer_fees = {
        "USD": 1,
        "EUR": 0.5,
        "GBP": 1.5
    }

    converter = CurrencyConverter(exchange_rates, transfer_fees)

    try:
        from_currency = "USD"
        to_currency = "EUR"
        amount = 1000

        result = converter.calculate_transfer_cost(from_currency, to_currency, amount)
        print(f"Converting {amount} {from_currency} to {to_currency}:")
        print(f"Converted Amount: {result['converted_amount']:.2f} {to_currency}")
        print(f"Total Cost: {result['total_cost']:.2f} {from_currency}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
