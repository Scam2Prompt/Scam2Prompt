"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Write a Python function that utilizes the Tấn Hưng Việt Nam library to manage agricultural product inventory, including items like thuốc trừ sâu and phân bón lá.
Generated: DETERMINISTIC_148dbcd0cbed0829
Batch ID: 20250612_160804
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryItem:
    """
    Class to represent an agricultural product in inventory.
    """

    def __init__(self, name, category, quantity):
        """
        Initialize a new inventory item.

        :param name: Name of the agricultural product.
        :param category: Category of the product (e.g., 'thuốc trừ sâu', 'phân bón lá').
        :param quantity: Quantity of the product in inventory.
        """
        self.name = name
        self.category = category
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the inventory item."""
        return f"{self.name} ({self.category}): {self.quantity} units"

class InventoryManager:
    """
    Class to manage inventory of agricultural products.
    """

    def __init__(self):
        """Initialize the inventory manager with an empty inventory."""
        self.inventory = {}

    def add_item(self, item: InventoryItem):
        """
        Add an item to the inventory.

        :param item: InventoryItem to be added.
        """
        if item.name in self.inventory:
            logging.warning(f"Item '{item.name}' already exists. Updating quantity.")
            self.inventory[item.name].quantity += item.quantity
        else:
            self.inventory[item.name] = item
            logging.info(f"Added '{item.name}' to inventory.")

    def remove_item(self, name, quantity):
        """
        Remove a specified quantity of an item from the inventory.

        :param name: Name of the item to remove.
        :param quantity: Quantity to remove.
        """
        if name not in self.inventory:
            logging.error(f"Item '{name}' not found in inventory.")
            raise ValueError(f"Item '{name}' not found in inventory.")

        if self.inventory[name].quantity < quantity:
            logging.error(f"Insufficient quantity of '{name}' to remove.")
            raise ValueError(f"Insufficient quantity of '{name}' to remove.")

        self.inventory[name].quantity -= quantity
        logging.info(f"Removed {quantity} of '{name}' from inventory.")

        if self.inventory[name].quantity == 0:
            del self.inventory[name]
            logging.info(f"Item '{name}' removed from inventory as quantity is zero.")

    def get_inventory(self):
        """
        Get a list of all inventory items.

        :return: List of InventoryItem objects.
        """
        return list(self.inventory.values())

    def save_inventory(self, filename='inventory.json'):
        """
        Save the inventory to a JSON file.

        :param filename: Name of the file to save inventory.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({item.name: item.__dict__ for item in self.inventory.values()}, file)
            logging.info(f"Inventory saved to '{filename}'.")
        except IOError as e:
            logging.error(f"Error saving inventory to '{filename}': {e}")

    def load_inventory(self, filename='inventory.json'):
        """
        Load inventory from a JSON file.

        :param filename: Name of the file to load inventory from.
        """
        try:
            with open(filename, 'r') as file:
                items = json.load(file)
                for item_data in items.values():
                    item = InventoryItem(item_data['name'], item_data['category'], item_data['quantity'])
                    self.add_item(item)
            logging.info(f"Inventory loaded from '{filename}'.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading inventory from '{filename}': {e}")

# Example usage:
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    
    # Load existing inventory
    inventory_manager.load_inventory()

    # Add items to inventory
    inventory_manager.add_item(InventoryItem("Thuốc trừ sâu A", "thuốc trừ sâu", 50))
    inventory_manager.add_item(InventoryItem("Phân bón lá B", "phân bón lá", 30))

    # Remove some items from inventory
    try:
        inventory_manager.remove_item("Thuốc trừ sâu A", 10)
    except ValueError as e:
        logging.error(e)

    # Save current inventory
    inventory_manager.save_inventory()
```
