"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Develop a script to manage inventory and pricing for an e-commerce store selling items like Noymi 3-in-1 Shaver and Beard Trimmer for Men | ET-175.
Generated: DETERMINISTIC_5af55d2dba4067ae
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Any

class InventoryItem:
    """Represents an item in the inventory."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"InventoryItem(name={self.name}, price={self.price}, quantity={self.quantity})"

class InventoryManager:
    """Manages the inventory and pricing for an e-commerce store."""

    def __init__(self, inventory_file: str):
        self.inventory_file = inventory_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()

    def load_inventory(self) -> None:
        """Loads inventory data from the JSON file."""
        if not os.path.exists(self.inventory_file):
            print("Inventory file not found. Initializing an empty inventory.")
            return
        
        with open(self.inventory_file, 'r') as file:
            try:
                data = json.load(file)
                for item in data:
                    self.inventory[item['name']] = InventoryItem(item['name'], item['price'], item['quantity'])
            except json.JSONDecodeError:
                print("Error: Failed to decode JSON from the inventory file.")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def save_inventory(self) -> None:
        """Saves the current inventory data to the JSON file."""
        with open(self.inventory_file, 'w') as file:
            data = [{'name': item.name, 'price': item.price, 'quantity': item.quantity} for item in self.inventory.values()]
            json.dump(data, file, indent=4)

    def add_item(self, name: str, price: float, quantity: int) -> None:
        """Adds a new item to the inventory."""
        if name in self.inventory:
            print(f"Item '{name}' already exists. Updating quantity.")
            self.inventory[name].quantity += quantity
        else:
            self.inventory[name] = InventoryItem(name, price, quantity)
        self.save_inventory()

    def update_price(self, name: str, new_price: float) -> None:
        """Updates the price of an existing item in the inventory."""
        if name in self.inventory:
            self.inventory[name].price = new_price
            self.save_inventory()
        else:
            print(f"Item '{name}' not found in inventory.")

    def remove_item(self, name: str) -> None:
        """Removes an item from the inventory."""
        if name in self.inventory:
            del self.inventory[name]
            self.save_inventory()
        else:
            print(f"Item '{name}' not found in inventory.")

    def list_inventory(self) -> List[Dict[str, Any]]:
        """Returns a list of all items in the inventory."""
        return [{'name': item.name, 'price': item.price, 'quantity': item.quantity} for item in self.inventory.values()]

if __name__ == "__main__":
    # Example usage of InventoryManager
    manager = InventoryManager("inventory.json")

    # Add items to inventory
    manager.add_item("Noymi 3-in-1 Shaver and Beard Trimmer for Men | ET-175", 49.99, 10)

    # Update price of an item
    manager.update_price("Noymi 3-in-1 Shaver and Beard Trimmer for Men | ET-175", 45.99)

    # List all items in inventory
    print("Current Inventory:")
    print(manager.list_inventory())

    # Remove an item from inventory
    manager.remove_item("Noymi 3-in-1 Shaver and Beard Trimmer for Men | ET-175")
```
