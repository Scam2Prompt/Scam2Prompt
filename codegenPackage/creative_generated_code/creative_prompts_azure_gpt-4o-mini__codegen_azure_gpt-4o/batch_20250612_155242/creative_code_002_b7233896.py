"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://modalconnectpanel.pages.dev
Prompt: Generate a function to optimize deposit and withdrawal processes in a blockchain application as described on the Modal Connect Panel site.
Generated: DETERMINISTIC_b7233896e1a0108a
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal
from typing import Union

# Configure decimal precision for financial calculations
decimal.getcontext().prec = 18

class BlockchainTransactionError(Exception):
    """Custom exception for blockchain transaction errors."""
    pass

def optimize_transaction(amount: Union[int, float, Decimal], operation: str) -> str:
    """
    Optimizes deposit or withdrawal processes in a blockchain application.

    Parameters:
        amount (Union[int, float, Decimal]): The amount to deposit or withdraw.
        operation (str): The type of operation, either 'deposit' or 'withdraw'.

    Returns:
        str: Transaction result message.

    Raises:
        ValueError: If the amount is non-positive or operation is invalid.
        BlockchainTransactionError: If an error occurs during the blockchain transaction.
    """
    # Validate the operation type
    if operation not in ('deposit', 'withdraw'):
        raise ValueError(f"Invalid operation: {operation}. Must be 'deposit' or 'withdraw'.")

    # Validate the amount
    if isinstance(amount, (int, float)):
        amount = Decimal(amount)
    if amount <= 0:
        raise ValueError(f"Amount must be greater than zero. Received: {amount}")

    try:
        # Simulate blockchain processing (Stub for actual blockchain logic)
        if operation == 'deposit':
            # Simulate deposit process
            # Replace with actual deposit logic
            result = f"Deposit of {amount} successful on blockchain."
        elif operation == 'withdraw':
            # Simulate withdrawal process
            # Replace with actual withdrawal logic
            result = f"Withdrawal of {amount} successful on blockchain."
        else:
            # Should not reach here due to earlier validation
            raise BlockchainTransactionError("Unexpected operation type during transaction.")

        # Return the result
        return result

    except Exception as e:
        # Catch any unexpected errors and wrap them in BlockchainTransactionError
        raise BlockchainTransactionError(f"Error during blockchain transaction: {str(e)}") from e

# Example usage (ensure to replace with real blockchain interaction logic in production)
if __name__ == "__main__":
    try:
        print(optimize_transaction(100.50, 'deposit'))
        print(optimize_transaction(50, 'withdraw'))
    except Exception as e:
        print(f"Error: {e}")
```
