"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Generate a code snippet for a sewing machine inventory management system that includes features for tracking mechanical and electronic sewing machines, overlockers, and accessories available at Isabel Reina Chic.
Generated: DETERMINISTIC_62b373b07e4a7c28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class SewingMachine:
    """Class to represent a sewing machine."""
    
    def __init__(self, id: int, type: str, brand: str, model: str, quantity: int):
        self.id = id
        self.type = type  # e.g., 'mechanical', 'electronic', 'overlocker'
        self.brand = brand
        self.model = model
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the sewing machine object to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'brand': self.brand,
            'model': self.model,
            'quantity': self.quantity
        }

class Inventory:
    """Class to manage the inventory of sewing machines and accessories."""
    
    def __init__(self):
        self.items: List[SewingMachine] = []

    def add_item(self, item: SewingMachine) -> None:
        """Add a new sewing machine to the inventory."""
        self.items.append(item)

    def remove_item(self, item_id: int) -> None:
        """Remove a sewing machine from the inventory by ID."""
        self.items = [item for item in self.items if item.id != item_id]

    def update_quantity(self, item_id: int, quantity: int) -> None:
        """Update the quantity of a sewing machine in the inventory."""
        for item in self.items:
            if item.id == item_id:
                item.quantity = quantity
                return
        raise ValueError(f"Item with ID {item_id} not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Get the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                inventory_data = json.load(file)
                self.items = [SewingMachine(**item) for item in inventory_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item(SewingMachine(1, 'mechanical', 'Singer', 'SewMate 5400', 5))
    inventory.add_item(SewingMachine(2, 'electronic', 'Brother', 'CS6000i', 3))
    inventory.add_item(SewingMachine(3, 'overlocker', 'Janome', 'MyLock 634D', 2))

    # Updating quantity
    try:
        inventory.update_quantity(1, 4)
    except ValueError as e:
        print(e)

    # Saving inventory to a file
    inventory.save_to_file('sewing_machine_inventory.json')

    # Loading inventory from a file
    inventory.load_from_file('sewing_machine_inventory.json')

    # Displaying the current inventory
    print(inventory.get_inventory())
```
