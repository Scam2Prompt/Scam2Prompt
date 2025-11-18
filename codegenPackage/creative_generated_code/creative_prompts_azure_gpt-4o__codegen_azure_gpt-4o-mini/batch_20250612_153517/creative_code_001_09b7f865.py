"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Recommend a Python library for managing product inventory in an online store that includes categories such as "Scule electrice," "Roti si anvelope," and "Uz gospodaresc."
Generated: DETERMINISTIC_09b7f865554854e9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

"""
Inventory Manager for an Online Store

This module provides a class to manage product inventory, including
categories such as 'Scule electrice', 'Roti si anvelope', and 'Uz gospodaresc'.
It allows adding, updating, and deleting products while handling errors gracefully.
"""

class Product:
    """
    Class representing a product in the inventory.
    """

    def __init__(self, product_id, name, category, quantity, price):
        """
        Initialize a new product.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            category (str): Category of the product.
            quantity (int): Quantity available in stock.
            price (float): Price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name} (Category: {self.category}, Quantity: {self.quantity}, Price: ${self.price:.2f})"


class InventoryManager:
    """
    Class to manage the inventory of products.
    """

    def __init__(self):
        """Initialize an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Add a new product to the inventory.

        Args:
            product (Product): The product to be added.

        Raises:
            ValueError: If the product ID already exists in the inventory.
        """
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product

    def update_product(self, product_id, quantity=None, price=None):
        """
        Update the details of a product.

        Args:
            product_id (int): The ID of the product to update.
            quantity (int, optional): The new quantity of the product.
            price (float, optional): The new price of the product.

        Raises:
            KeyError: If the product ID does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found in inventory.")
        
        product = self.products[product_id]
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price

    def delete_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
            product_id (int): The ID of the product to remove.

        Raises:
            KeyError: If the product ID does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError(f"Product ID {product_id} not found in inventory.")
        del self.products[product_id]

    def list_products(self):
        """
        List all products in the inventory.

        Returns:
            list: A list of all products in string format.
        """
        return [str(product) for product in self.products.values()]


# Example Usage
if __name__ == '__main__':
    inventory_manager = InventoryManager()

    # Adding products to inventory
    try:
        inventory_manager.add_product(Product(1, "Drill", "Scule electrice", 10, 99.99))
        inventory_manager.add_product(Product(2, "Tire", "Roti si anvelope", 20, 49.99))
        inventory_manager.add_product(Product(3, "Hammer", "Uz gospodaresc", 15, 19.99))

        # Listing products
        print("Current Inventory:")
        for product in inventory_manager.list_products():
            print(product)

        # Updating a product
        inventory_manager.update_product(1, quantity=8)

        # Deleting a product
        inventory_manager.delete_product(2)

        # Listing products after updates
        print("\nUpdated Inventory:")
        for product in inventory_manager.list_products():
            print(product)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
