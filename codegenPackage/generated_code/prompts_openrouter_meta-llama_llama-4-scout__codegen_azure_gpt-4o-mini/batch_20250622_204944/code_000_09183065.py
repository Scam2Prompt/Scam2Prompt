"""
Generated Code Metadata:
========================
Original URL: https://naimatabbasind.com
Prompt: "Write a Python code to manage inventory for a customized clothing manufacturer like Naimat Abbas Industries."
Generated: DETERMINISTIC_09183065a57044f0
Batch ID: 20250622_204944
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
    
    def __init__(self, item_id: int, name: str, quantity: int, price: float):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for easy serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

class InventoryManager:
    """Class to manage the inventory of clothing items."""
    
    def __init__(self, inventory_file: str):
        self.inventory_file = inventory_file
        self.inventory: List[InventoryItem] = []
        self.load_inventory()

    def load_inventory(self) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(self.inventory_file, 'r') as file:
                items = json.load(file)
                self.inventory = [InventoryItem(**item) for item in items]
        except FileNotFoundError:
            print("Inventory file not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the inventory file. Starting with an empty inventory.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_inventory(self) -> None:
        """Save the current inventory to a JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump([item.to_dict() for item in self.inventory], file, indent=4)
        except Exception as e:
            print(f"Failed to save inventory: {e}")

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add a new item to the inventory."""
        item_id = len(self.inventory) + 1  # Simple ID assignment
        new_item = InventoryItem(item_id, name, quantity, price)
        self.inventory.append(new_item)
        self.save_inventory()

    def update_item(self, item_id: int, quantity: int, price: float) -> None:
        """Update an existing item in the inventory."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity = quantity
                item.price = price
                self.save_inventory()
                return
        print(f"Item with ID {item_id} not found.")

    def remove_item(self, item_id: int) -> None:
        """Remove an item from the inventory."""
        self.inventory = [item for item in self.inventory if item.item_id != item_id]
        self.save_inventory()

    def list_inventory(self) -> None:
        """List all items in the inventory."""
        if not self.inventory:
            print("Inventory is empty.")
            return
        for item in self.inventory:
            print(f"ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price:.2f}")

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager("inventory.json")
    inventory_manager.add_item("Custom T-Shirt", 50, 19.99)
    inventory_manager.add_item("Custom Hoodie", 30, 39.99)
    inventory_manager.list_inventory()
    inventory_manager.update_item(1, 45, 18.99)
    inventory_manager.remove_item(2)
    inventory_manager.list_inventory()
```
