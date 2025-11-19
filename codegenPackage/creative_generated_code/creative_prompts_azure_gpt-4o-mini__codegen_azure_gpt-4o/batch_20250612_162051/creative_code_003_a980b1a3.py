"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gazibilisim.com.tr
Prompt: Provide an example of how to implement Logo WMS for real-time inventory tracking and management in a warehouse setting.
Generated: DETERMINISTIC_a980b1a3db209374
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Logo WMS - Real-Time Inventory Tracking and Management System
This example demonstrates a simplified implementation for tracking inventory in a warehouse
using Python. It includes functionality for adding, updating, and querying inventory.
"""

import logging
from datetime import datetime

# Configure logging for error handling and monitoring
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)

class WarehouseInventory:
    """
    A class to represent and manage warehouse inventory.
    """

    def __init__(self):
        # Initialize the inventory as an empty dictionary.
        # Each item will be stored as a key-value pair: {item_id: {"name": ..., "quantity": ..., "last_updated": ...}}
        self.inventory = {}

    def add_item(self, item_id, name, quantity):
        """
        Adds a new item to the inventory.

        :param item_id: Unique identifier for the item.
        :param name: Name of the item.
        :param quantity: Initial quantity of the item.
        """
        if item_id in self.inventory:
            logging.warning(f"Item with ID {item_id} already exists. Use update_item() to modify it.")
        else:
            self.inventory[item_id] = {
                "name": name,
                "quantity": quantity,
                "last_updated": datetime.now()
            }
            logging.info(f"Added item '{name}' with ID {item_id} and quantity {quantity}.")

    def update_item(self, item_id, quantity_change):
        """
        Updates the quantity of an existing item in the inventory.

        :param item_id: Unique identifier for the item.
        :param quantity_change: Change in quantity (positive or negative).
        """
        if item_id not in self.inventory:
            logging.error(f"Item with ID {item_id} does not exist.")
        else:
            self.inventory[item_id]["quantity"] += quantity_change
            self.inventory[item_id]["last_updated"] = datetime.now()

            # Ensure quantity does not go below zero
            if self.inventory[item_id]["quantity"] < 0:
                self.inventory[item_id]["quantity"] = 0
                logging.warning(f"Quantity for item ID {item_id} cannot go below 0.")
            
            logging.info(f"Updated item ID {item_id}. New quantity: {self.inventory[item_id]['quantity']}.")

    def query_item(self, item_id):
        """
        Retrieves information about a specific item.

        :param item_id: Unique identifier for the item.
        :return: A dictionary containing item details or None if the item does not exist.
        """
        if item_id not in self.inventory:
            logging.error(f"Item with ID {item_id} does not exist.")
            return None
        else:
            item_info = self.inventory[item_id]
            logging.info(f"Queried item ID {item_id}: {item_info}.")
            return item_info

    def list_inventory(self):
        """
        Lists all items in the inventory.

        :return: A dictionary representing the entire inventory.
        """
        if not self.inventory:
            logging.warning("Inventory is currently empty.")
        else:
            logging.info("Listing all items in the inventory.")
        return self.inventory


# Example usage of WarehouseInventory
if __name__ == "__main__":
    # Create an instance of the WarehouseInventory
    inventory_manager = WarehouseInventory()

    # Add items to the inventory
    inventory_manager.add_item("item101", "Widget A", 50)
    inventory_manager.add_item("item102", "Widget B", 30)

    # Update item quantities
    inventory_manager.update_item("item101", -10)  # Decrease quantity by 10
    inventory_manager.update_item("item102", 20)  # Increase quantity by 20

    # Query a specific item
    item_info = inventory_manager.query_item("item101")
    print("Queried Item:", item_info)

    # List all items in the inventory
    all_items = inventory_manager.list_inventory()
    print("Current Inventory:", all_items)
```
