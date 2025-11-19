"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Write a Python script to manage inventory for a menuiserie distribution company like Distribution Menuiserie, including classes for products (e.g., Fenêtres, Portes, Volets) and methods for tracking stock levels."
Generated: DETERMINISTIC_5ba35bc78ec29057
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

# Import necessary modules
import sys

class Product:
    """
    A class to represent a product in the inventory.
    Attributes:
        name (str): The name of the product.
        category (str): The category of the product (e.g., Fenêtres, Portes, Volets).
        stock (int): The current stock level of the product.
    """
    def __init__(self, name, category, stock=0):
        """
        Initialize a Product instance.
        :param name: Name of the product.
        :param category: Category of the product.
        :param stock: Initial stock level (default is 0).
        """
        self.name = name
        self.category = category
        self.stock = stock

    def add_stock(self, quantity):
        """
        Add stock to the product.
        :param quantity: The quantity to add.
        """
        if quantity < 0:
            raise ValueError("Quantity to add cannot be negative.")
        self.stock += quantity

    def remove_stock(self, quantity):
        """
        Remove stock from the product.
        :param quantity: The quantity to remove.
        """
        if quantity < 0:
            raise ValueError("Quantity to remove cannot be negative.")
        if quantity > self.stock:
            raise ValueError("Insufficient stock to remove the requested quantity.")
        self.stock -= quantity

    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f"Product(name={self.name}, category={self.category}, stock={self.stock})"


class Inventory:
    """
    A class to manage the inventory of products.
    Attributes:
        products (dict): A dictionary to store products with their names as keys.
    """
    def __init__(self):
        """
        Initialize an Inventory instance.
        """
        self.products = {}

    def add_product(self, product):
        """
        Add a new product to the inventory.
        :param product: An instance of the Product class.
        """
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")
        self.products[product.name] = product

    def remove_product(self, product_name):
        """
        Remove a product from the inventory.
        :param product_name: The name of the product to remove.
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' does not exist in the inventory.")
        del self.products[product_name]

    def update_stock(self, product_name, quantity, operation):
        """
        Update the stock level of a product.
        :param product_name: The name of the product.
        :param quantity: The quantity to add or remove.
        :param operation: The operation to perform ('add' or 'remove').
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' does not exist in the inventory.")
        product = self.products[product_name]
        if operation == 'add':
            product.add_stock(quantity)
        elif operation == 'remove':
            product.remove_stock(quantity)
        else:
            raise ValueError("Invalid operation. Use 'add' or 'remove'.")

    def list_products(self):
        """
        List all products in the inventory.
        """
        if not self.products:
            print("No products in the inventory.")
        for product in self.products.values():
            print(product)

    def get_product(self, product_name):
        """
        Get details of a specific product.
        :param product_name: The name of the product.
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' does not exist in the inventory.")
        return self.products[product_name]


# Example usage
if __name__ == "__main__":
    try:
        # Create an inventory instance
        inventory = Inventory()

        # Add products to the inventory
        inventory.add_product(Product(name="Fenêtre PVC", category="Fenêtres", stock=50))
        inventory.add_product(Product(name="Porte Bois", category="Portes", stock=30))
        inventory.add_product(Product(name="Volet Aluminium", category="Volets", stock=20))

        # List all products
        print("Initial Inventory:")
        inventory.list_products()

        # Update stock levels
        inventory.update_stock("Fenêtre PVC", 10, "add")
        inventory.update_stock("Porte Bois", 5, "remove")

        # List all products after stock update
        print("\nUpdated Inventory:")
        inventory.list_products()

        # Get details of a specific product
        print("\nDetails of 'Fenêtre PVC':")
        print(inventory.get_product("Fenêtre PVC"))

        # Remove a product from the inventory
        inventory.remove_product("Volet Aluminium")

        # List all products after removal
        print("\nFinal Inventory:")
        inventory.list_products()

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
```
