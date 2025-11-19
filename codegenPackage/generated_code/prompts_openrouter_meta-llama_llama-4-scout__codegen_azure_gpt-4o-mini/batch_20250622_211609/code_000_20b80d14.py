"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Write a Python code to manage inventory of construction machinery attachments like Hydraulic Breaker, Earth Auger Drill, and Pile Driver.
Generated: DETERMINISTIC_20b80d14bf1cb55d
Batch ID: 20250622_211609
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

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self) -> str:
        return f"InventoryItem(name={self.name}, quantity={self.quantity}, price={self.price})"

class Inventory:
    """Class to manage the inventory of construction machinery attachments."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item to the inventory."""
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = InventoryItem(name, quantity, price)

    def remove_item(self, name: str, quantity: int) -> None:
        """Remove a specified quantity of an item from the inventory."""
        if name in self.items:
            if self.items[name].quantity >= quantity:
                self.items[name].quantity -= quantity
                if self.items[name].quantity == 0:
                    del self.items[name]
            else:
                raise ValueError(f"Not enough quantity of {name} to remove.")
        else:
            raise KeyError(f"{name} not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Return a list of all items in the inventory."""
        return [vars(item) for item in self.items.values()]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item in items:
                    self.add_item(item['name'], item['quantity'], item['price'])
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item("Hydraulic Breaker", 10, 1500.00)
    inventory.add_item("Earth Auger Drill", 5, 1200.00)
    inventory.add_item("Pile Driver", 3, 2500.00)

    # Display current inventory
    print("Current Inventory:", inventory.get_inventory())

    # Removing an item
    try:
        inventory.remove_item("Earth Auger Drill", 2)
    except (ValueError, KeyError) as e:
        print(e)

    # Display updated inventory
    print("Updated Inventory:", inventory.get_inventory())

    # Save inventory to a file
    inventory.save_inventory("inventory.json")

    # Load inventory from a file
    new_inventory = Inventory()
    new_inventory.load_inventory("inventory.json")
    print("Loaded Inventory:", new_inventory.get_inventory())
```
