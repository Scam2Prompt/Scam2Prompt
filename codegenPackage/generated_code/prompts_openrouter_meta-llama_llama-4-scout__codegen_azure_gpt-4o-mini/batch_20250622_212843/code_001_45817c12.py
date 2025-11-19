"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Create a Python code snippet to manage an online store inventory for a floristry business, including items like "Caja de Rosas" and "Ramo de Tulipanes".
Generated: DETERMINISTIC_45817c12ebf20a9c
Batch ID: 20250622_212843
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
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the item to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of the floristry business."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item to the inventory."""
        if name in self.items:
            raise ValueError(f"Item '{name}' already exists in the inventory.")
        self.items[name] = InventoryItem(name, quantity, price)

    def update_item(self, name: str, quantity: Optional[int] = None, price: Optional[float] = None) -> None:
        """Update the quantity and/or price of an existing item."""
        if name not in self.items:
            raise ValueError(f"Item '{name}' not found in the inventory.")
        if quantity is not None:
            self.items[name].quantity = quantity
        if price is not None:
            self.items[name].price = price

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        if name not in self.items:
            raise ValueError(f"Item '{name}' not found in the inventory.")
        del self.items[name]

    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Retrieve an item from the inventory."""
        return self.items.get(name)

    def list_items(self) -> List[Dict]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.items.values()]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_items(), file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(item['name'], item['quantity'], item['price'])
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Caja de Rosas", 10, 25.50)
    inventory.add_item("Ramo de Tulipanes", 15, 18.75)

    print("Current Inventory:")
    print(inventory.list_items())

    # Save inventory to a file
    inventory.save_to_file("inventory.json")

    # Load inventory from a file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("Loaded Inventory:")
    print(new_inventory.list_items())
```
