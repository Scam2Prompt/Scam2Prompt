"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Create a script to manage inventory for office furniture, including desks, chairs, filing cabinets, and sofas, based on the product categories listed on Sanuri Supplies' website.
Generated: DETERMINISTIC_933cd8aa3716ce9c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Union

class InventoryItem:
    """Class to represent an item in the inventory."""

    def __init__(self, category: str, name: str, quantity: int, price: float):
        self.category = category
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """Convert the InventoryItem to a dictionary for serialization."""
        return {
            'category': self.category,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }

class InventoryManager:
    """Class to manage the office furniture inventory."""

    def __init__(self, inventory_file: str):
        self.inventory_file = inventory_file
        self.inventory: List[InventoryItem] = []

        # Load existing inventory from file if it exists
        self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                data = json.load(file)
                self.inventory = [InventoryItem(**item) for item in data]
        else:
            self.inventory = []

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump([item.to_dict() for item in self.inventory], file, indent=4)

    def add_item(self, category: str, name: str, quantity: int, price: float):
        """Add a new item to the inventory."""
        new_item = InventoryItem(category, name, quantity, price)
        self.inventory.append(new_item)
        self.save_inventory()

    def remove_item(self, name: str):
        """Remove an item from the inventory by name."""
        self.inventory = [item for item in self.inventory if item.name != name]
        self.save_inventory()

    def update_item(self, name: str, quantity: int = None, price: float = None):
        """Update the quantity or price of an item."""
        for item in self.inventory:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                self.save_inventory()
                return
        raise ValueError(f"Item with name '{name}' not found in inventory.")

    def list_inventory(self) -> List[Dict[str, Union[str, int, float]]]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.inventory]

def main():
    """Main function to run the inventory manager."""
    inventory_file = 'office_furniture_inventory.json'
    manager = InventoryManager(inventory_file)

    # Example usage
    try:
        manager.add_item('Desk', 'Executive Desk', 10, 299.99)
        manager.add_item('Chair', 'Office Chair', 20, 89.99)
        manager.update_item('Office Chair', quantity=25)
        manager.remove_item('Executive Desk')

        print("Current Inventory:")
        for item in manager.list_inventory():
            print(item)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
