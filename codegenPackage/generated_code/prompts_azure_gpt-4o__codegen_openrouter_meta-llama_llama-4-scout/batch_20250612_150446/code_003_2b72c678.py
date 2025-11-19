"""
Generated Code Metadata:
========================
Original URL: https://digitalwealthtraders.com
Prompt: Create a program to simulate an investment plan with parameters like minimum deposit, duration, and fixed interest rates, as outlined in Digitalwealthtraders' Bronze, Silver, Gold, and Platinum plans.
Generated: DETERMINISTIC_2b72c67896f0f1f9
Batch ID: 20250612_150446
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
    """Enum representing the different investment plans."""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4

class InvestmentPlanDetails:
    """Class to hold investment plan details."""
    def __init__(self, 
                 min_deposit: float, 
                 duration: int, 
                 interest_rate: float):
        """
        Initialize investment plan details.

        Args:
        - min_deposit (float): The minimum deposit required.
        - duration (int): The duration of the investment plan in months.
        - interest_rate (float): The fixed interest rate.
        """
        self.min_deposit = min_deposit
        self.duration = duration
        self.interest_rate = interest_rate

class InvestmentSimulator:
    """Class to simulate an investment plan."""
    def __init__(self):
        # Define investment plans
        self.plans: Dict[InvestmentPlan, InvestmentPlanDetails] = {
            InvestmentPlan.BRONZE: InvestmentPlanDetails(500, 6, 0.02),
            InvestmentPlan.SILVER: InvestmentPlanDetails(1000, 12, 0.04),
            InvestmentPlan.GOLD: InvestmentPlanDetails(5000, 24, 0.06),
            InvestmentPlan.PLATINUM: InvestmentPlanDetails(10000, 36, 0.08)
        }

    def simulate_investment(self, plan: InvestmentPlan, principal: float) -> Dict[str, float]:
        """
        Simulate an investment plan.

        Args:
        - plan (InvestmentPlan): The investment plan to simulate.
        - principal (float): The initial investment amount.

        Returns:
        - A dictionary containing the final amount and interest earned.

        Raises:
        - ValueError: If the principal is less than the minimum deposit.
        """
        plan_details = self.plans.get(plan)
        if plan_details is None:
            raise ValueError("Invalid investment plan")

        if principal < plan_details.min_deposit:
            raise ValueError(f"Principal must be at least {plan_details.min_deposit}")

        # Calculate the final amount using compound interest formula
        final_amount = principal * (1 + plan_details.interest_rate / 12) ** (plan_details.duration)
        interest_earned = final_amount - principal

        return {
            "final_amount": round(final_amount, 2),
            "interest_earned": round(interest_earned, 2)
        }

def main():
    simulator = InvestmentSimulator()

    # Example usage
    plan = InvestmentPlan.GOLD
    principal = 5000

    try:
        result = simulator.simulate_investment(plan, principal)
        print(f"Simulating {plan.name} plan with a principal of {principal}:")
        print(f"Final Amount: {result['final_amount']}")
        print(f"Interest Earned: {result['interest_earned']}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
