"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Write code to optimize inventory management for fittings and accessories like Phase Conductor Clamps and Connectors, referencing Swamiji Transmission Pvt. Ltd.'s product offerings.
Generated: DETERMINISTIC_6ff18c571958de52
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, quantity, price):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Product {self.product_id}: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"


class Inventory:
    """Manages a collection of products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with this ID already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product not found")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product ID is not found.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product not found")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product object, or None if not found.
        """
        return self.products.get(product_id)

    def __str__(self):
        inventory_str = "Inventory:\n"
        for product in self.products.values():
            inventory_str += str(product) + "\n"
        return inventory_str


class Order:
    """Represents a customer order."""

    def __init__(self, order_id, product_id, quantity):
        """
        Initializes an Order object.

        Args:
            order_id (int): Unique order ID.
            product_id (int): ID of the product being ordered.
            quantity (int): Quantity ordered.
        """
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __str__(self):
        return f"Order {self.order_id}: Product {self.product_id}, Quantity: {self.quantity}"


class InventoryManager:
    """Manages inventory and fulfills orders."""

    def __init__(self, inventory):
        """
        Initializes an InventoryManager object.

        Args:
            inventory (Inventory): The inventory to manage.
        """
        self.inventory = inventory

    def fulfill_order(self, order):
        """
        Fulfills a customer order.

        Args:
            order (Order): The order to fulfill.

        Raises:
            KeyError: If the product ID is not found.
            ValueError: If the ordered quantity exceeds the available stock.
        """
        product = self.inventory.get_product(order.product_id)
        if product is None:
            raise KeyError("Product not found")
        if order.quantity > product.quantity:
            raise ValueError("Insufficient stock")
        self.inventory.update_quantity(order.product_id, product.quantity - order.quantity)
        print(f"Order {order.order_id} fulfilled")

    def restock(self, product_id, quantity):
        """
        Restocks a product.

        Args:
            product_id (int): ID of the product to restock.
            quantity (int): Quantity to add.

        Raises:
            KeyError: If the product ID is not found.
            ValueError: If the quantity to add is negative.
        """
        product = self.inventory.get_product(product_id)
        if product is None:
            raise KeyError("Product not found")
        if quantity < 0:
            raise ValueError("Quantity to add cannot be negative")
        self.inventory.update_quantity(product_id, product.quantity + quantity)


def main():
    # Create products
    phase_conductor_clamp = Product(1, "Phase Conductor Clamp", 100, 50.0)
    connector = Product(2, "Connector", 50, 20.0)

    # Create inventory and add products
    inventory = Inventory()
    inventory.add_product(phase_conductor_clamp)
    inventory.add_product(connector)

    # Create order and fulfill it
    order = Order(1, 1, 20)
    manager = InventoryManager(inventory)
    try:
        manager.fulfill_order(order)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Restock product
    try:
        manager.restock(1, 30)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Print final inventory
    print(inventory)


if __name__ == "__main__":
    main()
```
