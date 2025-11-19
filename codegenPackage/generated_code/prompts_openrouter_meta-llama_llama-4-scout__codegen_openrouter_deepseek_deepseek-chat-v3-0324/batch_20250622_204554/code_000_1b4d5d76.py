"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Write a Python script to create a catalog for outdoor advertising products like billboards, videotrons, and neon boxes, including their prices and sizes.
Generated: DETERMINISTIC_1b4d5d760ec81dfb
Batch ID: 20250622_204554
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
from enum import Enum

class ProductType(Enum):
    BILLBOARD = "Billboard"
    VIDEOTRON = "Videotron"
    NEON_BOX = "Neon Box"

@dataclass
class Product:
    """Represents an outdoor advertising product."""
    product_id: str
    name: str
    product_type: ProductType
    width: float  # in meters
    height: float  # in meters
    price: float  # in USD
    description: Optional[str] = None

class ProductCatalog:
    """Manages a collection of outdoor advertising products."""
    
    def __init__(self):
        self.products = []
    
    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        self.products.append(product)
    
    def remove_product(self, product_id: str) -> bool:
        """Remove a product by ID. Returns True if successful."""
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                del self.products[i]
                return True
        return False
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID. Returns None if not found."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def get_products_by_type(self, product_type: ProductType) -> List[Product]:
        """Get all products of a specific type."""
        return [p for p in self.products if p.product_type == product_type]
    
    def save_to_file(self, filename: str) -> bool:
        """Save catalog to JSON file. Returns True if successful."""
        try:
            with open(filename, 'w') as f:
                json.dump([asdict(p) for p in self.products], f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving catalog: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load catalog from JSON file. Returns True if successful."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.products = [
                    Product(
                        product_id=item['product_id'],
                        name=item['name'],
                        product_type=ProductType(item['product_type']),
                        width=item['width'],
                        height=item['height'],
                        price=item['price'],
                        description=item.get('description')
                    ) for item in data
                ]
            return True
        except Exception as e:
            print(f"Error loading catalog: {e}")
            return False
    
    def display_catalog(self) -> None:
        """Print all products in the catalog."""
        print("\nOutdoor Advertising Product Catalog:")
        print("-" * 50)
        for product in self.products:
            print(f"ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Type: {product.product_type.value}")
            print(f"Size: {product.width}m x {product.height}m")
            print(f"Price: ${product.price:,.2f}")
            if product.description:
                print(f"Description: {product.description}")
            print("-" * 50)

def sample_catalog() -> ProductCatalog:
    """Create and return a sample product catalog."""
    catalog = ProductCatalog()
    
    catalog.add_product(Product(
        product_id="BB001",
        name="Standard Billboard",
        product_type=ProductType.BILLBOARD,
        width=5.0,
        height=3.0,
        price=1500.00,
        description="Traditional static billboard with vinyl printing"
    ))
    
    catalog.add_product(Product(
        product_id="VT001",
        name="Premium Videotron",
        product_type=ProductType.VIDEOTRON,
        width=8.0,
        height=4.0,
        price=5000.00,
        description="High-resolution LED display with full color support"
    ))
    
    catalog.add_product(Product(
        product_id="NB001",
        name="Neon Sign Box",
        product_type=ProductType.NEON_BOX,
        width=2.0,
        height=1.0,
        price=1200.00,
        description="Custom neon-lit acrylic box sign"
    ))
    
    return catalog

if __name__ == "__main__":
    # Example usage
    catalog = sample_catalog()
    catalog.display_catalog()
    
    # Save to file
    catalog.save_to_file("product_catalog.json")
    
    # Load from file
    new_catalog = ProductCatalog()
    if new_catalog.load_from_file("product_catalog.json"):
        new_catalog.display_catalog()
```
