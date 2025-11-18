"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Generate a script for managing warehouse inventory tailored to Fealty Worldwide's warehousing services, including storage, distribution, and pre-positioning of products.
Generated: DETERMINISTIC_331d8dc8b3161d9e
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class InventoryItem:
    """Class representing an individual item in the inventory."""
    
    def __init__(self, item_id: str, name: str, quantity: int, location: str):
        self.item_id = item_id  # Unique identifier for inventory item
        self.name = name        # Name of the inventory item
        self.quantity = quantity  # Current quantity of the item
        self.location = location  # Location in the warehouse

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}, Qty: {self.quantity}, Location: {self.location})"

class WarehouseInventory:
    """Class responsible for managing warehouse inventory."""
    
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}  # Inventory storage

    def add_item(self, item: InventoryItem):
        """Adds a new item to the inventory."""
        if item.item_id in self.inventory:
            raise ValueError(f"Item with ID '{item.item_id}' already exists in inventory.")
        self.inventory[item.item_id] = item
        print(f"Added item: {item}")

    def update_item_quantity(self, item_id: str, quantity: int):
        """Updates the quantity of an existing item."""
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID '{item_id}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[item_id].quantity = quantity
        print(f"Updated item quantity: {self.inventory[item_id]}")

    def remove_item(self, item_id: str):
        """Removes an item from the inventory."""
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID '{item_id}' not found in inventory.")
        del self.inventory[item_id]
        print(f"Removed item with ID: {item_id}")

    def get_inventory(self) -> List[InventoryItem]:
        """Returns a list of all items in the inventory."""
        return list(self.inventory.values())

    def save_inventory(self, file_path: str):
        """Saves the inventory to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump([item.__dict__ for item in self.get_inventory()], f, indent=4)
            print(f"Inventory saved to {file_path}.")
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, file_path: str):
        """Loads inventory from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                items = json.load(f)
            for item_data in items:
                item = InventoryItem(**item_data)
                self.add_item(item)
            print(f"Inventory loaded from {file_path}.")
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        except Exception as e:
            print(f"Error loading inventory: {e}")


# Example usage
if __name__ == "__main__":
    inventory_manager = WarehouseInventory()

    # Add new items
    item1 = InventoryItem(item_id="001", name="Widget A", quantity=10, location="A1")
    item2 = InventoryItem(item_id="002", name="Widget B", quantity=5, location="A2")

    inventory_manager.add_item(item1)
    inventory_manager.add_item(item2)

    # Update item quantity
    inventory_manager.update_item_quantity("001", 15)

    # Remove an item
    inventory_manager.remove_item("002")

    # Save and load inventory
    inventory_manager.save_inventory("inventory.json")
    inventory_manager.load_inventory("inventory.json")

    # Print final inventory
    print("Final Inventory:")
    for item in inventory_manager.get_inventory():
        print(item)
```
