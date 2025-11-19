"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Write a Python code snippet to manage an e-commerce product catalog for mobile accessories like car mounts and power banks.
Generated: DETERMINISTIC_b47ea837572265f0
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    """Represents a product in the catalog."""

    def __init__(self, product_id, name, description, price, stock_quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            stock_quantity (int): Current stock quantity.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}, Stock Quantity: {self.stock_quantity}"


class ProductCatalog:
    """Manages a collection of products."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the catalog.

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
        Removes a product from the catalog.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        del self.products[product_id]

    def update_product(self, product_id, name=None, description=None, price=None, stock_quantity=None):
        """
        Updates a product's details.

        Args:
            product_id (int): ID of the product to update.
            name (str, optional): New product name. Defaults to None.
            description (str, optional): New product description. Defaults to None.
            price (float, optional): New product price. Defaults to None.
            stock_quantity (int, optional): New stock quantity. Defaults to None.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        product = self.products[product_id]
        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if stock_quantity:
            product.stock_quantity = stock_quantity

    def get_product(self, product_id):
        """
        Retrieves a product by ID.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product object, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    # Create some products
    product1 = Product(1, "Car Mount", "A sturdy car mount for your phone.", 19.99, 10)
    product2 = Product(2, "Power Bank", "A portable power bank for charging your devices.", 29.99, 20)

    # Add products to the catalog
    catalog.add_product(product1)
    catalog.add_product(product2)

    # List all products
    print("Products:")
    for product in catalog.list_products():
        print(product)

    # Update a product
    catalog.update_product(1, stock_quantity=5)
    print("\nUpdated Product:")
    print(catalog.get_product(1))

    # Remove a product
    catalog.remove_product(2)

    # Try to retrieve a removed product
    try:
        print(catalog.get_product(2))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
