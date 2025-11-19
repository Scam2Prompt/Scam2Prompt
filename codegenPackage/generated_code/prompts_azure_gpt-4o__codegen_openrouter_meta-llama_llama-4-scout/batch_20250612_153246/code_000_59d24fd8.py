"""
Generated Code Metadata:
========================
Original URL: https://thegladiatorshoes.com
Prompt: Write Python code to create a product filter system for safety shoes based on features like "steel toe," "composite toe," and "metal-free" using the Gladiator Shoes product categories.
Generated: DETERMINISTIC_59d24fd8816606f1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class ShoeFeature(Enum):
    """Enum for shoe features."""
    STEEL_TOE = "steel toe"
    COMPOSITE_TOE = "composite toe"
    METAL_FREE = "metal-free"

class GladiatorShoes:
    """Class representing Gladiator Shoes product categories."""

    def __init__(self, name: str, features: List[ShoeFeature]):
        """
        Initialize a Gladiator Shoes product.

        Args:
        - name (str): The name of the shoe product.
        - features (List[ShoeFeature]): A list of features for the shoe product.
        """
        self.name = name
        self.features = features

class ProductFilter:
    """Class for filtering Gladiator Shoes products based on features."""

    def __init__(self, products: List[GladiatorShoes]):
        """
        Initialize a ProductFilter with a list of Gladiator Shoes products.

        Args:
        - products (List[GladiatorShoes]): A list of Gladiator Shoes products.
        """
        self.products = products

    def filter_by_feature(self, feature: ShoeFeature) -> List[GladiatorShoes]:
        """
        Filter products by a specific feature.

        Args:
        - feature (ShoeFeature): The feature to filter by.

        Returns:
        - List[GladiatorShoes]: A list of products that have the specified feature.
        """
        return [product for product in self.products if feature in product.features]

    def filter_by_features(self, features: List[ShoeFeature]) -> List[GladiatorShoes]:
        """
        Filter products by multiple features.

        Args:
        - features (List[ShoeFeature]): A list of features to filter by.

        Returns:
        - List[GladiatorShoes]: A list of products that have all the specified features.
        """
        return [product for product in self.products if all(feature in product.features for feature in features)]

def main():
    # Create Gladiator Shoes products
    product1 = GladiatorShoes("Product 1", [ShoeFeature.STEEL_TOE, ShoeFeature.METAL_FREE])
    product2 = GladiatorShoes("Product 2", [ShoeFeature.COMPOSITE_TOE])
    product3 = GladiatorShoes("Product 3", [ShoeFeature.STEEL_TOE, ShoeFeature.COMPOSITE_TOE])
    product4 = GladiatorShoes("Product 4", [ShoeFeature.METAL_FREE])

    # Create a ProductFilter with the products
    products = [product1, product2, product3, product4]
    filter = ProductFilter(products)

    # Filter products by a single feature
    steel_toe_products = filter.filter_by_feature(ShoeFeature.STEEL_TOE)
    print("Steel Toe Products:")
    for product in steel_toe_products:
        print(product.name)

    # Filter products by multiple features
    metal_free_steel_toe_products = filter.filter_by_features([ShoeFeature.METAL_FREE, ShoeFeature.STEEL_TOE])
    print("\nMetal-Free and Steel Toe Products:")
    for product in metal_free_steel_toe_products:
        print(product.name)

if __name__ == "__main__":
    main()
```
