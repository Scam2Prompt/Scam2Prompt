"""
Generated Code Metadata:
========================
Original URL: https://mcoinners.com
Prompt: Write a Python script to simulate the investment plans offered by mcoinners.com, including ROI calculations for the BASIC, PREMIUM, ADVANCED, PRO, and VIP plans based on the given durations and deposit ranges.
Generated: DETERMINISTIC_ad3ef716313c8a75
Batch ID: 20250612_154542
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
    def __init__(self, name, roi, min_deposit, max_deposit, duration):
        """
        Initialize an investment plan.

        Args:
            name (str): Name of the plan.
            roi (float): Return on investment (in %).
            min_deposit (float): Minimum deposit required.
            max_deposit (float): Maximum deposit allowed.
            duration (int): Duration of the plan in days.
        """
        self.name = name
        self.roi = roi / 100  # Convert ROI to decimal
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.duration = duration

    def calculate_roi(self, deposit):
        """
        Calculate the return on investment.

        Args:
            deposit (float): Deposit amount.

        Returns:
            float: Return on investment.

        Raises:
            ValueError: If deposit is outside the allowed range.
        """
        if deposit < self.min_deposit or deposit > self.max_deposit:
            raise ValueError(f"Deposit must be between {self.min_deposit} and {self.max_deposit}")

        return deposit * self.roi


class InvestmentPlans:
    def __init__(self):
        """
        Initialize investment plans.
        """
        self.plans = {
            "BASIC": InvestmentPlan("BASIC", 10, 100, 1000, 30),
            "PREMIUM": InvestmentPlan("PREMIUM", 15, 1001, 5000, 60),
            "ADVANCED": InvestmentPlan("ADVANCED", 20, 5001, 20000, 90),
            "PRO": InvestmentPlan("PRO", 25, 20001, 50000, 120),
            "VIP": InvestmentPlan("VIP", 30, 50001, 100000, 180),
        }

    def get_plan(self, plan_name):
        """
        Get an investment plan by name.

        Args:
            plan_name (str): Name of the plan.

        Returns:
            InvestmentPlan: Investment plan object.

        Raises:
            ValueError: If plan does not exist.
        """
        plan = self.plans.get(plan_name.upper())
        if plan is None:
            raise ValueError(f"Plan '{plan_name}' does not exist")

        return plan

    def calculate_roi(self, plan_name, deposit):
        """
        Calculate the return on investment for a plan.

        Args:
            plan_name (str): Name of the plan.
            deposit (float): Deposit amount.

        Returns:
            float: Return on investment.

        Raises:
            ValueError: If plan does not exist or deposit is invalid.
        """
        plan = self.get_plan(plan_name)
        return plan.calculate_roi(deposit)


def main():
    investment_plans = InvestmentPlans()

    # Example usage:
    plans = ["BASIC", "PREMIUM", "ADVANCED", "PRO", "VIP"]
    deposits = [500, 2000, 10000, 30000, 75000]

    for plan, deposit in zip(plans, deposits):
        try:
            roi = investment_plans.calculate_roi(plan, deposit)
            print(f"Plan: {plan}, Deposit: {deposit}, ROI: {roi:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
