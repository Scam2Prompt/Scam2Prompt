"""
Generated Code Metadata:
========================
Original URL: https://hildeinox.com
Prompt: What are the different types of stainless steel products offered by Hilde Inox, and what are their applications?
Generated: DETERMINISTIC_b6f80d909fbe3cd1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# stainless_steel_products.py

class StainlessSteelProduct:
    """Represents a stainless steel product offered by Hilde Inox."""

    def __init__(self, name, description, application):
        """
        Initializes a StainlessSteelProduct.

        Args:
            name (str): The name of the product.
            description (str): A brief description of the product.
            application (str): The application of the product.
        """
        self.name = name
        self.description = description
        self.application = application

    def __str__(self):
        return f"{self.name}: {self.description} - {self.application}"


class HildeInoxProductCatalog:
    """Represents the product catalog of Hilde Inox."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (StainlessSteelProduct): The product to add.
        """
        self.products.append(product)

    def get_products(self):
        """
        Retrieves all products in the catalog.

        Returns:
            list[StainlessSteelProduct]: A list of all products.
        """
        return self.products

    def get_product_by_name(self, name):
        """
        Retrieves a product by name.

        Args:
            name (str): The name of the product.

        Returns:
            StainlessSteelProduct: The product with the given name, or None if not found.
        """
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


def main():
    try:
        # Create product catalog
        catalog = HildeInoxProductCatalog()

        # Add products to catalog
        catalog.add_product(StainlessSteelProduct(
            "304 Stainless Steel Sheet",
            "A popular austenitic stainless steel sheet",
            "Construction, Decorations, Kitchenware"
        ))
        catalog.add_product(StainlessSteelProduct(
            "316L Stainless Steel Pipe",
            "A corrosion-resistant austenitic stainless steel pipe",
            "Industrial, Marine, Chemical Processing"
        ))
        catalog.add_product(StainlessSteelProduct(
            "410 Stainless Steel Bar",
            "A general-purpose ferritic stainless steel bar",
            "Construction, Automotive, Machinery"
        ))

        # Print all products
        print("Hilde Inox Stainless Steel Products:")
        for product in catalog.get_products():
            print(product)

        # Retrieve product by name
        product_name = "304 Stainless Steel Sheet"
        product = catalog.get_product_by_name(product_name)
        if product:
            print(f"\nProduct: {product}")
        else:
            print(f"\nProduct '{product_name}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
