"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Write a Python code to manage inventory of iron and steel products, including chapas galvanizadas and brancas, for a company like Eferroeaco."
Generated: DETERMINISTIC_d95152888d480591
Batch ID: 20250622_204617
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
    
    def __init__(self, name: str, quantity: int, unit_price: float):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units at ${self.unit_price:.2f} each"

    def total_value(self) -> float:
        """Calculate the total value of the inventory item."""
        return self.quantity * self.unit_price


class Inventory:
    """Class to manage the inventory of iron and steel products."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, unit_price: float) -> None:
        """Add a new item to the inventory."""
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = InventoryItem(name, quantity, unit_price)

    def remove_item(self, name: str, quantity: int) -> None:
        """Remove a specified quantity of an item from the inventory."""
        if name in self.items:
            if self.items[name].quantity >= quantity:
                self.items[name].quantity -= quantity
                if self.items[name].quantity == 0:
                    del self.items[name]
            else:
                raise ValueError(f"Not enough {name} in inventory to remove {quantity}.")
        else:
            raise KeyError(f"{name} not found in inventory.")

    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Retrieve an item from the inventory."""
        return self.items.get(name)

    def total_inventory_value(self) -> float:
        """Calculate the total value of the inventory."""
        return sum(item.total_value() for item in self.items.values())

    def list_inventory(self) -> List[str]:
        """List all items in the inventory."""
        return [str(item) for item in self.items.values()]

    def save_to_file(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({name: {'quantity': item.quantity, 'unit_price': item.unit_price} 
                        for name, item in self.items.items()}, file)

    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, details in data.items():
                    self.add_item(name, details['quantity'], details['unit_price'])
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}. Please check the file format.")


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Load existing inventory from file
    inventory.load_from_file('inventory.json')
    
    # Add items to inventory
    inventory.add_item('Chapa Galvanizada', 100, 50.0)
    inventory.add_item('Chapa Branca', 200, 45.0)

    # Remove some items
    try:
        inventory.remove_item('Chapa Galvanizada', 20)
    except (ValueError, KeyError) as e:
        print(e)

    # List current inventory
    print("Current Inventory:")
    for item in inventory.list_inventory():
        print(item)

    # Total inventory value
    print(f"Total Inventory Value: ${inventory.total_inventory_value():.2f}")

    # Save inventory to file
    inventory.save_to_file('inventory.json')
```
