"""
Generated Code Metadata:
========================
Original URL: https://vividolev.com
Prompt: Write a code snippet to manage inventory for a company like Vivid Olev that produces various types of vegetable oils and green fuels.
Generated: DETERMINISTIC_67bfbec98eeca4f1
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
from typing import Dict, List, Optional

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price_per_unit: float):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def __repr__(self):
        return f"InventoryItem(name={self.name}, quantity={self.quantity}, price_per_unit={self.price_per_unit})"

class InventoryManager:
    """Class to manage the inventory of vegetable oils and green fuels."""
    
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price_per_unit: float) -> None:
        """Add a new item to the inventory."""
        if quantity < 0 or price_per_unit < 0:
            raise ValueError("Quantity and price per unit must be non-negative.")
        
        if name in self.inventory:
            self.inventory[name].quantity += quantity
        else:
            self.inventory[name] = InventoryItem(name, quantity, price_per_unit)

    def remove_item(self, name: str, quantity: int) -> None:
        """Remove a specified quantity of an item from the inventory."""
        if name not in self.inventory:
            raise KeyError(f"Item '{name}' not found in inventory.")
        
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        
        if self.inventory[name].quantity < quantity:
            raise ValueError("Insufficient quantity in inventory.")
        
        self.inventory[name].quantity -= quantity
        
        if self.inventory[name].quantity == 0:
            del self.inventory[name]

    def get_inventory(self) -> List[InventoryItem]:
        """Return a list of all items in the inventory."""
        return list(self.inventory.values())

    def save_inventory(self, file_path: str) -> None:
        """Save the current inventory to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump({name: item.__dict__ for name, item in self.inventory.items()}, file)
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory to {file_path}: {e}")

    def load_inventory(self, file_path: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.inventory = {name: InventoryItem(**item) for name, item in data.items()}
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load inventory from {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    manager.add_item("Olive Oil", 100, 10.99)
    manager.add_item("Sunflower Oil", 200, 5.49)
    print(manager.get_inventory())
    
    manager.remove_item("Olive Oil", 50)
    print(manager.get_inventory())
    
    manager.save_inventory("inventory.json")
    manager.load_inventory("inventory.json")
    print(manager.get_inventory())
```
