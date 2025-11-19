"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Generate a function that calculates the total amount and total value increment for tokens deposited in a Solana Value Average app.
Generated: DETERMINISTIC_9bacd6abed423df6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class TokenDepositCalculator:
    """
    A class to calculate the total amount and total value increment for tokens deposited in a Solana Value Average app.
    """

    def __init__(self):
        """
        Initialize the calculator with empty lists for amounts and values.
        """
        self.amounts = []
        self.values = []

    def add_deposit(self, amount: float, current_value: float):
        """
        Adds a new deposit with the specified amount and current value.

        Args:
            amount (float): The amount of tokens deposited.
            current_value (float): The current value of the tokens at the time of deposit.
        
        Raises:
            ValueError: If amount or current_value is negative.
        """
        if amount < 0 or current_value < 0:
            raise ValueError("Amount and current value must be non-negative.")
        
        self.amounts.append(amount)
        self.values.append(current_value)

    def calculate_total(self) -> float:
        """
        Calculates the total amount of tokens deposited.

        Returns:
            float: The total amount of tokens.
        """
        total_amount = sum(self.amounts)
        return total_amount

    def calculate_total_value_increment(self) -> float:
        """
        Calculates the total value increment for all deposited tokens.

        Returns:
            float: The total value increment of the tokens.
        """
        if not self.amounts or not self.values:
            return 0.0

        total_value_increment = np.sum(np.array(self.values) * np.array(self.amounts))
        return total_value_increment

# Example usage:
if __name__ == "__main__":
    try:
        calculator = TokenDepositCalculator()
        calculator.add_deposit(10, 5)
        calculator.add_deposit(20, 3)
        total_amount = calculator.calculate_total()
        total_value_increment = calculator.calculate_total_value_increment()

        print(f"Total Amount: {total_amount}")  # Output: Total Amount: 30
        print(f"Total Value Increment: {total_value_increment}")  # Output: Total Value Increment: 90
    except ValueError as e:
        print(f"Error: {e}")
```
