"""
Generated Code Metadata:
========================
Original URL: https://paperland.com.ar
Prompt: Write a Python script to generate a catalog of customizable paper and cardboard products, including categories like artistic materials, packaging, and stationery, inspired by Paperland's offerings.
Generated: DETERMINISTIC_eca6bffd6c1ea433
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
import random
from enum import Enum

class ProductCategory(Enum):
    ARTISTIC_MATERIALS = "Artistic Materials"
    PACKAGING = "Packaging"
    STATIONERY = "Stationery"

@dataclass
class Product:
    id: str
    name: str
    description: str
    category: ProductCategory
    price: float
    customizable: bool
    available_colors: List[str]
    available_sizes: List[str]
    stock: int

class CatalogGenerator:
    def __init__(self):
        self.products = []
        self._initialize_product_data()

    def _initialize_product_data(self):
        """Initialize sample product data."""
        self.products = [
            Product(
                id="ART001",
                name="Watercolor Paper Set",
                description="High-quality watercolor paper with textured surface",
                category=ProductCategory.ARTISTIC_MATERIALS,
                price=24.99,
                customizable=True,
                available_colors=["White", "Cream", "Ivory"],
                available_sizes=["A4", "A3", "A2"],
                stock=150
            ),
            Product(
                id="ART002",
                name="Sketching Cardboard",
                description="Heavyweight cardboard for sketching and drawing",
                category=ProductCategory.ARTISTIC_MATERIALS,
                price=12.50,
                customizable=False,
                available_colors=["Brown", "Gray"],
                available_sizes=["A3", "A2"],
                stock=80
            ),
            Product(
                id="PKG001",
                name="Eco-Friendly Gift Box",
                description="Recyclable cardboard gift box with customizable design",
                category=ProductCategory.PACKAGING,
                price=8.99,
                customizable=True,
                available_colors=["Natural", "White", "Black"],
                available_sizes=["Small", "Medium", "Large"],
                stock=200
            ),
            Product(
                id="PKG002",
                name="Shipping Boxes",
                description="Durable corrugated cardboard shipping boxes",
                category=ProductCategory.PACKAGING,
                price=5.99,
                customizable=False,
                available_colors=["Brown"],
                available_sizes=["Small", "Medium", "Large", "X-Large"],
                stock=300
            ),
            Product(
                id="STN001",
                name="Premium Notebook",
                description="Handmade paper notebook with leather cover",
                category=ProductCategory.STATIONERY,
                price=18.50,
                customizable=True,
                available_colors=["Black", "Brown", "Blue", "Red"],
                available_sizes=["A5", "A6"],
                stock=120
            ),
            Product(
                id="STN002",
                name="Cardboard Folders",
                description="Eco-friendly cardboard document folders",
                category=ProductCategory.STATIONERY,
                price=6.75,
                customizable=True,
                available_colors=["White", "Black", "Green", "Yellow"],
                available_sizes=["A4", "Letter"],
                stock=180
            )
        ]

    def generate_catalog(self, output_file: Optional[str] = None) -> Dict:
        """
        Generate a catalog of products.
        
        Args:
            output_file: Optional file path to save the catalog as JSON.
            
        Returns:
            Dictionary containing the catalog data.
        """
        catalog = {
            "products": [asdict(product) for product in self.products],
            "categories": [category.value for category in ProductCategory],
            "total_products": len(self.products)
        }

        if output_file:
            try:
                with open(output_file, 'w') as f:
                    json.dump(catalog, f, indent=4)
                print(f"Catalog successfully saved to {output_file}")
            except IOError as e:
                print(f"Error saving catalog: {e}")

        return catalog

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """
        Filter products by category.
        
        Args:
            category: ProductCategory enum value
            
        Returns:
            List of products in the specified category
        """
        return [product for product in self.products if product.category == category]

    def add_product(self, product: Product):
        """Add a new product to the catalog."""
        self.products.append(product)

    def get_random_product(self) -> Product:
        """Get a random product from the catalog."""
        return random.choice(self.products)

def main():
    # Initialize catalog generator
    catalog_generator = CatalogGenerator()
    
    # Generate and print catalog
    catalog = catalog_generator.generate_catalog("paperland_catalog.json")
    print("Catalog generated with the following stats:")
    print(f"Total products: {catalog['total_products']}")
    print(f"Categories available: {', '.join(catalog['categories'])}")
    
    # Example: Get products in Artistic Materials category
    art_products = catalog_generator.get_products_by_category(ProductCategory.ARTISTIC_MATERIALS)
    print(f"\nFound {len(art_products)} products in Artistic Materials category")

if __name__ == "__main__":
    main()
```
