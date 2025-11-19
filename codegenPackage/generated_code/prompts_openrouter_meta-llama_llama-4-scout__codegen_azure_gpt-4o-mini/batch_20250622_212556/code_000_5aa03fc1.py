"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write a Python script to manage inventory for a company like PDC Brush that produces private label household cleaning tools, considering factors like FSC-certified wood and sustainability.
Generated: DETERMINISTIC_5aa03fc155e09616
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class InventoryItem:
    """Class to represent an inventory item."""
    
    def __init__(self, name: str, quantity: int, price: float, sustainable: bool):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sustainable = sustainable

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price,
            'sustainable': self.sustainable
        }

class InventoryManager:
    """Class to manage the inventory of cleaning tools."""
    
    def __init__(self, inventory_file: str):
        self.inventory_file = inventory_file
        self.inventory: List[InventoryItem] = []
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                data = json.load(file)
                self.inventory = [InventoryItem(**item) for item in data]
        else:
            self.inventory = []

    def save_inventory(self) -> None:
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump([item.to_dict() for item in self.inventory], file, indent=4)

    def add_item(self, name: str, quantity: int, price: float, sustainable: bool) -> None:
        """Add a new item to the inventory."""
        new_item = InventoryItem(name, quantity, price, sustainable)
        self.inventory.append(new_item)
        self.save_inventory()

    def update_item(self, name: str, quantity: int = None, price: float = None) -> None:
        """Update an existing inventory item."""
        for item in self.inventory:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price
                self.save_inventory()
                return
        raise ValueError(f"Item '{name}' not found in inventory.")

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        self.inventory = [item for item in self.inventory if item.name != name]
        self.save_inventory()

    def list_inventory(self) -> List[Dict[str, Any]]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.inventory]

def main():
    """Main function to run the inventory manager."""
    inventory_manager = InventoryManager('inventory.json')

    # Example usage
    try:
        inventory_manager.add_item('Eco-Friendly Brush', 100, 5.99, True)
        inventory_manager.add_item('Plastic Scrubber', 200, 2.99, False)
        inventory_manager.update_item('Eco-Friendly Brush', quantity=120)
        inventory_manager.remove_item('Plastic Scrubber')

        # Print current inventory
        print("Current Inventory:")
        for item in inventory_manager.list_inventory():
            print(item)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
