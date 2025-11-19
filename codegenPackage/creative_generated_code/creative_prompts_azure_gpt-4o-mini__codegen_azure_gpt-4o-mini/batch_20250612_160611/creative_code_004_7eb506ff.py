"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: What are the best practices for using Cedar International's electrical division products in a drilling operation? Provide a code example for inventory management.
Generated: DETERMINISTIC_7eb506ffd10c01cc
Batch ID: 20250612_160611
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


class InventoryItem:
    """Class to represent an inventory item for Cedar International's electrical division products."""
    
    def __init__(self, name: str, quantity: int, price_per_unit: float):
        """
        Initialize an InventoryItem.

        :param name: The name of the product.
        :param quantity: The quantity available in inventory.
        :param price_per_unit: The price per unit of the product.
        """
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def update_quantity(self, amount: int):
        """
        Update the quantity of the item in inventory.

        :param amount: The amount to change the quantity by (can be positive or negative).
        """
        if self.quantity + amount < 0:
            logging.error("Cannot update quantity, insufficient stock.")
            raise ValueError("Insufficient stock.")
        self.quantity += amount

    def total_value(self) -> float:
        """Calculate the total value of the inventory item."""
        return self.quantity * self.price_per_unit


class InventoryManager:
    """Class to manage the inventory of electrical division products."""
    
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}

    def add_item(self, name: str, quantity: int, price_per_unit: float):
        """
        Add a new item to the inventory.

        :param name: The name of the product.
        :param quantity: The initial quantity of the product.
        :param price_per_unit: The price per unit of the product.
        """
        if name in self.inventory:
            logging.warning(f"Item '{name}' already exists. Updating quantity.")
            self.inventory[name].update_quantity(quantity)
        else:
            self.inventory[name] = InventoryItem(name, quantity, price_per_unit)
            logging.info(f"Added item '{name}' to inventory with quantity {quantity}.")

    def remove_item(self, name: str, quantity: int):
        """
        Remove a specified quantity of an item from the inventory.

        :param name: The name of the item to remove.
        :param quantity: The quantity to remove.
        """
        if name in self.inventory:
            self.inventory[name].update_quantity(-quantity)
            logging.info(f"Removed {quantity} of item '{name}' from inventory.")
        else:
            logging.error(f"Item '{name}' not found in inventory.")
            raise KeyError(f"Item '{name}' not found in inventory.")

    def get_inventory_report(self) -> List[Dict[str, Any]]:
        """
        Generate a report of the current inventory.

        :return: A list of dictionaries representing the inventory items.
        """
        report = []
        for item in self.inventory.values():
            report.append({
                "name": item.name,
                "quantity": item.quantity,
                "price_per_unit": item.price_per_unit,
                "total_value": item.total_value()
            })
        return report

    def save_inventory_to_file(self, filename: str):
        """
        Save the inventory to a JSON file.

        :param filename: The name of the file to save the inventory to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory_report(), file, indent=4)
            logging.info(f"Inventory saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save inventory to file: {e}")
            raise


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    inventory_manager = InventoryManager()
    try:
        inventory_manager.add_item("Electrical Wire", 100, 0.50)
        inventory_manager.add_item("Circuit Breaker", 50, 15.00)
        inventory_manager.remove_item("Electrical Wire", 10)
        
        report = inventory_manager.get_inventory_report()
        print(json.dumps(report, indent=4))

        inventory_manager.save_inventory_to_file("inventory_report.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
