"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: "Write a Python code to manage inventory of dry facade system components, including products like aluminum runners and clips."
Generated: DETERMINISTIC_8bf4a042f349da3d
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
        """Convert the inventory item to a dictionary."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'InventoryItem':
        """Create an InventoryItem from a dictionary."""
        return cls(data['name'], data['quantity'], data['price'])


class Inventory:
    """Class to manage the inventory of facade system components."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory by name."""
        self.items = [item for item in self.items if item.name != name]

    def update_item(self, name: str, quantity: int, price: float) -> None:
        """Update the quantity and price of an existing item."""
        for item in self.items:
            if item.name == name:
                item.quantity = quantity
                item.price = price
                return
        raise ValueError(f"Item '{name}' not found in inventory.")

    def get_item(self, name: str) -> InventoryItem:
        """Retrieve an item from the inventory by name."""
        for item in self.items:
            if item.name == name:
                return item
        raise ValueError(f"Item '{name}' not found in inventory.")

    def list_items(self) -> List[Dict[str, Any]]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_items(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items_data = json.load(file)
                self.items = [InventoryItem.from_dict(item) for item in items_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item(InventoryItem("Aluminum Runner", 100, 2.50))
    inventory.add_item(InventoryItem("Clip", 200, 0.75))
    
    # Listing items
    print("Current Inventory:")
    print(inventory.list_items())
    
    # Updating an item
    inventory.update_item("Aluminum Runner", 120, 2.60)
    
    # Saving inventory to a file
    inventory.save_to_file("inventory.json")
    
    # Loading inventory from a file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("Loaded Inventory:")
    print(new_inventory.list_items())
```
