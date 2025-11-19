"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: "Write a Python code to manage inventory for a surgical instrument manufacturing company that offers custom instruments."
Generated: DETERMINISTIC_07800a01703a2fbe
Batch ID: 20250622_210703
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
    
    def __init__(self, name: str, quantity: int, custom: bool = False):
        self.name = name
        self.quantity = quantity
        self.custom = custom

    def to_dict(self) -> Dict:
        """Convert the InventoryItem to a dictionary."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'custom': self.custom
        }

class Inventory:
    """Class to manage the inventory of surgical instruments."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, name: str, quantity: int, custom: bool = False) -> None:
        """Add a new item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        item = InventoryItem(name, quantity, custom)
        self.items.append(item)

    def remove_item(self, name: str, quantity: int) -> None:
        """Remove a specified quantity of an item from the inventory."""
        for item in self.items:
            if item.name == name:
                if quantity > item.quantity:
                    raise ValueError("Cannot remove more than available quantity.")
                item.quantity -= quantity
                if item.quantity == 0:
                    self.items.remove(item)
                return
        raise ValueError("Item not found in inventory.")

    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Retrieve an item from the inventory by name."""
        for item in self.items:
            if item.name == name:
                return item
        return None

    def list_items(self) -> List[Dict]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_items(), file, indent=4)
        except IOError as e:
            raise Exception(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(item['name'], item['quantity'], item['custom'])
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Scalpel", 50)
    inventory.add_item("Custom Forceps", 20, custom=True)
    
    print("Current Inventory:")
    print(inventory.list_items())
    
    inventory.remove_item("Scalpel", 10)
    
    print("Updated Inventory:")
    print(inventory.list_items())
    
    # Save inventory to a file
    inventory.save_to_file("inventory.json")
    
    # Load inventory from a file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("Loaded Inventory from file:")
    print(new_inventory.list_items())
```
