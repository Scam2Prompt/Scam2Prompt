"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: "Write a Python code snippet to manage inventory for a company like PEW Engineering Pvt. Ltd. that manufactures brake system components, including Brake Cylinders, Reservoirs, and Angle Cocks."
Generated: DETERMINISTIC_92f5de39a873f985
Batch ID: 20250622_212859
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
    """Class to represent an inventory item."""
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"InventoryItem(name={self.name}, quantity={self.quantity}, price={self.price})"

class Inventory:
    """Class to manage the inventory of brake system components."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item to the inventory."""
        if name in self.items:
            raise ValueError(f"Item '{name}' already exists in inventory.")
        self.items[name] = InventoryItem(name, quantity, price)

    def update_item(self, name: str, quantity: Optional[int] = None, price: Optional[float] = None) -> None:
        """Update the quantity or price of an existing item."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in inventory.")
        if quantity is not None:
            self.items[name].quantity = quantity
        if price is not None:
            self.items[name].price = price

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in inventory.")
        del self.items[name]

    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Retrieve an item from the inventory."""
        return self.items.get(name)

    def list_items(self) -> List[InventoryItem]:
        """List all items in the inventory."""
        return list(self.items.values())

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({name: item.__dict__ for name, item in self.items.items()}, file)

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.items = {name: InventoryItem(**item) for name, item in data.items()}
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file '{filename}'. Please check the file format.")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding items to the inventory
    inventory.add_item("Brake Cylinder", 100, 150.0)
    inventory.add_item("Reservoir", 200, 75.0)
    inventory.add_item("Angle Cock", 150, 50.0)

    # Listing items
    print("Current Inventory:")
    for item in inventory.list_items():
        print(item)

    # Updating an item
    inventory.update_item("Brake Cylinder", quantity=120)

    # Saving inventory to a file
    inventory.save_to_file("inventory.json")

    # Loading inventory from a file
    inventory.load_from_file("inventory.json")
```
