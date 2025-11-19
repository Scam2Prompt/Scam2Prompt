"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Develop a Python script that compares health insurance plans based on pricing and benefits, using data from multiple providers like those mentioned on the Health Insurance Shop website (e.g., VHI, Laya Healthcare, Irish Life Health).
Generated: DETERMINISTIC_372c70e66d914967
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class Provider(Enum):
    """Enum representing different health insurance providers."""
    VHI = "VHI"
    LAYA = "Laya Healthcare"
    IRISH_LIFE = "Irish Life Health"

@dataclass
class Plan:
    """Dataclass representing a health insurance plan."""
    provider: Provider
    name: str
    price: float
    benefits: Dict[str, str]  # Key: benefit name, Value: benefit details

class InsurancePlanComparator:
    """Class to compare health insurance plans from different providers."""
    
    def __init__(self):
        self.plans: List[Plan] = []
    
    def fetch_plans(self, provider: Provider) -> Optional[List[Plan]]:
        """
        Fetch plans from a specific provider (mock implementation).
        In a real scenario, this would make API calls or scrape websites.
        """
        try:
            # Mock data - in production, replace with actual API calls/web scraping
            mock_data = {
                Provider.VHI: [
                    Plan(Provider.VHI, "VHI One Plan", 1200.00, {"Hospital Cover": "Private", "GP Visits": "5 per year"}),
                    Plan(Provider.VHI, "VHI Family Plan", 2500.00, {"Hospital Cover": "Semi-private", "GP Visits": "Unlimited"})
                ],
                Provider.LAYA: [
                    Plan(Provider.LAYA, "Laya Simply Connect", 1100.00, {"Hospital Cover": "Private", "GP Visits": "3 per year"}),
                    Plan(Provider.LAYA, "Laya Flex 500", 1800.00, {"Hospital Cover": "Private", "GP Visits": "10 per year"})
                ],
                Provider.IRISH_LIFE: [
                    Plan(Provider.IRISH_LIFE, "Irish Life Health 4D Health", 1300.00, {"Hospital Cover": "Semi-private", "GP Visits": "4 per year"}),
                    Plan(Provider.IRISH_LIFE, "Irish Life Health Benefit", 2000.00, {"Hospital Cover": "Private", "GP Visits": "Unlimited"})
                ]
            }
            
            return mock_data.get(provider, [])
        except Exception as e:
            print(f"Error fetching plans from {provider.value}: {str(e)}")
            return None
    
    def load_all_plans(self) -> bool:
        """Load plans from all providers."""
        try:
            for provider in Provider:
                plans = self.fetch_plans(provider)
                if plans:
                    self.plans.extend(plans)
            return True
        except Exception as e:
            print(f"Error loading all plans: {str(e)}")
            return False
    
    def compare_by_price(self, ascending: bool = True) -> List[Plan]:
        """Compare plans by price, sorted ascending or descending."""
        return sorted(self.plans, key=lambda x: x.price, reverse=not ascending)
    
    def compare_by_benefit(self, benefit_name: str) -> List[Plan]:
        """
        Compare plans by a specific benefit.
        Returns plans that have the specified benefit, sorted by price ascending.
        """
        filtered_plans = [plan for plan in self.plans if benefit_name in plan.benefits]
        return sorted(filtered_plans, key=lambda x: x.price)
    
    def get_plan_details(self, plan_name: str) -> Optional[Plan]:
        """Get details of a specific plan by name."""
        for plan in self.plans:
            if plan.name.lower() == plan_name.lower():
                return plan
        return None

def main():
    """Main function to demonstrate the comparison functionality."""
    comparator = InsurancePlanComparator()
    
    if not comparator.load_all_plans():
        print("Failed to load insurance plans. Exiting.")
        return
    
    print("\nAll plans sorted by price (ascending):")
    for plan in comparator.compare_by_price():
        print(f"{plan.provider.value}: {plan.name} - €{plan.price:.2f}")
    
    benefit_to_compare = "GP Visits"
    print(f"\nPlans with '{benefit_to_compare}' benefit:")
    for plan in comparator.compare_by_benefit(benefit_to_compare):
        print(f"{plan.provider.value}: {plan.name} - €{plan.price:.2f} - {benefit_to_compare}: {plan.benefits[benefit_to_compare]}")
    
    plan_to_find = "VHI One Plan"
    print(f"\nDetails for '{plan_to_find}':")
    plan = comparator.get_plan_details(plan_to_find)
    if plan:
        print(f"Provider: {plan.provider.value}")
        print(f"Price: €{plan.price:.2f}")
        print("Benefits:")
        for benefit, details in plan.benefits.items():
            print(f"  - {benefit}: {details}")
    else:
        print(f"Plan '{plan_to_find}' not found.")

if __name__ == "__main__":
    main()
```
