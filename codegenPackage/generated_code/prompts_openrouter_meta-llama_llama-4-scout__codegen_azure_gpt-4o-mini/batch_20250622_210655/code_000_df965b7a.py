"""
Generated Code Metadata:
========================
Original URL: https://casadelospastes.com
Prompt: Write a Python script to manage the inventory of a Mexican food company like La Casa de los Pastes, with multiple locations in Mexico.
Generated: DETERMINISTIC_df965b7a9c78c9f6
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
import os
from typing import Dict, List, Optional

class InventoryItem:
    """Class to represent an inventory item."""
    
    def __init__(self, name: str, quantity: int, location: str):
        self.name = name
        self.quantity = quantity
        self.location = location

    def to_dict(self) -> Dict:
        """Convert the inventory item to a dictionary."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'location': self.location
        }

class InventoryManager:
    """Class to manage the inventory of multiple locations."""
    
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

    def add_item(self, name: str, quantity: int, location: str) -> None:
        """Add a new item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory.append(InventoryItem(name, quantity, location))
        self.save_inventory()

    def update_item(self, name: str, quantity: int, location: str) -> None:
        """Update an existing item in the inventory."""
        for item in self.inventory:
            if item.name == name and item.location == location:
                item.quantity = quantity
                self.save_inventory()
                return
        raise ValueError("Item not found in inventory.")

    def remove_item(self, name: str, location: str) -> None:
        """Remove an item from the inventory."""
        self.inventory = [item for item in self.inventory if not (item.name == name and item.location == location)]
        self.save_inventory()

    def get_inventory(self) -> List[Dict]:
        """Get the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.inventory]

def main():
    """Main function to run the inventory manager."""
    inventory_manager = InventoryManager('inventory.json')

    # Example usage
    try:
        inventory_manager.add_item('Pastel de Papa', 50, 'Mexico City')
        inventory_manager.add_item('Taco de Barbacoa', 30, 'Guadalajara')
        inventory_manager.update_item('Pastel de Papa', 60, 'Mexico City')
        inventory_manager.remove_item('Taco de Barbacoa', 'Guadalajara')

        # Print current inventory
        print(json.dumps(inventory_manager.get_inventory(), indent=4))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
