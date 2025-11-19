"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoiniswaptokens.blogspot.com
Prompt: Generate a Python script that simulates the inventory management for a hardware store, including tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_0e16e23d0579bb1c
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class InventoryItem:
    """Class to represent an item in the inventory."""

    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"InventoryItem(name={self.name}, quantity={self.quantity}, price={self.price})"

    def update_quantity(self, amount: int):
        """Update the quantity of the item."""
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

class Inventory:
    """Class to manage the inventory of the hardware store."""

    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price: float):
        """Add a new item to the inventory."""
        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = InventoryItem(name, quantity, price)

    def remove_item(self, name: str, quantity: int):
        """Remove a specified quantity of an item from the inventory."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in inventory.")
        self.items[name].update_quantity(-quantity)

    def get_inventory(self) -> List[InventoryItem]:
        """Return a list of all inventory items."""
        return list(self.items.values())

    def save_to_file(self, filename: str):
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({name: vars(item) for name, item in self.items.items()}, file)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename: str):
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, item in data.items():
                    self.items[name] = InventoryItem(**item)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

def main():
    """Main function to simulate inventory management."""
    store_inventory = Inventory()

    # Sample data
    store_inventory.add_item("alicate", 10, 15.50)
    store_inventory.add_item("furadeira", 5, 250.00)
    store_inventory.add_item("parafusadeira", 8, 180.00)

    # Display current inventory
    print("Current Inventory:")
    for item in store_inventory.get_inventory():
        print(item)

    # Simulate removing an item
    try:
        store_inventory.remove_item("alicate", 2)
        print("\nInventory after removing 2 alicates:")
        for item in store_inventory.get_inventory():
            print(item)
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)

    # Save inventory to file
    store_inventory.save_to_file("inventory.json")

    # Load inventory from file
    new_inventory = Inventory()
    new_inventory.load_from_file("inventory.json")
    print("\nLoaded Inventory from file:")
    for item in new_inventory.get_inventory():
        print(item)

if __name__ == "__main__":
    main()
```
