"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Write a Python code to generate a catalog for a custom box packaging company like Box Creatived Semarang.
Generated: DETERMINISTIC_a1a9bbff45843c5f
Batch ID: 20250622_210703
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

class BoxType(Enum):
    """Enumeration for different box types."""
    STANDARD = "Standard"
    CUSTOM = "Custom"
    LUXURY = "Luxury"
    ECO_FRIENDLY = "Eco-Friendly"

@dataclass
class BoxSpecification:
    """Dataclass representing box specifications."""
    length: float  # in cm
    width: float   # in cm
    height: float  # in cm
    weight_limit: float  # in kg
    material: str

@dataclass
class BoxProduct:
    """Dataclass representing a box product."""
    product_id: str
    name: str
    description: str
    box_type: BoxType
    specifications: BoxSpecification
    price: float
    available: bool = True
    customization_options: Optional[List[str]] = None

class BoxCatalog:
    """Class representing a catalog of box products."""
    def __init__(self):
        self.products = []
    
    def add_product(self, product: BoxProduct) -> None:
        """Add a product to the catalog."""
        self.products.append(product)
    
    def remove_product(self, product_id: str) -> bool:
        """Remove a product from the catalog by ID."""
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                del self.products[i]
                return True
        return False
    
    def get_product(self, product_id: str) -> Optional[BoxProduct]:
        """Get a product by ID."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def get_available_products(self) -> List[BoxProduct]:
        """Get all available products."""
        return [product for product in self.products if product.available]
    
    def search_products(self, query: str) -> List[BoxProduct]:
        """Search products by name or description."""
        query = query.lower()
        return [
            product for product in self.products
            if query in product.name.lower() or query in product.description.lower()
        ]
    
    def filter_by_type(self, box_type: BoxType) -> List[BoxProduct]:
        """Filter products by box type."""
        return [product for product in self.products if product.box_type == box_type]
    
    def to_json(self, filename: str) -> bool:
        """Export catalog to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([asdict(product) for product in self.products], f, indent=4)
            return True
        except Exception as e:
            print(f"Error exporting catalog: {e}")
            return False
    
    @classmethod
    def from_json(cls, filename: str) -> 'BoxCatalog':
        """Import catalog from JSON file."""
        catalog = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    specs = BoxSpecification(**item['specifications'])
                    item['box_type'] = BoxType(item['box_type'])
                    item['specifications'] = specs
                    catalog.add_product(BoxProduct(**item))
        except Exception as e:
            print(f"Error importing catalog: {e}")
        return catalog

# Example usage
if __name__ == "__main__":
    # Create a catalog
    catalog = BoxCatalog()
    
    # Add some sample products
    catalog.add_product(BoxProduct(
        product_id="BX001",
        name="Standard Shipping Box",
        description="Durable cardboard box for shipping",
        box_type=BoxType.STANDARD,
        specifications=BoxSpecification(
            length=30.0,
            width=20.0,
            height=15.0,
            weight_limit=10.0,
            material="Corrugated Cardboard"
        ),
        price=5.99
    ))
    
    catalog.add_product(BoxProduct(
        product_id="BX002",
        name="Luxury Gift Box",
        description="Premium gift box with velvet lining",
        box_type=BoxType.LUXURY,
        specifications=BoxSpecification(
            length=25.0,
            width=25.0,
            height=10.0,
            weight_limit=5.0,
            material="Hardboard with Velvet Lining"
        ),
        price=19.99,
        customization_options=["Color", "Monogram"]
    ))
    
    # Export catalog to JSON
    catalog.to_json("box_catalog.json")
    
    # Import catalog from JSON
    imported_catalog = BoxCatalog.from_json("box_catalog.json")
    
    # Print available products
    print("Available Products:")
    for product in imported_catalog.get_available_products():
        print(f"{product.product_id}: {product.name} - ${product.price:.2f}")
```
