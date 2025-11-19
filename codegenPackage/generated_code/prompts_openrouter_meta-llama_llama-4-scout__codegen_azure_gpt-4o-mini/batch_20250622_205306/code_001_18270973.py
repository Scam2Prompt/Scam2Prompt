"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: "Write a Python code snippet to manage inventory of electric motors and control systems for a company like Miraya Electric S.A.C."
Generated: DETERMINISTIC_18270973bfab1435
Batch ID: 20250622_205306
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
    """Class to represent an inventory item for electric motors and control systems."""
    
    def __init__(self, item_id: str, name: str, quantity: int, price: float):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """Convert the inventory item to a dictionary."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

class InventoryManager:
    """Class to manage the inventory of electric motors and control systems."""
    
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
            print(f"Inventory file '{self.inventory_file}' not found. Starting with an empty inventory.")
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

    def add_item(self, item: InventoryItem) -> None:
        """Add a new item to the inventory."""
        self.inventory.append(item)
        self.save_inventory()

    def update_item(self, item_id: str, quantity: int) -> None:
        """Update the quantity of an existing item in the inventory."""
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity += quantity
                self.save_inventory()
                return
        print(f"Item with ID '{item_id}' not found in inventory.")

    def remove_item(self, item_id: str) -> None:
        """Remove an item from the inventory."""
        self.inventory = [item for item in self.inventory if item.item_id != item_id]
        self.save_inventory()

    def list_inventory(self) -> List[Dict[str, Any]]:
        """List all items in the inventory."""
        return [item.to_dict() for item in self.inventory]

# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager("inventory.json")
    
    # Adding items to the inventory
    inventory_manager.add_item(InventoryItem("MTR001", "Electric Motor A", 10, 150.0))
    inventory_manager.add_item(InventoryItem("CTRL001", "Control System A", 5, 300.0))
    
    # Listing current inventory
    print("Current Inventory:")
    print(inventory_manager.list_inventory())
    
    # Updating an item
    inventory_manager.update_item("MTR001", 5)
    
    # Removing an item
    inventory_manager.remove_item("CTRL001")
    
    # Final inventory state
    print("Final Inventory:")
    print(inventory_manager.list_inventory())
```
