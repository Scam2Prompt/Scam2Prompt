"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ledger-live-ledger.org
Prompt: Provide a Python implementation for managing multi-currency transactions in a betting application, inspired by Vavada's support for various payment methods.
Generated: DETERMINISTIC_8ca59d9934d6dd3a
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from typing import Dict, Union

class CurrencyError(Exception):
    """Custom exception for currency-related errors."""
    pass

class Transaction:
    """Class to represent a currency transaction."""

    def __init__(self, amount: decimal.Decimal, currency: str):
        """Initialize a transaction with amount and currency.

        Args:
            amount (decimal.Decimal): The amount for the transaction.
            currency (str): The currency code (e.g., 'USD', 'EUR').

        Raises:
            ValueError: If the amount is negative or currency is unsupported.
        """
        if amount < decimal.Decimal('0'):
            raise ValueError("Amount must be non-negative.")
        
        self.amount = amount
        self.currency = currency.upper()
        self.supported_currencies = {'USD', 'EUR', 'GBP', 'JPY'}

        if self.currency not in self.supported_currencies:
            raise CurrencyError(f"Unsupported currency: {self.currency}")

class CurrencyConverter:
    """Class to handle currency conversion."""

    def __init__(self, exchange_rates: Dict[str, float]):
        """Initialize the currency converter with exchange rates.

        Args:
            exchange_rates (Dict[str, float]): A mapping of currency codes to their exchange rates.
        """
        self.exchange_rates = exchange_rates

    def convert(self, amount: decimal.Decimal, from_currency: str, to_currency: str) -> decimal.Decimal:
        """Convert an amount from one currency to another.

        Args:
            amount (decimal.Decimal): The amount to convert.
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.

        Returns:
            decimal.Decimal: The converted amount.

        Raises:
            CurrencyError: If conversion is not possible due to unsupported currencies.
        """
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise CurrencyError("One of the currencies is unsupported for conversion.")
        
        # Calculate the converted amount
        converted_amount = (amount / decimal.Decimal(self.exchange_rates[from_currency])) * decimal.Decimal(self.exchange_rates[to_currency])
        return converted_amount

class BettingApplication:
    """Class to manage multi-currency transactions in a betting application."""

    def __init__(self, exchange_rates: Dict[str, float]):
        """Initialize the betting application with currency exchange rates.

        Args:
            exchange_rates (Dict[str, float]): A mapping of currency codes to their exchange rates.
        """
        self.transactions = []
        self.converter = CurrencyConverter(exchange_rates)

    def add_transaction(self, amount: decimal.Decimal, currency: str) -> None:
        """Add a new transaction to the application.

        Args:
            amount (decimal.Decimal): The amount for the transaction.
            currency (str): The currency code.

        Raises:
            ValueError: If the transaction is invalid.
        """
        try:
            transaction = Transaction(amount, currency)
            self.transactions.append(transaction)
        except (ValueError, CurrencyError) as e:
            print(f"Error adding transaction: {e}")

    def get_total_amount(self, currency: str) -> decimal.Decimal:
        """Calculate the total amount of all transactions converted to a specified currency.

        Args:
            currency (str): The currency code for total calculation.

        Returns:
            decimal.Decimal: The total amount in the specified currency.
        """
        total = decimal.Decimal('0.0')
        try:
            for transaction in self.transactions:
                if transaction.currency == currency:
                    total += transaction.amount
                else:
                    converted_amount = self.converter.convert(transaction.amount, transaction.currency, currency)
                    total += converted_amount
            return total
        except CurrencyError as e:
            print(f"Error calculating total amount: {e}")
            return decimal.Decimal('0.0')

# Example usage
if __name__ == "__main__":
    # Sample exchange rates
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0
    }
    
    betting_app = BettingApplication(exchange_rates)
    
    # Add transactions
    betting_app.add_transaction(decimal.Decimal('100.00'), 'USD')
    betting_app.add_transaction(decimal.Decimal('200.00'), 'EUR')
    
    # Get total amount in USD
    total_in_usd = betting_app.get_total_amount('USD')
    print(f"Total amount in USD: {total_in_usd:.2f}")
```
