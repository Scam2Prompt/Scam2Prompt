"""
Generated Code Metadata:
========================
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for a coffee roastery like First Crack Coffee Roasters, including product categories and prices.
Generated: DETERMINISTIC_563a14750164ae37
Batch ID: 20250622_212702
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

    def __init__(self, product_id, name, description, price, category):
        """
        Initializes a Product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            category (str): Product category.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ProductCatalog:
    """Represents a product catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}
        self.categories = set()

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If product ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.product_id] = product
        self.categories.add(product.category)

    def get_product(self, product_id):
        """
        Retrieves a product by ID.

        Args:
            product_id (int): Product ID.

        Returns:
            Product: Product with matching ID, or None if not found.
        """
        return self.products.get(product_id)

    def get_products_by_category(self, category):
        """
        Retrieves products by category.

        Args:
            category (str): Category name.

        Returns:
            list[Product]: Products in the specified category.
        """
        return [product for product in self.products.values() if product.category == category]

    def __str__(self):
        catalog_str = "Product Catalog:\n"
        for product in self.products.values():
            catalog_str += f"- {product}\n"
        return catalog_str


def main():
    # Create a product catalog
    catalog = ProductCatalog()

    # Create products
    products = [
        Product(1, "French Roast", "Dark and smoky", 12.99, "Coffee"),
        Product(2, "Italian Roast", "Medium and balanced", 11.99, "Coffee"),
        Product(3, "Espresso Roast", "Strong and bold", 13.99, "Coffee"),
        Product(4, "Coffee Maker", "Automatic drip coffee maker", 49.99, "Equipment"),
        Product(5, "Coffee Grinder", "Burr grinder for fresh coffee", 29.99, "Equipment"),
    ]

    # Add products to catalog
    for product in products:
        try:
            catalog.add_product(product)
        except ValueError as e:
            print(f"Error: {e}")

    # Print catalog
    print(catalog)

    # Retrieve product by ID
    product_id = 1
    product = catalog.get_product(product_id)
    if product:
        print(f"\nProduct {product_id}: {product}")
    else:
        print(f"\nProduct {product_id} not found")

    # Retrieve products by category
    category = "Coffee"
    products_in_category = catalog.get_products_by_category(category)
    print(f"\n{category} products:")
    for product in products_in_category:
        print(product)


if __name__ == "__main__":
    main()
```
