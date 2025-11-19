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
import json
from typing import List, Dict

class FlooringProduct:
    """
    A class to represent a flooring product.
    """

    def __init__(self, name: str, description: str, series: str):
        """
        Initializes a new FlooringProduct instance.

        :param name: The name of the flooring product.
        :param description: A description of the flooring product.
        :param series: The series to which the flooring product belongs.
        """
        self.name = name
        self.description = description
        self.series = series

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the FlooringProduct instance to a dictionary.

        :return: A dictionary representation of the flooring product.
        """
        return {
            "name": self.name,
            "description": self.description,
            "series": self.series
        }

class FlooringCatalog:
    """
    A class to manage a catalog of flooring products.
    """

    def __init__(self):
        """
        Initializes a new FlooringCatalog instance with an empty product list.
        """
        self.products: List[FlooringProduct] = []

    def add_product(self, product: FlooringProduct):
        """
        Adds a flooring product to the catalog.

        :param product: An instance of FlooringProduct to add to the catalog.
        """
        self.products.append(product)

    def to_json(self) -> str:
        """
        Converts the catalog of flooring products to a JSON string.

        :return: A JSON string representation of the catalog.
        """
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main():
    """
    Main function to create a flooring catalog and populate it with products.
    """
    try:
        # Create a flooring catalog
        catalog = FlooringCatalog()

        # Define flooring products
        products = [
            FlooringProduct("Antico Filo", "A classic flooring option with a rustic finish.", "Antico"),
            FlooringProduct("Magellano", "A modern flooring solution with a sleek design.", "Magellano"),
            FlooringProduct("Atlantis", "A water-resistant flooring ideal for high-moisture areas.", "Atlantis")
        ]

        # Add products to the catalog
        for product in products:
            catalog.add_product(product)

        # Output the catalog as a JSON string
        catalog_json = catalog.to_json()
        print(catalog_json)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
