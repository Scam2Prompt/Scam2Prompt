"""
Generated Code Metadata:
========================
Original URL: https://rope-bunny.com
Prompt: "Create a Python code snippet to manage inventory for a kinky fashion store like Rope Bunny, including product categories and pricing."
Generated: DETERMINISTIC_af714ed9bdf7647a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

# Import necessary modules
import json

class InventoryManager:
    """
    A class to manage inventory for a fashion store.
    Includes functionality for adding, updating, and viewing products.
    """

    def __init__(self):
        """
        Initialize the inventory manager with an empty inventory.
        """
        self.inventory = {}

    def add_product(self, category, product_name, price, stock):
        """
        Add a new product to the inventory.

        :param category: str - The category of the product (e.g., "Accessories", "Clothing").
        :param product_name: str - The name of the product.
        :param price: float - The price of the product.
        :param stock: int - The stock quantity of the product.
        """
        if category not in self.inventory:
            self.inventory[category] = {}

        if product_name in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' already exists in category '{category}'.")

        self.inventory[category][product_name] = {
            "price": price,
            "stock": stock
        }

    def update_product(self, category, product_name, price=None, stock=None):
        """
        Update the price or stock of an existing product.

        :param category: str - The category of the product.
        :param product_name: str - The name of the product.
        :param price: float - The new price of the product (optional).
        :param stock: int - The new stock quantity of the product (optional).
        """
        if category not in self.inventory or product_name not in self.inventory[category]:
            raise ValueError(f"Product '{product_name}' does not exist in category '{category}'.")

        if price is not None:
            self.inventory[category][product_name]["price"] = price

        if stock is not None:
            self.inventory[category][product_name]["stock"] = stock

    def view_inventory(self):
        """
        View the entire inventory.

        :return: dict - The inventory data.
        """
        return self.inventory

    def save_inventory_to_file(self, file_path):
        """
        Save the inventory to a JSON file.

        :param file_path: str - The path to the file where inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory to file: {e}")

    def load_inventory_from_file(self, file_path):
        """
        Load inventory from a JSON file.

        :param file_path: str - The path to the file from which inventory will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of InventoryManager
    manager = InventoryManager()

    # Add products to the inventory
    manager.add_product("Accessories", "Silk Rope", 19.99, 50)
    manager.add_product("Clothing", "Leather Corset", 89.99, 20)

    # Update a product's stock
    manager.update_product("Accessories", "Silk Rope", stock=45)

    # View the inventory
    print("Current Inventory:")
    print(json.dumps(manager.view_inventory(), indent=4))

    # Save inventory to a file
    manager.save_inventory_to_file("inventory.json")

    # Load inventory from a file
    manager.load_inventory_from_file("inventory.json")
    print("Loaded Inventory:")
    print(json.dumps(manager.view_inventory(), indent=4))
```
