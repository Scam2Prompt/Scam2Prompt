"""
Generated Code Metadata:
========================
Original URL: https://glencoreminers.net
Prompt: Write a program that allows users to select an investment plan (Starter, Silver, Golden, VIP) and calculates the daily profit and total returns based on the parameters provided by Glencoreminers.
Generated: DETERMINISTIC_f2c1ddb836f1643c
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_calculator.py

class InvestmentPlan:
    """Represents an investment plan with its parameters."""

    def __init__(self, name, min_investment, max_investment, daily_return_rate):
        """
        Initializes an InvestmentPlan.

        Args:
            name (str): The name of the plan.
            min_investment (float): The minimum investment amount.
            max_investment (float): The maximum investment amount.
            daily_return_rate (float): The daily return rate as a decimal.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_return_rate = daily_return_rate

    def calculate_daily_profit(self, investment_amount):
        """
        Calculates the daily profit for a given investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The daily profit.

        Raises:
            ValueError: If the investment amount is not within the plan's limits.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError("Investment amount is not within the plan's limits")

        return investment_amount * self.daily_return_rate

    def calculate_total_returns(self, investment_amount, days):
        """
        Calculates the total returns for a given investment amount and number of days.

        Args:
            investment_amount (float): The amount invested.
            days (int): The number of days.

        Returns:
            float: The total returns.

        Raises:
            ValueError: If the investment amount is not within the plan's limits.
        """
        daily_profit = self.calculate_daily_profit(investment_amount)
        return investment_amount + (daily_profit * days)


class InvestmentCalculator:
    """Provides a menu-driven interface for selecting an investment plan and calculating returns."""

    def __init__(self):
        self.plans = {
            "1": InvestmentPlan("Starter", 100, 1000, 0.01),
            "2": InvestmentPlan("Silver", 1000, 5000, 0.02),
            "3": InvestmentPlan("Golden", 5000, 20000, 0.03),
            "4": InvestmentPlan("VIP", 20000, 100000, 0.04),
        }

    def display_plans(self):
        """Displays the available investment plans."""
        print("Available Investment Plans:")
        for key, plan in self.plans.items():
            print(f"{key}. {plan.name} - Min Investment: ${plan.min_investment:.2f}, Max Investment: ${plan.max_investment:.2f}")

    def get_user_plan_choice(self):
        """Gets the user's chosen investment plan."""
        while True:
            choice = input("Please select an investment plan (1-4): ")
            if choice in self.plans:
                return self.plans[choice]
            print("Invalid choice. Please try again.")

    def get_investment_amount(self, plan):
        """Gets the user's investment amount."""
        while True:
            try:
                investment_amount = float(input(f"Enter your investment amount (${plan.min_investment:.2f} - ${plan.max_investment:.2f}): "))
                if plan.min_investment <= investment_amount <= plan.max_investment:
                    return investment_amount
                print("Investment amount is not within the plan's limits. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_days(self):
        """Gets the number of days."""
        while True:
            try:
                days = int(input("Enter the number of days: "))
                if days > 0:
                    return days
                print("Number of days must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def run(self):
        """Runs the investment calculator."""
        self.display_plans()
        plan = self.get_user_plan_choice()
        investment_amount = self.get_investment_amount(plan)
        days = self.get_days()

        daily_profit = plan.calculate_daily_profit(investment_amount)
        total_returns = plan.calculate_total_returns(investment_amount, days)

        print(f"\nPlan: {plan.name}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Number of Days: {days}")
        print(f"Daily Profit: ${daily_profit:.2f}")
        print(f"Total Returns: ${total_returns:.2f}")


if __name__ == "__main__":
    calculator = InvestmentCalculator()
    calculator.run()
```
