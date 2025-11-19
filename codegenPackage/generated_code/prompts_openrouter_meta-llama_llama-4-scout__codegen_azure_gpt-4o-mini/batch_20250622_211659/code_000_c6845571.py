"""
Generated Code Metadata:
========================
Original URL: https://homefoodsghana.com
Prompt: Write a Python code snippet to manage inventory for a company like Homefoods that produces various food products, including seasonings and ready-to-eat meals.
Generated: DETERMINISTIC_c68455710de66750
Batch ID: 20250622_211659
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
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of food products."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item to the inventory."""
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")
        self.items.append(InventoryItem(name, quantity, price))

    def update_item(self, name: str, quantity: int = None, price: float = None) -> None:
        """Update the quantity or price of an existing item."""
        for item in self.items:
            if item.name == name:
                if quantity is not None:
                    if quantity < 0:
                        raise ValueError("Quantity must be non-negative.")
                    item.quantity = quantity
                if price is not None:
                    if price < 0:
                        raise ValueError("Price must be non-negative.")
                    item.price = price
                return
        raise ValueError(f"Item '{name}' not found in inventory.")

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return
        raise ValueError(f"Item '{name}' not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get a list of all items in the inventory."""
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
                    self.add_item(item['name'], item['quantity'], item['price'])
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Spice Mix", 100, 5.99)
    inventory.add_item("Ready Meal", 50, 8.49)
    
    print("Current Inventory:")
    print(inventory.get_inventory())
    
    inventory.update_item("Spice Mix", quantity=120)
    inventory.save_to_file("inventory.json")
    
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("Loaded Inventory:")
    print(new_inventory.get_inventory())
```
