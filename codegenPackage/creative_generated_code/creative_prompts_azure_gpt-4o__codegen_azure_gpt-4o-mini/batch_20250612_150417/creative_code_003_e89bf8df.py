"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Provide a Python implementation to simulate monthly withdrawals based on Sabka Future's policy of withdrawing interest amount once per month.
Generated: DETERMINISTIC_e89bf8df9b0ec3cc
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SavingsAccount:
    """
    A class to represent a savings account with monthly interest withdrawal.

    Attributes:
        balance (float): The current balance of the account.
        monthly_interest_rate (float): The monthly interest rate as a decimal.
    """

    def __init__(self, initial_balance: float, monthly_interest_rate: float):
        """
        Initializes a new SavingsAccount instance.

        Args:
            initial_balance (float): The initial balance of the account.
            monthly_interest_rate (float): The monthly interest rate as a decimal.

        Raises:
            ValueError: If initial_balance is negative or monthly_interest_rate is not between 0 and 1.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        if not (0 <= monthly_interest_rate <= 1):
            raise ValueError("Monthly interest rate must be between 0 and 1.")

        self.balance = initial_balance
        self.monthly_interest_rate = monthly_interest_rate

    def withdraw_interest(self):
        """
        Withdraws the interest earned for the month from the account balance.

        Raises:
            ValueError: If the balance is insufficient to cover the interest withdrawal.
        """
        interest_amount = self.balance * self.monthly_interest_rate

        if interest_amount > self.balance:
            raise ValueError("Insufficient balance to withdraw interest.")

        self.balance -= interest_amount
        print(f"Withdrew interest: {interest_amount:.2f}. New balance: {self.balance:.2f}")

    def simulate_months(self, months: int):
        """
        Simulates monthly withdrawals of interest for a given number of months.

        Args:
            months (int): The number of months to simulate.

        Raises:
            ValueError: If months is negative.
        """
        if months < 0:
            raise ValueError("Number of months cannot be negative.")

        for month in range(months):
            print(f"Month {month + 1}:")
            self.withdraw_interest()

# Example usage:
if __name__ == "__main__":
    try:
        # Create a savings account with an initial balance and a monthly interest rate of 5%
        account = SavingsAccount(initial_balance=1000.0, monthly_interest_rate=0.05)

        # Simulate 12 months of interest withdrawals
        account.simulate_months(months=12)

    except ValueError as e:
        print(f"Error: {e}")
```
