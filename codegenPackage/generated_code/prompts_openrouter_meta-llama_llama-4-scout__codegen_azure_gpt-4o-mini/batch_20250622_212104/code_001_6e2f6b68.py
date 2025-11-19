"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Write a Python code snippet to manage inventory of ferramentas and equipment, including tracking device serial numbers and maintenance schedules.
Generated: DETERMINISTIC_6e2f6b68669d157b
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name, serial_number, maintenance_due):
        """
        Initialize an inventory item.

        :param name: Name of the item
        :param serial_number: Serial number of the item
        :param maintenance_due: Date when maintenance is due
        """
        self.name = name
        self.serial_number = serial_number
        self.maintenance_due = maintenance_due

    def is_maintenance_due(self):
        """Check if maintenance is due."""
        return datetime.now() >= self.maintenance_due

    def __repr__(self):
        return f"InventoryItem(name={self.name}, serial_number={self.serial_number}, maintenance_due={self.maintenance_due.strftime('%Y-%m-%d')})"


class Inventory:
    """Class to manage the inventory of items."""
    
    def __init__(self):
        """Initialize the inventory with an empty list."""
        self.items = []

    def add_item(self, item):
        """
        Add an item to the inventory.

        :param item: InventoryItem to be added
        """
        if not isinstance(item, InventoryItem):
            raise ValueError("item must be an instance of InventoryItem")
        self.items.append(item)

    def remove_item(self, serial_number):
        """
        Remove an item from the inventory by its serial number.

        :param serial_number: Serial number of the item to be removed
        :raises ValueError: If the item is not found
        """
        for item in self.items:
            if item.serial_number == serial_number:
                self.items.remove(item)
                return
        raise ValueError(f"Item with serial number {serial_number} not found.")

    def get_due_maintenance_items(self):
        """Return a list of items that are due for maintenance."""
        return [item for item in self.items if item.is_maintenance_due()]

    def save_to_file(self, filename):
        """
        Save the inventory to a JSON file.

        :param filename: Name of the file to save the inventory
        """
        try:
            with open(filename, 'w') as file:
                json.dump([item.__dict__ for item in self.items], file, default=str)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename):
        """
        Load the inventory from a JSON file.

        :param filename: Name of the file to load the inventory from
        """
        try:
            with open(filename, 'r') as file:
                items_data = json.load(file)
                self.items = [InventoryItem(item['name'], item['serial_number'], datetime.fromisoformat(item['maintenance_due'])) for item in items_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item(InventoryItem("Drill", "SN123456", datetime.now() + timedelta(days=30)))
    inventory.add_item(InventoryItem("Saw", "SN654321", datetime.now() - timedelta(days=1)))  # Maintenance overdue

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")

    # Checking for items due for maintenance
    due_items = inventory.get_due_maintenance_items()
    print("Items due for maintenance:", due_items)
```
