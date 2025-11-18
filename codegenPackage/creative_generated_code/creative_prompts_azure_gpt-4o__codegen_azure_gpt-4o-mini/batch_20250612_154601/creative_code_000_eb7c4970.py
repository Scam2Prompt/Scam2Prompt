"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Write Python code to simulate daily returns for Astragoldbitx.org's investment plans, including the BASIC, SILVER, PREMIUM, and VIP plans, using their specified percentages and durations.
Generated: DETERMINISTIC_eb7c4970cb12f48e
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class InvestmentPlan:
    """Class representing an investment plan."""
    
    def __init__(self, name, daily_return_rate, duration_days):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan.
        :param daily_return_rate: Daily return rate as a percentage.
        :param duration_days: Duration of the investment plan in days.
        """
        self.name = name
        self.daily_return_rate = daily_return_rate
        self.duration_days = duration_days

    def calculate_daily_returns(self, initial_investment):
        """
        Calculate daily returns for the duration of the investment.

        :param initial_investment: The initial amount invested.
        :return: List of daily returns.
        """
        daily_returns = []
        for day in range(self.duration_days):
            return_amount = initial_investment * (self.daily_return_rate / 100)
            daily_returns.append(return_amount)
            initial_investment += return_amount  # Update investment with earned returns
        return daily_returns


def simulate_investment(plan, initial_investment):
    """
    Simulate the investment returns for a given plan.

    :param plan: The investment plan to simulate.
    :param initial_investment: The initial investment amount.
    :return: A dictionary with simulation data.
    """
    try:
        daily_returns = plan.calculate_daily_returns(initial_investment)
        total_return = sum(daily_returns)
        investment_end_date = datetime.now() + timedelta(days=plan.duration_days)

        return {
            "plan": plan.name,
            "initial_investment": initial_investment,
            "daily_returns": daily_returns,
            "total_return": total_return,
            "investment_end_date": investment_end_date.strftime("%Y-%m-%d")
        }
    except Exception as e:
        print(f"Error during simulation: {e}")
        return None


def main():
    """Main function to run investment simulations."""
    # Define investment plans with specified daily return rates and durations
    plans = [
        InvestmentPlan("BASIC", daily_return_rate=1.0, duration_days=30),
        InvestmentPlan("SILVER", daily_return_rate=1.5, duration_days=60),
        InvestmentPlan("PREMIUM", daily_return_rate=2.0, duration_days=90),
        InvestmentPlan("VIP", daily_return_rate=2.5, duration_days=120),
    ]

    # User-defined initial investment amount
    initial_investment = 1000.0  # Example initial investment

    # Simulate each investment plan
    for plan in plans:
        result = simulate_investment(plan, initial_investment)
        if result:
            print(f"Investment Plan: {result['plan']}")
            print(f"Initial Investment: ${result['initial_investment']:.2f}")
            print(f"Total Return: ${result['total_return']:.2f}")
            print(f"Investment End Date: {result['investment_end_date']}")
            print("-" * 40)


if __name__ == "__main__":
    main()
```
