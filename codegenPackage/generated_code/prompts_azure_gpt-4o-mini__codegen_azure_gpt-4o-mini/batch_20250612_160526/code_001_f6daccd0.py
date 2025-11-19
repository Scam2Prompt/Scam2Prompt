"""
Generated Code Metadata:
========================
Original URL: https://screciclados.mx
Prompt: How can I implement a recycling management system that tracks electronic waste, inspired by the practices of SCR Reciclados?
Generated: DETERMINISTIC_f6daccd07b85d5c6
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class ElectronicWaste:
    """Class to represent electronic waste items."""
    
    def __init__(self, item_id, name, weight, category, date_received):
        self.item_id = item_id
        self.name = name
        self.weight = weight  # in kilograms
        self.category = category
        self.date_received = date_received  # datetime object

    def to_dict(self):
        """Convert the ElectronicWaste object to a dictionary."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "weight": self.weight,
            "category": self.category,
            "date_received": self.date_received.isoformat()
        }

class RecyclingManagementSystem:
    """Class to manage electronic waste recycling operations."""
    
    def __init__(self, storage_file='ewaste_data.json'):
        self.storage_file = storage_file
        self.waste_items = self.load_data()

    def load_data(self):
        """Load electronic waste data from a JSON file."""
        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                return [ElectronicWaste(**item) for item in data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted.")
            return []

    def save_data(self):
        """Save electronic waste data to a JSON file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([item.to_dict() for item in self.waste_items], file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_waste_item(self, name, weight, category):
        """Add a new electronic waste item to the system."""
        item_id = len(self.waste_items) + 1  # Simple ID generation
        date_received = datetime.now()
        new_item = ElectronicWaste(item_id, name, weight, category, date_received)
        self.waste_items.append(new_item)
        self.save_data()

    def list_waste_items(self):
        """List all electronic waste items in the system."""
        for item in self.waste_items:
            print(f"ID: {item.item_id}, Name: {item.name}, Weight: {item.weight}kg, "
                  f"Category: {item.category}, Date Received: {item.date_received}")

    def find_waste_item(self, item_id):
        """Find an electronic waste item by its ID."""
        for item in self.waste_items:
            if item.item_id == item_id:
                return item
        return None

# Example usage
if __name__ == "__main__":
    system = RecyclingManagementSystem()
    
    # Adding electronic waste items
    system.add_waste_item("Old Laptop", 2.5, "Computers")
    system.add_waste_item("Broken Smartphone", 0.3, "Mobile Devices")
    
    # Listing all waste items
    system.list_waste_items()
    
    # Finding a specific waste item
    item = system.find_waste_item(1)
    if item:
        print(f"Found item: {item.name}, Weight: {item.weight}kg")
    else:
        print("Item not found.")
```
