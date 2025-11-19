"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Write a Python code snippet to manage an e-commerce inventory of mobile phone accessories, including products like LDNIO cables and SODO headphones.
Generated: DETERMINISTIC_b391393cc004203d
Batch ID: 20250622_205236
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
    A class to manage an e-commerce inventory of mobile phone accessories.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, quantity, price):
        """
        Adds a product to the inventory or updates an existing product.

        Args:
            product_name (str): Name of the product.
            quantity (int): Quantity of the product.
            price (float): Price of the product.

        Raises:
            ValueError: If quantity or price is negative.
        """
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be non-negative.")

        if product_name in self.inventory:
            # Update existing product
            self.inventory[product_name]['quantity'] += quantity
            self.inventory[product_name]['price'] = price
        else:
            # Add new product
            self.inventory[product_name] = {'quantity': quantity, 'price': price}

    def remove_product(self, product_name):
        """
        Removes a product from the inventory.

        Args:
            product_name (str): Name of the product to remove.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        del self.inventory[product_name]

    def update_quantity(self, product_name, quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_name (str): Name of the product.
            quantity (int): New quantity of the product.

        Raises:
            ValueError: If quantity is negative.
            KeyError: If the product does not exist in the inventory.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        self.inventory[product_name]['quantity'] = quantity

    def get_inventory(self):
        """
        Returns the current inventory.

        Returns:
            dict: The inventory dictionary.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

        Args:
            file_path (str): Path to the file where inventory will be saved.

        Raises:
            IOError: If there is an error writing to the file.
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
            IOError: If there is an error reading the file.
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

    # Add products
    manager.add_product("LDNIO Cable", 50, 5.99)
    manager.add_product("SODO Headphones", 20, 29.99)

    # Update quantity
    manager.update_quantity("LDNIO Cable", 60)

    # Remove a product
    try:
        manager.remove_product("Nonexistent Product")
    except KeyError as e:
        print(e)

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")

    # Print current inventory
    print(manager.get_inventory())
```
