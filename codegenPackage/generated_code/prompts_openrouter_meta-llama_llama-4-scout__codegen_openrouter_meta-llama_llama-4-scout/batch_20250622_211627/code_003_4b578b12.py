"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: Generate a product catalog for Mahadev Enterprise's agricultural commodities, including product descriptions, pricing, and packaging details.
Generated: DETERMINISTIC_4b578b12d19d02df
Batch ID: 20250622_211627
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
    """Represents an agricultural commodity product."""

    def __init__(self, name, description, price, packaging):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price per unit.
            packaging (str): Product packaging details.
        """
        self.name = name
        self.description = description
        self.price = price
        self.packaging = packaging

    def __str__(self):
        return f"{self.name}: {self.description}, Price: ${self.price:.2f}, Packaging: {self.packaging}"


class ProductCatalog:
    """Represents a catalog of agricultural commodity products."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product_id, name, description, price, packaging):
        """
        Adds a product to the catalog.

        Args:
            product_id (str): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price per unit.
            packaging (str): Product packaging details.

        Raises:
            ValueError: If product ID already exists in the catalog.
        """
        if product_id in self.products:
            raise ValueError(f"Product ID '{product_id}' already exists in the catalog.")
        self.products[product_id] = Product(name, description, price, packaging)

    def remove_product(self, product_id):
        """
        Removes a product from the catalog.

        Args:
            product_id (str): Unique product ID.

        Raises:
            ValueError: If product ID does not exist in the catalog.
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID '{product_id}' does not exist in the catalog.")
        del self.products[product_id]

    def update_product(self, product_id, name=None, description=None, price=None, packaging=None):
        """
        Updates a product in the catalog.

        Args:
            product_id (str): Unique product ID.
            name (str, optional): New product name. Defaults to None.
            description (str, optional): New product description. Defaults to None.
            price (float, optional): New product price per unit. Defaults to None.
            packaging (str, optional): New product packaging details. Defaults to None.

        Raises:
            ValueError: If product ID does not exist in the catalog.
        """
        if product_id not in self.products:
            raise ValueError(f"Product ID '{product_id}' does not exist in the catalog.")
        product = self.products[product_id]
        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if packaging:
            product.packaging = packaging

    def get_product(self, product_id):
        """
        Retrieves a product from the catalog.

        Args:
            product_id (str): Unique product ID.

        Returns:
            Product: Product instance if found, otherwise None.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product("P001", "Wheat", "High-quality wheat for baking.", 2.50, "50 lbs")
    catalog.add_product("P002", "Corn", "Fresh corn for cooking.", 1.75, "12 pieces")
    catalog.add_product("P003", "Soybean", "Organic soybean for cooking oil.", 3.00, "20 lbs")

    # List all products in the catalog
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Retrieve a product by ID
    product_id = "P002"
    product = catalog.get_product(product_id)
    if product:
        print(f"\nProduct {product_id} Details:")
        print(product)
    else:
        print(f"\nProduct ID '{product_id}' not found in the catalog.")

    # Update a product
    catalog.update_product("P001", price=2.75)
    print("\nUpdated Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Remove a product
    catalog.remove_product("P003")
    print("\nUpdated Product Catalog after removal:")
    for product in catalog.list_products():
        print(product)


if __name__ == "__main__":
    main()
```
