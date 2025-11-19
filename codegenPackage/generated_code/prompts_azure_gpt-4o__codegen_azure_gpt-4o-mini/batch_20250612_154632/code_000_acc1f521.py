"""
Generated Code Metadata:
========================
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Write a Python script to calculate fixed daily profits for an investment plan based on the minimum and maximum amounts provided by Corner Stone Investment's packages (e.g., Starter Plan, VIP Plan, etc.).
Generated: DETERMINISTIC_acc1f5217d5d9c09
Batch ID: 20250612_154632
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
    A class to represent an investment plan with fixed daily profits.
    """

    def __init__(self, name, min_investment, max_investment, daily_profit_rate):
        """
        Initializes an investment plan with the given parameters.

        :param name: Name of the investment plan
        :param min_investment: Minimum investment amount
        :param max_investment: Maximum investment amount
        :param daily_profit_rate: Daily profit rate as a percentage
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_profit_rate = daily_profit_rate / 100  # Convert percentage to decimal

    def calculate_daily_profit(self, investment_amount):
        """
        Calculates the daily profit based on the investment amount.

        :param investment_amount: The amount invested
        :return: Daily profit amount
        :raises ValueError: If the investment amount is outside the plan's limits
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between {self.min_investment} and {self.max_investment}.")

        daily_profit = investment_amount * self.daily_profit_rate
        return daily_profit


def main():
    """
    Main function to demonstrate the investment plan profit calculation.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("Starter Plan", 100, 1000, 5),  # 5% daily profit
        InvestmentPlan("VIP Plan", 1000, 10000, 7)     # 7% daily profit
    ]

    # Example investment amounts
    investment_amounts = [150, 500, 1200]  # Some test amounts

    for plan in plans:
        print(f"\nCalculating profits for {plan.name}:")
        for amount in investment_amounts:
            try:
                profit = plan.calculate_daily_profit(amount)
                print(f"Investment: {amount}, Daily Profit: {profit:.2f}")
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    main()
```
