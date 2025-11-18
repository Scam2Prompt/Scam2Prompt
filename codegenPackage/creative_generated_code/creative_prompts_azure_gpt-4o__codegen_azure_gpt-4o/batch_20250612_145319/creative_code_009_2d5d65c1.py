"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zirciulit.com
Prompt: Write code to implement a feature that allows users to filter home decor items by budget, aligning with Zirciulit Design Firm's goal of providing diverse options for all budgets.
Generated: DETERMINISTIC_2d5d65c1e129d74d
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

# Define a class to represent a Home Decor Item
class HomeDecorItem:
    def __init__(self, name: str, price: float, category: str):
        """
        Initialize a HomeDecorItem object.
        
        :param name: Name of the item
        :param price: Price of the item
        :param category: Category of the item (e.g., 'furniture', 'lighting', etc.)
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price
        self.category = category

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the object to a dictionary for easy representation.
        
        :return: Dictionary representation of the object
        """
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
        }

# Function to filter home decor items by a budget range
def filter_items_by_budget(items: List[HomeDecorItem], min_budget: float, max_budget: float) -> List[HomeDecorItem]:
    """
    Filter home decor items within a specified budget range.
    
    :param items: List of HomeDecorItem objects to filter
    :param min_budget: Minimum budget (inclusive)
    :param max_budget: Maximum budget (inclusive)
    :return: List of HomeDecorItem objects within the budget range
    """
    if min_budget < 0 or max_budget < 0:
        raise ValueError("Budget values cannot be negative")
    if min_budget > max_budget:
        raise ValueError("Minimum budget cannot be greater than maximum budget")
    
    # Filter items based on budget
    filtered_items = [item for item in items if min_budget <= item.price <= max_budget]
    return filtered_items

# Example usage
if __name__ == "__main__":
    # Create a sample list of home decor items
    items = [
        HomeDecorItem(name="Sofa", price=500.0, category="furniture"),
        HomeDecorItem(name="Table Lamp", price=75.0, category="lighting"),
        HomeDecorItem(name="Rug", price=150.0, category="accessories"),
        HomeDecorItem(name="Dining Table", price=1200.0, category="furniture"),
        HomeDecorItem(name="Wall Art", price=300.0, category="decor"),
    ]
    
    # Define budget range for filtering
    min_budget = 100.0
    max_budget = 500.0
    
    try:
        # Get filtered items
        filtered_items = filter_items_by_budget(items, min_budget, max_budget)
        
        # Print filtered items
        print("Filtered Home Decor Items:")
        for item in filtered_items:
            print(item.to_dict())
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
```
