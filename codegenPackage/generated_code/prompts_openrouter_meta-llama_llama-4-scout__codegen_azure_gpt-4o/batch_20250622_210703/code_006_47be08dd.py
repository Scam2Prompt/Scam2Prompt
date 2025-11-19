"""
Generated Code Metadata:
========================
Original URL: https://elo.mk
Prompt: "Develop a system for managing inventory and tracking orders for a baby products e-commerce platform."
Generated: DETERMINISTIC_47be08dd8dfe941f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

import uuid
from datetime import datetime

class Product:
    """
    Represents a product in the inventory.
    """
    def __init__(self, name, price, stock):
        self.id = str(uuid.uuid4())  # Unique identifier for the product
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """
        Updates the stock of the product.
        :param quantity: The quantity to add or subtract from stock.
        """
        if self.stock + quantity < 0:
            raise ValueError("Insufficient stock to complete the operation.")
        self.stock += quantity

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, stock={self.stock})"


class Order:
    """
    Represents an order placed by a customer.
    """
    def __init__(self, customer_name, products):
        self.id = str(uuid.uuid4())  # Unique identifier for the order
        self.customer_name = customer_name
        self.products = products  # List of tuples (Product, quantity)
        self.timestamp = datetime.now()
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        """
        Calculates the total price of the order.
        """
        return sum(product.price * quantity for product, quantity in self.products)

    def __str__(self):
        return f"Order(id={self.id}, customer_name={self.customer_name}, total_price={self.total_price}, timestamp={self.timestamp})"


class InventoryManager:
    """
    Manages the inventory and orders for the e-commerce platform.
    """
    def __init__(self):
        self.products = {}  # Dictionary to store products by their ID
        self.orders = {}  # Dictionary to store orders by their ID

    def add_product(self, name, price, stock):
        """
        Adds a new product to the inventory.
        :param name: Name of the product.
        :param price: Price of the product.
        :param stock: Initial stock of the product.
        """
        product = Product(name, price, stock)
        self.products[product.id] = product
        return product

    def update_product_stock(self, product_id, quantity):
        """
        Updates the stock of a product.
        :param product_id: ID of the product to update.
        :param quantity: Quantity to add or subtract from stock.
        """
        if product_id not in self.products:
            raise ValueError("Product not found.")
        self.products[product_id].update_stock(quantity)

    def place_order(self, customer_name, product_quantities):
        """
        Places an order for the customer.
        :param customer_name: Name of the customer.
        :param product_quantities: List of tuples (product_id, quantity).
        """
        products = []
        for product_id, quantity in product_quantities:
            if product_id not in self.products:
                raise ValueError(f"Product with ID {product_id} not found.")
            product = self.products[product_id]
            if product.stock < quantity:
                raise ValueError(f"Insufficient stock for product {product.name}.")
            products.append((product, quantity))

        # Deduct stock for each product
        for product, quantity in products:
            product.update_stock(-quantity)

        # Create and store the order
        order = Order(customer_name, products)
        self.orders[order.id] = order
        return order

    def get_product(self, product_id):
        """
        Retrieves a product by its ID.
        :param product_id: ID of the product to retrieve.
        """
        return self.products.get(product_id, None)

    def get_order(self, order_id):
        """
        Retrieves an order by its ID.
        :param order_id: ID of the order to retrieve.
        """
        return self.orders.get(order_id, None)

    def list_products(self):
        """
        Lists all products in the inventory.
        """
        return list(self.products.values())

    def list_orders(self):
        """
        Lists all orders placed.
        """
        return list(self.orders.values())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the inventory manager
        inventory_manager = InventoryManager()

        # Add products to the inventory
        product1 = inventory_manager.add_product("Baby Bottle", 10.99, 100)
        product2 = inventory_manager.add_product("Diapers", 25.99, 200)

        print("Products in inventory:")
        for product in inventory_manager.list_products():
            print(product)

        # Place an order
        order = inventory_manager.place_order("Alice", [(product1.id, 2), (product2.id, 3)])
        print("\nOrder placed:")
        print(order)

        print("\nProducts in inventory after order:")
        for product in inventory_manager.list_products():
            print(product)

        # Retrieve an order
        retrieved_order = inventory_manager.get_order(order.id)
        print("\nRetrieved order:")
        print(retrieved_order)

    except Exception as e:
        print(f"Error: {e}")
```
