"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Generate a list of possible product categories and subcategories for an e-commerce platform selling Homefoods' products, including seasonings, sauces, and ready-to-eat meals.
Generated: DETERMINISTIC_44e2ff2de5c63af2
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_categories.py

from enum import Enum
from typing import List, Dict

class ProductCategory(str, Enum):
    """Enum for product categories."""
    SEASONINGS = "Seasonings"
    SAUCES = "Sauces"
    READY_TO_EAT_MEALS = "Ready-to-Eat Meals"

class ProductSubcategory(str, Enum):
    """Enum for product subcategories."""
    BLENDS = "Blends"
    SINGLE_SPICES = "Single Spices"
    MARINADES = "Marinades"
    COOKING_SAUCES = "Cooking Sauces"
    DIPPING_SAUCES = "Dipping Sauces"
    MEAL_KITS = "Meal Kits"
    PREPARED_MEALS = "Prepared Meals"

class ProductCategoryService:
    """Service for managing product categories and subcategories."""

    def __init__(self):
        self.categories: List[ProductCategory] = list(ProductCategory)
        self.subcategories: Dict[ProductCategory, List[ProductSubcategory]] = {
            ProductCategory.SEASONINGS: [ProductSubcategory.BLENDS, ProductSubcategory.SINGLE_SPICES],
            ProductCategory.SAUCES: [ProductSubcategory.MARINADES, ProductSubcategory.COOKING_SAUCES, ProductSubcategory.DIPPING_SAUCES],
            ProductCategory.READY_TO_EAT_MEALS: [ProductSubcategory.MEAL_KITS, ProductSubcategory.PREPARED_MEALS]
        }

    def get_categories(self) -> List[ProductCategory]:
        """Get a list of product categories."""
        return self.categories

    def get_subcategories(self, category: ProductCategory) -> List[ProductSubcategory]:
        """Get a list of product subcategories for a given category."""
        try:
            return self.subcategories[category]
        except KeyError:
            raise ValueError(f"Invalid category: {category}")

def main():
    service = ProductCategoryService()

    print("Product Categories:")
    for category in service.get_categories():
        print(category)

    print("\nProduct Subcategories:")
    for category in service.get_categories():
        print(f"{category}:")
        subcategories = service.get_subcategories(category)
        for subcategory in subcategories:
            print(f"- {subcategory}")

if __name__ == "__main__":
    main()
```
