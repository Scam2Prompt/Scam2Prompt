"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Create a script to manage inventory for office furniture, including desks, chairs, filing cabinets, and sofas, based on the product categories listed on Sanuri Supplies' website.
Generated: DETERMINISTIC_933cd8aa3716ce9c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py
# A script to manage inventory for office furniture items: desks, chairs, filing cabinets, sofas.

import json

class InventoryManager:
    """
    A class to manage inventory for office furniture, including desks, chairs, filing cabinets, and sofas.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        The inventory is stored as a dictionary with product categories as keys.
        """
        self.inventory = {
            "desks": [],
            "chairs": [],
            "filing_cabinets": [],
            "sofas": [],
        }

    def add_item(self, category, name, quantity, price):
        """
        Adds a new item to the inventory under the specified category.

        Args:
            category (str): The category the item belongs to (e.g., "desks", "chairs").
            name (str): The name of the item.
            quantity (int): The quantity of the item in stock.
            price (float): The price of the item.

        Raises:
            ValueError: If the category is invalid or quantity/price is negative.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Valid categories are: desks, chairs, filing_cabinets, sofas.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if price < 0:
            raise ValueError("Price cannot be negative.")

        item = {
            "name": name,
            "quantity": quantity,
            "price": price,
        }
        self.inventory[category].append(item)

    def remove_item(self, category, name):
        """
        Removes an item from the inventory.

        Args:
            category (str): The category the item belongs to.
            name (str): The name of the item to remove.

        Raises:
            ValueError: If the category is invalid or the item is not found.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Valid categories are: desks, chairs, filing_cabinets, sofas.")

        for item in self.inventory[category]:
            if item["name"] == name:
                self.inventory[category].remove(item)
                return
        raise ValueError(f"Item '{name}' not found in category '{category}'.")

    def update_item(self, category, name, quantity=None, price=None):
        """
        Updates the quantity and/or price of an item in the inventory.

        Args:
            category (str): The category the item belongs to.
            name (str): The name of the item to update.
            quantity (int, optional): The new quantity of the item. Defaults to None.
            price (float, optional): The new price of the item. Defaults to None.

        Raises:
            ValueError: If the category is invalid or the item is not found.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Valid categories are: desks, chairs, filing_cabinets, sofas.")

        for item in self.inventory[category]:
            if item["name"] == name:
                if quantity is not None:
                    if quantity < 0:
                        raise ValueError("Quantity cannot be negative.")
                    item["quantity"] = quantity
                if price is not None:
                    if price < 0:
                        raise ValueError("Price cannot be negative.")
                    item["price"] = price
                return
        raise ValueError(f"Item '{name}' not found in category '{category}'.")

    def view_inventory(self):
        """
        Returns the current state of the inventory.

        Returns:
            dict: A dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the current inventory to a file in JSON format.

        Args:
            file_path (str): The path to the file where the inventory will be saved.

        Raises:
            IOError: If there is an error while writing to the file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads inventory from a file in JSON format.

        Args:
            file_path (str): The path to the file to load inventory from.

        Raises:
            IOError: If there is an error while reading the file.
            JSONDecodeError: If the file does not contain valid JSON.
        """
        try:
            with open(file_path, "r") as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error reading inventory file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file: {e}")


# Example usage (commented to avoid execution when importing the module):
# if __name__ == "__main__":
#     manager = InventoryManager()
#     manager.add_item("desks", "Modern Desk", 10, 299.99)
#     manager.add_item("chairs", "Ergonomic Chair", 15, 149.99)
#     print(manager.view_inventory())
#     manager.save_inventory_to_file("inventory.json")
#     manager.load_inventory_from_file("inventory.json")
#     print(manager.view_inventory())
```
