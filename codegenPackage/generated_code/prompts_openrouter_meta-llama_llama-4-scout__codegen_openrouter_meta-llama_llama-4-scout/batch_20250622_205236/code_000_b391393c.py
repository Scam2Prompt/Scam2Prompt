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
# inventory_manager.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, price, quantity):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity in stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Inventory:
    """Manages the e-commerce inventory of mobile phone accessories."""

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
            raise ValueError("Product with the same ID already exists.")
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
            raise KeyError("Product ID not found in the inventory.")
        del self.products[product_id]

    def update_product_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product ID is not found in the inventory.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        if new_quantity < 0:
            raise ValueError("New quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance if found, otherwise None.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create some products
    ldnio_cable = Product(1, "LDNIO Cable", 5.99, 100)
    sodo_headphones = Product(2, "SODO Headphones", 29.99, 50)

    # Add products to the inventory
    inventory.add_product(ldnio_cable)
    inventory.add_product(sodo_headphones)

    # List all products
    print("Products in the inventory:")
    for product in inventory.list_products():
        print(product)

    # Update product quantity
    inventory.update_product_quantity(1, 80)
    print("\nUpdated LDNIO Cable quantity:")
    print(inventory.get_product(1))

    # Remove a product
    inventory.remove_product(2)
    print("\nProducts in the inventory after removal:")
    for product in inventory.list_products():
        print(product)


if __name__ == "__main__":
    main()
```
