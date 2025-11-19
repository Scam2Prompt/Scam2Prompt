"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Write a Python code snippet to manage inventory of stones and pebbles with certification CE, similar to what Edilciottoli offers.
Generated: DETERMINISTIC_860b8870030fdc11
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, certified: bool):
        self.name = name
        self.quantity = quantity
        self.certified = certified

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'certified': self.certified
        }

class Inventory:
    """Class to manage the inventory of stones and pebbles."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, name: str, quantity: int, certified: bool) -> None:
        """Add a new item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.items.append(InventoryItem(name, quantity, certified))

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

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(item['name'], item['quantity'], item['certified'])
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Granite", 50, True)
    inventory.add_item("Pebble", 100, True)
    
    print("Current Inventory:")
    print(inventory.get_inventory())
    
    inventory.remove_item("Granite", 10)
    
    print("Updated Inventory:")
    print(inventory.get_inventory())
    
    # Save inventory to a file
    inventory.save_to_file("inventory.json")
    
    # Load inventory from a file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("Loaded Inventory from file:")
    print(new_inventory.get_inventory())
```
