"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Write a program to filter and sort products like leggings, tank tops, and varsity jackets by attributes such as material (Polyester/Elastane), fit (next-to-skin), and features (anti-UV, breathable) as described on Rising Star International.
Generated: DETERMINISTIC_4596787fa1206cd7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Product:
    """
    A class to represent a product.

    Attributes:
        name (str): Name of the product.
        material (str): Material of the product.
        fit (str): Fit type of the product.
        features (list): List of features of the product.
    """
    def __init__(self, name, material, fit, features):
        self.name = name
        self.material = material
        self.fit = fit
        self.features = features

    def __str__(self):
        return f"{self.name} ({self.material}, {self.fit}, Features: {', '.join(self.features)})"


def filter_products(products, material=None, fit=None, features=None):
    """
    Filter products based on material, fit, and features.

    Args:
        products (list): List of Product objects.
        material (str): Material to filter by.
        fit (str): Fit type to filter by.
        features (list): Features to filter by.

    Returns:
        list: Filtered list of Product objects.
    """
    filtered = products
    
    if material:
        filtered = [p for p in filtered if p.material == material]
    
    if fit:
        filtered = [p for p in filtered if p.fit == fit]
    
    if features:
        filtered = [p for p in filtered if all(feature in p.features for feature in features)]
    
    return filtered


def sort_products(products, key):
    """
    Sort products based on a key.

    Args:
        products (list): List of Product objects.
        key (str): Attribute name to sort by ('name', 'material', 'fit').

    Returns:
        list: Sorted list of Product objects.
    """
    return sorted(products, key=lambda p: getattr(p, key))


def main():
    """
    Main function to demonstrate filtering and sorting of products.
    """
    try:
        # Define product catalog
        product_catalog = [
            Product("Leggings", "Polyester/Elastane", "next-to-skin", ["anti-UV", "breathable"]),
            Product("Tank Top", "Polyester", "next-to-skin", ["breathable"]),
            Product("Varsity Jacket", "Polyester", "regular", ["breathable"]),
            Product("Sport Shorts", "Elastane", "next-to-skin", ["anti-UV", "quick-dry"]),
        ]

        # Filter products
        print("Filtered products (material=Polyester/Elastane, fit=next-to-skin, features=['anti-UV']):")
        filtered_products = filter_products(
            product_catalog,
            material="Polyester/Elastane",
            fit="next-to-skin",
            features=["anti-UV"]
        )
        for product in filtered_products:
            print(product)

        # Sort products
        print("\nSorted products by name:")
        sorted_products = sort_products(product_catalog, key="name")
        for product in sorted_products:
            print(product)
    
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
