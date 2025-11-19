"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: "Write a Python code snippet to manage inventory for a metal distribution company like Meta+, including products such as stainless steel, aluminum, and copper."
Generated: DETERMINISTIC_ee9cf0023989e79d
Batch ID: 20250622_205348
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

class Inventory:
    """Class to manage the inventory of a metal distribution company."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price_per_unit: float) -> None:
        """Add a new item to the inventory."""
        if name in self.items:
            raise ValueError(f"Item '{name}' already exists in the inventory.")
        self.items[name] = InventoryItem(name, quantity, price_per_unit)

    def update_item(self, name: str, quantity: Optional[int] = None, price_per_unit: Optional[float] = None) -> None:
        """Update the quantity or price of an existing item."""
        if name not in self.items:
            raise ValueError(f"Item '{name}' not found in the inventory.")
        if quantity is not None:
            self.items[name].quantity = quantity
        if price_per_unit is not None:
            self.items[name].price_per_unit = price_per_unit

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        if name not in self.items:
            raise ValueError(f"Item '{name}' not found in the inventory.")
        del self.items[name]

    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Retrieve an item from the inventory."""
        return self.items.get(name)

    def list_items(self) -> List[InventoryItem]:
        """List all items in the inventory."""
        return list(self.items.values())

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({name: item.__dict__ for name, item in self.items.items()}, file)

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, item_data in data.items():
                    self.items[name] = InventoryItem(**item_data)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file '{filename}'. Please check the file format.")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Stainless Steel", 100, 2.5)
    inventory.add_item("Aluminum", 200, 1.5)
    inventory.add_item("Copper", 150, 3.0)

    print("Current Inventory:")
    print(inventory.list_items())

    inventory.update_item("Aluminum", quantity=250)
    print("\nUpdated Inventory:")
    print(inventory.list_items())

    inventory.save_to_file("inventory.json")
    inventory.load_from_file("inventory.json")
```
