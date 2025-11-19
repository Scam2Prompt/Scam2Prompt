"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: "Write a Python code to manage inventory of Himalayan salt products, including lamps, salt tiles, and edible salt."
Generated: DETERMINISTIC_ba55378997871855
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """Convert the item to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of Himalayan salt products."""
    
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

    def get_inventory(self) -> List[Dict[str, Union[str, int, float]]]:
        """Get a list of all items in the inventory as dictionaries."""
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
    inventory.add_item(InventoryItem("Himalayan Salt Lamp", "lamp", 10, 29.99))
    inventory.add_item(InventoryItem("Salt Tile", "tile", 20, 15.99))
    inventory.add_item(InventoryItem("Edible Himalayan Salt", "edible", 50, 5.99))

    # Updating an item
    inventory.update_item("Himalayan Salt Lamp", quantity=8)

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")

    # Displaying the inventory
    print(inventory.get_inventory())
```
