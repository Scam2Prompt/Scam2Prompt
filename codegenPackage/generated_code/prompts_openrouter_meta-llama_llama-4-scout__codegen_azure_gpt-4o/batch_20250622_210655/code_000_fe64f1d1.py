"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Write a Python code to manage an e-commerce inventory for inhaler accessories, including items like trachea for ultrasonic inhalers and nebulizer kits.
Generated: DETERMINISTIC_fe64f1d1ff83cc30
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class InventoryManager:
    """
    A class to manage e-commerce inventory for inhaler accessories.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        """
        Adds a new item to the inventory or updates an existing item.

        Args:
            item_name (str): Name of the item.
            quantity (int): Quantity of the item.
            price (float): Price of the item.

        Raises:
            ValueError: If quantity or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

        if item_name in self.inventory:
            # Update existing item
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['price'] = price
        else:
            # Add new item
            self.inventory[item_name] = {'quantity': quantity, 'price': price}

    def remove_item(self, item_name, quantity):
        """
        Removes a specified quantity of an item from the inventory.

        Args:
            item_name (str): Name of the item.
            quantity (int): Quantity to remove.

        Raises:
            ValueError: If quantity is negative or exceeds available stock.
            KeyError: If the item does not exist in the inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        if item_name not in self.inventory:
            raise KeyError(f"Item '{item_name}' not found in inventory.")

        if self.inventory[item_name]['quantity'] < quantity:
            raise ValueError("Insufficient stock to remove the requested quantity.")

        self.inventory[item_name]['quantity'] -= quantity

        # Remove item completely if quantity becomes zero
        if self.inventory[item_name]['quantity'] == 0:
            del self.inventory[item_name]

    def get_inventory(self):
        """
        Returns the current inventory.

        Returns:
            dict: A dictionary representing the inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

        Args:
            file_path (str): Path to the file where inventory will be saved.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.

        Args:
            file_path (str): Path to the file from which inventory will be loaded.

        Raises:
            IOError: If there is an issue reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add items to inventory
    manager.add_item("Trachea for Ultrasonic Inhaler", 50, 19.99)
    manager.add_item("Nebulizer Kit", 30, 24.99)

    # Remove items from inventory
    try:
        manager.remove_item("Trachea for Ultrasonic Inhaler", 10)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

    # Display current inventory
    print("Current Inventory:")
    print(manager.get_inventory())

    # Save inventory to file
    try:
        manager.save_inventory_to_file("inventory.json")
    except IOError as e:
        print(f"Error: {e}")

    # Load inventory from file
    try:
        manager.load_inventory_from_file("inventory.json")
        print("Inventory loaded from file:")
        print(manager.get_inventory())
    except (IOError, ValueError) as e:
        print(f"Error: {e}")
```
