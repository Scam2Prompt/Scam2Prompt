"""
Generated Code Metadata:
========================
Original URL: https://villapanorea.com
Prompt: Recommend a customer relationship management (CRM) system for a small hospitality business, considering features like guest review management and personalized offers.
Generated: DETERMINISTIC_0a4aaa5508f9aca5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CRM System Recommendation for Small Hospitality Business
"""

import json
from typing import Dict, List, Optional

class CRMSystem:
    """Base class for CRM system recommendations."""
    
    def __init__(self, name: str, features: List[str], pricing: Dict[str, float]):
        self.name = name
        self.features = features
        self.pricing = pricing
    
    def has_feature(self, feature: str) -> bool:
        """Check if CRM has a specific feature."""
        return feature.lower() in [f.lower() for f in self.features]
    
    def get_pricing_plan(self, plan: str) -> Optional[float]:
        """Get pricing for a specific plan."""
        return self.pricing.get(plan.lower())
    
    def to_dict(self) -> Dict:
        """Convert CRM details to dictionary."""
        return {
            "name": self.name,
            "features": self.features,
            "pricing": self.pricing
        }

def recommend_crm(business_type: str, required_features: List[str], budget: Optional[float] = None) -> List[CRMSystem]:
    """
    Recommend CRM systems based on business type, required features, and budget.
    
    Args:
        business_type: Type of business (e.g., 'hospitality')
        required_features: List of required features
        budget: Optional budget constraint
        
    Returns:
        List of recommended CRM systems
    """
    # Database of CRM systems (in a real app, this would be from a database or API)
    crm_systems = [
        CRMSystem(
            name="HubSpot",
            features=[
                "Contact Management",
                "Email Marketing",
                "Guest Review Management",
                "Personalized Offers",
                "Analytics"
            ],
            pricing={
                "starter": 45,
                "professional": 800,
                "enterprise": 3200
            }
        ),
        CRMSystem(
            name="Zoho CRM",
            features=[
                "Contact Management",
                "Workflow Automation",
                "Guest Review Management",
                "Mobile App"
            ],
            pricing={
                "standard": 20,
                "professional": 35,
                "enterprise": 50
            }
        ),
        CRMSystem(
            name="Salesforce",
            features=[
                "Contact Management",
                "Advanced Analytics",
                "Personalized Offers",
                "AI-powered Insights"
            ],
            pricing={
                "essentials": 25,
                "professional": 75,
                "enterprise": 150
            }
        ),
        CRMSystem(
            name="Little Hotelier",
            features=[
                "Property Management",
                "Guest Review Management",
                "Booking Engine",
                "Personalized Offers",
                "Hospitality-specific"
            ],
            pricing={
                "basic": 99,
                "premium": 199
            }
        )
    ]
    
    # Filter CRM systems by business type and features
    recommended = []
    for crm in crm_systems:
        # Check if all required features are present
        has_all_features = all(crm.has_feature(feat) for feat in required_features)
        
        if has_all_features:
            if budget is not None:
                # Check if any pricing plan fits within budget
                fits_budget = any(
                    price <= budget 
                    for price in crm.pricing.values() 
                    if price is not None
                )
                if fits_budget:
                    recommended.append(crm)
            else:
                recommended.append(crm)
    
    # Sort by lowest starting price
    recommended.sort(key=lambda x: min(x.pricing.values()))
    
    return recommended

def main():
    """Example usage of the CRM recommendation system."""
    try:
        # Example: Small hospitality business needs
        business_type = "hospitality"
        required_features = ["Guest Review Management", "Personalized Offers"]
        budget = 100.0
        
        recommendations = recommend_crm(business_type, required_features, budget)
        
        print(f"Recommended CRM Systems for {business_type}:")
        for idx, crm in enumerate(recommendations, 1):
            print(f"\n{idx}. {crm.name}")
            print("Features:")
            for feature in crm.features:
                print(f" - {feature}")
            print("Pricing Plans:")
            for plan, price in crm.pricing.items():
                print(f" - {plan.capitalize()}: ${price}/month")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
