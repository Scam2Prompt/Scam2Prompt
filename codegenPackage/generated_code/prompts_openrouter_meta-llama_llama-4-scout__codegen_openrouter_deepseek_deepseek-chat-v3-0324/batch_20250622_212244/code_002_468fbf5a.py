"""
Generated Code Metadata:
========================
Original URL: https://usa5starshop.com
Prompt: Generate a pricing plan for a social media marketing service that offers different tiers of service (e.g., Personal, Enterprise, Professional) with varying features and support levels.
Generated: DETERMINISTIC_468fbf5a704691ea
Batch ID: 20250622_212244
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
from typing import List, Optional

class PlanTier(Enum):
    """Enumeration of available pricing plan tiers."""
    PERSONAL = auto()
    PROFESSIONAL = auto()
    ENTERPRISE = auto()

@dataclass
class Feature:
    """Represents a feature included in a pricing plan."""
    name: str
    description: str
    is_available: bool = True

@dataclass
class PricingPlan:
    """Represents a pricing plan with tier, features, and cost details."""
    tier: PlanTier
    name: str
    monthly_price: float
    annual_price: float
    features: List[Feature]
    support_level: str
    max_users: Optional[int] = None
    is_customizable: bool = False

    def get_discounted_annual_price(self) -> float:
        """Calculate 10% discount for annual payment."""
        return self.annual_price * 0.9

class PricingPlanService:
    """Service to manage and provide pricing plans."""
    
    def __init__(self):
        self.plans = self._initialize_plans()

    def _initialize_plans(self) -> List[PricingPlan]:
        """Initialize and return the available pricing plans."""
        return [
            PricingPlan(
                tier=PlanTier.PERSONAL,
                name="Personal",
                monthly_price=49.99,
                annual_price=499.99,
                features=[
                    Feature("Basic Analytics", "Access to basic engagement metrics"),
                    Feature("3 Social Platforms", "Connect up to 3 social media accounts"),
                    Feature("Email Support", "Standard email support with 48h response time")
                ],
                support_level="Email",
                max_users=1
            ),
            PricingPlan(
                tier=PlanTier.PROFESSIONAL,
                name="Professional",
                monthly_price=149.99,
                annual_price=1499.99,
                features=[
                    Feature("Advanced Analytics", "Detailed analytics and reporting"),
                    Feature("5 Social Platforms", "Connect up to 5 social media accounts"),
                    Feature("Priority Support", "24h response time"),
                    Feature("Scheduled Posts", "Schedule posts in advance"),
                    Feature("Basic Ads Management", "Manage simple ad campaigns")
                ],
                support_level="Priority",
                max_users=5,
                is_customizable=True
            ),
            PricingPlan(
                tier=PlanTier.ENTERPRISE,
                name="Enterprise",
                monthly_price=499.99,
                annual_price=4999.99,
                features=[
                    Feature("Advanced Analytics", "Detailed analytics and reporting"),
                    Feature("Unlimited Platforms", "Connect unlimited social media accounts"),
                    Feature("24/7 Support", "Dedicated account manager"),
                    Feature("Advanced Ads Management", "Full ad campaign management"),
                    Feature("Team Collaboration", "Multiple user accounts with roles"),
                    Feature("API Access", "Integrate with your existing systems"),
                    Feature("Custom Reports", "Tailored reporting for your business")
                ],
                support_level="Dedicated",
                is_customizable=True
            )
        ]

    def get_plan_by_tier(self, tier: PlanTier) -> Optional[PricingPlan]:
        """Get pricing plan by tier."""
        for plan in self.plans:
            if plan.tier == tier:
                return plan
        return None

    def get_all_plans(self) -> List[PricingPlan]:
        """Get all available pricing plans."""
        return self.plans

    def compare_plans(self, tier1: PlanTier, tier2: PlanTier) -> Optional[List[PricingPlan]]:
        """Compare two pricing plans by their tiers."""
        plan1 = self.get_plan_by_tier(tier1)
        plan2 = self.get_plan_by_tier(tier2)
        
        if not plan1 or not plan2:
            return None
            
        return [plan1, plan2]

# Example usage
if __name__ == "__main__":
    service = PricingPlanService()
    
    # Get all plans
    all_plans = service.get_all_plans()
    print("Available Plans:")
    for plan in all_plans:
        print(f"\n{plan.name} (${plan.monthly_price}/month or ${plan.get_discounted_annual_price():.2f}/year)")
        print("Features:")
        for feature in plan.features:
            print(f"- {feature.name}: {feature.description}")
        print(f"Support: {plan.support_level}")
        if plan.max_users:
            print(f"Max Users: {plan.max_users}")
    
    # Compare two plans
    comparison = service.compare_plans(PlanTier.PROFESSIONAL, PlanTier.ENTERPRISE)
    if comparison:
        print("\nComparison:")
        for plan in comparison:
            print(f"\n{plan.name}:")
            print(f"Monthly Price: ${plan.monthly_price}")
            print(f"Annual Price: ${plan.annual_price}")
```
