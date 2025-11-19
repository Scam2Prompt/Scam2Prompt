"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Generate a Python code snippet to manage inventory for a construction supply company like One World Supply, including product categories such as valves, couplings, and plumbing fixtures."
Generated: DETERMINISTIC_ebaa9e61860a371b
Batch ID: 20250622_212444
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
        """Convert the inventory item to a dictionary."""
        return {
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

class Inventory:
    """Class to manage the inventory of construction supplies."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.items.append(item)

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory by name."""
        self.items = [item for item in self.items if item.name != name]

    def update_item(self, name: str, quantity: int = None, price: float = None) -> None:
        """Update the quantity and/or price of an existing item."""
        for item in self.items:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                return
        raise ValueError(f"Item '{name}' not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
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
    inventory.add_item(InventoryItem("Ball Valve", "Valves", 100, 15.99))
    inventory.add_item(InventoryItem("PVC Coupling", "Couplings", 200, 0.99))
    inventory.add_item(InventoryItem("Faucet", "Plumbing Fixtures", 50, 49.99))

    # Updating an item
    inventory.update_item("Ball Valve", quantity=90)

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")

    # Displaying the inventory
    print(inventory.get_inventory())
```
