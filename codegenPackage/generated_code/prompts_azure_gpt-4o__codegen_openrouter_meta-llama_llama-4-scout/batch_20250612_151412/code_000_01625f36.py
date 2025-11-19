"""
Generated Code Metadata:
========================
Original URL: https://thechampionsshop.com
Prompt: Write code to create a shopping cart system for a website selling replica wrestling championship belts, including categories like AEW Belts, WWE Belts, and MLB Title Belts.
Generated: DETERMINISTIC_01625f360ddfb1ef
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart_system.py

from enum import Enum
from typing import Dict, List

class BeltCategory(str, Enum):
    """Enum for belt categories."""
    AEW = "AEW Belts"
    WWE = "WWE Belts"
    MLB = "MLB Title Belts"

class Belt:
    """Class representing a wrestling championship belt."""
    def __init__(self, id: int, name: str, category: BeltCategory, price: float):
        """
        Initialize a Belt object.

        Args:
        id (int): Unique identifier for the belt.
        name (str): Name of the belt.
        category (BeltCategory): Category of the belt.
        price (float): Price of the belt.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price

class ShoppingCart:
    """Class representing a shopping cart."""
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[int, int] = {}  # belt_id: quantity

    def add_item(self, belt: Belt, quantity: int):
        """
        Add a belt to the shopping cart.

        Args:
        belt (Belt): Belt to add.
        quantity (int): Quantity of the belt to add.

        Raises:
        ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if belt.id in self.items:
            self.items[belt.id] += quantity
        else:
            self.items[belt.id] = quantity

    def remove_item(self, belt_id: int):
        """
        Remove a belt from the shopping cart.

        Args:
        belt_id (int): ID of the belt to remove.

        Raises:
        KeyError: If the belt is not in the shopping cart.
        """
        if belt_id not in self.items:
            raise KeyError("Belt not found in shopping cart")
        del self.items[belt_id]

    def update_quantity(self, belt_id: int, quantity: int):
        """
        Update the quantity of a belt in the shopping cart.

        Args:
        belt_id (int): ID of the belt to update.
        quantity (int): New quantity of the belt.

        Raises:
        KeyError: If the belt is not in the shopping cart.
        ValueError: If quantity is less than 1.
        """
        if belt_id not in self.items:
            raise KeyError("Belt not found in shopping cart")
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")
        self.items[belt_id] = quantity

    def calculate_total(self, belts: List[Belt]) -> float:
        """
        Calculate the total cost of the items in the shopping cart.

        Args:
        belts (List[Belt]): List of all available belts.

        Returns:
        float: Total cost of the items in the shopping cart.
        """
        total = 0.0
        for belt_id, quantity in self.items.items():
            belt = next((belt for belt in belts if belt.id == belt_id), None)
            if belt:
                total += belt.price * quantity
        return total

def main():
    # Create belts
    belts = [
        Belt(1, "AEW World Championship", BeltCategory.AEW, 49.99),
        Belt(2, "WWE Championship", BeltCategory.WWE, 59.99),
        Belt(3, "MLB World Series Championship", BeltCategory.MLB, 39.99),
    ]

    # Create shopping cart
    cart = ShoppingCart()

    # Add items to cart
    cart.add_item(belts[0], 2)
    cart.add_item(belts[1], 1)

    # Calculate total
    total = cart.calculate_total(belts)
    print(f"Total: ${total:.2f}")

    # Update quantity
    cart.update_quantity(1, 3)
    total = cart.calculate_total(belts)
    print(f"Updated Total: ${total:.2f}")

    # Remove item
    cart.remove_item(2)
    total = cart.calculate_total(belts)
    print(f"Total after removal: ${total:.2f}")

if __name__ == "__main__":
    main()
```
