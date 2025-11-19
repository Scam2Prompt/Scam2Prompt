"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Write a Python script to manage inventory for a retail partner of PDC Brush, including tracking orders, stock levels, and shipping information.
Generated: DETERMINISTIC_4d169b3d599dfcf0
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            quantity (int): Initial quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

class Order:
    """Represents an order in the inventory management system."""

    def __init__(self, order_id, product_id, quantity, shipping_address):
        """
        Initializes an Order object.

        Args:
            order_id (int): Unique identifier for the order.
            product_id (int): Foreign key referencing the Product object.
            quantity (int): Quantity of the product ordered.
            shipping_address (str): Shipping address for the order.
        """
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.shipping_address = shipping_address
        self.shipping_status = "Pending"

class Inventory:
    """Manages the inventory for PDC Brush retail partner."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}
        self.orders = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product object to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with ID {} already exists.".format(product.product_id))
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product with ID {} does not exist.".format(product_id))
        del self.products[product_id]

    def update_product_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product with ID {} does not exist.".format(product_id))
        self.products[product_id].quantity = new_quantity

    def place_order(self, order):
        """
        Places an order in the inventory management system.

        Args:
            order (Order): Order object to place.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the ordered quantity exceeds the available stock.
        """
        if order.product_id not in self.products:
            raise KeyError("Product with ID {} does not exist.".format(order.product_id))
        product = self.products[order.product_id]
        if order.quantity > product.quantity:
            raise ValueError("Insufficient stock to fulfill order.")
        self.orders[order.order_id] = order
        product.quantity -= order.quantity

    def update_shipping_status(self, order_id, status):
        """
        Updates the shipping status of an order.

        Args:
            order_id (int): ID of the order to update.
            status (str): New shipping status.

        Raises:
            KeyError: If the order does not exist in the inventory.
        """
        if order_id not in self.orders:
            raise KeyError("Order with ID {} does not exist.".format(order_id))
        self.orders[order_id].shipping_status = status

def main():
    # Create an instance of the Inventory class
    inventory = Inventory()

    # Create products
    product1 = Product(1, "PDC Brush", 100)
    product2 = Product(2, "PDC Brush Set", 50)

    # Add products to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Place orders
    order1 = Order(1, 1, 20, "123 Main St")
    order2 = Order(2, 2, 10, "456 Elm St")
    inventory.place_order(order1)
    inventory.place_order(order2)

    # Update shipping status
    inventory.update_shipping_status(1, "Shipped")

    # Print inventory and order information
    print("Products:")
    for product in inventory.products.values():
        print("ID: {}, Name: {}, Quantity: {}".format(product.product_id, product.name, product.quantity))

    print("\nOrders:")
    for order in inventory.orders.values():
        print("ID: {}, Product ID: {}, Quantity: {}, Shipping Status: {}".format(
            order.order_id, order.product_id, order.quantity, order.shipping_status))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)))
```
