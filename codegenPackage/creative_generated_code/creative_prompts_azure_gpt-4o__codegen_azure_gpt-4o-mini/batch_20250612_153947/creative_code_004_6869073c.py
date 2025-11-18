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
class ProductVariant:
    """
    Class to manage a product variant including its attributes and pricing.
    """
    
    def __init__(self, variant_name: str, price: float):
        """
        Initialize a new ProductVariant.

        :param variant_name: Name of the product variant (e.g., 'SHRED - 30 Capsules').
        :param price: Price of the product variant.
        :raises ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.variant_name = variant_name
        self.price = price

class Product:
    """
    Class to manage a product with multiple variants and their pricing.
    """

    def __init__(self, product_name: str):
        """
        Initialize a new Product.

        :param product_name: Name of the product (e.g., 'SHRED Peptide Capsules').
        """
        self.product_name = product_name
        self.variants = {}

    def add_variant(self, variant_name: str, price: float):
        """
        Add a new variant to the product.

        :param variant_name: Name of the product variant.
        :param price: Price of the product variant.
        """
        try:
            variant = ProductVariant(variant_name, price)
            self.variants[variant_name] = variant
        except ValueError as e:
            print(f"Error adding variant: {e}")

    def update_variant_price(self, variant_name: str, new_price: float):
        """
        Update the price of an existing variant.

        :param variant_name: Name of the product variant to update.
        :param new_price: New price for the variant.
        :raises KeyError: If the variant does not exist.
        """
        if variant_name not in self.variants:
            raise KeyError(f"Variant '{variant_name}' does not exist.")
        
        if new_price < 0:
            raise ValueError("New price cannot be negative.")
        
        self.variants[variant_name].price = new_price

    def get_variant_price(self, variant_name: str) -> float:
        """
        Retrieve the price of a specific variant.

        :param variant_name: Name of the product variant.
        :return: Price of the variant.
        :raises KeyError: If the variant does not exist.
        """
        if variant_name not in self.variants:
            raise KeyError(f"Variant '{variant_name}' does not exist.")
        
        return self.variants[variant_name].price

    def list_variants(self):
        """
        List all variants and their prices for the product.
        
        :return: A dictionary of variant names and their corresponding prices.
        """
        return {variant_name: variant.price for variant_name, variant in self.variants.items()}

# Example usage
if __name__ == "__main__":
    # Create a new product
    shred_product = Product("SHRED Peptide Capsules")
    
    # Add variants
    shred_product.add_variant("SHRED - 30 Capsules", 29.99)
    shred_product.add_variant("SHRED - 60 Capsules", 49.99)
    
    # Update a variant price
    try:
        shred_product.update_variant_price("SHRED - 30 Capsules", 24.99)
    except (KeyError, ValueError) as e:
        print(e)
    
    # Retrieve a variant price
    try:
        price = shred_product.get_variant_price("SHRED - 60 Capsules")
        print(f"Price of SHRED - 60 Capsules: ${price:.2f}")
    except KeyError as e:
        print(e)
    
    # List all variants
    print("All product variants and prices:", shred_product.list_variants())
```
