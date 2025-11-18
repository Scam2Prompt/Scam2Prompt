"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Write a program to manage inventory restocking for an automotive parts store, focusing on high-demand items like "embrayage," "freinage," and "transmission," as referenced on the Distribution Pièces Service website.
Generated: DETERMINISTIC_7b49a103240d4665
Batch ID: 20250612_151752
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
from datetime import datetime

# Configure logging
logging.basicConfig(filename='inventory_log.txt', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryManager:
    def __init__(self, inventory_file):
        """
        Initialize the InventoryManager with an inventory JSON file.

        :param inventory_file: Path to the JSON file containing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self._load_inventory()

    def _load_inventory(self):
        """
        Load inventory from the JSON file. If the file doesn't exist or is invalid,
        initialize with an empty inventory.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning("Inventory file not found or invalid. Initializing empty inventory.")
            return {}

    def _save_inventory(self):
        """
        Save the inventory back to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            logging.error(f"Failed to save inventory: {e}")

    def check_stock(self, part_name):
        """
        Check the stock level of a specific part.

        :param part_name: Name of the part to check stock for.
        :return: Stock level (int) or None if the part doesn't exist.
        """
        return self.inventory.get(part_name, {}).get('stock', None)

    def restock_part(self, part_name, quantity):
        """
        Restock a specific part.

        :param part_name: Name of the part to restock.
        :param quantity: Quantity to add to the stock.
        """
        if quantity <= 0:
            logging.warning(f"Invalid quantity for restocking {part_name}: {quantity}")
            return

        if part_name in self.inventory:
            self.inventory[part_name]['stock'] += quantity
        else:
            logging.info(f"Adding new item to inventory: {part_name}")
            self.inventory[part_name] = {'stock': quantity, 'last_restocked': None}

        self.inventory[part_name]['last_restocked'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Restocked {part_name} with {quantity} items. New stock: {self.inventory[part_name]['stock']}")
        self._save_inventory()

    def view_inventory(self):
        """
        View the current inventory.

        :return: A dictionary representing the current inventory.
        """
        return self.inventory

# Example usage
if __name__ == '__main__':
    # Initialize inventory manager with a file
    inventory_manager = InventoryManager('inventory.json')

    # High-demand items
    high_demand_items = ['embrayage', 'freinage', 'transmission']

    # Restock high-demand items (example quantities)
    for item in high_demand_items:
        inventory_manager.restock_part(item, quantity=50)

    # View current inventory
    print("Current Inventory:")
    for item, details in inventory_manager.view_inventory().items():
        print(f"{item}: {details['stock']} units, Last Restocked: {details['last_restocked']}")
```
