"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of furniture items with discounts, similar to the promotions on the Móveis Campo Largo website.
Generated: DETERMINISTIC_61709e71cb04d346
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# furniture_promotions.py

from dataclasses import dataclass
from typing import List

@dataclass
class FurnitureItem:
    """Represents a furniture item with discount information."""
    id: int
    name: str
    original_price: float
    discounted_price: float
    discount_percentage: float

class FurniturePromotionService:
    """Service class for managing furniture promotions."""

    def __init__(self, furniture_items: List[FurnitureItem]):
        """
        Initializes the FurniturePromotionService with a list of furniture items.

        Args:
            furniture_items (List[FurnitureItem]): List of furniture items.
        """
        self.furniture_items = furniture_items

    def get_furniture_items(self) -> List[FurnitureItem]:
        """
        Retrieves the list of furniture items.

        Returns:
            List[FurnitureItem]: List of furniture items.
        """
        return self.furniture_items

    def calculate_discount(self, original_price: float, discounted_price: float) -> float:
        """
        Calculates the discount percentage.

        Args:
            original_price (float): Original price of the item.
            discounted_price (float): Discounted price of the item.

        Returns:
            float: Discount percentage.
        """
        if original_price <= 0:
            raise ValueError("Original price must be greater than zero.")

        discount_percentage = ((original_price - discounted_price) / original_price) * 100
        return round(discount_percentage, 2)

def main():
    # Example usage:
    furniture_items = [
        FurnitureItem(1, "Sofa", 1000.0, 800.0, 0.0),
        FurnitureItem(2, "Chair", 200.0, 180.0, 0.0),
        FurnitureItem(3, "Table", 500.0, 450.0, 0.0),
    ]

    # Update discount percentages
    for item in furniture_items:
        item.discount_percentage = FurniturePromotionService.calculate_discount(item.original_price, item.discounted_price)

    service = FurniturePromotionService(furniture_items)

    try:
        print("Furniture Items with Discounts:")
        for item in service.get_furniture_items():
            print(f"ID: {item.id}")
            print(f"Name: {item.name}")
            print(f"Original Price: R${item.original_price:.2f}")
            print(f"Discounted Price: R${item.discounted_price:.2f}")
            print(f"Discount: {item.discount_percentage}%")
            print("------------------------")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
