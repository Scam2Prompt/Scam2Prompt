"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Create a Python script to manage inventory for RV repair parts, including awnings, electrical components, and plumbing supplies, with tracking for mobile service vehicles.
Generated: DETERMINISTIC_632e24816a6a7038
Batch ID: 20250612_145203
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
from typing import List, Dict


class InventoryItem:
    """Class to represent an inventory item for RV repair parts."""
    
    def __init__(self, name: str, category: str, quantity: int, location: str):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.location = location

    def __repr__(self):
        return f"InventoryItem(name={self.name}, category={self.category}, quantity={self.quantity}, location={self.location})"


class InventoryManager:
    """Class to manage the inventory of RV repair parts."""
    
    def __init__(self, inventory_file: str):
        self.inventory_file = inventory_file
        self.inventory: List[InventoryItem] = []
        self.load_inventory()

    def load_inventory(self):
        """Load the inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, 'r') as file:
                    items = json.load(file)
                    self.inventory = [InventoryItem(**item) for item in items]
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading inventory: {e}")

    def save_inventory(self):
        """Save the inventory to a JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump([item.__dict__ for item in self.inventory], file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_item(self, name: str, category: str, quantity: int, location: str):
        """Add a new item to the inventory."""
        item = InventoryItem(name, category, quantity, location)
        self.inventory.append(item)
        self.save_inventory()

    def update_item(self, name: str, quantity: int):
        """Update the quantity of an existing item in the inventory."""
        for item in self.inventory:
            if item.name == name:
                item.quantity = quantity
                self.save_inventory()
                return
        print(f"Item '{name}' not found in inventory.")

    def delete_item(self, name: str):
        """Delete an item from the inventory."""
        self.inventory = [item for item in self.inventory if item.name != name]
        self.save_inventory()

    def list_inventory(self) -> List[Dict]:
        """List all items in the inventory."""
        return [item.__dict__ for item in self.inventory]


def main():
    """Main function to run the inventory manager."""
    inventory_file = 'inventory.json'
    manager = InventoryManager(inventory_file)

    # Example usage
    manager.add_item('Awnings', 'Exterior', 10, 'Service Vehicle A')
    manager.add_item('Wiring Kit', 'Electrical', 5, 'Service Vehicle B')
    manager.add_item('Water Pump', 'Plumbing', 2, 'Service Vehicle A')

    print("Current Inventory:")
    for item in manager.list_inventory():
        print(item)

    # Update an item
    manager.update_item('Wiring Kit', 8)

    # Delete an item
    manager.delete_item('Water Pump')

    print("\nUpdated Inventory:")
    for item in manager.list_inventory():
        print(item)


if __name__ == "__main__":
    main()
```
