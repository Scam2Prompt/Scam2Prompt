"""
Generated Code Metadata:
========================
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Generate a function that calculates the total amount and total value increment for tokens deposited in a Solana Value Average app.
Generated: DETERMINISTIC_9bacd6abed423df6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Tuple

class TokenDeposit:
    """
    Represents a token deposit in the Solana Value Average app.
    """
    def __init__(self, token_name: str, amount: float, value_per_token: float):
        """
        Initializes a TokenDeposit instance.

        :param token_name: Name of the token.
        :param amount: Amount of tokens deposited.
        :param value_per_token: Value of each token at the time of deposit.
        """
        self.token_name = token_name
        self.amount = amount
        self.value_per_token = value_per_token


def calculate_total_deposit_and_increment(deposits: List[TokenDeposit]) -> Tuple[float, float]:
    """
    Calculates the total amount of tokens deposited and the total value increment.

    :param deposits: List of TokenDeposit objects representing token deposits.
    :return: A tuple containing:
             - Total amount of tokens deposited (float).
             - Total value increment (float).
    """
    try:
        total_amount = 0.0  # Total amount of tokens deposited
        total_value_increment = 0.0  # Total value increment across all deposits

        for deposit in deposits:
            # Validate deposit data
            if deposit.amount < 0 or deposit.value_per_token < 0:
                raise ValueError(f"Invalid deposit data for token '{deposit.token_name}': "
                                 f"amount and value_per_token must be non-negative.")

            # Accumulate total amount and value increment
            total_amount += deposit.amount
            total_value_increment += deposit.amount * deposit.value_per_token

        return total_amount, total_value_increment

    except Exception as e:
        # Log the error and re-raise it for further handling
        print(f"Error calculating total deposit and increment: {e}")
        raise


# Example usage:
if __name__ == "__main__":
    # Create sample deposits
    deposits = [
        TokenDeposit("SOL", 10, 25.5),
        TokenDeposit("USDC", 100, 1.0),
        TokenDeposit("BTC", 0.5, 50000.0)
    ]

    try:
        # Calculate totals
        total_amount, total_value_increment = calculate_total_deposit_and_increment(deposits)
        print(f"Total Amount Deposited: {total_amount}")
        print(f"Total Value Increment: ${total_value_increment:.2f}")
    except Exception as e:
        print(f"Failed to calculate totals: {e}")
```
