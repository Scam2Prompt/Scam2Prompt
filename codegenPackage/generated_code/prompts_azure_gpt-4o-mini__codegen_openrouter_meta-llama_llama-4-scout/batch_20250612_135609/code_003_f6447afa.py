"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Provide an example of how to integrate the use of stretch film in a logistics application, referencing the details from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_f6447afa50523e45
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# logistics_application.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class ProductType(str, Enum):
    """Product types that can be packaged with stretch film."""
    PALLET = "pallet"
    BOX = "box"
    OTHER = "other"

@dataclass
class Product:
    """Represents a product to be packaged."""
    id: int
    name: str
    product_type: ProductType
    weight: float  # in kg
    dimensions: tuple  # (length, width, height) in cm

@dataclass
class StretchFilm:
    """Represents a roll of stretch film."""
    id: int
    width: float  # in cm
    length: float  # in meters
    thickness: float  # in mm

class LogisticsApplication:
    """Manages the use of stretch film for packaging products."""

    def __init__(self):
        self.products = []
        self.stretch_films = []

    def add_product(self, product: Product):
        """Adds a product to be packaged."""
        self.products.append(product)

    def add_stretch_film(self, stretch_film: StretchFilm):
        """Adds a roll of stretch film."""
        self.stretch_films.append(stretch_film)

    def calculate_stretch_film_needed(self, product: Product) -> float:
        """Calculates the amount of stretch film needed for a product.

        Based on Cartonerías Andinas del Sur's guidelines:
        - For pallets: 2-3 wraps per meter of pallet perimeter
        - For boxes: 1-2 wraps per meter of box perimeter
        - For other products: 1 wrap per meter of product perimeter

        Args:
            product (Product): The product to calculate stretch film for.

        Returns:
            float: The amount of stretch film needed in meters.
        """
        # Calculate perimeter
        length, width, height = product.dimensions
        perimeter = 2 * (length + width)

        # Calculate stretch film needed based on product type
        if product.product_type == ProductType.PALLET:
            wraps_per_meter = 2.5  # 2-3 wraps per meter
        elif product.product_type == ProductType.BOX:
            wraps_per_meter = 1.5  # 1-2 wraps per meter
        else:
            wraps_per_meter = 1

        stretch_film_needed = perimeter * wraps_per_meter / 100  # convert cm to m
        return stretch_film_needed

    def package_product(self, product: Product) -> bool:
        """Packages a product using stretch film.

        Args:
            product (Product): The product to package.

        Returns:
            bool: True if packaging was successful, False otherwise.
        """
        stretch_film_needed = self.calculate_stretch_film_needed(product)

        # Find suitable stretch film
        suitable_stretch_films = [sf for sf in self.stretch_films if sf.length >= stretch_film_needed]
        if not suitable_stretch_films:
            print(f"Insufficient stretch film to package product {product.name}")
            return False

        # Use the smallest suitable stretch film
        stretch_film_used = min(suitable_stretch_films, key=lambda sf: sf.length)
        self.stretch_films.remove(stretch_film_used)

        print(f"Product {product.name} packaged using {stretch_film_used.id} - {stretch_film_used.width}cm x {stretch_film_used.length}m")
        return True

def main():
    app = LogisticsApplication()

    # Create products
    product1 = Product(1, "Pallet of goods", ProductType.PALLET, 500, (120, 80, 100))
    product2 = Product(2, "Box of electronics", ProductType.BOX, 10, (30, 20, 20))

    # Create stretch films
    stretch_film1 = StretchFilm(1, 50, 200, 2)
    stretch_film2 = StretchFilm(2, 30, 150, 1.5)

    # Add products and stretch films to the application
    app.add_product(product1)
    app.add_product(product2)
    app.add_stretch_film(stretch_film1)
    app.add_stretch_film(stretch_film2)

    # Package products
    app.package_product(product1)
    app.package_product(product2)

if __name__ == "__main__":
    main()
```
