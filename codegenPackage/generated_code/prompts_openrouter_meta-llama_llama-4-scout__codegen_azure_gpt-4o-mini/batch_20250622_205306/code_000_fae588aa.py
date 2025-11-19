"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Write a Python script to manage inventory of packaging materials for exporting blueberries and grapes, considering variables such as product type and destination country."
Generated: DETERMINISTIC_fae588aa94cd6dbc
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

class InventoryManager:
    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with a specified inventory file.
        
        :param inventory_file: Path to the JSON file that stores inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, Any]:
        """
        Loads inventory data from a JSON file.
        
        :return: A dictionary containing the inventory data.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Inventory file '{self.inventory_file}' not found. Starting with an empty inventory.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the inventory file '{self.inventory_file}'. Starting with an empty inventory.")
            return {}

    def save_inventory(self) -> None:
        """
        Saves the current inventory data to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to '{self.inventory_file}': {e}")

    def add_product(self, product_type: str, quantity: int, destination_country: str) -> None:
        """
        Adds a product to the inventory.
        
        :param product_type: Type of the product (e.g., 'blueberries', 'grapes').
        :param quantity: Quantity of the product to add.
        :param destination_country: The destination country for the product.
        """
        if product_type not in self.inventory:
            self.inventory[product_type] = {}
        
        if destination_country not in self.inventory[product_type]:
            self.inventory[product_type][destination_country] = 0
        
        self.inventory[product_type][destination_country] += quantity
        self.save_inventory()
        print(f"Added {quantity} of {product_type} for {destination_country}. Total: {self.inventory[product_type][destination_country]}")

    def remove_product(self, product_type: str, quantity: int, destination_country: str) -> None:
        """
        Removes a product from the inventory.
        
        :param product_type: Type of the product (e.g., 'blueberries', 'grapes').
        :param quantity: Quantity of the product to remove.
        :param destination_country: The destination country for the product.
        """
        try:
            if product_type in self.inventory and destination_country in self.inventory[product_type]:
                if self.inventory[product_type][destination_country] >= quantity:
                    self.inventory[product_type][destination_country] -= quantity
                    self.save_inventory()
                    print(f"Removed {quantity} of {product_type} for {destination_country}. Remaining: {self.inventory[product_type][destination_country]}")
                else:
                    print(f"Cannot remove {quantity} of {product_type} for {destination_country}. Not enough stock.")
            else:
                print(f"No inventory found for {product_type} in {destination_country}.")
        except Exception as e:
            print(f"Error removing product: {e}")

    def get_inventory(self) -> Dict[str, Any]:
        """
        Returns the current inventory.
        
        :return: A dictionary representing the current inventory.
        """
        return self.inventory

if __name__ == "__main__":
    # Example usage
    inventory_manager = InventoryManager('inventory.json')
    
    # Adding products
    inventory_manager.add_product('blueberries', 100, 'USA')
    inventory_manager.add_product('grapes', 50, 'Canada')
    
    # Removing products
    inventory_manager.remove_product('blueberries', 30, 'USA')
    
    # Displaying current inventory
    print("Current Inventory:", inventory_manager.get_inventory())
```
