"""
Generated Code Metadata:
========================
Original URL: https://theaflac.com
Prompt: Recommend a suitable Aflac insurance product for a small business owner in Oklahoma, taking into account the state's specific policy forms (e.g., QN81100MOK) and regulations.
Generated: DETERMINISTIC_e5e500930a2b5f8d
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class AflacProductRecommender:
    """
    Recommends suitable Aflac insurance products for small business owners in Oklahoma.
    Handles Oklahoma-specific policy forms and regulations.
    """
    
    def __init__(self):
        self.oklahoma_policies = self._load_oklahoma_policies()
    
    def _load_oklahoma_policies(self) -> Dict:
        """Load Oklahoma-specific policy data"""
        return {
            "QN81100MOK": {
                "name": "Accident Insurance",
                "description": "Provides cash benefits for covered accidents",
                "business_types": ["retail", "restaurant", "construction"],
                "employee_count_range": (1, 50)
            },
            "QN81200MOK": {
                "name": "Critical Illness Insurance",
                "description": "Provides lump-sum payment for covered critical illnesses",
                "business_types": ["professional", "medical", "financial"],
                "employee_count_range": (1, 100)
            },
            "QN81300MOK": {
                "name": "Hospital Indemnity Insurance",
                "description": "Provides cash benefits for hospital stays",
                "business_types": ["all"],
                "employee_count_range": (1, 200)
            },
            "QN81400MOK": {
                "name": "Dental Insurance",
                "description": "Provides coverage for dental procedures",
                "business_types": ["all"],
                "employee_count_range": (1, 500)
            }
        }
    
    def recommend_products(self, business_type: str, employee_count: int) -> List[Dict]:
        """
        Recommends Aflac products based on business type and size.
        
        Args:
            business_type: Type of business (e.g., 'retail', 'medical')
            employee_count: Number of employees in the business
            
        Returns:
            List of recommended products with details
        """
        if not isinstance(employee_count, int) or employee_count <= 0:
            raise ValueError("Employee count must be a positive integer")
            
        if not business_type or not isinstance(business_type, str):
            raise ValueError("Business type must be a non-empty string")
            
        recommendations = []
        
        for policy_id, policy in self.oklahoma_policies.items():
            if (business_type.lower() in policy["business_types"] or 
                "all" in policy["business_types"]):
                min_emp, max_emp = policy["employee_count_range"]
                if min_emp <= employee_count <= max_emp:
                    recommendations.append({
                        "policy_id": policy_id,
                        "name": policy["name"],
                        "description": policy["description"],
                        "suitability": self._calculate_suitability_score(
                            business_type, employee_count, policy
                        )
                    })
        
        # Sort by suitability score (descending)
        return sorted(recommendations, key=lambda x: x["suitability"], reverse=True)
    
    def _calculate_suitability_score(self, 
                                   business_type: str, 
                                   employee_count: int, 
                                   policy: Dict) -> float:
        """
        Calculates a suitability score (0-1) for a policy based on business characteristics.
        """
        type_match = 0.5 if "all" in policy["business_types"] else 1.0
        min_emp, max_emp = policy["employee_count_range"]
        size_match = 1 - (abs(employee_count - (min_emp + max_emp)/2) / (max_emp - min_emp))
        
        return (type_match * 0.6) + (size_match * 0.4)

# Example usage
if __name__ == "__main__":
    try:
        recommender = AflacProductRecommender()
        business_type = "medical"
        employee_count = 15
        recommendations = recommender.recommend_products(business_type, employee_count)
        
        print(f"Recommended Aflac products for {business_type} business with {employee_count} employees:")
        for product in recommendations:
            print(f"\nPolicy ID: {product['policy_id']}")
            print(f"Product: {product['name']}")
            print(f"Description: {product['description']}")
            print(f"Suitability Score: {product['suitability']:.2f}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
