"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Write a Python script to manage inventory of door hardware, including keypads, deadbolts, and handle sets, for a company like Southern Brass that serves builders and construction companies.
Generated: DETERMINISTIC_737ea473b941553b
Batch ID: 20250622_210650
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
    """Class to represent an inventory item for door hardware."""
    
    def __init__(self, item_id, name, category, quantity, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """Convert the item to a dictionary for easy serialization."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price': self.price
        }

class InventoryManager:
    """Class to manage the inventory of door hardware."""
    
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

    def add_item(self, item):
        """Add a new item to the inventory."""
        self.inventory.append(item)
        self.save_inventory()

    def update_item(self, item_id, quantity):
        """Update the quantity of an existing item."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity += quantity
                self.save_inventory()
                return
        raise ValueError(f"Item with ID {item_id} not found.")

    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        self.inventory = [item for item in self.inventory if item.item_id != item_id]
        self.save_inventory()

    def list_inventory(self):
        """List all items in the inventory."""
        return self.inventory

def main():
    """Main function to run the inventory management system."""
    manager = InventoryManager()

    # Example usage
    try:
        # Adding items
        manager.add_item(InventoryItem(item_id='KP001', name='Keypad Lock', category='Keypads', quantity=10, price=99.99))
        manager.add_item(InventoryItem(item_id='DB001', name='Deadbolt', category='Deadbolts', quantity=15, price=49.99))
        
        # Listing inventory
        for item in manager.list_inventory():
            print(f"{item.name} (ID: {item.item_id}) - Quantity: {item.quantity}, Price: ${item.price:.2f}")

        # Updating an item
        manager.update_item('KP001', 5)

        # Removing an item
        manager.remove_item('DB001')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
