"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Write a Python code snippet to manage an e-commerce inventory system for a beauty store like Eclat, including products such as nail polish, nail art supplies, and eyelash extensions.
Generated: DETERMINISTIC_e362bc32664413e7
Batch ID: 20250622_205955
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
    A class to manage the inventory of an e-commerce beauty store.
    """

    def __init__(self):
        """
        Initializes the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, product_name, category, quantity, price):
        """
        Adds a new product to the inventory or updates an existing product.

        Args:
            product_name (str): Name of the product.
            category (str): Category of the product (e.g., nail polish, nail art supplies, eyelash extensions).
            quantity (int): Quantity of the product in stock.
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
            self.inventory[product_name] = {
                'category': category,
                'quantity': quantity,
                'price': price
            }

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
            KeyError: If the product does not exist in the inventory.
            ValueError: If quantity is negative.
        """
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        self.inventory[product_name]['quantity'] = quantity

    def get_product_info(self, product_name):
        """
        Retrieves information about a product.

        Args:
            product_name (str): Name of the product.

        Returns:
            dict: Information about the product (category, quantity, price).

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        return self.inventory[product_name]

    def list_products(self):
        """
        Lists all products in the inventory.

        Returns:
            dict: The entire inventory.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Saves the inventory to a JSON file.

        Args:
            file_path (str): Path to the file where inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Loads the inventory from a JSON file.

        Args:
            file_path (str): Path to the file from which inventory will be loaded.

        Raises:
            IOError: If there is an error reading the file.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except IOError as e:
            print(f"Error loading inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product("Nail Polish - Red", "Nail Polish", 50, 9.99)
    manager.add_product("Nail Art Stickers", "Nail Art Supplies", 100, 4.99)
    manager.add_product("Eyelash Extensions - Natural", "Eyelash Extensions", 30, 19.99)

    # Update quantity
    manager.update_quantity("Nail Polish - Red", 60)

    # Get product info
    print(manager.get_product_info("Nail Polish - Red"))

    # List all products
    print(manager.list_products())

    # Save inventory to file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from file
    manager.load_inventory_from_file("inventory.json")
    print(manager.list_products())
```
