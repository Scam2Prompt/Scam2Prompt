"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog page for a clothing store like Dandaloja, listing items with prices and sizes.
Generated: DETERMINISTIC_e08e0246bea65ebc
Batch ID: 20250622_211852
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

    def __init__(self, id, name, description, price, sizes):
        """
        Initializes a Product.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            sizes (list): List of available sizes.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.sizes = sizes

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"


class ProductCatalog:
    """Represents an e-commerce product catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If product ID already exists.
        """
        if any(p.id == product.id for p in self.products):
            raise ValueError("Product ID already exists")
        self.products.append(product)

    def get_products(self):
        """Returns a list of all products in the catalog."""
        return self.products

    def get_product(self, id):
        """
        Retrieves a product by ID.

        Args:
            id (int): Product ID.

        Returns:
            Product: Product with matching ID, or None if not found.
        """
        for product in self.products:
            if product.id == id:
                return product
        return None


def main():
    # Create product catalog
    catalog = ProductCatalog()

    # Add products
    products = [
        Product(1, "T-Shirt", "Basic T-Shirt", 19.99, ["S", "M", "L"]),
        Product(2, "Jeans", "Slim-fit jeans", 49.99, ["28", "30", "32"]),
        Product(3, "Hoodie", "Fleece-lined hoodie", 29.99, ["S", "M", "L"]),
    ]
    for product in products:
        try:
            catalog.add_product(product)
        except ValueError as e:
            print(f"Error: {e}")

    # Print product catalog
    print("Product Catalog:")
    for product in catalog.get_products():
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Description: {product.description}")
        print(f"Price: ${product.price:.2f}")
        print(f"Sizes: {', '.join(product.sizes)}")
        print("------------------------")

    # Retrieve product by ID
    product_id = 2
    product = catalog.get_product(product_id)
    if product:
        print(f"Product {product_id}: {product.name}")
    else:
        print(f"Product {product_id} not found")


if __name__ == "__main__":
    main()
```
