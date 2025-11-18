"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradezeenetwork.com
Prompt: Write Python code to calculate profit accruals for an investment plan based on the Tradezeenetwork model, where returns are calculated every 24-72 hours depending on the plan chosen.
Generated: DETERMINISTIC_4a76fb0372e38f1e
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random

class InvestmentPlan:
    """
    Class to represent an Investment Plan with a specific profit accrual interval.
    """
    def __init__(self, name, min_interval, max_interval, interest_rate):
        """
        Initialize an investment plan.
        
        :param name: Name of the investment plan.
        :param min_interval: Minimum interval in hours for profit accrual.
        :param max_interval: Maximum interval in hours for profit accrual.
        :param interest_rate: Interest rate for profit accrual (as a percentage).
        """
        self.name = name
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.interest_rate = interest_rate


class InvestmentAccount:
    """
    Class to represent an Investment Account for a user.
    """
    def __init__(self, initial_balance, investment_plan):
        """
        Initialize an investment account.
        
        :param initial_balance: Initial balance of the account.
        :param investment_plan: Investment plan associated with the account.
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than zero.")
        
        self.balance = initial_balance
        self.investment_plan = investment_plan
        self.last_accrual_time = datetime.datetime.now()

    def accrue_profit(self):
        """
        Calculate and accrue profit based on the investment plan's interval and interest rate.
        """
        current_time = datetime.datetime.now()
        interval_hours = random.randint(self.investment_plan.min_interval, self.investment_plan.max_interval)
        next_accrual_time = self.last_accrual_time + datetime.timedelta(hours=interval_hours)

        if current_time >= next_accrual_time:
            # Calculate profit
            profit = self.balance * (self.investment_plan.interest_rate / 100)
            self.balance += profit
            self.last_accrual_time = current_time
            return profit
        else:
            return 0  # No accrual yet


def main():
    """
    Main function to demonstrate the investment profit accrual system.
    """
    try:
        # Define investment plans
        basic_plan = InvestmentPlan(name="Basic", min_interval=24, max_interval=48, interest_rate=2.5)
        premium_plan = InvestmentPlan(name="Premium", min_interval=48, max_interval=72, interest_rate=3.5)

        # Create investment accounts
        basic_account = InvestmentAccount(initial_balance=1000, investment_plan=basic_plan)
        premium_account = InvestmentAccount(initial_balance=5000, investment_plan=premium_plan)

        # Simulate profit accruals
        print("Starting balances:")
        print(f"Basic Account: ${basic_account.balance}")
        print(f"Premium Account: ${premium_account.balance}")

        for _ in range(10):  # Simulate 10 profit accrual checks
            basic_profit = basic_account.accrue_profit()
            premium_profit = premium_account.accrue_profit()

            if basic_profit > 0:
                print(f"Basic Plan accrued profit: ${basic_profit:.2f}, New Balance: ${basic_account.balance:.2f}")
            if premium_profit > 0:
                print(f"Premium Plan accrued profit: ${premium_profit:.2f}, New Balance: ${premium_account.balance:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
