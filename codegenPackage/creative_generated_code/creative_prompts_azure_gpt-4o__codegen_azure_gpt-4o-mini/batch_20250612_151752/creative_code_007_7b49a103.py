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
from typing import List, Dict

class InventoryManager:
    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with a path to the inventory file.
        
        :param inventory_file: Path to the JSON inventory file.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, int]:
        """
        Loads inventory from the JSON file.
        
        :return: A dictionary representing the inventory with item names as keys and quantities as values.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.inventory_file} was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: The inventory file is not a valid JSON.")
            return {}
        
    def save_inventory(self) -> None:
        """
        Saves the current inventory to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError:
            print(f"Error: Unable to write to the file {self.inventory_file}.")
        
    def restock_item(self, item: str, quantity: int) -> None:
        """
        Restocks an item by a specified quantity.
        
        :param item: The name of the item to restock.
        :param quantity: The quantity to add to the inventory.
        """
        if quantity < 0:
            print("Error: Quantity must be a non-negative number.")
            return
        
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        
        self.save_inventory()
        print(f"Restocked {quantity} units of {item}. Current stock: {self.inventory[item]}")

    def check_stock(self, item: str) -> int:
        """
        Checks the stock level of a specified item.
        
        :param item: The name of the item to check.
        :return: The current stock level of the item.
        """
        return self.inventory.get(item, 0)

def main():
    # Initialize the inventory manager
    inventory_manager = InventoryManager('inventory.json')

    # Define high-demand items
    high_demand_items = ["embrayage", "freinage", "transmission"]

    # Example usage
    for item in high_demand_items:
        stock_level = inventory_manager.check_stock(item)
        print(f"{item.capitalize()} stock level: {stock_level}")
        
        # Example: Restock each high-demand item
        inventory_manager.restock_item(item, 10)  # Restocking with 10 units

if __name__ == "__main__":
    main()
```
