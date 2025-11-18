"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Create a script to automate the process of managing raw material inventory for high-performance cosmetic production, based on Fabricare Cosméticos' emphasis on advanced technology and rich active ingredients.
Generated: DETERMINISTIC_6317ae913246c583
Batch ID: 20250612_153517
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
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryManager:
    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with the specified inventory file.

        :param inventory_file: Path to the JSON file where inventory data is stored.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, int]:
        """
        Loads inventory data from the JSON file.

        :return: A dictionary with raw material names as keys and their respective quantities as values.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                inventory = json.load(file)
                logging.info("Inventory loaded successfully.")
                return inventory
        except FileNotFoundError:
            logging.warning(f"Inventory file {self.inventory_file} not found. Starting with an empty inventory.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the inventory file. Please check the file format.")
            return {}

    def save_inventory(self):
        """
        Saves the current inventory data to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
                logging.info("Inventory saved successfully.")
        except IOError as e:
            logging.error(f"Error saving inventory to file: {e}")

    def add_material(self, material: str, quantity: int):
        """
        Adds a specified quantity of a raw material to the inventory.

        :param material: The name of the raw material.
        :param quantity: The quantity to add.
        """
        if quantity <= 0:
            logging.error("Quantity must be greater than zero.")
            return

        self.inventory[material] = self.inventory.get(material, 0) + quantity
        logging.info(f"Added {quantity} of {material} to inventory.")
        self.save_inventory()

    def remove_material(self, material: str, quantity: int):
        """
        Removes a specified quantity of a raw material from the inventory.

        :param material: The name of the raw material.
        :param quantity: The quantity to remove.
        """
        if quantity <= 0:
            logging.error("Quantity must be greater than zero.")
            return

        current_quantity = self.inventory.get(material, 0)
        if current_quantity < quantity:
            logging.error(f"Not enough {material} in inventory. Current quantity: {current_quantity}.")
            return

        self.inventory[material] -= quantity
        if self.inventory[material] == 0:
            del self.inventory[material]
            logging.info(f"{material} removed from inventory as quantity is now zero.")
        else:
            logging.info(f"Removed {quantity} of {material} from inventory. Remaining: {self.inventory[material]}.")

        self.save_inventory()

    def get_inventory(self) -> Dict[str, int]:
        """
        Retrieves the current inventory.

        :return: A dictionary of the current inventory.
        """
        return self.inventory

    def list_inventory(self) -> List[str]:
        """
        Lists all raw materials in the inventory.

        :return: A list of raw material names and their quantities.
        """
        inventory_list = [f"{material}: {quantity}" for material, quantity in self.inventory.items()]
        logging.info("Current inventory listed.")
        return inventory_list


if __name__ == "__main__":
    # Example usage
    inventory_manager = InventoryManager('inventory.json')

    # Add materials
    inventory_manager.add_material('Hyaluronic Acid', 50)
    inventory_manager.add_material('Vitamin C', 100)

    # Remove materials
    inventory_manager.remove_material('Hyaluronic Acid', 10)

    # List current inventory
    current_inventory = inventory_manager.list_inventory()
    print("Current Inventory:")
    for item in current_inventory:
        print(item)
```
