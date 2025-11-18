"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Write a script to manage warehousing logistics, including inventory tracking and safety protocols for goods stored for days or months, as offered by Portline Shipping.
Generated: DETERMINISTIC_51765cbb2b812f78
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, item_id, name, quantity, stored_date):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.stored_date = stored_date  # Expected to be a datetime object
    
    def days_in_storage(self):
        """Calculate how many days the item has been stored."""
        return (datetime.now() - self.stored_date).days

    def is_expired(self, max_storage_days):
        """Check if the item has exceeded the maximum storage period."""
        return self.days_in_storage() > max_storage_days

class Warehouse:
    """Class to manage a warehouse and its inventory."""
    
    def __init__(self):
        self.inventory = {}
    
    def add_item(self, item_id, name, quantity, stored_date):
        """Add a new item to the inventory."""
        if item_id in self.inventory:
            raise ValueError(f"Item with ID {item_id} already exists.")
        self.inventory[item_id] = InventoryItem(item_id, name, quantity, stored_date)
    
    def remove_item(self, item_id):
        """Remove an item from the inventory."""
        if item_id not in self.inventory:
            raise ValueError(f"Item with ID {item_id} not found in inventory.")
        del self.inventory[item_id]
    
    def check_inventory(self):
        """Return the current status of the inventory."""
        return {item_id: {"name": item.name, "quantity": item.quantity, "stored_date": item.stored_date.strftime("%Y-%m-%d"), "days_in_storage": item.days_in_storage()} 
                        for item_id, item in self.inventory.items()}
    
    def check_expired_items(self, max_storage_days):
        """Return a list of expired items."""
        expired_items = {item_id: item for item_id, item in self.inventory.items() if item.is_expired(max_storage_days)}
        return expired_items

def save_inventory_to_file(warehouse, filename):
    """Save the current inventory state to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(warehouse.check_inventory(), file, default=str)
    except IOError as e:
        print(f"Error saving inventory to file: {e}")

def load_inventory_from_file(warehouse, filename):
    """Load inventory state from a JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for item_id, item_data in data.items():
                warehouse.add_item(item_id, item_data["name"], item_data["quantity"], datetime.strptime(item_data["stored_date"], "%Y-%m-%d"))
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    warehouse = Warehouse()
    
    # Adding items to the inventory
    warehouse.add_item("001", "Widget A", 100, datetime.now() - timedelta(days=5))
    warehouse.add_item("002", "Widget B", 50, datetime.now() - timedelta(days=10))
    
    # Check the current inventory
    print(warehouse.check_inventory())
    
    # Check for expired items
    expired_items = warehouse.check_expired_items(max_storage_days=7)
    print("Expired Items:", expired_items)
    
    # Save inventory to file
    save_inventory_to_file(warehouse, 'inventory.json')
    
    # Load inventory from file
    load_inventory_from_file(warehouse, 'inventory.json')
```
