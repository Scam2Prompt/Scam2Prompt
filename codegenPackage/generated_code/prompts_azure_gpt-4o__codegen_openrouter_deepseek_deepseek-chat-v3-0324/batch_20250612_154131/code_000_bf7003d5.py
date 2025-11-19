"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Write Python code to generate a product catalog for sportswear and fitness wear, including categories like soccer uniforms, compression tops, and stringer hoodies, based on the structure of Rising Star International's product offerings.
Generated: DETERMINISTIC_bf7003d537bdb7de
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
from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto

class ProductCategory(Enum):
    SOCCER_UNIFORMS = auto()
    COMPRESSION_TOPS = auto()
    STRINGER_HOODIES = auto()
    TRAINING_SHORTS = auto()
    SPORTS_BRAS = auto()
    RUNNING_LEGGINGS = auto()

@dataclass
class ProductVariant:
    size: str
    color: str
    price: float
    sku: str
    stock_quantity: int

@dataclass
class Product:
    id: str
    name: str
    description: str
    category: ProductCategory
    variants: List[ProductVariant]
    material: Optional[str] = None
    is_featured: bool = False

class ProductCatalog:
    def __init__(self):
        self.products = []
    
    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to the catalog")
        self.products.append(product)
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Retrieve products by category."""
        return [product for product in self.products if product.category == category]
    
    def get_featured_products(self) -> List[Product]:
        """Retrieve featured products."""
        return [product for product in self.products if product.is_featured]
    
    def to_json(self, file_path: str) -> None:
        """Export catalog to JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump([asdict(product) for product in self.products], f, indent=4, default=str)
        except IOError as e:
            print(f"Error writing to file: {e}")
    
    @classmethod
    def from_json(cls, file_path: str) -> 'ProductCatalog':
        """Import catalog from JSON file."""
        catalog = cls()
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    variants = [ProductVariant(**v) for v in item['variants']]
                    item['category'] = ProductCategory[item['category']]
                    catalog.add_product(Product(
                        id=item['id'],
                        name=item['name'],
                        description=item['description'],
                        category=item['category'],
                        variants=variants,
                        material=item.get('material'),
                        is_featured=item.get('is_featured', False)
                    ))
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error reading from file: {e}")
        return catalog

def generate_sample_catalog() -> ProductCatalog:
    """Generate a sample product catalog for sportswear."""
    catalog = ProductCatalog()
    
    # Soccer Uniforms
    catalog.add_product(Product(
        id="SU001",
        name="Elite Soccer Jersey",
        description="High-performance soccer jersey with moisture-wicking technology",
        category=ProductCategory.SOCCER_UNIFORMS,
        material="100% Polyester",
        is_featured=True,
        variants=[
            ProductVariant(size="S", color="Red", price=49.99, sku="SU001-RED-S", stock_quantity=100),
            ProductVariant(size="M", color="Red", price=49.99, sku="SU001-RED-M", stock_quantity=150),
            ProductVariant(size="L", color="Blue", price=49.99, sku="SU001-BLUE-L", stock_quantity=75),
        ]
    ))
    
    # Compression Tops
    catalog.add_product(Product(
        id="CT002",
        name="Performance Compression Shirt",
        description="Breathable compression top for enhanced muscle support",
        category=ProductCategory.COMPRESSION_TOPS,
        material="88% Polyester, 12% Spandex",
        variants=[
            ProductVariant(size="XS", color="Black", price=34.99, sku="CT002-BLK-XS", stock_quantity=50),
            ProductVariant(size="M", color="Black", price=34.99, sku="CT002-BLK-M", stock_quantity=120),
            ProductVariant(size="XL", color="Navy", price=34.99, sku="CT002-NAV-XL", stock_quantity=60),
        ]
    ))
    
    # Stringer Hoodies
    catalog.add_product(Product(
        id="SH003",
        name="Athletic Stringer Hoodie",
        description="Lightweight hoodie with mesh panels for ventilation",
        category=ProductCategory.STRINGER_HOODIES,
        material="80% Cotton, 20% Polyester",
        is_featured=True,
        variants=[
            ProductVariant(size="S", color="Gray", price=59.99, sku="SH003-GRY-S", stock_quantity=80),
            ProductVariant(size="L", color="Black", price=59.99, sku="SH003-BLK-L", stock_quantity=90),
        ]
    ))
    
    return catalog

if __name__ == "__main__":
    # Generate and export sample catalog
    catalog = generate_sample_catalog()
    catalog.to_json("sportswear_catalog.json")
    
    # Example of loading the catalog
    loaded_catalog = ProductCatalog.from_json("sportswear_catalog.json")
    featured_products = loaded_catalog.get_featured_products()
    print(f"Featured Products: {[p.name for p in featured_products]}")
```
