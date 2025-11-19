"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Write a Python script to manage home staging inventory, including furniture and décor, for a company like Unique Home Staging & Redesign by Dee.
Generated: DETERMINISTIC_708fb24d72e76b13
Batch ID: 20250622_210856
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
    
    def __init__(self, name, category, quantity, condition):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.condition = condition

    def to_dict(self):
        """Convert the item to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'condition': self.condition
        }

class InventoryManager:
    """Class to manage the home staging inventory."""
    
    def __init__(self, inventory_file='inventory.json'):
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, 'r') as file:
                return [InventoryItem(**item) for item in json.load(file)]
        return []

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.inventory_file, 'w') as file:
            json.dump([item.to_dict() for item in self.inventory], file, indent=4)

    def add_item(self, name, category, quantity, condition):
        """Add a new item to the inventory."""
        new_item = InventoryItem(name, category, quantity, condition)
        self.inventory.append(new_item)
        self.save_inventory()

    def remove_item(self, name):
        """Remove an item from the inventory by name."""
        self.inventory = [item for item in self.inventory if item.name != name]
        self.save_inventory()

    def update_item(self, name, quantity=None, condition=None):
        """Update the quantity and/or condition of an existing item."""
        for item in self.inventory:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if condition is not None:
                    item.condition = condition
                self.save_inventory()
                return
        raise ValueError(f"Item '{name}' not found in inventory.")

    def list_inventory(self):
        """List all items in the inventory."""
        return [item.to_dict() for item in self.inventory]

def main():
    """Main function to run the inventory manager."""
    manager = InventoryManager()

    # Example usage
    try:
        manager.add_item('Sofa', 'Furniture', 5, 'New')
        manager.add_item('Coffee Table', 'Furniture', 3, 'Used')
        manager.update_item('Sofa', quantity=4)
        manager.remove_item('Coffee Table')

        # Print current inventory
        inventory_list = manager.list_inventory()
        print(json.dumps(inventory_list, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
