"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Write code to simulate an inventory management system for a dealership that uses "Гарант" as a supplier for automotive glass adhesives and primers.
Generated: DETERMINISTIC_a328d6f4d26fc0b0
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class InventoryItem:
    """Class representing an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, supplier: str):
        self.name = name
        self.quantity = quantity
        self.supplier = supplier

    def __repr__(self):
        return f"InventoryItem(name={self.name}, quantity={self.quantity}, supplier={self.supplier})"

class InventoryManagementSystem:
    """Class to manage the inventory of automotive glass adhesives and primers."""
    
    def __init__(self):
        self.inventory: List[InventoryItem] = []

    def add_item(self, name: str, quantity: int, supplier: str = "Гарант") -> None:
        """Add a new item to the inventory."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        item = InventoryItem(name, quantity, supplier)
        self.inventory.append(item)
        print(f"Added item: {item}")

    def remove_item(self, name: str, quantity: int) -> None:
        """Remove a specified quantity of an item from the inventory."""
        for item in self.inventory:
            if item.name == name:
                if quantity > item.quantity:
                    raise ValueError("Cannot remove more than available in inventory.")
                item.quantity -= quantity
                print(f"Removed {quantity} of {name}. Remaining: {item.quantity}")
                if item.quantity == 0:
                    self.inventory.remove(item)
                return
        raise ValueError(f"Item '{name}' not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Optional[str]]]:
        """Return the current inventory as a list of dictionaries."""
        return [{"name": item.name, "quantity": item.quantity, "supplier": item.supplier} for item in self.inventory]

    def save_inventory(self, filename: str) -> None:
        """Save the current inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
            print(f"Inventory saved to {filename}.")
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(item['name'], item['quantity'], item['supplier'])
            print(f"Inventory loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

# Example usage
if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.add_item("Glass Adhesive", 50)
    ims.add_item("Glass Primer", 30)
    print(ims.get_inventory())
    ims.remove_item("Glass Adhesive", 10)
    ims.save_inventory("inventory.json")
    ims.load_inventory("inventory.json")
```
