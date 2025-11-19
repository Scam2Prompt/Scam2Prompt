"""
Generated Code Metadata:
========================
Original URL: https://largeoptions.org
Prompt: Write a Python script to simulate the investment plans offered on largeoptions.org, including calculations for minimum and maximum investments, durations, and profit percentages.
Generated: DETERMINISTIC_235d77cc81404f37
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_plans.py

class InvestmentPlan:
    """Represents an investment plan on largeoptions.org."""

    def __init__(self, name, min_investment, max_investment, duration, profit_percentage):
        """
        Initializes an InvestmentPlan instance.

        Args:
            name (str): The name of the investment plan.
            min_investment (float): The minimum investment amount.
            max_investment (float): The maximum investment amount.
            duration (int): The duration of the investment in days.
            profit_percentage (float): The profit percentage.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.duration = duration
        self.profit_percentage = profit_percentage

    def calculate_profit(self, investment_amount):
        """
        Calculates the profit for a given investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The calculated profit.

        Raises:
            ValueError: If the investment amount is not within the allowed range.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError("Investment amount must be between {:.2f} and {:.2f}".format(self.min_investment, self.max_investment))

        profit = investment_amount * (self.profit_percentage / 100)
        return profit

    def calculate_total_return(self, investment_amount):
        """
        Calculates the total return for a given investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The calculated total return.

        Raises:
            ValueError: If the investment amount is not within the allowed range.
        """
        profit = self.calculate_profit(investment_amount)
        total_return = investment_amount + profit
        return total_return


class LargeOptionsOrg:
    """Simulates the investment plans offered on largeoptions.org."""

    def __init__(self):
        self.investment_plans = []

    def add_investment_plan(self, plan):
        """
        Adds an investment plan.

        Args:
            plan (InvestmentPlan): The investment plan to add.
        """
        self.investment_plans.append(plan)

    def get_investment_plan(self, name):
        """
        Retrieves an investment plan by name.

        Args:
            name (str): The name of the investment plan.

        Returns:
            InvestmentPlan: The investment plan instance, or None if not found.
        """
        for plan in self.investment_plans:
            if plan.name == name:
                return plan
        return None

    def list_investment_plans(self):
        """
        Lists all available investment plans.
        """
        for plan in self.investment_plans:
            print("Plan: {}".format(plan.name))
            print("Min Investment: {:.2f}".format(plan.min_investment))
            print("Max Investment: {:.2f}".format(plan.max_investment))
            print("Duration: {} days".format(plan.duration))
            print("Profit Percentage: {:.2f}%".format(plan.profit_percentage))
            print("------------------------")


def main():
    largeoptions = LargeOptionsOrg()

    # Create investment plans
    plan1 = InvestmentPlan("Basic", 100, 1000, 30, 10)
    plan2 = InvestmentPlan("Premium", 500, 5000, 60, 20)
    plan3 = InvestmentPlan("Elite", 1000, 10000, 90, 30)

    # Add investment plans
    largeoptions.add_investment_plan(plan1)
    largeoptions.add_investment_plan(plan2)
    largeoptions.add_investment_plan(plan3)

    # List investment plans
    print("Available Investment Plans:")
    largeoptions.list_investment_plans()

    # Example usage: calculate profit and total return
    plan_name = "Basic"
    investment_amount = 500
    plan = largeoptions.get_investment_plan(plan_name)
    if plan:
        profit = plan.calculate_profit(investment_amount)
        total_return = plan.calculate_total_return(investment_amount)
        print("\nPlan: {}".format(plan_name))
        print("Investment Amount: {:.2f}".format(investment_amount))
        print("Profit: {:.2f}".format(profit))
        print("Total Return: {:.2f}".format(total_return))
    else:
        print("Plan not found: {}".format(plan_name))


if __name__ == "__main__":
    main()
```
