"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: What are the best practices for using Cedar International's electrical division products in a drilling operation? Provide a code example for inventory management.
Generated: DETERMINISTIC_7eb506ffd10c01cc
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for Cedar International's Electrical Division Products.
This script is designed to manage and track inventory for a drilling operation
to ensure the availability of electrical components while following best practices
for inventory control.

Features:
- Add, update, and delete items in inventory.
- Track quantities and reorder levels.
- Provide error handling for invalid operations.
"""

import sys

class InventoryError(Exception):
    """Custom exception class for inventory-related errors."""
    pass


class InventoryItem:
    """
    Represents a single inventory item.

    Attributes:
        item_id (str): Unique identifier for the item.
        name (str): Name of the item.
        category (str): Category of the item (e.g., electrical components, tools).
        quantity (int): Current quantity in inventory.
        reorder_level (int): Minimum quantity before a reorder is triggered.
    """
    def __init__(self, item_id, name, category, quantity, reorder_level):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.reorder_level = reorder_level

    def __str__(self):
        return f"ItemID: {self.item_id}, Name: {self.name}, Category: {self.category}, Quantity: {self.quantity}, Reorder Level: {self.reorder_level}"


class InventoryManager:
    """
    Manages inventory for Cedar International's products.

    Methods:
        add_item(item): Adds a new item to the inventory.
        update_quantity(item_id, quantity): Updates the quantity of an existing item.
        delete_item(item_id): Removes an item from the inventory.
        check_reorder(item_id): Checks if an item needs to be reordered.
        display_inventory(): Displays all items in the inventory.
    """
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        """Adds a new item to the inventory."""
        if item.item_id in self.inventory:
            raise InventoryError(f"Item with ID {item.item_id} already exists.")
        self.inventory[item.item_id] = item

    def update_quantity(self, item_id, quantity):
        """Updates the quantity of an item."""
        if item_id not in self.inventory:
            raise InventoryError(f"Item with ID {item_id} not found.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[item_id].quantity = quantity

    def delete_item(self, item_id):
        """Removes an item from the inventory."""
        if item_id not in self.inventory:
            raise InventoryError(f"Item with ID {item_id} not found.")
        del self.inventory[item_id]

    def check_reorder(self, item_id):
        """Checks if an item needs to be reordered."""
        if item_id not in self.inventory:
            raise InventoryError(f"Item with ID {item_id} not found.")
        item = self.inventory[item_id]
        if item.quantity <= item.reorder_level:
            return True
        return False

    def display_inventory(self):
        """Displays all items in the inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        for item in self.inventory.values():
            print(item)


# Example usage
if __name__ == "__main__":
    try:
        # Create the inventory manager
        manager = InventoryManager()

        # Add items to inventory
        item1 = InventoryItem("E001", "Drilling Cable", "Electrical Components", 100, 20)
        item2 = InventoryItem("E002", "Control Panel", "Electrical Components", 50, 10)

        manager.add_item(item1)
        manager.add_item(item2)

        # Display inventory
        print("Initial Inventory:")
        manager.display_inventory()

        # Update quantity
        manager.update_quantity("E001", 15)

        # Check reorder status
        if manager.check_reorder("E001"):
            print("Reorder needed for Item E001.")

        # Delete an item
        manager.delete_item("E002")

        # Display inventory after updates
        print("\nUpdated Inventory:")
        manager.display_inventory()

    except InventoryError as e:
        print(f"Inventory error: {e}", file=sys.stderr)
    except ValueError as ve:
        print(f"Value error: {ve}", file=sys.stderr)
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}", file=sys.stderr)
```
