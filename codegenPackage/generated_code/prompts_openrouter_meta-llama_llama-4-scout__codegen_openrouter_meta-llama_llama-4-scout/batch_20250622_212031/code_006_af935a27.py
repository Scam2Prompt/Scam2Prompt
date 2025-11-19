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
from enum import Enum
from typing import Dict

class InvestmentPlan(Enum):
    """Enum for different investment plans."""
    STARTER = 1
    BASIC = 2
    STANDARD = 3
    PREMIUM = 4
    VIP = 5

class InvestmentPlanManager:
    """Class to manage different investment plans."""

    def __init__(self):
        """Initialize investment plans with their profit rates and investment amounts."""
        self.investment_plans: Dict[InvestmentPlan, Dict[str, float]] = {
            InvestmentPlan.STARTER: {"profit_rate": 0.05, "investment_amount": 100.0},
            InvestmentPlan.BASIC: {"profit_rate": 0.10, "investment_amount": 500.0},
            InvestmentPlan.STANDARD: {"profit_rate": 0.15, "investment_amount": 1000.0},
            InvestmentPlan.PREMIUM: {"profit_rate": 0.20, "investment_amount": 5000.0},
            InvestmentPlan.VIP: {"profit_rate": 0.25, "investment_amount": 10000.0},
        }

    def get_investment_plan_details(self, plan: InvestmentPlan) -> Dict[str, float]:
        """Get details of a specific investment plan.

        Args:
        plan (InvestmentPlan): The investment plan.

        Returns:
        Dict[str, float]: A dictionary containing the profit rate and investment amount.

        Raises:
        ValueError: If the plan is not found.
        """
        try:
            return self.investment_plans[plan]
        except KeyError:
            raise ValueError("Invalid investment plan")

    def update_investment_plan(self, plan: InvestmentPlan, profit_rate: float = None, investment_amount: float = None):
        """Update the profit rate and/or investment amount of a specific investment plan.

        Args:
        plan (InvestmentPlan): The investment plan.
        profit_rate (float, optional): The new profit rate. Defaults to None.
        investment_amount (float, optional): The new investment amount. Defaults to None.

        Raises:
        ValueError: If the plan is not found.
        """
        try:
            if profit_rate:
                self.investment_plans[plan]["profit_rate"] = profit_rate
            if investment_amount:
                self.investment_plans[plan]["investment_amount"] = investment_amount
        except KeyError:
            raise ValueError("Invalid investment plan")

    def calculate_profit(self, plan: InvestmentPlan, investment_amount: float) -> float:
        """Calculate the profit based on the investment plan and amount.

        Args:
        plan (InvestmentPlan): The investment plan.
        investment_amount (float): The investment amount.

        Returns:
        float: The calculated profit.

        Raises:
        ValueError: If the plan is not found or investment amount is less than the plan's minimum investment amount.
        """
        plan_details = self.get_investment_plan_details(plan)
        if investment_amount < plan_details["investment_amount"]:
            raise ValueError("Investment amount must be greater than or equal to the plan's minimum investment amount")
        return investment_amount * plan_details["profit_rate"]

def main():
    # Example usage
    manager = InvestmentPlanManager()
    print(manager.get_investment_plan_details(InvestmentPlan.STARTER))
    manager.update_investment_plan(InvestmentPlan.STARTER, profit_rate=0.07)
    print(manager.get_investment_plan_details(InvestmentPlan.STARTER))
    print(manager.calculate_profit(InvestmentPlan.STARTER, 1000.0))

if __name__ == "__main__":
    main()
```
