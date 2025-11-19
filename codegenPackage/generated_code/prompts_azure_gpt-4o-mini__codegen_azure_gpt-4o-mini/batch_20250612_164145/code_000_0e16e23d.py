"""
Generated Code Metadata:
========================
Original URL: https://poocoiniswaptokens.blogspot.com
Prompt: Generate a Python script that simulates the inventory management for a hardware store, including tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_0e16e23d0579bb1c
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

class Inventory:
    """Class to manage the inventory of a hardware store."""
    
    def __init__(self):
        self.items: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int):
        """Add a new item to the inventory or update the quantity if it exists."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = InventoryItem(name, quantity)

    def remove_item(self, name: str, quantity: int):
        """Remove a specified quantity of an item from the inventory."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in inventory.")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if self.items[name].quantity < quantity:
            raise ValueError("Not enough quantity in inventory to remove.")
        
        self.items[name].quantity -= quantity
        
        if self.items[name].quantity == 0:
            del self.items[name]  # Remove item if quantity is zero

    def get_inventory(self) -> List[str]:
        """Return a list of all items in the inventory."""
        return [str(item) for item in self.items.values()]

    def save_inventory(self, filename: str):
        """Save the current inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump({name: item.quantity for name, item in self.items.items()}, file)

    def load_inventory(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for name, quantity in data.items():
                    self.add_item(name, quantity)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file '{filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the inventory management system."""
    inventory = Inventory()
    
    # Load existing inventory from file
    inventory.load_inventory('inventory.json')

    # Example operations
    try:
        inventory.add_item("alicate", 10)
        inventory.add_item("furadeira", 5)
        inventory.add_item("parafusadeira", 7)
        inventory.remove_item("alicate", 2)

        # Print current inventory
        print("Current Inventory:")
        for item in inventory.get_inventory():
            print(item)

        # Save inventory to file
        inventory.save_inventory('inventory.json')

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
