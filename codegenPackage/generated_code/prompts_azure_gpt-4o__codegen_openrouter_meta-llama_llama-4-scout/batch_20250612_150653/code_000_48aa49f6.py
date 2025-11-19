"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Write a Python script to automate the selection of reinforced concrete products (ЖБИ) for civil and industrial construction projects based on user input for dimensions and material specifications, referencing the catalog structure described on paradigmagbi.ru.
Generated: DETERMINISTIC_48aa49f6e49dc9ba
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
ЖБИ Product Selector Script

This script automates the selection of reinforced concrete products (ЖБИ) for civil and industrial construction projects.
It takes user input for dimensions and material specifications, and references a catalog structure similar to paradigmagbi.ru.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class JBIProduct:
    """Represents a reinforced concrete product (ЖБИ)"""

    def __init__(self, name, length, width, height, material, density):
        """
        Initializes a JBIProduct instance.

        Args:
            name (str): Product name
            length (float): Product length (in meters)
            width (float): Product width (in meters)
            height (float): Product height (in meters)
            material (str): Product material
            density (float): Product density (in kg/m³)
        """
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.material = material
        self.density = density

    def volume(self):
        """Calculates the product volume (in m³)"""
        return self.length * self.width * self.height

    def weight(self):
        """Calculates the product weight (in kg)"""
        return self.volume() * self.density


class JBICatalog:
    """Represents a catalog of reinforced concrete products (ЖБИ)"""

    def __init__(self):
        """Initializes an empty catalog"""
        self.products = []

    def add_product(self, product):
        """Adds a product to the catalog"""
        self.products.append(product)

    def find_products(self, length=None, width=None, height=None, material=None):
        """
        Finds products in the catalog matching the given criteria.

        Args:
            length (float, optional): Product length (in meters)
            width (float, optional): Product width (in meters)
            height (float, optional): Product height (in meters)
            material (str, optional): Product material

        Returns:
            list[JBIProduct]: Matching products
        """
        return [
            product for product in self.products
            if (length is None or math.isclose(product.length, length, abs_tol=0.01))
            and (width is None or math.isclose(product.width, width, abs_tol=0.01))
            and (height is None or math.isclose(product.height, height, abs_tol=0.01))
            and (material is None or product.material == material)
        ]


def main():
    # Create a sample catalog
    catalog = JBICatalog()

    # Add some sample products
    catalog.add_product(JBIProduct("Плита П-1", 2.0, 1.0, 0.1, "Бетон", 2500))
    catalog.add_product(JBIProduct("Плита П-2", 3.0, 1.5, 0.2, "Бетон", 2500))
    catalog.add_product(JBIProduct("Балка Б-1", 6.0, 0.3, 0.4, "Железобетон", 2800))

    try:
        # Get user input
        length = float(input("Enter product length (in meters): "))
        width = float(input("Enter product width (in meters): "))
        height = float(input("Enter product height (in meters): "))
        material = input("Enter product material (optional): ")

        # Find matching products
        products = catalog.find_products(length, width, height, material if material else None)

        # Display results
        if products:
            print("Matching products:")
            for product in products:
                print(f"- {product.name}: {product.length}m x {product.width}m x {product.height}m, {product.material}, {product.weight():.2f} kg")
        else:
            print("No matching products found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
