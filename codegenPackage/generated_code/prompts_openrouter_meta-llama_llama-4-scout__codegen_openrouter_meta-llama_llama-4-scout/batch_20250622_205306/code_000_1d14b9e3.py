"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Write a Python code to manage an e-commerce jewelry store's inventory, including categories like RINGS, EARRINGS, and PENDANTS.
Generated: DETERMINISTIC_1d14b9e30b4ef74d
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

from enum import Enum
from typing import Dict, List

class JewelryCategory(str, Enum):
    """Enum for jewelry categories."""
    RINGS = "RINGS"
    EARRINGS = "EARRINGS"
    PENDANTS = "PENDANTS"

class JewelryItem:
    """Represents a jewelry item in the inventory."""
    
    def __init__(self, item_id: int, name: str, category: JewelryCategory, price: float, quantity: int):
        """
        Initializes a JewelryItem.

        Args:
        item_id (int): Unique identifier for the item.
        name (str): Name of the jewelry item.
        category (JewelryCategory): Category of the jewelry item.
        price (float): Price of the jewelry item.
        quantity (int): Quantity of the jewelry item in stock.
        """
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"JewelryItem(item_id={self.item_id}, name='{self.name}', category={self.category}, price={self.price}, quantity={self.quantity})"


class Inventory:
    """Manages the jewelry store's inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.items: Dict[int, JewelryItem] = {}

    def add_item(self, item: JewelryItem):
        """
        Adds a jewelry item to the inventory.

        Args:
        item (JewelryItem): The item to add.

        Raises:
        ValueError: If an item with the same ID already exists.
        """
        if item.item_id in self.items:
            raise ValueError(f"Item with ID {item.item_id} already exists.")
        self.items[item.item_id] = item

    def remove_item(self, item_id: int):
        """
        Removes a jewelry item from the inventory.

        Args:
        item_id (int): The ID of the item to remove.

        Raises:
        KeyError: If the item does not exist in the inventory.
        """
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist.")
        del self.items[item_id]

    def update_quantity(self, item_id: int, new_quantity: int):
        """
        Updates the quantity of a jewelry item.

        Args:
        item_id (int): The ID of the item to update.
        new_quantity (int): The new quantity.

        Raises:
        KeyError: If the item does not exist in the inventory.
        ValueError: If the new quantity is negative.
        """
        if item_id not in self.items:
            raise KeyError(f"Item with ID {item_id} does not exist.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.items[item_id].quantity = new_quantity

    def get_items_by_category(self, category: JewelryCategory) -> List[JewelryItem]:
        """
        Retrieves a list of jewelry items by category.

        Args:
        category (JewelryCategory): The category to filter by.

        Returns:
        List[JewelryItem]: A list of jewelry items in the specified category.
        """
        return [item for item in self.items.values() if item.category == category]

    def __repr__(self):
        return f"Inventory(items={list(self.items.values())})"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create jewelry items
    ring = JewelryItem(1, "Diamond Ring", JewelryCategory.RINGS, 500.0, 10)
    earring = JewelryItem(2, "Gold Earrings", JewelryCategory.EARRINGS, 200.0, 20)
    pendant = JewelryItem(3, "Silver Pendant", JewelryCategory.PENDANTS, 100.0, 30)

    # Add items to the inventory
    inventory.add_item(ring)
    inventory.add_item(earring)
    inventory.add_item(pendant)

    # Print all items
    print("All Items:")
    for item in inventory.items.values():
        print(item)

    # Print items by category
    print("\nRINGS:")
    for item in inventory.get_items_by_category(JewelryCategory.RINGS):
        print(item)

    # Update quantity
    inventory.update_quantity(1, 5)
    print("\nUpdated Ring Quantity:")
    print(inventory.items[1])

    # Remove item
    inventory.remove_item(2)
    print("\nItems after removal:")
    for item in inventory.items.values():
        print(item)


if __name__ == "__main__":
    main()
```
