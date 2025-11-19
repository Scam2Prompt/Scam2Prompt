"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: "Generate a code snippet for tracking inventory of agricultural equipment, including motoculture and irrigation systems, for a company like SARL VERDIER IRRIGATION."
Generated: DETERMINISTIC_9656d0a145c4c835
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
    
    def __init__(self, name: str, category: str, quantity: int, price_per_unit: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary."""
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "price_per_unit": self.price_per_unit
        }

class Inventory:
    """Class to manage the inventory of agricultural equipment."""
    
    def __init__(self):
        self.items: List[InventoryItem] = []

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        """Remove an item from the inventory by name."""
        self.items = [item for item in self.items if item.name != item_name]

    def update_item_quantity(self, item_name: str, quantity: int) -> None:
        """Update the quantity of an existing item."""
        for item in self.items:
            if item.name == item_name:
                item.quantity = quantity
                return
        raise ValueError(f"Item '{item_name}' not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries."""
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
    inventory.add_item(InventoryItem("Tractor", "Motoculture", 5, 25000.00))
    inventory.add_item(InventoryItem("Irrigation Pump", "Irrigation", 10, 1500.00))
    
    # Updating item quantity
    try:
        inventory.update_item_quantity("Tractor", 4)
    except ValueError as e:
        print(e)

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")

    # Displaying the current inventory
    print(inventory.get_inventory())
```
