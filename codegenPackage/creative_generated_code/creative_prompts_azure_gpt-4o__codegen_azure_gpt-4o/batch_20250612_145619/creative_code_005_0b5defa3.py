"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfor.com
Prompt: Develop a function to calculate fees for transactions on the TonFOR platform, considering the pool type and token denomination.
Generated: DETERMINISTIC_0b5defa3f629b3a7
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from typing import Union


class TransactionFeeCalculator:
    """
    A class to calculate fees for transactions on the TonFOR platform.
    """

    # Define constants for fee rates based on pool type
    FEE_RATES = {
        "stable": 0.001,  # Stable pools have a 0.1% fee
        "volatile": 0.003,  # Volatile pools have a 0.3% fee
    }

    def __init__(self):
        """
        Initialize TransactionFeeCalculator instance.
        """
        pass

    @staticmethod
    def calculate_fee(transaction_amount: float, pool_type: str, token_denomination: str) -> Union[float, str]:
        """
        Calculate the transaction fee based on the pool type and token denomination.

        Args:
            transaction_amount (float): The amount of the transaction.
            pool_type (str): The pool type ('stable' or 'volatile').
            token_denomination (str): The token denomination (e.g., 'TON', 'USDT').

        Returns:
            Union[float, str]: The calculated fee or an error message if inputs are invalid.
        """

        # Validate inputs
        if transaction_amount <= 0:
            return "Error: Transaction amount must be greater than zero."
        if pool_type not in TransactionFeeCalculator.FEE_RATES:
            return f"Error: Invalid pool type. Must be one of {list(TransactionFeeCalculator.FEE_RATES.keys())}."
        if not token_denomination or not isinstance(token_denomination, str):
            return "Error: Invalid token denomination. Must be a non-empty string."

        # Get the fee rate for the given pool type
        fee_rate = TransactionFeeCalculator.FEE_RATES[pool_type]

        # Calculate the fee
        fee = transaction_amount * fee_rate

        # Return the calculated fee
        return fee


# Example usage (uncomment to test)
# calculator = TransactionFeeCalculator()
# print(calculator.calculate_fee(1000, 'stable', 'TON'))  # Should return 1.0
# print(calculator.calculate_fee(1000, 'volatile', 'USDT'))  # Should return 3.0
# print(calculator.calculate_fee(-500, 'stable', 'TON'))  # Should return an error message
```
