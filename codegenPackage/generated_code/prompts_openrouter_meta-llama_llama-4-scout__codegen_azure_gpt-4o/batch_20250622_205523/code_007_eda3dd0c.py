"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Design a data structure to store and manage inventory of performance parts for racing cars, including air filters, drive flanges, and suspension components.
Generated: DETERMINISTIC_eda3dd0c0f6d8f05
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class InventoryItem:
    """
    Represents a single inventory item.
    Attributes:
        name (str): Name of the item.
        category (str): Category of the item (e.g., air filter, drive flange, suspension component).
        quantity (int): Quantity of the item in stock.
        price (float): Price of the item.
    """
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    """
    Manages the inventory of performance parts for racing cars.
    Provides methods to add, update, remove, and retrieve inventory items.
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item):
        """
        Adds a new item to the inventory.
        Args:
            item_id (str): Unique identifier for the item.
            item (InventoryItem): The inventory item to add.
        Raises:
            ValueError: If the item_id already exists in the inventory.
        """
        if item_id in self.items:
            raise ValueError(f"Item ID '{item_id}' already exists in the inventory.")
        self.items[item_id] = item

    def update_item(self, item_id, quantity=None, price=None):
        """
        Updates the quantity and/or price of an existing item.
        Args:
            item_id (str): Unique identifier for the item.
            quantity (int, optional): New quantity of the item.
            price (float, optional): New price of the item.
        Raises:
            KeyError: If the item_id does not exist in the inventory.
        """
        if item_id not in self.items:
            raise KeyError(f"Item ID '{item_id}' not found in the inventory.")
        if quantity is not None:
            self.items[item_id].quantity = quantity
        if price is not None:
            self.items[item_id].price = price

    def remove_item(self, item_id):
        """
        Removes an item from the inventory.
        Args:
            item_id (str): Unique identifier for the item.
        Raises:
            KeyError: If the item_id does not exist in the inventory.
        """
        if item_id not in self.items:
            raise KeyError(f"Item ID '{item_id}' not found in the inventory.")
        del self.items[item_id]

    def get_item(self, item_id):
        """
        Retrieves an item from the inventory.
        Args:
            item_id (str): Unique identifier for the item.
        Returns:
            InventoryItem: The requested inventory item.
        Raises:
            KeyError: If the item_id does not exist in the inventory.
        """
        if item_id not in self.items:
            raise KeyError(f"Item ID '{item_id}' not found in the inventory.")
        return self.items[item_id]

    def list_items(self):
        """
        Lists all items in the inventory.
        Returns:
            list: A list of all inventory items.
        """
        return [str(item) for item in self.items.values()]


# Example usage
if __name__ == "__main__":
    try:
        # Create inventory instance
        inventory = Inventory()

        # Add items to inventory
        inventory.add_item("AF001", InventoryItem("High-Performance Air Filter", "Air Filter", 50, 29.99))
        inventory.add_item("DF001", InventoryItem("Drive Flange", "Drive Flange", 20, 99.99))
        inventory.add_item("SC001", InventoryItem("Suspension Component", "Suspension", 15, 199.99))

        # List all items
        print("Current Inventory:")
        for item in inventory.list_items():
            print(item)

        # Update an item
        inventory.update_item("AF001", quantity=45, price=27.99)

        # Retrieve a specific item
        print("\nUpdated Item:")
        print(inventory.get_item("AF001"))

        # Remove an item
        inventory.remove_item("DF001")

        # List all items after removal
        print("\nInventory After Removal:")
        for item in inventory.list_items():
            print(item)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
