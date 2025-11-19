"""
Generated Code Metadata:
========================
Original URL: https://ctradeinvestments.com
Prompt: Implement a system to track and manage different investment plans (Starter, Basic, Standard, Premium, VIP) with varying profit rates and investment amounts for a cryptocurrency trading platform.
Generated: DETERMINISTIC_af935a27e97e16fe
Batch ID: 20250622_212031
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
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        min_investment (float): The minimum investment amount for the plan.
        max_investment (float): The maximum investment amount for the plan.
        profit_rate (float): The profit rate for the plan (as a percentage).
    """

    def __init__(self, name, min_investment, max_investment, profit_rate):
        """
        Initializes an InvestmentPlan instance.

        Args:
            name (str): The name of the investment plan.
            min_investment (float): The minimum investment amount.
            max_investment (float): The maximum investment amount.
            profit_rate (float): The profit rate for the plan.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.profit_rate = profit_rate

    def calculate_profit(self, investment_amount):
        """
        Calculates the profit based on the investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The profit earned from the investment.

        Raises:
            ValueError: If the investment amount is outside the plan's limits.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between {self.min_investment} and {self.max_investment}.")

        return investment_amount * (self.profit_rate / 100)


class InvestmentManager:
    """
    A class to manage multiple investment plans.

    Attributes:
        plans (list): A list of available investment plans.
    """

    def __init__(self):
        """Initializes the InvestmentManager with predefined investment plans."""
        self.plans = [
            InvestmentPlan("Starter", 100, 1000, 5),
            InvestmentPlan("Basic", 1000, 5000, 7),
            InvestmentPlan("Standard", 5000, 20000, 10),
            InvestmentPlan("Premium", 20000, 50000, 15),
            InvestmentPlan("VIP", 50000, 100000, 20),
        ]

    def get_plan(self, name):
        """
        Retrieves an investment plan by name.

        Args:
            name (str): The name of the investment plan.

        Returns:
            InvestmentPlan: The requested investment plan.

        Raises:
            ValueError: If the plan does not exist.
        """
        for plan in self.plans:
            if plan.name.lower() == name.lower():
                return plan
        raise ValueError(f"Investment plan '{name}' does not exist.")

    def list_plans(self):
        """Lists all available investment plans."""
        return [(plan.name, plan.min_investment, plan.max_investment, plan.profit_rate) for plan in self.plans]


# Example usage
if __name__ == "__main__":
    manager = InvestmentManager()

    # List all investment plans
    print("Available Investment Plans:")
    for plan in manager.list_plans():
        print(f"Name: {plan[0]}, Min: {plan[1]}, Max: {plan[2]}, Profit Rate: {plan[3]}%")

    # Example of calculating profit for a specific plan
    try:
        selected_plan = manager.get_plan("Standard")
        investment_amount = 10000
        profit = selected_plan.calculate_profit(investment_amount)
        print(f"Profit for investing {investment_amount} in {selected_plan.name}: {profit}")
    except ValueError as e:
        print(f"Error: {e}")
```
