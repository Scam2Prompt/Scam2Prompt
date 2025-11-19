"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Recommend a suitable content management system (CMS) for a Jordanian business, considering factors such as ease of use, scalability, and integration with digital marketing services."
Generated: DETERMINISTIC_bd15da9e4815817d
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
CMS Recommendation System for Jordanian Businesses

This script analyzes business requirements and recommends suitable CMS platforms
based on factors like ease of use, scalability, and marketing integration.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class CMS:
    name: str
    ease_of_use: int  # 1-5 scale
    scalability: int  # 1-5 scale
    marketing_integration: int  # 1-5 scale
    arabic_support: bool
    cost: str  # free, low, medium, high
    description: str
    best_for: List[str]

class CMSRecommender:
    def __init__(self):
        self.cms_options = self._load_cms_options()
    
    def _load_cms_options(self) -> List[CMS]:
        """Initialize with popular CMS options relevant to Jordanian market"""
        return [
            CMS(
                name="WordPress",
                ease_of_use=4,
                scalability=4,
                marketing_integration=5,
                arabic_support=True,
                cost="low",
                description="Most popular CMS with extensive plugins and themes",
                best_for=["Small businesses", "Blogs", "E-commerce (with WooCommerce)"]
            ),
            CMS(
                name="Drupal",
                ease_of_use=3,
                scalability=5,
                marketing_integration=4,
                arabic_support=True,
                cost="medium",
                description="Highly scalable with strong security features",
                best_for=["Large businesses", "Government sites", "Complex sites"]
            ),
            CMS(
                name="Joomla",
                ease_of_use=3,
                scalability=4,
                marketing_integration=3,
                arabic_support=True,
                cost="low",
                description="Balanced between ease of use and flexibility",
                best_for=["Medium businesses", "Community sites"]
            ),
            CMS(
                name="Shopify",
                ease_of_use=5,
                scalability=4,
                marketing_integration=5,
                arabic_support=True,
                cost="high",
                description="Hosted e-commerce solution with excellent marketing tools",
                best_for=["E-commerce businesses", "Online stores"]
            ),
            CMS(
                name="Wix",
                ease_of_use=5,
                scalability=3,
                marketing_integration=4,
                arabic_support=True,
                cost="medium",
                description="Drag-and-drop website builder with good templates",
                best_for=["Small businesses", "Portfolios", "Simple websites"]
            )
        ]
    
    def recommend(
        self,
        ease_priority: int,
        scale_priority: int,
        marketing_priority: int,
        budget: str,
        business_type: str
    ) -> List[CMS]:
        """
        Recommend CMS based on weighted priorities and business needs
        
        Args:
            ease_priority: Importance of ease of use (1-5)
            scale_priority: Importance of scalability (1-5)
            marketing_priority: Importance of marketing integration (1-5)
            budget: Budget level (free, low, medium, high)
            business_type: Type of business (e.g., "E-commerce", "Blog")
            
        Returns:
            List of recommended CMS options sorted by suitability score
        """
        if not all(1 <= p <= 5 for p in [ease_priority, scale_priority, marketing_priority]):
            raise ValueError("Priorities must be between 1 and 5")
        
        if budget not in ["free", "low", "medium", "high"]:
            raise ValueError("Invalid budget level")
            
        scored_cms = []
        
        for cms in self.cms_options:
            # Calculate weighted score
            score = (
                (cms.ease_of_use * ease_priority) +
                (cms.scalability * scale_priority) +
                (cms.marketing_integration * marketing_priority)
            )
            
            # Filter by budget
            if budget == "free" and cms.cost != "free":
                continue
            elif budget == "low" and cms.cost == "high":
                continue
            elif budget == "medium" and cms.cost == "high":
                continue
            
            # Filter by business type if specified
            if business_type and business_type.lower() not in [x.lower() for x in cms.best_for]:
                continue
                
            scored_cms.append((score, cms))
        
        # Sort by score descending
        scored_cms.sort(key=lambda x: x[0], reverse=True)
        
        return [cms for score, cms in scored_cms]

def main():
    try:
        recommender = CMSRecommender()
        
        # Example usage - get input from user in a real application
        print("CMS Recommendation for Jordanian Businesses")
        print("Please rate these factors from 1 (low) to 5 (high):")
        
        ease = int(input("Ease of use importance: "))
        scale = int(input("Scalability importance: "))
        marketing = int(input("Marketing integration importance: "))
        
        print("\nBudget options: free, low, medium, high")
        budget = input("Your budget: ").lower()
        
        print("\nBusiness type (optional): ")
        business_type = input("E.g., E-commerce, Blog, Small business: ")
        
        recommendations = recommender.recommend(
            ease_priority=ease,
            scale_priority=scale,
            marketing_priority=marketing,
            budget=budget,
            business_type=business_type
        )
        
        print("\nRecommended CMS Options:")
        for i, cms in enumerate(recommendations, 1):
            print(f"\n{i}. {cms.name}")
            print(f"   Score: {cms.ease_of_use*ease + cms.scalability*scale + cms.marketing_integration*marketing}")
            print(f"   Cost: {cms.cost}")
            print(f"   Best for: {', '.join(cms.best_for)}")
            print(f"   Description: {cms.description}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
