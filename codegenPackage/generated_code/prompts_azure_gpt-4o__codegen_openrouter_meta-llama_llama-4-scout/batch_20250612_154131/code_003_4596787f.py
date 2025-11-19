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
# product_filter.py

class Product:
    """Represents a product with attributes."""

    def __init__(self, name, material, fit, features):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            material (str): Product material.
            fit (str): Product fit.
            features (list[str]): Product features.
        """
        self.name = name
        self.material = material
        self.fit = fit
        self.features = features

    def __repr__(self):
        return f"Product('{self.name}', '{self.material}', '{self.fit}', {self.features})"


class ProductFilter:
    """Filters and sorts products by attributes."""

    def __init__(self, products):
        """
        Initializes a ProductFilter.

        Args:
            products (list[Product]): List of products.
        """
        self.products = products

    def filter_by_material(self, material):
        """
        Filters products by material.

        Args:
            material (str): Material to filter by.

        Returns:
            list[Product]: Filtered products.
        """
        return [product for product in self.products if product.material == material]

    def filter_by_fit(self, fit):
        """
        Filters products by fit.

        Args:
            fit (str): Fit to filter by.

        Returns:
            list[Product]: Filtered products.
        """
        return [product for product in self.products if product.fit == fit]

    def filter_by_features(self, features):
        """
        Filters products by features.

        Args:
            features (list[str]): Features to filter by.

        Returns:
            list[Product]: Filtered products.
        """
        return [
            product
            for product in self.products
            if all(feature in product.features for feature in features)
        ]

    def sort_by_name(self):
        """
        Sorts products by name.

        Returns:
            list[Product]: Sorted products.
        """
        return sorted(self.products, key=lambda product: product.name)

    def sort_by_material(self):
        """
        Sorts products by material.

        Returns:
            list[Product]: Sorted products.
        """
        return sorted(self.products, key=lambda product: product.material)


def main():
    # Example products
    products = [
        Product("Leggings", "Polyester/Elastane", "next-to-skin", ["anti-UV", "breathable"]),
        Product("Tank Top", "Cotton", "loose", ["breathable"]),
        Product("Varsity Jacket", "Polyester", "regular", ["water-resistant"]),
        Product("Leggings 2", "Polyester/Elastane", "next-to-skin", ["anti-UV", "breathable"]),
    ]

    filter = ProductFilter(products)

    print("All Products:")
    for product in filter.sort_by_name():
        print(product)

    print("\nFiltered by Material (Polyester/Elastane):")
    for product in filter.filter_by_material("Polyester/Elastane"):
        print(product)

    print("\nFiltered by Fit (next-to-skin):")
    for product in filter.filter_by_fit("next-to-skin"):
        print(product)

    print("\nFiltered by Features (anti-UV, breathable):")
    for product in filter.filter_by_features(["anti-UV", "breathable"]):
        print(product)

    print("\nSorted by Material:")
    for product in filter.sort_by_material():
        print(product)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
