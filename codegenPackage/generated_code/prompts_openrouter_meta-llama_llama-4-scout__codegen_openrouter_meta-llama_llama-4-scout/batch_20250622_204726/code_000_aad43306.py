"""
Generated Code Metadata:
========================
Original URL: https://azimutfloor.com
Prompt: Write a Python script to generate a catalog of flooring products, including descriptions of Azimut Flooring's series, such as Antico filo, Magellano, and Atlantis.
Generated: DETERMINISTIC_aad433060d7c81f7
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# flooring_catalog.py

class FlooringProduct:
    """Represents a flooring product with its characteristics."""

    def __init__(self, name, description, series, price):
        """
        Initializes a FlooringProduct instance.

        Args:
            name (str): Product name.
            description (str): Product description.
            series (str): Product series.
            price (float): Product price.
        """
        self.name = name
        self.description = description
        self.series = series
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.series}\n  Description: {self.description}\n  Price: ${self.price:.2f}"


class FlooringCatalog:
    """Represents a catalog of flooring products."""

    def __init__(self):
        """Initializes an empty catalog."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (FlooringProduct): Product to add.
        """
        self.products.append(product)

    def __str__(self):
        catalog_str = "Flooring Catalog:\n\n"
        for i, product in enumerate(self.products, start=1):
            catalog_str += f"Product {i}:\n{product}\n\n"
        return catalog_str


def main():
    try:
        # Create flooring catalog
        catalog = FlooringCatalog()

        # Azimut Flooring series
        azimut_series = [
            FlooringProduct(
                "Antico Filo",
                "A classic, rustic look with a distressed finish.",
                "Antico Filo",
                3.99,
            ),
            FlooringProduct(
                "Magellano",
                "A sophisticated, nautical-inspired design.",
                "Magellano",
                4.99,
            ),
            FlooringProduct(
                "Atlantis",
                "A modern, sleek design with a hint of elegance.",
                "Atlantis",
                5.99,
            ),
        ]

        # Add products to catalog
        for product in azimut_series:
            catalog.add_product(product)

        # Print catalog
        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
