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
# investment_manager.py

class InvestmentPlan:
    """
    Represents an investment plan with a name, profit rate, and minimum investment amount.
    """
    def __init__(self, name, profit_rate, min_investment):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan (e.g., Starter, Basic, etc.)
        :param profit_rate: Profit rate as a percentage (e.g., 5 for 5%)
        :param min_investment: Minimum investment amount required for the plan
        """
        self.name = name
        self.profit_rate = profit_rate
        self.min_investment = min_investment

    def calculate_profit(self, investment_amount):
        """
        Calculate the profit for a given investment amount.

        :param investment_amount: Amount invested
        :return: Profit earned
        :raises ValueError: If the investment amount is less than the minimum required
        """
        if investment_amount < self.min_investment:
            raise ValueError(f"Investment amount must be at least {self.min_investment} for the {self.name} plan.")
        return investment_amount * (self.profit_rate / 100)

    def __str__(self):
        """
        String representation of the investment plan.
        """
        return f"Plan: {self.name}, Profit Rate: {self.profit_rate}%, Minimum Investment: {self.min_investment}"


class InvestmentManager:
    """
    Manages multiple investment plans and user investments.
    """
    def __init__(self):
        """
        Initialize the investment manager with predefined plans.
        """
        self.plans = {
            "Starter": InvestmentPlan("Starter", profit_rate=5, min_investment=100),
            "Basic": InvestmentPlan("Basic", profit_rate=10, min_investment=500),
            "Standard": InvestmentPlan("Standard", profit_rate=15, min_investment=1000),
            "Premium": InvestmentPlan("Premium", profit_rate=20, min_investment=5000),
            "VIP": InvestmentPlan("VIP", profit_rate=25, min_investment=10000),
        }

    def get_plan(self, plan_name):
        """
        Retrieve an investment plan by name.

        :param plan_name: Name of the plan
        :return: InvestmentPlan object
        :raises KeyError: If the plan name does not exist
        """
        if plan_name not in self.plans:
            raise KeyError(f"Plan '{plan_name}' does not exist.")
        return self.plans[plan_name]

    def calculate_profit(self, plan_name, investment_amount):
        """
        Calculate profit for a given plan and investment amount.

        :param plan_name: Name of the investment plan
        :param investment_amount: Amount invested
        :return: Profit earned
        :raises KeyError: If the plan name does not exist
        :raises ValueError: If the investment amount is invalid for the plan
        """
        plan = self.get_plan(plan_name)
        return plan.calculate_profit(investment_amount)

    def list_plans(self):
        """
        List all available investment plans.

        :return: List of investment plan details
        """
        return [str(plan) for plan in self.plans.values()]


# Example usage
if __name__ == "__main__":
    try:
        manager = InvestmentManager()

        # List all available plans
        print("Available Investment Plans:")
        for plan in manager.list_plans():
            print(plan)

        # Calculate profit for a specific plan
        plan_name = "Standard"
        investment_amount = 1500
        profit = manager.calculate_profit(plan_name, investment_amount)
        print(f"\nProfit for investing {investment_amount} in {plan_name} plan: {profit}")

    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
