"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glencoreminers.net
Prompt: Write a program that allows users to select an investment plan (Starter, Silver, Golden, VIP) and calculates the daily profit and total returns based on the parameters provided by Glencoreminers.
Generated: DETERMINISTIC_f2c1ddb836f1643c
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class representing an investment plan with daily profit calculations."""

    def __init__(self, name, daily_profit_percentage):
        """
        Initialize an investment plan with a name and daily profit percentage.

        :param name: Name of the investment plan.
        :param daily_profit_percentage: Daily profit percentage for the plan.
        """
        self.name = name
        self.daily_profit_percentage = daily_profit_percentage

    def calculate_daily_profit(self, investment_amount):
        """
        Calculate the daily profit based on the investment amount.

        :param investment_amount: The amount of money invested.
        :return: The calculated daily profit.
        """
        return investment_amount * (self.daily_profit_percentage / 100)

    def calculate_total_returns(self, investment_amount, days):
        """
        Calculate total returns after a certain number of days.

        :param investment_amount: The amount of money invested.
        :param days: The number of days the money is invested.
        :return: The total amount after the specified days.
        """
        total_profit = self.calculate_daily_profit(investment_amount) * days
        return investment_amount + total_profit


def get_investment_plan(plan_name):
    """
    Retrieve the investment plan based on the provided plan name.

    :param plan_name: The name of the investment plan.
    :return: An instance of InvestmentPlan.
    """
    plans = {
        'Starter': InvestmentPlan("Starter", 1.0),
        'Silver': InvestmentPlan("Silver", 2.5),
        'Golden': InvestmentPlan("Golden", 5.0),
        'VIP': InvestmentPlan("VIP", 10.0),
    }
    return plans.get(plan_name)


def main():
    """Main function to execute the investment plan calculations."""
    print("Select an investment plan: Starter, Silver, Golden, VIP")
    plan_name = input("Enter the investment plan: ").strip()

    # Fetch the selected investment plan
    investment_plan = get_investment_plan(plan_name)
    
    if investment_plan is None:
        print("Invalid investment plan selected. Please try again.")
        return

    try:
        investment_amount = float(input("Enter the investment amount: "))
        days = int(input("Enter the number of days to invest: "))

        if investment_amount < 0 or days < 0:
            raise ValueError("Investment amount and days must be non-negative.")

        # Calculate daily profit and total returns
        daily_profit = investment_plan.calculate_daily_profit(investment_amount)
        total_returns = investment_plan.calculate_total_returns(investment_amount, days)

        # Display results
        print(f"Daily profit for {plan_name} plan: ${daily_profit:.2f}")
        print(f"Total returns after {days} days: ${total_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    main()
```
