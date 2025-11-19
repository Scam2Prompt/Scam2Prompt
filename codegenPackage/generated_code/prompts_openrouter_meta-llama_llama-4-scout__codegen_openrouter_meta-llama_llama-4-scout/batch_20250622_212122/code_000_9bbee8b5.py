"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Write a Python script to manage inventory for a kitchen utensil store like Varejão das Louças in Pedreira-SP.
Generated: DETERMINISTIC_9bbee8b51ca2588f
Batch ID: 20250622_212122
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
    """Represents a kitchen utensil product."""

    def __init__(self, id: int, name: str, quantity: int, price: float):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            quantity (int): Initial product quantity.
            price (float): Product price.
        """
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', quantity={self.quantity}, price={self.price})"


class Inventory:
    """Manages kitchen utensil inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists.")
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product does not exist.
        """
        if product_id not in self.products:
            raise KeyError(f"Product with ID {product_id} does not exist.")
        del self.products[product_id]

    def update_quantity(self, product_id: int, new_quantity: int):
        """
        Updates the quantity of a product.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product does not exist.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError(f"Product with ID {product_id} does not exist.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by ID.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance.

        Raises:
            KeyError: If the product does not exist.
        """
        if product_id not in self.products:
            raise KeyError(f"Product with ID {product_id} does not exist.")
        return self.products[product_id]

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Add some products
    products = [
        Product(1, "Spatula", 10, 5.99),
        Product(2, "Whisk", 5, 3.99),
        Product(3, "Cutting Board", 8, 19.99),
    ]
    for product in products:
        try:
            inventory.add_product(product)
        except ValueError as e:
            print(f"Error: {e}")

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(product)

    # Update quantity
    try:
        inventory.update_quantity(1, 15)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Get product
    try:
        product = inventory.get_product(2)
        print(f"Product {product.id}: {product.name}, Quantity: {product.quantity}")
    except KeyError as e:
        print(f"Error: {e}")

    # Remove product
    try:
        inventory.remove_product(3)
    except KeyError as e:
        print(f"Error: {e}")

    # List products again
    print("Products after removal:")
    for product in inventory.list_products():
        print(product)


if __name__ == "__main__":
    main()
```
