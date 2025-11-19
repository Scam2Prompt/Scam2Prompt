"""
Generated Code Metadata:
========================
Original URL: https://portlineshipping.com
Prompt: Illustrate how to implement a warehouse management system that aligns with the logistics and warehousing services provided by Portline Shipping.
Generated: DETERMINISTIC_5289e9ee2d1e06c8
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# warehouse_management.py

class Warehouse:
    """
    A class to represent a warehouse for managing inventory and logistics.
    """

    def __init__(self):
        """
        Initializes the warehouse with an empty inventory.
        """
        self.inventory = {}

    def add_item(self, item_name, quantity):
        """
        Adds a specified quantity of an item to the warehouse inventory.

        :param item_name: Name of the item to add
        :param quantity: Quantity of the item to add
        :raises ValueError: If quantity is not a positive integer
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

        print(f"Added {quantity} of {item_name}. Current stock: {self.inventory[item_name]}")

    def remove_item(self, item_name, quantity):
        """
        Removes a specified quantity of an item from the warehouse inventory.

        :param item_name: Name of the item to remove
        :param quantity: Quantity of the item to remove
        :raises ValueError: If quantity is not a positive integer or exceeds available stock
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if item_name not in self.inventory:
            raise ValueError(f"Item '{item_name}' not found in inventory.")
        
        if self.inventory[item_name] < quantity:
            raise ValueError(f"Insufficient stock for item '{item_name}'. Available: {self.inventory[item_name]}")

        self.inventory[item_name] -= quantity
        print(f"Removed {quantity} of {item_name}. Current stock: {self.inventory[item_name]}")

    def get_inventory(self):
        """
        Returns the current inventory of the warehouse.

        :return: A dictionary representing the current inventory
        """
        return self.inventory

    def check_item(self, item_name):
        """
        Checks the stock level of a specific item.

        :param item_name: Name of the item to check
        :return: Quantity of the item in stock
        :raises ValueError: If item is not found in inventory
        """
        if item_name not in self.inventory:
            raise ValueError(f"Item '{item_name}' not found in inventory.")
        
        return self.inventory[item_name]


# Example usage
if __name__ == "__main__":
    warehouse = Warehouse()

    try:
        warehouse.add_item("Widget A", 100)
        warehouse.add_item("Widget B", 50)
        print(warehouse.get_inventory())

        warehouse.remove_item("Widget A", 20)
        print(warehouse.get_inventory())

        stock_level = warehouse.check_item("Widget B")
        print(f"Stock level of Widget B: {stock_level}")

    except ValueError as e:
        print(f"Error: {e}")
```
