"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Generate a script for managing warehouse inventory tailored to Fealty Worldwide's warehousing services, including storage, distribution, and pre-positioning of products.
Generated: DETERMINISTIC_331d8dc8b3161d9e
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryItem:
    """Class to represent an item in the warehouse inventory."""
    
    def __init__(self, item_id: str, name: str, quantity: int):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(item_id={self.item_id}, name={self.name}, quantity={self.quantity})"

class WarehouseInventory:
    """Class to manage warehouse inventory operations."""
    
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}

    def add_item(self, item_id: str, name: str, quantity: int) -> None:
        """Add a new item to the inventory."""
        if item_id in self.inventory:
            logging.warning(f"Item with ID {item_id} already exists. Updating quantity.")
            self.inventory[item_id].quantity += quantity
        else:
            self.inventory[item_id] = InventoryItem(item_id, name, quantity)
        logging.info(f"Added/Updated item: {self.inventory[item_id]}")

    def remove_item(self, item_id: str, quantity: int) -> None:
        """Remove a specified quantity of an item from the inventory."""
        if item_id not in self.inventory:
            logging.error(f"Item with ID {item_id} not found in inventory.")
            raise ValueError(f"Item with ID {item_id} not found in inventory.")
        
        if self.inventory[item_id].quantity < quantity:
            logging.error(f"Insufficient quantity for item ID {item_id}. Available: {self.inventory[item_id].quantity}, Requested: {quantity}")
            raise ValueError(f"Insufficient quantity for item ID {item_id}.")
        
        self.inventory[item_id].quantity -= quantity
        logging.info(f"Removed {quantity} of item ID {item_id}. Remaining quantity: {self.inventory[item_id].quantity}")

    def get_inventory(self) -> List[InventoryItem]:
        """Return a list of all items in the inventory."""
        return list(self.inventory.values())

    def save_inventory(self, file_path: str) -> None:
        """Save the current inventory to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump({item_id: item.__dict__ for item_id, item in self.inventory.items()}, file)
            logging.info(f"Inventory saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to save inventory: {e}")
            raise

    def load_inventory(self, file_path: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                items = json.load(file)
                for item_id, item_data in items.items():
                    self.inventory[item_id] = InventoryItem(**item_data)
            logging.info(f"Inventory loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load inventory: {e}")
            raise

# Example usage
if __name__ == "__main__":
    inventory_manager = WarehouseInventory()
    
    # Adding items to the inventory
    inventory_manager.add_item("001", "Widget A", 100)
    inventory_manager.add_item("002", "Widget B", 200)
    
    # Removing items from the inventory
    try:
        inventory_manager.remove_item("001", 50)
    except ValueError as e:
        logging.error(e)
    
    # Saving inventory to a file
    inventory_manager.save_inventory("inventory.json")
    
    # Loading inventory from a file
    try:
        inventory_manager.load_inventory("inventory.json")
    except ValueError as e:
        logging.error(e)
```
