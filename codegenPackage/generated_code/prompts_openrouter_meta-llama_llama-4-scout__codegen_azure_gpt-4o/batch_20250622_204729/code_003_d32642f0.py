"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: "Create a code snippet to manage a printing press's inventory, including items like paper, ink, and printing materials, inspired by Ram Digi's infrastructure and services."
Generated: DETERMINISTIC_d32642f039bf9d47
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# printing_press_inventory.py

import json

class InventoryItem:
    """
    Represents an item in the printing press inventory.
    """
    def __init__(self, name, category, quantity, unit_price):
        """
        Initialize an inventory item.

        :param name: Name of the item
        :param category: Category of the item (e.g., paper, ink, etc.)
        :param quantity: Quantity of the item in stock
        :param unit_price: Price per unit of the item
        """
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price

    def update_quantity(self, amount):
        """
        Update the quantity of the item.

        :param amount: Amount to add (positive) or subtract (negative)
        """
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.quantity += amount

    def calculate_total_value(self):
        """
        Calculate the total value of the item in stock.

        :return: Total value of the item
        """
        return self.quantity * self.unit_price

    def to_dict(self):
        """
        Convert the item to a dictionary for serialization.

        :return: Dictionary representation of the item
        """
        return {
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "unit_price": self.unit_price
        }


class PrintingPressInventory:
    """
    Manages the inventory of a printing press.
    """
    def __init__(self):
        """
        Initialize the inventory.
        """
        self.items = {}

    def add_item(self, item):
        """
        Add a new item to the inventory.

        :param item: InventoryItem object
        """
        if item.name in self.items:
            raise ValueError(f"Item '{item.name}' already exists in the inventory.")
        self.items[item.name] = item

    def remove_item(self, item_name):
        """
        Remove an item from the inventory.

        :param item_name: Name of the item to remove
        """
        if item_name not in self.items:
            raise ValueError(f"Item '{item_name}' does not exist in the inventory.")
        del self.items[item_name]

    def update_item_quantity(self, item_name, amount):
        """
        Update the quantity of an item in the inventory.

        :param item_name: Name of the item
        :param amount: Amount to add (positive) or subtract (negative)
        """
        if item_name not in self.items:
            raise ValueError(f"Item '{item_name}' does not exist in the inventory.")
        self.items[item_name].update_quantity(amount)

    def get_inventory_value(self):
        """
        Calculate the total value of the inventory.

        :return: Total value of the inventory
        """
        return sum(item.calculate_total_value() for item in self.items.values())

    def save_to_file(self, file_path):
        """
        Save the inventory to a file in JSON format.

        :param file_path: Path to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({name: item.to_dict() for name, item in self.items.items()}, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save inventory to file: {e}")

    def load_from_file(self, file_path):
        """
        Load the inventory from a file in JSON format.

        :param file_path: Path to the file
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.items = {name: InventoryItem(**item_data) for name, item_data in data.items()}
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize inventory
        inventory = PrintingPressInventory()

        # Add items
        inventory.add_item(InventoryItem("A4 Paper", "Paper", 500, 0.10))
        inventory.add_item(InventoryItem("Black Ink", "Ink", 100, 15.00))
        inventory.add_item(InventoryItem("Glossy Paper", "Paper", 200, 0.25))

        # Update item quantity
        inventory.update_item_quantity("A4 Paper", -50)

        # Calculate total inventory value
        print(f"Total inventory value: ${inventory.get_inventory_value():.2f}")

        # Save inventory to file
        inventory.save_to_file("inventory.json")

        # Load inventory from file
        inventory.load_from_file("inventory.json")
        print("Inventory loaded successfully.")

    except Exception as e:
        print(f"Error: {e}")
```
