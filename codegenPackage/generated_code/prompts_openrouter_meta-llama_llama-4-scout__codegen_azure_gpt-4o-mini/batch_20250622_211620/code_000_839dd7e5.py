"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Write a Python code snippet to manage inventory for a wholesale distributor of natural stone products and deicing materials, including bulk salt and packaged deicers.
Generated: DETERMINISTIC_839dd7e5d6acf8d1
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price_per_unit: float):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def __repr__(self):
        return f"InventoryItem(name={self.name}, quantity={self.quantity}, price_per_unit={self.price_per_unit})"

    def update_quantity(self, amount: int):
        """Update the quantity of the item."""
        if self.quantity + amount < 0:
            raise ValueError("Cannot reduce quantity below zero.")
        self.quantity += amount

    def total_value(self) -> float:
        """Calculate the total value of the item in inventory."""
        return self.quantity * self.price_per_unit


class Inventory:
    """Class to manage the inventory of natural stone products and deicing materials."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price_per_unit: float):
        """Add a new item to the inventory."""
        if name in self.items:
            raise ValueError("Item already exists in inventory.")
        self.items[name] = InventoryItem(name, quantity, price_per_unit)

    def update_item_quantity(self, name: str, amount: int):
        """Update the quantity of an existing item."""
        if name not in self.items:
            raise KeyError("Item not found in inventory.")
        self.items[name].update_quantity(amount)

    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Retrieve an item from the inventory."""
        return self.items.get(name)

    def total_inventory_value(self) -> float:
        """Calculate the total value of the entire inventory."""
        return sum(item.total_value() for item in self.items.values())

    def save_to_file(self, filename: str):
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({name: item.__dict__ for name, item in self.items.items()}, file)

    def load_from_file(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, item_data in data.items():
                    self.items[name] = InventoryItem(**item_data)
        except FileNotFoundError:
            print("File not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the file format.")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item("Bulk Salt", 1000, 0.05)
    inventory.add_item("Packaged Deicer", 500, 1.50)

    # Updating item quantity
    inventory.update_item_quantity("Bulk Salt", -200)

    # Retrieving an item
    item = inventory.get_item("Packaged Deicer")
    print(item)

    # Calculating total inventory value
    total_value = inventory.total_inventory_value()
    print(f"Total Inventory Value: ${total_value:.2f}")

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")
```
