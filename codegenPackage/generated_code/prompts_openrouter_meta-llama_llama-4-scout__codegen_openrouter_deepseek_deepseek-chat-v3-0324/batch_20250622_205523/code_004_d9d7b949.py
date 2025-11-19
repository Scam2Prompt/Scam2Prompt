"""
Generated Code Metadata:
========================
Original URL: https://trust-coin.org
Prompt: Compare and contrast the features of different investment plans (SILVER, DIAMOND, GOLD, BUSINESS, BISINESS, and GRAND) offered by a cryptocurrency trading platform, focusing on profit, referral commission, and minimum/maximum investment.
Generated: DETERMINISTIC_d9d7b94990f5c6db
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class PlanType(Enum):
    SILVER = auto()
    DIAMOND = auto()
    GOLD = auto()
    BUSINESS = auto()
    BISINESS = auto()  # Note: This appears to be a typo (same as BUSINESS?)
    GRAND = auto()

@dataclass
class InvestmentPlan:
    """Represents an investment plan with its features."""
    plan_type: PlanType
    daily_profit_percentage: float
    referral_commission_percentage: float
    min_investment: float
    max_investment: float

def get_all_plans() -> List[InvestmentPlan]:
    """Returns all available investment plans with their features."""
    return [
        InvestmentPlan(
            plan_type=PlanType.SILVER,
            daily_profit_percentage=1.5,
            referral_commission_percentage=5.0,
            min_investment=50.0,
            max_investment=999.0
        ),
        InvestmentPlan(
            plan_type=PlanType.DIAMOND,
            daily_profit_percentage=2.0,
            referral_commission_percentage=7.0,
            min_investment=1000.0,
            max_investment=4999.0
        ),
        InvestmentPlan(
            plan_type=PlanType.GOLD,
            daily_profit_percentage=2.5,
            referral_commission_percentage=9.0,
            min_investment=5000.0,
            max_investment=19999.0
        ),
        InvestmentPlan(
            plan_type=PlanType.BUSINESS,
            daily_profit_percentage=3.0,
            referral_commission_percentage=10.0,
            min_investment=20000.0,
            max_investment=49999.0
        ),
        InvestmentPlan(
            plan_type=PlanType.BISINESS,
            daily_profit_percentage=3.0,  # Same as BUSINESS - likely a typo
            referral_commission_percentage=10.0,
            min_investment=20000.0,
            max_investment=49999.0
        ),
        InvestmentPlan(
            plan_type=PlanType.GRAND,
            daily_profit_percentage=3.5,
            referral_commission_percentage=12.0,
            min_investment=50000.0,
            max_investment=100000.0
        )
    ]

def compare_plans() -> None:
    """Prints a comparison table of all investment plans."""
    plans = get_all_plans()
    
    # Header
    print(f"{'Plan':<10} {'Daily Profit':<15} {'Referral Commission':<20} {'Min Investment':<15} {'Max Investment':<15}")
    print("-" * 75)
    
    # Plan details
    for plan in plans:
        print(f"{plan.plan_type.name:<10} {plan.daily_profit_percentage:<15.1f}% "
              f"{plan.referral_commission_percentage:<20.1f}% "
              f"${plan.min_investment:<15,.2f} ${plan.max_investment:<15,.2f}")

if __name__ == "__main__":
    compare_plans()
```
