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
import datetime

class SabkaFutureAccount:
    """
    Class to simulate monthly withdrawals based on Sabka Future's policy.
    Withdraws the interest amount once per month.
    """
    def __init__(self, initial_balance, annual_interest_rate):
        """
        Initializes the account with an initial balance and annual interest rate.

        :param initial_balance: Initial amount in the account.
        :param annual_interest_rate: Annual interest rate as a percentage.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        
        self.balance = initial_balance
        self.annual_interest_rate = annual_interest_rate
        self.last_withdrawal_date = None

    def calculate_monthly_interest(self):
        """
        Calculates the monthly interest based on the annual interest rate.

        :return: Monthly interest amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        return self.balance * monthly_interest_rate

    def withdraw_interest(self):
        """
        Withdraws the interest amount for the current month if eligible.

        :return: The amount withdrawn (interest) or None if not eligible for withdrawal.
        """
        today = datetime.date.today()
        
        # Check if a withdrawal has already been made this month.
        if self.last_withdrawal_date and self.last_withdrawal_date.month == today.month:
            return None  # Withdrawal already made this month.
        
        # Calculate and withdraw monthly interest.
        monthly_interest = self.calculate_monthly_interest()
        self.balance -= monthly_interest
        self.last_withdrawal_date = today
        
        return monthly_interest

    def get_balance(self):
        """
        Returns the current balance of the account.

        :return: Current account balance.
        """
        return self.balance


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the account.
        account = SabkaFutureAccount(initial_balance=10000, annual_interest_rate=6)

        # Simulate monthly withdrawals.
        print("Initial Balance:", account.get_balance())
        withdrawn_interest = account.withdraw_interest()
        if withdrawn_interest:
            print(f"Interest Withdrawn: {withdrawn_interest:.2f}")
        else:
            print("No withdrawal made this month.")

        print("Balance after withdrawal:", account.get_balance())
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
