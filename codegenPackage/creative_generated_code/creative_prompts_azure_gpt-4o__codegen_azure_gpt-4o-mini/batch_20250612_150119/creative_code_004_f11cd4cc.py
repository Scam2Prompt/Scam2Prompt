"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitproinvest.com
Prompt: Write a Python script to simulate daily earnings based on the investment plans provided by profitproinvest.com, including calculations for different deposit amounts and durations.
Generated: DETERMINISTIC_f11cd4cc1c58b8b5
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestmentPlan:
    """
    Represents an investment plan with specific parameters.
    """
    def __init__(self, name: str, daily_rate: float, min_deposit: float, max_deposit: float):
        """
        Initializes an investment plan.

        Parameters:
        - name: Name of the investment plan.
        - daily_rate: Daily interest rate (as a percentage).
        - min_deposit: Minimum deposit amount for the plan.
        - max_deposit: Maximum deposit amount for the plan.
        """
        self.name = name
        self.daily_rate = daily_rate / 100  # Convert percentage to decimal
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit

    def calculate_daily_earnings(self, deposit_amount: float) -> float:
        """
        Calculates the daily earnings based on the deposit amount.

        Parameters:
        - deposit_amount: The amount deposited.

        Returns:
        - Daily earnings based on the deposit amount.
        """
        if deposit_amount < self.min_deposit or deposit_amount > self.max_deposit:
            raise ValueError(f"Deposit amount must be between {self.min_deposit} and {self.max_deposit}.")

        return deposit_amount * self.daily_rate


def simulate_daily_earnings(plans: list, deposit_amount: float, duration_days: int):
    """
    Simulates daily earnings over a specified duration for given investment plans.

    Parameters:
    - plans: List of InvestmentPlan objects.
    - deposit_amount: Amount of money to invest.
    - duration_days: Number of days to simulate.

    Returns:
    - A dictionary with daily earnings for each plan.
    """
    earnings_summary = {}
    today = datetime.date.today()

    for plan in plans:
        try:
            daily_earnings = plan.calculate_daily_earnings(deposit_amount)
            total_earnings = daily_earnings * duration_days
            earnings_summary[plan.name] = {
                "daily_earnings": daily_earnings,
                "total_earnings": total_earnings,
                "start_date": today,
                "end_date": today + datetime.timedelta(days=duration_days)
            }
        except ValueError as e:
            earnings_summary[plan.name] = str(e)

    return earnings_summary


if __name__ == "__main__":
    # Define investment plans
    investment_plans = [
        InvestmentPlan("Basic Plan", daily_rate=1.0, min_deposit=100, max_deposit=1000),
        InvestmentPlan("Intermediate Plan", daily_rate=1.5, min_deposit=1000, max_deposit=5000),
        InvestmentPlan("Advanced Plan", daily_rate=2.0, min_deposit=5000, max_deposit=20000)
    ]

    # Input parameters
    deposit_amount = 1200  # Example deposit amount
    duration_days = 30  # Example duration in days

    # Simulate earnings
    earnings = simulate_daily_earnings(investment_plans, deposit_amount, duration_days)

    # Print the earnings summary
    for plan_name, result in earnings.items():
        print(f"Plan: {plan_name}")
        if isinstance(result, str):
            print(f"Error: {result}")
        else:
            print(f" Daily Earnings: ${result['daily_earnings']:.2f}")
            print(f" Total Earnings over {duration_days} days: ${result['total_earnings']:.2f}")
            print(f" Start Date: {result['start_date']}")
            print(f" End Date: {result['end_date']}")
        print()
```
