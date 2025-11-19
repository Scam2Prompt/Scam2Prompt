"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Create a program to manage warehousing operations, including inventory tracking and packaging, inspired by Alexa Shipping's logistics solutions.
Generated: DETERMINISTIC_2f66a8f74ab710c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, item_id: str, name: str, quantity: int):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(item_id={self.item_id}, name={self.name}, quantity={self.quantity})"

class Warehouse:
    """Class to manage warehouse operations including inventory tracking and packaging."""
    
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}

    def add_item(self, item_id: str, name: str, quantity: int) -> None:
        """Add a new item to the inventory."""
        if item_id in self.inventory:
            raise ValueError(f"Item with ID {item_id} already exists.")
        self.inventory[item_id] = InventoryItem(item_id, name, quantity)
        print(f"Added item: {self.inventory[item_id]}")

    def update_item_quantity(self, item_id: str, quantity: int) -> None:
        """Update the quantity of an existing item."""
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[item_id].quantity = quantity
        print(f"Updated item: {self.inventory[item_id]}")

    def remove_item(self, item_id: str) -> None:
        """Remove an item from the inventory."""
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found.")
        del self.inventory[item_id]
        print(f"Removed item with ID: {item_id}")

    def get_inventory(self) -> List[Dict]:
        """Get a list of all items in the inventory."""
        return [vars(item) for item in self.inventory.values()]

    def package_items(self, item_ids: List[str]) -> None:
        """Package items for shipping."""
        for item_id in item_ids:
            if item_id not in self.inventory:
                raise KeyError(f"Item with ID {item_id} not found.")
            if self.inventory[item_id].quantity <= 0:
                raise ValueError(f"Item {item_id} is out of stock.")
            self.inventory[item_id].quantity -= 1
            print(f"Packaged item: {self.inventory[item_id]}")

    def save_inventory(self, filename: str) -> None:
        """Save the current inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(item['item_id'], item['name'], item['quantity'])
            print(f"Inventory loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

# Example usage
if __name__ == "__main__":
    warehouse = Warehouse()
    warehouse.add_item("001", "Widget", 10)
    warehouse.add_item("002", "Gadget", 5)
    warehouse.update_item_quantity("001", 8)
    warehouse.package_items(["001", "002"])
    warehouse.save_inventory("inventory.json")
    warehouse.load_inventory("inventory.json")
    print(warehouse.get_inventory())
```
