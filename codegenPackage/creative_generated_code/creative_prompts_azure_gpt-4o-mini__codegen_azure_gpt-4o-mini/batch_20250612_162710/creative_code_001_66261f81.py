"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frontiersistem.ro
Prompt: Write a Python script that utilizes a library for managing inventory and import data, similar to the solutions provided by FRONTIER SISTEM.
Generated: DETERMINISTIC_66261f8185decc3e
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryManager:
    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with the specified inventory file.

        :param inventory_file: Path to the JSON file where inventory data is stored.
        """
        self.inventory_file = inventory_file
        self.inventory_data = self.load_inventory()

    def load_inventory(self) -> Dict[str, Any]:
        """
        Loads inventory data from the specified JSON file.

        :return: A dictionary containing the inventory data.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                data = json.load(file)
                logging.info("Inventory loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("Inventory file not found. Starting with an empty inventory.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON. Returning empty inventory.")
            return {}
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}. Returning empty inventory.")
            return {}

    def save_inventory(self) -> None:
        """
        Saves the current inventory data back to the specified JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory_data, file, indent=4)
                logging.info("Inventory saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save inventory: {e}")

    def add_item(self, item_name: str, quantity: int) -> None:
        """
        Adds a new item to the inventory or updates the quantity if it already exists.

        :param item_name: The name of the item to add to inventory.
        :param quantity: The number of items to add.
        """
        if quantity < 0:
            logging.error("Quantity must be non-negative.")
            return
        
        if item_name in self.inventory_data:
            self.inventory_data[item_name] += quantity
            logging.info(f"Updated {item_name} quantity to {self.inventory_data[item_name]}.")
        else:
            self.inventory_data[item_name] = quantity
            logging.info(f"Added new item {item_name} with quantity {quantity}.")
        
        self.save_inventory()

    def remove_item(self, item_name: str, quantity: int) -> None:
        """
        Removes a specified quantity of an item from the inventory.

        :param item_name: The name of the item to remove from inventory.
        :param quantity: The number of items to remove.
        """
        if item_name not in self.inventory_data:
            logging.warning(f"Item {item_name} not found in inventory.")
            return
        
        if quantity < 0:
            logging.error("Quantity must be non-negative.")
            return
        
        if self.inventory_data[item_name] < quantity:
            logging.error(f"Insufficient quantity of {item_name} to remove. Current quantity: {self.inventory_data[item_name]}.")
            return
        
        self.inventory_data[item_name] -= quantity
        if self.inventory_data[item_name] == 0:
            del self.inventory_data[item_name]
            logging.info(f"Removed item {item_name} from inventory since quantity is now zero.")
        else:
            logging.info(f"Reduced {item_name} quantity to {self.inventory_data[item_name]}.")
        
        self.save_inventory()

    def get_inventory(self) -> Dict[str, int]:
        """
        Returns the current inventory data.

        :return: A dictionary with item names as keys and their quantities as values.
        """
        return self.inventory_data

if __name__ == "__main__":
    # Example usage of the InventoryManager
    inventory_manager = InventoryManager('inventory.json')
    
    # Adding items to inventory
    inventory_manager.add_item('Widget', 10)
    inventory_manager.add_item('Gadget', 5)

    # Removing items from inventory
    inventory_manager.remove_item('Widget', 3)

    # Displaying current inventory
    current_inventory = inventory_manager.get_inventory()
    logging.info(f"Current inventory: {current_inventory}")
```
