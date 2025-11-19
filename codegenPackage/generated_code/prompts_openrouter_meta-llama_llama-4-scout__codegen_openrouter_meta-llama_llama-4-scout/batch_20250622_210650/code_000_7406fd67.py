"""
Generated Code Metadata:
========================
Original URL: https://sevalcikolata.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for Seval Çikolata's chocolate products, including their names, descriptions, and prices.
Generated: DETERMINISTIC_7406fd67e769eab0
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_product_catalog.py

class Product:
    """Represents a product in the catalog."""

    def __init__(self, name: str, description: str, price: float):
        """
        Initializes a Product.

        Args:
            name (str): The product's name.
            description (str): The product's description.
            price (float): The product's price.

        Raises:
            ValueError: If price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}', price={self.price})"


class ProductCatalog:
    """Represents a product catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): The product to add.

        Raises:
            ValueError: If a product with the same name already exists.
        """
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists")

        self.products[product.name] = product

    def remove_product(self, name: str):
        """
        Removes a product from the catalog.

        Args:
            name (str): The name of the product to remove.

        Raises:
            ValueError: If the product does not exist.
        """
        if name not in self.products:
            raise ValueError(f"Product '{name}' does not exist")

        del self.products[name]

    def get_product(self, name: str) -> Product:
        """
        Retrieves a product from the catalog.

        Args:
            name (str): The name of the product to retrieve.

        Returns:
            Product: The product.

        Raises:
            ValueError: If the product does not exist.
        """
        if name not in self.products:
            raise ValueError(f"Product '{name}' does not exist")

        return self.products[name]

    def list_products(self):
        """Lists all products in the catalog."""
        return list(self.products.values())


def main():
    # Create a product catalog
    catalog = ProductCatalog()

    # Create Seval Çikolata's chocolate products
    products = [
        Product("Sütlü Çikolata", "Seval Çikolata's milk chocolate", 5.99),
        Product("Bitter Çikolata", "Seval Çikolata's dark chocolate", 6.99),
        Product("Fındıklı Çikolata", "Seval Çikolata's chocolate with hazelnuts", 7.99),
    ]

    # Add products to the catalog
    for product in products:
        try:
            catalog.add_product(product)
        except ValueError as e:
            print(f"Error: {e}")

    # List products in the catalog
    print("Seval Çikolata's Product Catalog:")
    for product in catalog.list_products():
        print(f"Name: {product.name}")
        print(f"Description: {product.description}")
        print(f"Price: ${product.price:.2f}")
        print("------------------------")

    # Retrieve a product
    try:
        product = catalog.get_product("Sütlü Çikolata")
        print(f"Retrieved Product: {product.name}")
    except ValueError as e:
        print(f"Error: {e}")

    # Remove a product
    try:
        catalog.remove_product("Bitter Çikolata")
        print("Product removed successfully")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
