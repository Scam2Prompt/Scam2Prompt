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
    Represents a flooring product with its attributes.
    """
    def __init__(self, name: str, series: str, description: str, features: List[str]):
        self.name = name
        self.series = series
        self.description = description
        self.features = features

    def to_dict(self) -> Dict:
        """
        Converts the product to a dictionary for serialization.
        """
        return {
            "name": self.name,
            "series": self.series,
            "description": self.description,
            "features": self.features
        }

class FlooringCatalog:
    """
    Manages a collection of flooring products.
    """
    def __init__(self):
        self.products = []

    def add_product(self, product: FlooringProduct) -> None:
        """
        Adds a product to the catalog.
        """
        self.products.append(product)

    def generate_catalog(self, filename: str) -> None:
        """
        Generates a JSON catalog file from the products.
        """
        try:
            catalog_data = [product.to_dict() for product in self.products]
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(catalog_data, f, indent=4, ensure_ascii=False)
            print(f"Catalog successfully generated as {filename}")
        except IOError as e:
            print(f"Error writing catalog file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

def main():
    """
    Main function to create and generate the flooring catalog.
    """
    catalog = FlooringCatalog()

    # Add Azimut Flooring products
    catalog.add_product(FlooringProduct(
        name="Antico Filo",
        series="Azimut Flooring",
        description="A classic wood flooring with a timeless design.",
        features=["Natural wood grains", "Durable finish", "Wide plank options"]
    ))

    catalog.add_product(FlooringProduct(
        name="Magellano",
        series="Azimut Flooring",
        description="Modern wood flooring with innovative textures.",
        features=["Contemporary design", "Scratch-resistant", "Easy maintenance"]
    ))

    catalog.add_product(FlooringProduct(
        name="Atlantis",
        series="Azimut Flooring",
        description="Luxury wood flooring with water-resistant properties.",
        features=["Waterproof core", "Real wood veneer", "Stable structure"]
    ))

    # Generate the catalog file
    catalog.generate_catalog("azimut_flooring_catalog.json")

if __name__ == "__main__":
    main()
```
