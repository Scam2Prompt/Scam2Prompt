"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Generate a product catalog for Rising Star International's work wear section, including descriptions and prices for each item.
Generated: DETERMINISTIC_5e27429b7f8b9c5a
Batch ID: 20250622_212843
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

    def __init__(self, name, description, price):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name}: {self.description}, ${self.price:.2f}"


class ProductCatalog:
    """Represents a product catalog."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def remove_product(self, name):
        """
        Removes a product from the catalog.

        Args:
            name (str): Name of the product to remove.

        Raises:
            ValueError: If the product is not found.
        """
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return
        raise ValueError(f"Product '{name}' not found.")

    def get_product(self, name):
        """
        Gets a product from the catalog.

        Args:
            name (str): Name of the product to get.

        Returns:
            Product: The product, or None if not found.
        """
        for product in self.products:
            if product.name == name:
                return product
        return None

    def __str__(self):
        """Returns a string representation of the catalog."""
        catalog_str = "Rising Star International Work Wear Catalog\n"
        for product in self.products:
            catalog_str += f"- {product}\n"
        return catalog_str


def main():
    # Create a product catalog
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product(Product("Work Shirt", "A high-quality, breathable work shirt.", 19.99))
    catalog.add_product(Product("Work Pants", "Durable, comfortable work pants.", 29.99))
    catalog.add_product(Product("Safety Vest", "A reflective safety vest for increased visibility.", 9.99))
    catalog.add_product(Product("Work Boots", "Sturdy, waterproof work boots.", 49.99))

    # Print the catalog
    print(catalog)

    # Get a product
    product = catalog.get_product("Work Shirt")
    if product:
        print(f"\nProduct: {product}")
    else:
        print("\nProduct not found.")

    # Remove a product
    try:
        catalog.remove_product("Safety Vest")
        print("\nProduct removed.")
    except ValueError as e:
        print(f"\nError: {e}")

    # Print the updated catalog
    print(catalog)


if __name__ == "__main__":
    main()
```
