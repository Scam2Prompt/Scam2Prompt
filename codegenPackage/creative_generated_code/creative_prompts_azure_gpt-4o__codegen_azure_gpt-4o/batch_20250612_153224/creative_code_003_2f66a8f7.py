"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Create a program to manage warehousing operations, including inventory tracking and packaging, inspired by Alexa Shipping's logistics solutions.
Generated: DETERMINISTIC_2f66a8f74ab710c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Dict, List

# Define a custom exception for inventory-related errors
class InventoryError(Exception):
    pass

# Class to represent a single item in the inventory
class Item:
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        """
        Initialize an item instance.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param quantity: Quantity available in inventory
        :param price: Price per unit of the item
        """
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"

# Class to manage the inventory system
class InventoryManager:
    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory: Dict[str, Item] = {}

    def add_item(self, item_id: str, name: str, quantity: int, price: float):
        """
        Add a new item to the inventory or update existing item.

        :param item_id: Unique identifier for the item
        :param name: Name of the item
        :param quantity: Quantity to add
        :param price: Price per unit of the item
        """
        if item_id in self.inventory:
            # Update existing item's quantity and price
            existing_item = self.inventory[item_id]
            existing_item.quantity += quantity
            existing_item.price = price  # Update price if changed
        else:
            # Add a new item to the inventory
            self.inventory[item_id] = Item(item_id, name, quantity, price)

    def remove_item(self, item_id: str, quantity: int):
        """
        Remove a specific quantity of an item from the inventory.

        :param item_id: Unique identifier for the item
        :param quantity: Quantity to remove
        :raises InventoryError: If item does not exist or insufficient stock
        """
        if item_id not in self.inventory:
            raise InventoryError(f"Item with ID {item_id} does not exist.")
        
        item = self.inventory[item_id]
        if item.quantity < quantity:
            raise InventoryError(f"Insufficient stock for item {item_id}. Available: {item.quantity}, Requested: {quantity}")
        
        item.quantity -= quantity
        if item.quantity == 0:
            del self.inventory[item_id]  # Remove item if quantity is zero

    def get_inventory_summary(self) -> List[str]:
        """
        Get a summary of all items in the inventory.

        :return: List of strings representing each item
        """
        return [str(item) for item in self.inventory.values()]

# Class to handle packaging operations
class PackagingManager:
    def __init__(self):
        """
        Initialize the packaging manager with an empty packaging history.
        """
        self.packaging_history: List[Dict] = []

    def package_items(self, item_id: str, quantity: int, inventory_manager: InventoryManager):
        """
        Package items from the inventory.

        :param item_id: Unique identifier for the item
        :param quantity: Quantity to package
        :param inventory_manager: Instance of InventoryManager to interact with inventory
        :raises InventoryError: If packaging fails due to inventory issues
        """
        try:
            inventory_manager.remove_item(item_id, quantity)
            package_record = {
                "item_id": item_id,
                "quantity": quantity,
                "timestamp": datetime.datetime.now()
            }
            self.packaging_history.append(package_record)
        except InventoryError as e:
            raise InventoryError(f"Packaging error: {e}")

    def get_packaging_history(self) -> List[Dict]:
        """
        Get the history of all packaging operations.

        :return: List of dictionaries representing packaging records
        """
        return self.packaging_history


# Example usage of the above classes
if __name__ == "__main__":
    # Create inventory manager and packaging manager instances
    inventory_manager = InventoryManager()
    packaging_manager = PackagingManager()

    # Add items to inventory
    inventory_manager.add_item("A001", "Widget", 100, 2.50)
    inventory_manager.add_item("A002", "Gadget", 50, 5.00)

    # Print inventory summary
    print("Current Inventory:")
    for item in inventory_manager.get_inventory_summary():
        print(item)

    # Package items
    try:
        packaging_manager.package_items("A001", 10, inventory_manager)
        packaging_manager.package_items("A002", 5, inventory_manager)
    except InventoryError as e:
        print(e)

    # Show updated inventory
    print("\nUpdated Inventory:")
    for item in inventory_manager.get_inventory_summary():
        print(item)

    # Show packaging history
    print("\nPackaging History:")
    for record in packaging_manager.get_packaging_history():
        print(record)
```
