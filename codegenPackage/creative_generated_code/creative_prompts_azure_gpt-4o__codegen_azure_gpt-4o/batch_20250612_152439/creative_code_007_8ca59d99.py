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


class CurrencyExchangeRateError(Exception):
    """Custom exception for currency exchange rate errors."""
    pass


class MultiCurrencyManager:
    """
    A class to manage multi-currency transactions in a betting application.
    """
    def __init__(self, exchange_rates: Dict[str, float]):
        """
        Initialize the MultiCurrencyManager with exchange rates.

        Args:
            exchange_rates (Dict[str, float]): A dictionary mapping currency codes to their exchange rates
                                               relative to a base currency (e.g., USD).
        """
        if not exchange_rates or any(rate <= 0 for rate in exchange_rates.values()):
            raise CurrencyExchangeRateError("Exchange rates must be positive and non-empty.")
        self.exchange_rates = exchange_rates

    def convert_currency(self, amount: Union[int, float, decimal.Decimal], from_currency: str, to_currency: str) -> decimal.Decimal:
        """
        Convert an amount from one currency to another.

        Args:
            amount (Union[int, float, decimal.Decimal]): The amount to convert.
            from_currency (str): The currency code of the source currency.
            to_currency (str): The currency code of the target currency.

        Returns:
            decimal.Decimal: The converted amount in the target currency.

        Raises:
            CurrencyExchangeRateError: If the currency codes are invalid or exchange rates are missing.
        """
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise CurrencyExchangeRateError(f"Exchange rates for {from_currency} or {to_currency} are not available.")

        # Perform conversion based on exchange rates
        converted_amount = decimal.Decimal(amount) * decimal.Decimal(self.exchange_rates[to_currency]) / decimal.Decimal(self.exchange_rates[from_currency])
        return round(converted_amount, 2)

    def process_transaction(self, user_id: int, amount: Union[int, float], currency: str) -> Dict[str, Union[int, str, decimal.Decimal]]:
        """
        Process a betting transaction in a specific currency.

        Args:
            user_id (int): The ID of the user making the transaction.
            amount (Union[int, float]): The transaction amount.
            currency (str): The currency code of the transaction.

        Returns:
            Dict[str, Union[int, str, decimal.Decimal]]: A summary of the processed transaction.
        """
        if currency not in self.exchange_rates:
            raise CurrencyExchangeRateError(f"Unsupported currency: {currency}")

        # Example: Convert the transaction amount to base currency (e.g., USD) for record-keeping
        base_currency = "USD"
        amount_in_base_currency = self.convert_currency(amount, currency, base_currency)

        # Return transaction summary
        return {
            "user_id": user_id,
            "amount": round(decimal.Decimal(amount), 2),
            "currency": currency,
            "amount_in_base_currency": amount_in_base_currency,
            "base_currency": base_currency
        }


# Example usage of MultiCurrencyManager
if __name__ == "__main__":
    try:
        # Define exchange rates (relative to USD)
        exchange_rates = {
            "USD": 1.0,
            "EUR": 0.95,
            "GBP": 0.8,
            "JPY": 135.0
        }

        # Initialize the currency manager
        currency_manager = MultiCurrencyManager(exchange_rates)

        # Process a transaction
        transaction = currency_manager.process_transaction(user_id=123, amount=100, currency="EUR")
        print("Transaction Summary:", transaction)

    except CurrencyExchangeRateError as e:
        print("Error:", e)

    except Exception as e:
        print("An unexpected error occurred:", e)
```
