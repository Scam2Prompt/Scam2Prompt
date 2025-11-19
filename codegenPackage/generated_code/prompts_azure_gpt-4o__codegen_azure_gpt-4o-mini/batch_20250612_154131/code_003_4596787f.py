"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write a program to filter and sort products like leggings, tank tops, and varsity jackets by attributes such as material (Polyester/Elastane), fit (next-to-skin), and features (anti-UV, breathable) as described on Rising Star International.
Generated: DETERMINISTIC_4596787fa1206cd7
Batch ID: 20250612_154131
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

class Product:
    """Class representing a product with various attributes."""
    
    def __init__(self, name: str, material: str, fit: str, features: List[str]):
        self.name = name
        self.material = material
        self.fit = fit
        self.features = features

    def __repr__(self):
        return f"Product(name={self.name}, material={self.material}, fit={self.fit}, features={self.features})"

def filter_products(products: List[Product], material: str = None, fit: str = None, features: List[str] = None) -> List[Product]:
    """Filter products based on material, fit, and features.

    Args:
        products (List[Product]): List of products to filter.
        material (str): Material to filter by (e.g., 'Polyester', 'Elastane').
        fit (str): Fit to filter by (e.g., 'next-to-skin').
        features (List[str]): List of features to filter by (e.g., ['anti-UV', 'breathable']).

    Returns:
        List[Product]: Filtered list of products.
    """
    filtered_products = products
    
    if material:
        filtered_products = [p for p in filtered_products if p.material == material]
    
    if fit:
        filtered_products = [p for p in filtered_products if p.fit == fit]
    
    if features:
        filtered_products = [p for p in filtered_products if all(feature in p.features for feature in features)]
    
    return filtered_products

def sort_products(products: List[Product], key: str, reverse: bool = False) -> List[Product]:
    """Sort products based on a specified key.

    Args:
        products (List[Product]): List of products to sort.
        key (str): The attribute to sort by (e.g., 'name', 'material').
        reverse (bool): Whether to sort in descending order.

    Returns:
        List[Product]: Sorted list of products.
    """
    try:
        return sorted(products, key=lambda p: getattr(p, key), reverse=reverse)
    except AttributeError as e:
        print(f"Error: {e}. Invalid sort key provided.")
        return products

def main():
    """Main function to demonstrate filtering and sorting of products."""
    # Sample product data
    products_data = [
        {"name": "Leggings A", "material": "Polyester", "fit": "next-to-skin", "features": ["breathable", "anti-UV"]},
        {"name": "Tank Top B", "material": "Elastane", "fit": "next-to-skin", "features": ["breathable"]},
        {"name": "Varsity Jacket C", "material": "Polyester", "fit": "loose", "features": ["water-resistant"]},
        {"name": "Leggings D", "material": "Polyester", "fit": "next-to-skin", "features": ["anti-UV"]},
    ]

    # Convert product data to Product objects
    products = [Product(**data) for data in products_data]

    # Filter products by material and fit
    filtered = filter_products(products, material="Polyester", fit="next-to-skin", features=["anti-UV"])
    
    # Sort filtered products by name
    sorted_products = sort_products(filtered, key="name")

    # Output the results
    print("Filtered and Sorted Products:")
    for product in sorted_products:
        print(product)

if __name__ == "__main__":
    main()
```
