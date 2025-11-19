"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write a Python script to manage inventory of replica firearms and police uniforms for a film production company, considering NSW legislation and regulations.
Generated: DETERMINISTIC_0fd7ad78668636bf
Batch ID: 20250622_204920
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

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name, quantity, item_type):
        """
        Initialize an inventory item.

        :param name: Name of the item
        :param quantity: Quantity of the item
        :param item_type: Type of the item (e.g., 'firearm', 'uniform')
        """
        self.name = name
        self.quantity = quantity
        self.item_type = item_type

    def to_dict(self):
        """Convert the item to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'item_type': self.item_type
        }

class InventoryManager:
    """Class to manage the inventory of items."""
    
    def __init__(self, inventory_file='inventory.json'):
        """
        Initialize the inventory manager.

        :param inventory_file: Path to the inventory JSON file
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                try:
                    return [InventoryItem(**item) for item in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading inventory: {e}")
                    return []
        return []

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump([item.to_dict() for item in self.inventory], file, indent=4)

    def add_item(self, name, quantity, item_type):
        """Add a new item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if item_type not in ['firearm', 'uniform']:
            raise ValueError("Item type must be 'firearm' or 'uniform'.")
        
        self.inventory.append(InventoryItem(name, quantity, item_type))
        self.save_inventory()

    def remove_item(self, name):
        """Remove an item from the inventory by name."""
        self.inventory = [item for item in self.inventory if item.name != name]
        self.save_inventory()

    def update_item_quantity(self, name, quantity):
        """Update the quantity of an existing item."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        for item in self.inventory:
            if item.name == name:
                item.quantity = quantity
                self.save_inventory()
                return
        raise ValueError("Item not found in inventory.")

    def list_inventory(self):
        """List all items in the inventory."""
        return [(item.name, item.quantity, item.item_type) for item in self.inventory]

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_item("Replica Pistol", 10, "firearm")
        manager.add_item("Police Uniform", 5, "uniform")
        print("Current Inventory:")
        for item in manager.list_inventory():
            print(item)
        
        manager.update_item_quantity("Replica Pistol", 8)
        manager.remove_item("Police Uniform")
        
        print("Updated Inventory:")
        for item in manager.list_inventory():
            print(item)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
