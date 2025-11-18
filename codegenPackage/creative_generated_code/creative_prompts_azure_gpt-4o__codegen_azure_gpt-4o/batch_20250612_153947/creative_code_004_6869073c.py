"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Write a Python function to manage product variants and pricing for items like "SHRED" peptide capsules, which have multiple variants and prices, as seen on BioLongevity Labs.
Generated: DETERMINISTIC_6869073ca6d0f413
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict, Union

# Define a class to manage product variants and pricing
class ProductManager:
    def __init__(self, product_name: str):
        """
        Initialize the ProductManager with a product name and an empty variants dictionary.

        :param product_name: Name of the product (e.g., "SHRED Peptide Capsules")
        """
        self.product_name = product_name
        self.variants = {}  # Dictionary to store variants and their prices

    def add_variant(self, variant_name: str, price: float):
        """
        Add a new product variant with its price.

        :param variant_name: Name of the variant (e.g., "30 Capsules", "60 Capsules")
        :param price: Price of the variant
        :raises ValueError: If the price is not positive
        """
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        self.variants[variant_name] = price

    def update_price(self, variant_name: str, new_price: float):
        """
        Update the price of an existing product variant.

        :param variant_name: Name of the variant to update
        :param new_price: New price of the variant
        :raises KeyError: If the variant does not exist
        :raises ValueError: If the new price is not positive
        """
        if variant_name not in self.variants:
            raise KeyError(f"Variant '{variant_name}' does not exist.")
        if new_price <= 0:
            raise ValueError("Price must be a positive value.")
        self.variants[variant_name] = new_price

    def get_price(self, variant_name: str) -> Union[float, None]:
        """
        Retrieve the price of a specific product variant.

        :param variant_name: Name of the variant to retrieve the price for
        :return: Price of the variant, or None if the variant does not exist
        """
        return self.variants.get(variant_name)

    def list_variants(self) -> List[Dict[str, Union[str, float]]]:
        """
        List all available product variants and their prices.

        :return: List of dictionaries with variant names and prices
        """
        return [{"variant": name, "price": price} for name, price in self.variants.items()]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the ProductManager with the product name
        manager = ProductManager("SHRED Peptide Capsules")

        # Add product variants and their prices
        manager.add_variant("30 Capsules", 29.99)
        manager.add_variant("60 Capsules", 49.99)

        # Update the price of an existing variant
        manager.update_price("60 Capsules", 47.99)

        # Retrieve the price of a specific variant
        price = manager.get_price("30 Capsules")
        print(f"Price for '30 Capsules': ${price:.2f}")

        # List all variants and their prices
        variants = manager.list_variants()
        print("Available variants and pricing:")
        for variant in variants:
            print(f"{variant['variant']}: ${variant['price']:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
