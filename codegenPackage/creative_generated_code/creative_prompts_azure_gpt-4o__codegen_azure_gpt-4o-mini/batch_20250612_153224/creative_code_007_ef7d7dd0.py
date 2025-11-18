"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afranaden.org
Prompt: Write a program to manage inventory for a charitable bakery system, inspired by the "Aden Charity Bakery" initiative described on the Gulf and Aden Development and Humanitarian Services Authority's site.
Generated: DETERMINISTIC_ef7d7dd0106dff65
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class InventoryItem:
    """Class representing an inventory item for the bakery."""
    
    def __init__(self, name: str, quantity: int, unit_price: float):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
    
    def update_quantity(self, quantity: int):
        """Update the quantity of the inventory item."""
        self.quantity += quantity
    
    def __repr__(self):
        return f"InventoryItem(name={self.name}, quantity={self.quantity}, unit_price={self.unit_price})"

class InventoryManager:
    """Class to manage the inventory of the bakery."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}
    
    def add_item(self, name: str, quantity: int, unit_price: float):
        """Add a new item to the inventory or update an existing item's quantity."""
        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = InventoryItem(name, quantity, unit_price)
    
    def remove_item(self, name: str, quantity: int):
        """Remove a specified quantity of an item from the inventory."""
        if name in self.items:
            if self.items[name].quantity >= quantity:
                self.items[name].update_quantity(-quantity)
            else:
                raise ValueError(f"Insufficient quantity of {name} in inventory.")
        else:
            raise KeyError(f"Item {name} not found in inventory.")
    
    def get_inventory(self) -> List[InventoryItem]:
        """Return a list of all inventory items."""
        return list(self.items.values())

    def save_inventory(self, file_path: str):
        """Save the current inventory to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump({name: {"quantity": item.quantity, "unit_price": item.unit_price} 
                            for name, item in self.items.items()}, f)
        except IOError as e:
            print(f"Error saving inventory to {file_path}: {e}")
    
    def load_inventory(self, file_path: str):
        """Load inventory from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for name, details in data.items():
                    self.add_item(name, details['quantity'], details['unit_price'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {file_path}: {e}")

def main():
    """Main function to demonstrate the inventory management system."""
    inventory_manager = InventoryManager()
    
    # Load inventory from file if it exists
    inventory_manager.load_inventory('inventory.json')
    
    # Example operations
    inventory_manager.add_item('Flour', 50, 0.5)
    inventory_manager.add_item('Sugar', 30, 0.3)
    inventory_manager.add_item('Eggs', 20, 0.2)
    
    # Print current inventory
    print("Current Inventory:")
    for item in inventory_manager.get_inventory():
        print(item)
    
    # Save inventory to file
    inventory_manager.save_inventory('inventory.json')

if __name__ == "__main__":
    main()
```
