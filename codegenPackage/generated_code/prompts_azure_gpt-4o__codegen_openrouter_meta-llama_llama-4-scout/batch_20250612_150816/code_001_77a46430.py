"""
Generated Code Metadata:
========================
Original URL: https://fintradeoptions.com
Prompt: Generate code to implement an investment plan selection system for Fintradeoptions, allowing users to choose between Starter, Premium, Advanced, Pro, and Trial plans and calculate returns.
Generated: DETERMINISTIC_77a46430b89c0f01
Batch ID: 20250612_150816
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

class PlanType(str, Enum):
    """ Enum for plan types """
    STARTER = "Starter"
    PREMIUM = "Premium"
    ADVANCED = "Advanced"
    PRO = "Pro"
    TRIAL = "Trial"

class InvestmentPlan:
    """ Class representing an investment plan """

    def __init__(self, plan_type: PlanType, principal: float, rate: float, duration: int):
        """
        Initialize an investment plan

        Args:
        - plan_type (PlanType): Type of plan
        - principal (float): Initial investment amount
        - rate (float): Rate of return as a decimal
        - duration (int): Duration of investment in years
        """
        self.plan_type = plan_type
        self.principal = principal
        self.rate = rate
        self.duration = duration

    def calculate_returns(self) -> float:
        """
        Calculate returns based on the plan details

        Returns:
        - float: Total returns
        """
        # Calculate total returns using compound interest formula
        returns = self.principal * (1 + self.rate) ** self.duration
        return returns

class InvestmentPlanSelector:
    """ Class for selecting investment plans and calculating returns """

    def __init__(self):
        # Define plan details as a dictionary
        self.plans: Dict[PlanType, Dict[str, float]] = {
            PlanType.STARTER: {"rate": 0.05, "min_principal": 1000},
            PlanType.PREMIUM: {"rate": 0.07, "min_principal": 5000},
            PlanType.ADVANCED: {"rate": 0.10, "min_principal": 10000},
            PlanType.PRO: {"rate": 0.12, "min_principal": 50000},
            PlanType.TRIAL: {"rate": 0.03, "min_principal": 100},
        }

    def select_plan(self, plan_type: PlanType, principal: float, duration: int) -> InvestmentPlan:
        """
        Select an investment plan and validate input

        Args:
        - plan_type (PlanType): Type of plan
        - principal (float): Initial investment amount
        - duration (int): Duration of investment in years

        Returns:
        - InvestmentPlan: Selected investment plan

        Raises:
        - ValueError: If plan type is invalid or principal is less than minimum required
        """
        if plan_type not in self.plans:
            raise ValueError("Invalid plan type")

        plan_details = self.plans[plan_type]
        if principal < plan_details["min_principal"]:
            raise ValueError(f"Principal must be at least {plan_details['min_principal']}")

        rate = plan_details["rate"]
        return InvestmentPlan(plan_type, principal, rate, duration)

def main():
    selector = InvestmentPlanSelector()

    # Example usage
    try:
        plan = selector.select_plan(PlanType.PREMIUM, 10000, 5)
        returns = plan.calculate_returns()
        print(f"Plan: {plan.plan_type.value}")
        print(f"Returns: {returns:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
