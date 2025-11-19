"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Generate a Python script to categorize the products (e.g., Buttweld Pipe Fittings, Socket Weld Fittings, Perforated Sheets) from Dinkar Alloys based on their material type and application.
Generated: DETERMINISTIC_9220f59b7917e840
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_categorizer.py

from enum import Enum
from typing import Dict, List

class MaterialType(str, Enum):
    """Material types for products"""
    STAINLESS_STEEL = "Stainless Steel"
    CARBON_STEEL = "Carbon Steel"
    ALLOY_STEEL = "Alloy Steel"
    OTHER = "Other"

class Application(str, Enum):
    """Application areas for products"""
    INDUSTRIAL = "Industrial"
    COMMERCIAL = "Commercial"
    RESIDENTIAL = "Residential"
    OTHER = "Other"

class Product:
    """Represents a product with material type and application"""
    def __init__(self, name: str, material_type: MaterialType, application: Application):
        self.name = name
        self.material_type = material_type
        self.application = application

    def __repr__(self):
        return f"Product('{self.name}', '{self.material_type.value}', '{self.application.value}')"

class ProductCategorizer:
    """Categorizes products by material type and application"""
    def __init__(self):
        self.products: List[Product] = []
        self.categories: Dict[MaterialType, Dict[Application, List[Product]]] = {}

    def add_product(self, product: Product):
        """Add a product to the categorizer"""
        self.products.append(product)
        self._update_categories(product)

    def _update_categories(self, product: Product):
        """Update categories dictionary with a new product"""
        if product.material_type not in self.categories:
            self.categories[product.material_type] = {}
        
        if product.application not in self.categories[product.material_type]:
            self.categories[product.material_type][product.application] = []
        
        self.categories[product.material_type][product.application].append(product)

    def get_categories(self) -> Dict[MaterialType, Dict[Application, List[Product]]]:
        """Get categorized products"""
        return self.categories

def main():
    # Example usage
    categorizer = ProductCategorizer()

    products = [
        Product("Buttweld Pipe Fittings", MaterialType.STAINLESS_STEEL, Application.INDUSTRIAL),
        Product("Socket Weld Fittings", MaterialType.CARBON_STEEL, Application.COMMERCIAL),
        Product("Perforated Sheets", MaterialType.ALLOY_STEEL, Application.INDUSTRIAL),
        Product("Flanges", MaterialType.STAINLESS_STEEL, Application.RESIDENTIAL),
    ]

    for product in products:
        categorizer.add_product(product)

    categories = categorizer.get_categories()

    for material_type, applications in categories.items():
        print(f"Material Type: {material_type.value}")
        for application, products in applications.items():
            print(f"  Application: {application.value}")
            for product in products:
                print(f"    - {product.name}")
        print()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
