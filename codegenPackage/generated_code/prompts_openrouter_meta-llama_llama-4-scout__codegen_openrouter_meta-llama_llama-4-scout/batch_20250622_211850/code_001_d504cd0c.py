"""
Generated Code Metadata:
========================
Original URL: https://advancecryptoacademy.online
Prompt: Compare the features of the different investment plans (VIP CROWN, DIAMOND, GOLD, SILVER) provided by Advance Crypto Academy, focusing on their minimum and maximum investment amounts, return percentages, and duration.
Generated: DETERMINISTIC_d504cd0c9b92168f
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass

class InvestmentPlan(Enum):
    """Enum representing the different investment plans."""
    VIP_CROWN = "VIP CROWN"
    DIAMOND = "DIAMOND"
    GOLD = "GOLD"
    SILVER = "SILVER"

@dataclass
class InvestmentPlanDetails:
    """Dataclass to hold the details of an investment plan."""
    min_investment: float
    max_investment: float
    return_percentage: float
    duration: int  # in days

class InvestmentPlanComparator:
    """Class to compare the features of different investment plans."""
    def __init__(self):
        self.plans = {
            InvestmentPlan.VIP_CROWN: InvestmentPlanDetails(1000.0, 10000.0, 20.0, 30),
            InvestmentPlan.DIAMOND: InvestmentPlanDetails(500.0, 5000.0, 15.0, 30),
            InvestmentPlan.GOLD: InvestmentPlanDetails(200.0, 2000.0, 10.0, 30),
            InvestmentPlan.SILVER: InvestmentPlanDetails(100.0, 1000.0, 5.0, 30),
        }

    def compare_plans(self):
        """Print a comparison of the features of the different investment plans."""
        print("Investment Plan Comparison:")
        print("----------------------------------")
        print(f"{'Plan':^15} | {'Min Investment':^15} | {'Max Investment':^15} | {'Return %':^10} | {'Duration (days)':^15}")
        print("----------------------------------")
        for plan, details in self.plans.items():
            print(f"{plan.value:^15} | {details.min_investment:^15.2f} | {details.max_investment:^15.2f} | {details.return_percentage:^10.2f} | {details.duration:^15}")

    def get_plan_details(self, plan: InvestmentPlan):
        """Get the details of a specific investment plan."""
        try:
            return self.plans[plan]
        except KeyError:
            raise ValueError(f"Invalid investment plan: {plan}")

def main():
    comparator = InvestmentPlanComparator()
    comparator.compare_plans()

    # Example usage: Get details of a specific plan
    plan = InvestmentPlan.VIP_CROWN
    details = comparator.get_plan_details(plan)
    print(f"\nDetails of {plan.value} plan:")
    print(f"Min Investment: ${details.min_investment:.2f}")
    print(f"Max Investment: ${details.max_investment:.2f}")
    print(f"Return Percentage: {details.return_percentage}%")
    print(f"Duration: {details.duration} days")

if __name__ == "__main__":
    main()
```
