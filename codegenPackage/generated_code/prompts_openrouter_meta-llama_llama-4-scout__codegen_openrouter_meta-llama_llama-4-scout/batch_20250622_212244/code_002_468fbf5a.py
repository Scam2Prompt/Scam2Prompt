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
from enum import Enum
from typing import List, Dict

class SupportLevel(Enum):
    """Enum for support levels"""
    BASIC = "Basic"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"

class PricingPlan:
    """Class representing a pricing plan"""
    def __init__(self, name: str, price: float, features: List[str], support_level: SupportLevel):
        """
        Initialize a pricing plan

        Args:
        - name (str): Name of the plan
        - price (float): Price of the plan
        - features (List[str]): Features included in the plan
        - support_level (SupportLevel): Support level of the plan
        """
        self.name = name
        self.price = price
        self.features = features
        self.support_level = support_level

    def __str__(self):
        return f"Plan: {self.name}, Price: ${self.price:.2f}, Features: {', '.join(self.features)}, Support: {self.support_level.value}"

class PricingService:
    """Class representing a pricing service"""
    def __init__(self):
        self.plans: Dict[str, PricingPlan] = {}

    def add_plan(self, plan: PricingPlan):
        """
        Add a plan to the pricing service

        Args:
        - plan (PricingPlan): Plan to add
        """
        self.plans[plan.name] = plan

    def get_plan(self, name: str) -> PricingPlan:
        """
        Get a plan by name

        Args:
        - name (str): Name of the plan

        Returns:
        - PricingPlan: Plan with the given name, or None if not found
        """
        return self.plans.get(name)

    def list_plans(self) -> List[PricingPlan]:
        """
        List all plans

        Returns:
        - List[PricingPlan]: List of all plans
        """
        return list(self.plans.values())

def main():
    try:
        # Create pricing service
        pricing_service = PricingService()

        # Create plans
        personal_plan = PricingPlan(
            "Personal",
            9.99,
            ["Social media monitoring", "Basic analytics"],
            SupportLevel.BASIC
        )
        professional_plan = PricingPlan(
            "Professional",
            49.99,
            ["Social media monitoring", "Advanced analytics", "Content creation"],
            SupportLevel.PREMIUM
        )
        enterprise_plan = PricingPlan(
            "Enterprise",
            199.99,
            ["Social media monitoring", "Advanced analytics", "Content creation", "Dedicated support"],
            SupportLevel.ENTERPRISE
        )

        # Add plans to pricing service
        pricing_service.add_plan(personal_plan)
        pricing_service.add_plan(professional_plan)
        pricing_service.add_plan(enterprise_plan)

        # List plans
        print("Pricing Plans:")
        for plan in pricing_service.list_plans():
            print(plan)

        # Get plan
        print("\nGet Plan:")
        plan = pricing_service.get_plan("Professional")
        if plan:
            print(plan)
        else:
            print("Plan not found")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
