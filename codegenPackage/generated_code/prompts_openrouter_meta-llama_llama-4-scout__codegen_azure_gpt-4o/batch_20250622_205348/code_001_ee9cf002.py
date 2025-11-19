"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: "Write a Python code snippet to manage inventory for a metal distribution company like Meta+, including products such as stainless steel, aluminum, and copper."
Generated: DETERMINISTIC_ee9cf0023989e79d
Batch ID: 20250622_205348
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
    A class to manage inventory for a metal distribution company.
    Handles products such as stainless steel, aluminum, and copper.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, quantity):
        """
        Adds a product to the inventory or updates its quantity.

        Args:
            product_name (str): Name of the product (e.g., 'stainless steel').
            quantity (int): Quantity to add to the inventory.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity

    def remove_product(self, product_name, quantity):
        """
        Removes a specified quantity of a product from the inventory.

        Args:
            product_name (str): Name of the product to remove.
            quantity (int): Quantity to remove from the inventory.

        Raises:
            ValueError: If quantity is negative or exceeds available stock.
            KeyError: If the product does not exist in the inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        
        if self.inventory[product_name] < quantity:
            raise ValueError(f"Insufficient stock of '{product_name}' to remove {quantity}.")
        
        self.inventory[product_name] -= quantity
        
        # Remove the product from inventory if quantity becomes zero
        if self.inventory[product_name] == 0:
            del self.inventory[product_name]

    def get_inventory(self):
        """
        Returns the current inventory.

        Returns:
            dict: A dictionary containing product names and their quantities.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the current inventory to a JSON file.

        Args:
            file_path (str): Path to the file where inventory will be saved.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads inventory from a JSON file.

        Args:
            file_path (str): Path to the file from which inventory will be loaded.

        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            raise IOError(f"Failed to load inventory from file: {e}")
        except ValueError as e:
            raise ValueError(f"Invalid data in inventory file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products to inventory
    manager.add_product("stainless steel", 100)
    manager.add_product("aluminum", 50)
    manager.add_product("copper", 75)

    # Remove products from inventory
    try:
        manager.remove_product("aluminum", 20)
    except Exception as e:
        print(f"Error: {e}")

    # Display current inventory
    print("Current Inventory:", manager.get_inventory())

    # Save inventory to file
    try:
        manager.save_inventory_to_file("inventory.json")
    except Exception as e:
        print(f"Error: {e}")

    # Load inventory from file
    try:
        manager.load_inventory_from_file("inventory.json")
        print("Loaded Inventory:", manager.get_inventory())
    except Exception as e:
        print(f"Error: {e}")
```
