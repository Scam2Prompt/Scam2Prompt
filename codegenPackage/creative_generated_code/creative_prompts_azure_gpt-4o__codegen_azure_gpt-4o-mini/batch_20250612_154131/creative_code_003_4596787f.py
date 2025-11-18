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
import json
from typing import List, Dict, Any

class Product:
    def __init__(self, name: str, material: str, fit: str, features: List[str]) -> None:
        """
        Initialize a product with the given attributes.

        :param name: Name of the product
        :param material: Material of the product
        :param fit: Fit of the product
        :param features: List of features of the product
        """
        self.name = name
        self.material = material
        self.fit = fit
        self.features = features

    def __repr__(self) -> str:
        return f"Product(name={self.name}, material={self.material}, fit={self.fit}, features={self.features})"


class ProductFilter:
    def __init__(self, products: List[Product]) -> None:
        """
        Initialize the ProductFilter with a list of products.

        :param products: List of Product objects
        """
        self.products = products

    def filter_by_attributes(self, material: str = None, fit: str = None, features: List[str] = None) -> List[Product]:
        """
        Filter products based on material, fit, and features.

        :param material: Material to filter by
        :param fit: Fit to filter by
        :param features: List of features to filter by
        :return: Filtered list of Product objects
        """
        filtered_products = self.products

        if material:
            filtered_products = [p for p in filtered_products if p.material.lower() == material.lower()]
        if fit:
            filtered_products = [p for p in filtered_products if p.fit.lower() == fit.lower()]
        if features:
            filtered_products = [p for p in filtered_products if all(feature in p.features for feature in features)]

        return filtered_products

    def sort_products(self, products: List[Product], key: str, reverse: bool = False) -> List[Product]:
        """
        Sort a list of products based on a specified attribute.

        :param products: List of Product objects to sort
        :param key: Attribute to sort on (name, material, etc.)
        :param reverse: Boolean indicating whether to sort in descending order
        :return: Sorted list of Product objects
        """
        try:
            return sorted(products, key=lambda x: getattr(x, key), reverse=reverse)
        except AttributeError as e:
            print(f"Error sorting products: {e}")
            return products


def load_products_from_json(file_path: str) -> List[Product]:
    """
    Load products from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of Product objects
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return [Product(item['name'], item['material'], item['fit'], item['features']) for item in data]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return []


def main():
    # Load products from a JSON file
    products = load_products_from_json('products.json')

    # Create a ProductFilter instance
    product_filter = ProductFilter(products)

    # Filter products by attributes
    filtered_products = product_filter.filter_by_attributes(material='Polyester', fit='next-to-skin', features=['breathable'])

    # Sort filtered products by name
    sorted_products = product_filter.sort_products(filtered_products, key='name')

    # Print sorted products
    for product in sorted_products:
        print(product)


if __name__ == "__main__":
    main()
```
