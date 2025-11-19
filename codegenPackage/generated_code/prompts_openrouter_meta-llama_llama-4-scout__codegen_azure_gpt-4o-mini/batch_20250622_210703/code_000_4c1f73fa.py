"""
Generated Code Metadata:
========================
Original URL: https://bekon.rs
Prompt: Write a Python script to manage inventory for a butcher shop like Bekon Promet, including tracking of fresh meat, sausages, and dry products.
Generated: DETERMINISTIC_4c1f73fabe0a379c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, category: str, quantity: int, price_per_unit: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def __repr__(self):
        return f"{self.name} ({self.category}): {self.quantity} units at ${self.price_per_unit:.2f} each"

    def total_value(self) -> float:
        """Calculate the total value of the item in inventory."""
        return self.quantity * self.price_per_unit


class Inventory:
    """Class to manage the inventory of the butcher shop."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        if item.name in self.items:
            raise ValueError(f"Item '{item.name}' already exists in the inventory.")
        self.items[item.name] = item

    def update_item(self, name: str, quantity: int = None, price_per_unit: float = None) -> None:
        """Update the quantity or price of an existing item."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in the inventory.")
        
        if quantity is not None:
            self.items[name].quantity = quantity
        if price_per_unit is not None:
            self.items[name].price_per_unit = price_per_unit

    def remove_item(self, name: str) -> None:
        """Remove an item from the inventory."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in the inventory.")
        del self.items[name]

    def get_inventory_value(self) -> float:
        """Calculate the total value of the inventory."""
        return sum(item.total_value() for item in self.items.values())

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({name: item.__dict__ for name, item in self.items.items()}, file)

    def load_from_file(self, filename: str) -> None:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, item_data in data.items():
                    self.items[name] = InventoryItem(**item_data)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file '{filename}'. Please check the file format.")


def main():
    """Main function to manage the inventory."""
    inventory = Inventory()

    # Load existing inventory from file
    inventory.load_from_file('inventory.json')

    # Example operations
    try:
        # Adding items
        inventory.add_item(InventoryItem("Fresh Beef", "Fresh Meat", 50, 5.99))
        inventory.add_item(InventoryItem("Pork Sausage", "Sausages", 30, 3.49))
        inventory.add_item(InventoryItem("Dried Ham", "Dry Products", 20, 12.99))

        # Updating an item
        inventory.update_item("Fresh Beef", quantity=45)

        # Removing an item
        inventory.remove_item("Dried Ham")

        # Display total inventory value
        print(f"Total inventory value: ${inventory.get_inventory_value():.2f}")

        # Save inventory to file
        inventory.save_to_file('inventory.json')

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
