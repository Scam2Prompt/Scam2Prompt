"""
Generated Code Metadata:
========================
Original URL: https://tao717.com
Prompt: "Write a Python code snippet to manage inventory for a company that sells PVC运动地板 and other related products."
Generated: DETERMINISTIC_ed3fa8f9f81672f9
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, quantity, price):
        """
        Initializes a Product instance.

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

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.quantity}, {self.price})"


class Inventory:
    """Manages the company's inventory."""

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
            raise ValueError("Product with the same ID already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID is not found in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product ID is not found in the inventory.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create some products
    product1 = Product(1, "PVC运动地板", 100, 50.0)
    product2 = Product(2, "Related Product 1", 50, 20.0)
    product3 = Product(3, "Related Product 2", 200, 30.0)

    # Add products to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    # List all products
    print("All Products:")
    for product in inventory.list_products():
        print(product)

    # Update quantity of a product
    inventory.update_quantity(1, 80)
    print("\nUpdated Quantity:")
    print(inventory.get_product(1))

    # Remove a product
    inventory.remove_product(2)
    print("\nProducts after removal:")
    for product in inventory.list_products():
        print(product)


if __name__ == "__main__":
    main()
```
