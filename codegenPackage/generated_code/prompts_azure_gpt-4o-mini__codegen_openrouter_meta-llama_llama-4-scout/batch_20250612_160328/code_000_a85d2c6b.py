"""
Generated Code Metadata:
========================
Original URL: https://prospectlimited.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Prospect Limited, including the Starter, Standard, Premium, Gold, and Executive plans.
Generated: DETERMINISTIC_a85d2c6b87f03357
Batch ID: 20250612_160328
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
    """Base class for investment plans."""

    def __init__(self, name, min_investment, max_investment, interest_rate):
        """
        Initialize an investment plan.

        Args:
            name (str): Name of the plan.
            min_investment (float): Minimum investment amount.
            max_investment (float): Maximum investment amount.
            interest_rate (float): Interest rate as a decimal.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.interest_rate = interest_rate

    def calculate_returns(self, investment_amount):
        """
        Calculate potential returns based on the investment amount.

        Args:
            investment_amount (float): Amount invested.

        Returns:
            float: Potential returns.

        Raises:
            ValueError: If investment amount is outside the plan's limits.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between ${self.min_investment:.2f} and ${self.max_investment:.2f}")

        return investment_amount * self.interest_rate


class ProspectLimited:
    """Represents Prospect Limited's investment plans."""

    def __init__(self):
        self.plans = {
            "Starter": InvestmentPlan("Starter", 1000, 5000, 0.05),
            "Standard": InvestmentPlan("Standard", 5000, 20000, 0.07),
            "Premium": InvestmentPlan("Premium", 20000, 50000, 0.10),
            "Gold": InvestmentPlan("Gold", 50000, 100000, 0.12),
            "Executive": InvestmentPlan("Executive", 100000, float("inf"), 0.15),
        }

    def get_plan(self, plan_name):
        """
        Get an investment plan by name.

        Args:
            plan_name (str): Name of the plan.

        Returns:
            InvestmentPlan: The investment plan.

        Raises:
            ValueError: If the plan does not exist.
        """
        try:
            return self.plans[plan_name]
        except KeyError:
            raise ValueError(f"Invalid plan name: {plan_name}")

    def calculate_returns(self, plan_name, investment_amount):
        """
        Calculate potential returns based on the investment plan and amount.

        Args:
            plan_name (str): Name of the plan.
            investment_amount (float): Amount invested.

        Returns:
            float: Potential returns.

        Raises:
            ValueError: If the plan does not exist or investment amount is invalid.
        """
        plan = self.get_plan(plan_name)
        return plan.calculate_returns(investment_amount)


def main():
    prospect_limited = ProspectLimited()

    plans = {
        "1": "Starter",
        "2": "Standard",
        "3": "Premium",
        "4": "Gold",
        "5": "Executive",
    }

    print("Prospect Limited Investment Plans:")
    for key, plan_name in plans.items():
        print(f"{key}. {plan_name}")

    plan_choice = input("Choose a plan (1-5): ")
    plan_name = plans.get(plan_choice)

    if plan_name is None:
        print("Invalid plan choice.")
        return

    try:
        investment_amount = float(input("Enter investment amount: $"))
    except ValueError:
        print("Invalid investment amount.")
        return

    try:
        returns = prospect_limited.calculate_returns(plan_name, investment_amount)
        print(f"Potential returns for {plan_name} plan: ${returns:.2f}")
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
```
