"""
Generated Code Metadata:
========================
Original URL: https://aphatradespro.com
Prompt: Create a Python script to manage investment plans with varying durations (e.g., 7 days, 14 days, 1 month, 6 months) and calculate projected profits, as described in Aphatradespro's investment offerings.
Generated: DETERMINISTIC_17b855e4cf460814
Batch ID: 20250612_154632
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
    """Represents an investment plan with a duration and interest rate."""

    def __init__(self, name, duration, interest_rate):
        """
        Initializes an InvestmentPlan.

        Args:
            name (str): The name of the investment plan.
            duration (int): The duration of the investment plan in days.
            interest_rate (float): The interest rate of the investment plan as a decimal.
        """
        self.name = name
        self.duration = duration
        self.interest_rate = interest_rate

    def calculate_projected_profit(self, principal):
        """
        Calculates the projected profit for the investment plan.

        Args:
            principal (float): The principal amount invested.

        Returns:
            float: The projected profit.
        """
        return principal * self.interest_rate * (self.duration / 365)


class InvestmentManager:
    """Manages a collection of investment plans."""

    def __init__(self):
        """Initializes an InvestmentManager."""
        self.plans = {}

    def add_plan(self, plan):
        """
        Adds an investment plan to the manager.

        Args:
            plan (InvestmentPlan): The investment plan to add.
        """
        self.plans[plan.name] = plan

    def get_plan(self, name):
        """
        Retrieves an investment plan by name.

        Args:
            name (str): The name of the investment plan.

        Returns:
            InvestmentPlan: The investment plan, or None if not found.
        """
        return self.plans.get(name)

    def calculate_projected_profits(self, principal, plan_names):
        """
        Calculates the projected profits for a list of investment plans.

        Args:
            principal (float): The principal amount invested.
            plan_names (list[str]): The names of the investment plans.

        Returns:
            dict[str, float]: A dictionary of plan names to projected profits.
        """
        projected_profits = {}
        for name in plan_names:
            plan = self.get_plan(name)
            if plan:
                projected_profits[name] = plan.calculate_projected_profit(principal)
            else:
                raise ValueError(f"Unknown investment plan: {name}")
        return projected_profits


def main():
    # Create investment plans
    plans = [
        InvestmentPlan("7 Days", 7, 0.05),
        InvestmentPlan("14 Days", 14, 0.10),
        InvestmentPlan("1 Month", 30, 0.15),
        InvestmentPlan("6 Months", 183, 0.30),
    ]

    # Create investment manager
    manager = InvestmentManager()
    for plan in plans:
        manager.add_plan(plan)

    # Calculate projected profits
    principal = 1000.0
    plan_names = ["7 Days", "14 Days", "1 Month", "6 Months"]
    try:
        projected_profits = manager.calculate_projected_profits(principal, plan_names)
        print("Projected Profits:")
        for name, profit in projected_profits.items():
            print(f"{name}: ${profit:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
