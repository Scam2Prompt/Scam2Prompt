"""
Generated Code Metadata:
========================
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Generate a Python script to calculate potential returns based on the investment plans offered by SmartglobalwealthFx, including the BASIC, SILVER, DIAMOND, and VIP plans.
Generated: DETERMINISTIC_bef64895af006ed0
Batch ID: 20250612_160124
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
    def __init__(self, name, min_investment, max_investment, daily_return):
        """
        Initialize an investment plan.

        Args:
            name (str): Name of the plan.
            min_investment (float): Minimum investment amount.
            max_investment (float): Maximum investment amount.
            daily_return (float): Daily return percentage.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.daily_return = daily_return

    def calculate_return(self, investment_amount, days):
        """
        Calculate the potential return for a given investment amount and number of days.

        Args:
            investment_amount (float): Amount invested.
            days (int): Number of days.

        Returns:
            float: Potential return.

        Raises:
            ValueError: If investment amount is outside the plan's limits.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between ${self.min_investment:.2f} and ${self.max_investment:.2f}")

        daily_return_amount = investment_amount * (self.daily_return / 100)
        total_return = investment_amount + (daily_return_amount * days)
        return total_return


class SmartglobalwealthFx:
    def __init__(self):
        """
        Initialize the SmartglobalwealthFx investment plans.
        """
        self.plans = {
            "BASIC": InvestmentPlan("BASIC", 100, 1000, 2),
            "SILVER": InvestmentPlan("SILVER", 1000, 5000, 3),
            "DIAMOND": InvestmentPlan("DIAMOND", 5000, 20000, 4),
            "VIP": InvestmentPlan("VIP", 20000, 100000, 5),
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
        plan = self.plans.get(plan_name.upper())
        if plan is None:
            raise ValueError(f"Invalid plan: {plan_name}")
        return plan

    def calculate_potential_return(self, plan_name, investment_amount, days):
        """
        Calculate the potential return for a given plan, investment amount, and number of days.

        Args:
            plan_name (str): Name of the plan.
            investment_amount (float): Amount invested.
            days (int): Number of days.

        Returns:
            float: Potential return.

        Raises:
            ValueError: If the plan does not exist or investment amount is invalid.
        """
        plan = self.get_plan(plan_name)
        return plan.calculate_return(investment_amount, days)


def main():
    smartglobalwealth_fx = SmartglobalwealthFx()

    # Example usage:
    plan_name = "BASIC"
    investment_amount = 500
    days = 30

    try:
        potential_return = smartglobalwealth_fx.calculate_potential_return(plan_name, investment_amount, days)
        print(f"Potential return for {plan_name} plan with ${investment_amount:.2f} investment for {days} days: ${potential_return:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
