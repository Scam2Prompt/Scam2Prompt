"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Write a Python code to manage an e-commerce inventory for inhaler accessories, including items like trachea for ultrasonic inhalers and nebulizer kits.
Generated: DETERMINISTIC_fe64f1d1ff83cc30
Batch ID: 20250622_210655
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
        """Convert the item to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of inhaler accessories."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        """Remove an item from the inventory by name."""
        self.items = [item for item in self.items if item.name != item_name]

    def update_item(self, item_name: str, quantity: int, price: float) -> None:
        """Update the quantity and price of an existing item."""
        for item in self.items:
            if item.name == item_name:
                item.quantity = quantity
                item.price = price
                return
        raise ValueError(f"Item '{item_name}' not found in inventory.")

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
    inventory.add_item(InventoryItem("Trachea for Ultrasonic Inhalers", 50, 19.99))
    inventory.add_item(InventoryItem("Nebulizer Kit", 30, 29.99))
    
    # Updating an item
    try:
        inventory.update_item("Trachea for Ultrasonic Inhalers", 45, 18.99)
    except ValueError as e:
        print(e)

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")

    # Displaying the inventory
    print(inventory.get_inventory())
```
