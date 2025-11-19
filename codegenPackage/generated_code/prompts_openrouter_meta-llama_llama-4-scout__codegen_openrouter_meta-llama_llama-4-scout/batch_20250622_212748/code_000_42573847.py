"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Write a Python code to manage a product catalog for a company like Yobugo that offers various types of liquors, such as Licor de café, Pisco Afrutado, and Cremas.
Generated: DETERMINISTIC_4257384709ae60ed
Batch ID: 20250622_212748
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

    def __init__(self, id: int, name: str, description: str, price: float, stock: int):
        """
        Initializes a Product.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            stock (int): Product stock quantity.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ProductCatalog:
    """Manages a catalog of products."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.id] = product

    def remove_product(self, id: int):
        """
        Removes a product from the catalog.

        Args:
            id (int): ID of the product to remove.

        Raises:
            KeyError: If the product does not exist.
        """
        if id not in self.products:
            raise KeyError("Product does not exist.")
        del self.products[id]

    def update_product(self, id: int, **kwargs):
        """
        Updates a product in the catalog.

        Args:
            id (int): ID of the product to update.
            **kwargs: Updated product attributes.

        Raises:
            KeyError: If the product does not exist.
        """
        if id not in self.products:
            raise KeyError("Product does not exist.")
        product = self.products[id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise ValueError(f"Invalid attribute: {key}")

    def get_product(self, id: int) -> Product:
        """
        Retrieves a product from the catalog.

        Args:
            id (int): ID of the product to retrieve.

        Returns:
            Product: Retrieved product.

        Raises:
            KeyError: If the product does not exist.
        """
        if id not in self.products:
            raise KeyError("Product does not exist.")
        return self.products[id]

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    # Create products
    products = [
        Product(1, "Licor de café", "Coffee liqueur", 15.99, 100),
        Product(2, "Pisco Afrutado", "Fruit-flavored Pisco", 12.99, 50),
        Product(3, "Cremas", "Cream-based liqueur", 10.99, 200),
    ]

    # Add products to catalog
    for product in products:
        try:
            catalog.add_product(product)
        except ValueError as e:
            print(f"Error: {e}")

    # List products
    print("Products:")
    for product in catalog.list_products():
        print(product)

    # Update product
    try:
        catalog.update_product(1, price=16.99)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Get product
    try:
        product = catalog.get_product(2)
        print(f"\nProduct: {product}")
        print(f"Description: {product.description}")
        print(f"Stock: {product.stock}")
    except KeyError as e:
        print(f"Error: {e}")

    # Remove product
    try:
        catalog.remove_product(3)
    except KeyError as e:
        print(f"Error: {e}")

    # List products again
    print("\nUpdated products:")
    for product in catalog.list_products():
        print(product)


if __name__ == "__main__":
    main()
```
