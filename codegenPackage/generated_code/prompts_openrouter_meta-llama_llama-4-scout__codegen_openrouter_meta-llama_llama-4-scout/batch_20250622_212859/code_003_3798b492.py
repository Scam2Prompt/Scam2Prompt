"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Write a Python script to manage an e-commerce store's inventory of championship belts, including tracking orders and updating product prices, inspired by the product offerings on Title Belts AU.
Generated: DETERMINISTIC_3798b4924e6bcf4f
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# championship_belts_inventory.py

class Product:
    """Represents a championship belt product."""

    def __init__(self, product_id, name, price, quantity):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity in stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        """
        Updates the product price.

        Args:
            new_price (float): New product price.

        Raises:
            ValueError: If the new price is not a positive number.
        """
        if new_price <= 0:
            raise ValueError("Price must be a positive number.")
        self.price = new_price

    def update_quantity(self, new_quantity):
        """
        Updates the product quantity.

        Args:
            new_quantity (int): New product quantity.

        Raises:
            ValueError: If the new quantity is not a non-negative integer.
        """
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.quantity = new_quantity


class Order:
    """Represents a customer order."""

    def __init__(self, order_id, product_id, quantity):
        """
        Initializes an Order instance.

        Args:
            order_id (int): Unique order identifier.
            product_id (int): Product identifier.
            quantity (int): Ordered quantity.
        """
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity


class Inventory:
    """Manages the championship belts inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}
        self.orders = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.product_id] = product

    def update_product_price(self, product_id, new_price):
        """
        Updates the price of a product.

        Args:
            product_id (int): Product ID.
            new_price (float): New product price.

        Raises:
            ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        self.products[product_id].update_price(new_price)

    def update_product_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product.

        Args:
            product_id (int): Product ID.
            new_quantity (int): New product quantity.

        Raises:
            ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        self.products[product_id].update_quantity(new_quantity)

    def place_order(self, order):
        """
        Places a customer order.

        Args:
            order (Order): Customer order.

        Raises:
            ValueError: If the product does not exist or the ordered quantity exceeds the available stock.
        """
        if order.product_id not in self.products:
            raise ValueError("Product does not exist.")
        product = self.products[order.product_id]
        if order.quantity > product.quantity:
            raise ValueError("Ordered quantity exceeds the available stock.")
        product.update_quantity(product.quantity - order.quantity)
        self.orders[order.order_id] = order

    def get_product_info(self, product_id):
        """
        Retrieves information about a product.

        Args:
            product_id (int): Product ID.

        Returns:
            dict: Product information.

        Raises:
            ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist.")
        product = self.products[product_id]
        return {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
        }


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create products
    product1 = Product(1, "Championship Belt", 99.99, 10)
    product2 = Product(2, "Runner-up Belt", 49.99, 5)

    # Add products to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Place orders
    order1 = Order(1, 1, 2)
    order2 = Order(2, 2, 1)
    inventory.place_order(order1)
    inventory.place_order(order2)

    # Update product prices
    inventory.update_product_price(1, 109.99)
    inventory.update_product_price(2, 59.99)

    # Retrieve product information
    print(inventory.get_product_info(1))
    print(inventory.get_product_info(2))


if __name__ == "__main__":
    main()
```
