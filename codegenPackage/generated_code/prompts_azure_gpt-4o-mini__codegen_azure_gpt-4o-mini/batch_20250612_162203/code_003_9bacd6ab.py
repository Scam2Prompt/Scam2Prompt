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
    def __init__(self, amount: float, value_increment: float):
        """
        Initialize a TokenDeposit instance.

        :param amount: The amount of tokens deposited.
        :param value_increment: The value increment of the tokens.
        """
        self.amount = amount
        self.value_increment = value_increment

def calculate_total(deposits: List[TokenDeposit]) -> Tuple[float, float]:
    """
    Calculate the total amount and total value increment for a list of token deposits.

    :param deposits: A list of TokenDeposit instances.
    :return: A tuple containing the total amount and total value increment.
    """
    total_amount = 0.0
    total_value_increment = 0.0

    for deposit in deposits:
        if deposit.amount < 0 or deposit.value_increment < 0:
            raise ValueError("Token amount and value increment must be non-negative.")

        total_amount += deposit.amount
        total_value_increment += deposit.value_increment

    return total_amount, total_value_increment

# Example usage
if __name__ == "__main__":
    try:
        deposits = [
            TokenDeposit(amount=10.0, value_increment=0.5),
            TokenDeposit(amount=20.0, value_increment=1.0),
            TokenDeposit(amount=5.0, value_increment=0.2)
        ]

        total_amount, total_value_increment = calculate_total(deposits)
        print(f"Total Amount: {total_amount}, Total Value Increment: {total_value_increment}")

    except ValueError as e:
        print(f"Error: {e}")
```
