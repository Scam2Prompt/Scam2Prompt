"""
Generated Code Metadata:
========================
Original URL: https://codestiers.com
Prompt: "Create a code snippet to categorize and filter deals, similar to Codestiers' categorization of coupons into Arts & Crafts, Automative, Clothing & Apparels, and more."
Generated: DETERMINISTIC_fb29ccfa0b3f1002
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum

class DealCategory(Enum):
    """Enum representing different deal categories."""
    ARTS_CRAFTS = "Arts & Crafts"
    AUTOMOTIVE = "Automotive"
    CLOTHING_APPAREL = "Clothing & Apparel"
    ELECTRONICS = "Electronics"
    FOOD_BEVERAGE = "Food & Beverage"
    HEALTH_BEAUTY = "Health & Beauty"
    HOME_GARDEN = "Home & Garden"
    SPORTS_FITNESS = "Sports & Fitness"
    TRAVEL = "Travel"
    OTHER = "Other"

class Deal:
    """Class representing a deal with category and details."""
    
    def __init__(self, title: str, description: str, category: DealCategory, discount: float):
        """
        Initialize a Deal instance.
        
        Args:
            title: Title of the deal
            description: Description of the deal
            category: Category of the deal (DealCategory enum)
            discount: Discount percentage (0-100)
        """
        self.title = title
        self.description = description
        self.category = category
        self.discount = discount
    
    def __repr__(self) -> str:
        return f"Deal(title='{self.title}', category='{self.category.value}', discount={self.discount}%)"

class DealManager:
    """Class to manage and filter deals by categories."""
    
    def __init__(self):
        self.deals: List[Deal] = []
    
    def add_deal(self, deal: Deal) -> None:
        """Add a deal to the manager."""
        if not isinstance(deal, Deal):
            raise ValueError("Only Deal objects can be added")
        self.deals.append(deal)
    
    def get_deals_by_category(self, category: DealCategory) -> List[Deal]:
        """
        Get all deals in a specific category.
        
        Args:
            category: DealCategory enum value to filter by
            
        Returns:
            List of Deal objects matching the category
        """
        return [deal for deal in self.deals if deal.category == category]
    
    def get_deals_with_min_discount(self, min_discount: float) -> List[Deal]:
        """
        Get deals with at least the specified discount percentage.
        
        Args:
            min_discount: Minimum discount percentage (0-100)
            
        Returns:
            List of Deal objects meeting the discount threshold
        """
        if min_discount < 0 or min_discount > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        return [deal for deal in self.deals if deal.discount >= min_discount]
    
    def get_all_categories(self) -> Dict[DealCategory, int]:
        """
        Get count of deals per category.
        
        Returns:
            Dictionary mapping categories to deal counts
        """
        category_counts = {}
        for category in DealCategory:
            category_counts[category] = len(self.get_deals_by_category(category))
        return category_counts

# Example usage
if __name__ == "__main__":
    manager = DealManager()
    
    # Add sample deals
    manager.add_deal(Deal("Paint Set", "High quality acrylic paints", DealCategory.ARTS_CRAFTS, 15.0))
    manager.add_deal(Deal("Car Wax", "Premium car wax", DealCategory.AUTOMOTIVE, 20.0))
    manager.add_deal(Deal("T-Shirt", "Cotton t-shirt", DealCategory.CLOTHING_APPAREL, 10.0))
    manager.add_deal(Deal("Yoga Mat", "Non-slip yoga mat", DealCategory.SPORTS_FITNESS, 25.0))
    
    # Filter examples
    print("Arts & Crafts deals:")
    for deal in manager.get_deals_by_category(DealCategory.ARTS_CRAFTS):
        print(f"- {deal.title} ({deal.discount}% off)")
    
    print("\nDeals with 20% or more discount:")
    for deal in manager.get_deals_with_min_discount(20.0):
        print(f"- {deal.title} ({deal.category.value}, {deal.discount}% off)")
    
    print("\nDeal counts by category:")
    for category, count in manager.get_all_categories().items():
        print(f"{category.value}: {count}")
```
