"""
Generated Code Metadata:
========================
Original URL: https://swifttradeexpress.com
Prompt: Write Python code to calculate daily, weekly, and monthly income based on the investment plans provided by SwiftTrade Express, including the Basic, Standard, Variety, Fixed, and Children Scholarships plans.
Generated: DETERMINISTIC_c7d57d053b87e1c6
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan and calculate income based on the plan type.
    """

    def __init__(self, plan_type, investment_amount):
        """
        Initializes the InvestmentPlan with a plan type and investment amount.

        :param plan_type: str - The type of investment plan (Basic, Standard, Variety, Fixed, Children Scholarships)
        :param investment_amount: float - The amount invested in the plan
        """
        self.plan_type = plan_type
        self.investment_amount = investment_amount
        self.daily_rate = self.get_daily_rate()

    def get_daily_rate(self):
        """
        Returns the daily interest rate based on the investment plan type.

        :return: float - Daily interest rate
        :raises ValueError: If the plan type is not recognized
        """
        rates = {
            "Basic": 0.01,  # 1% daily
            "Standard": 0.015,  # 1.5% daily
            "Variety": 0.02,  # 2% daily
            "Fixed": 0.025,  # 2.5% daily
            "Children Scholarships": 0.03  # 3% daily
        }

        if self.plan_type not in rates:
            raise ValueError(f"Unrecognized plan type: {self.plan_type}")

        return rates[self.plan_type]

    def calculate_daily_income(self):
        """
        Calculates the daily income based on the investment amount and daily rate.

        :return: float - Daily income
        """
        return self.investment_amount * self.daily_rate

    def calculate_weekly_income(self):
        """
        Calculates the weekly income based on the daily income.

        :return: float - Weekly income
        """
        return self.calculate_daily_income() * 7

    def calculate_monthly_income(self):
        """
        Calculates the monthly income based on the daily income.

        :return: float - Monthly income
        """
        return self.calculate_daily_income() * 30  # Assuming 30 days in a month

def main():
    """
    Main function to demonstrate the income calculation for different investment plans.
    """
    try:
        # Example investment amounts for different plans
        investment_amounts = {
            "Basic": 1000,
            "Standard": 2000,
            "Variety": 3000,
            "Fixed": 4000,
            "Children Scholarships": 5000
        }

        for plan, amount in investment_amounts.items():
            investment_plan = InvestmentPlan(plan, amount)
            print(f"Plan: {plan}")
            print(f"  Daily Income: ${investment_plan.calculate_daily_income():.2f}")
            print(f"  Weekly Income: ${investment_plan.calculate_weekly_income():.2f}")
            print(f"  Monthly Income: ${investment_plan.calculate_monthly_income():.2f}")
            print("-" * 30)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
