"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peng-six.vercel.app
Prompt: Develop a script to calculate potential transaction taxes for $PENG tokens, considering the 0/0 tax structure mentioned on the site.
Generated: DETERMINISTIC_4d7230532d1878dc
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal, InvalidOperation

# Configure decimal for financial calculations to avoid floating-point inaccuracies
decimal.getcontext().prec = 28

class TransactionTaxCalculator:
    """
    A class to calculate transaction taxes for $PENG tokens.
    As per the 0/0 tax structure mentioned, no taxes are applied.
    """

    def __init__(self):
        """
        Initialize the calculator.
        """
        self.tax_rate_buy = Decimal("0.0")  # Buy tax rate (0%)
        self.tax_rate_sell = Decimal("0.0")  # Sell tax rate (0%)

    def calculate_tax(self, transaction_type: str, amount: str) -> Decimal:
        """
        Calculate the tax for a given transaction type and amount.

        Args:
            transaction_type (str): Type of transaction ('buy' or 'sell').
            amount (str): Amount of tokens involved in the transaction as a string (to handle large values).

        Returns:
            Decimal: The calculated tax amount (always 0 for $PENG tokens).

        Raises:
            ValueError: If the transaction type is invalid or the amount is non-numeric.
        """
        try:
            # Validate the transaction type
            if transaction_type.lower() not in ["buy", "sell"]:
                raise ValueError("Invalid transaction type. Use 'buy' or 'sell'.")

            # Convert the amount to Decimal for precise calculations
            token_amount = Decimal(amount)
            if token_amount < 0:
                raise ValueError("Transaction amount cannot be negative.")

            # Determine tax rate based on transaction type
            tax_rate = self.tax_rate_buy if transaction_type.lower() == "buy" else self.tax_rate_sell

            # Calculate the tax (always 0 for $PENG tokens)
            tax_amount = token_amount * tax_rate
            
            return tax_amount
        except InvalidOperation:
            raise ValueError("Invalid amount. Please provide a numeric value.")
        except ValueError as ve:
            raise ve

# Entry point for running the script
if __name__ == "__main__":
    # Example usage
    try:
        calculator = TransactionTaxCalculator()
        
        # Simulate transactions
        print("=== $PENG Token Transaction Tax Calculator ===")
        transaction_type = input("Enter transaction type ('buy' or 'sell'): ").strip()
        amount = input("Enter transaction amount (e.g., 1000): ").strip()

        tax = calculator.calculate_tax(transaction_type, amount)
        print(f"Transaction type: {transaction_type}")
        print(f"Transaction amount: {amount}")
        print(f"Calculated tax: {tax} PENG (0/0 tax structure)")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
