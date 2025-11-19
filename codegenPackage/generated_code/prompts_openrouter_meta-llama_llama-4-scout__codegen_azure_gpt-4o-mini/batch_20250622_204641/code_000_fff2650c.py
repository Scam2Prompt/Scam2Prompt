"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Write a Python code snippet to manage an e-commerce inventory system for computer hardware products like SSDs, Pen Drives, and USB mice.
Generated: DETERMINISTIC_fff2650c98988f6c
Batch ID: 20250622_204641
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
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of hardware products."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.items.append(item)

    def remove_item(self, name: str) -> bool:
        """Remove an item from the inventory by name."""
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return True
        return False

    def update_item(self, name: str, quantity: int = None, price: float = None) -> bool:
        """Update the quantity and/or price of an existing item."""
        for item in self.items:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                return True
        return False

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get a list of all items in the inventory."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                self.items = [InventoryItem(**item) for item in items]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item(InventoryItem("Samsung SSD", "SSD", 10, 99.99))
    inventory.add_item(InventoryItem("SanDisk Pen Drive", "Pen Drive", 50, 19.99))
    inventory.add_item(InventoryItem("Logitech USB Mouse", "Mouse", 30, 29.99))
    
    # Updating an item
    inventory.update_item("Samsung SSD", quantity=8)
    
    # Removing an item
    inventory.remove_item("Logitech USB Mouse")
    
    # Saving inventory to a file
    inventory.save_to_file("inventory.json")
    
    # Loading inventory from a file
    inventory.load_from_file("inventory.json")
    
    # Displaying the current inventory
    print(inventory.get_inventory())
```
