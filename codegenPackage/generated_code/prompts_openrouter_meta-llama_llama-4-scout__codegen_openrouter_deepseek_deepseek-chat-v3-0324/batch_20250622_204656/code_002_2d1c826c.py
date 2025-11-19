"""
Generated Code Metadata:
========================
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: "Generate a product catalog for a glass manufacturing company, including descriptions of laminated glass, reflective glass, and decorative glass lines, with specifications and use cases."
Generated: DETERMINISTIC_2d1c826c296d962d
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Catalog for Glass Manufacturing Company

This module contains classes and functions to represent a product catalog
for a glass manufacturing company. It includes product specifications,
descriptions, and use cases for different glass types.
"""

from dataclasses import dataclass
from typing import List, Optional
import json

@dataclass
class ProductSpecification:
    """Dataclass to hold product specifications"""
    thickness: str
    size_range: str
    color_options: List[str]
    thermal_properties: Optional[str] = None
    acoustic_properties: Optional[str] = None
    safety_rating: Optional[str] = None

@dataclass
class GlassProduct:
    """Base class for glass products"""
    name: str
    description: str
    specifications: ProductSpecification
    use_cases: List[str]
    product_code: str

class ProductCatalog:
    """Main catalog class to manage glass products"""
    
    def __init__(self):
        self.products = []
        
    def add_product(self, product: GlassProduct) -> None:
        """Add a product to the catalog"""
        self.products.append(product)
        
    def get_product_by_code(self, product_code: str) -> Optional[GlassProduct]:
        """Retrieve product by its code"""
        for product in self.products:
            if product.product_code == product_code:
                return product
        return None
    
    def get_all_products(self) -> List[GlassProduct]:
        """Get all products in the catalog"""
        return self.products
    
    def to_json(self) -> str:
        """Serialize catalog to JSON"""
        return json.dumps([product.__dict__ for product in self.products], indent=2)

def initialize_catalog() -> ProductCatalog:
    """Initialize the product catalog with sample data"""
    catalog = ProductCatalog()
    
    # Laminated Glass
    laminated_spec = ProductSpecification(
        thickness="6mm to 25mm",
        size_range="Up to 3000mm x 2000mm",
        color_options=["Clear", "Bronze", "Gray", "Blue", "Green"],
        safety_rating="ANSI Z97.1, EN 12600",
        acoustic_properties="STC 35-40"
    )
    laminated = GlassProduct(
        name="Laminated Safety Glass",
        description="Two or more layers of glass bonded with PVB interlayer for safety and security",
        specifications=laminated_spec,
        use_cases=[
            "Automotive windshields",
            "Skylights and overhead glazing",
            "Balcony and stair railings",
            "Hurricane-resistant windows"
        ],
        product_code="LAM-001"
    )
    
    # Reflective Glass
    reflective_spec = ProductSpecification(
        thickness="4mm to 12mm",
        size_range="Up to 3300mm x 2400mm",
        color_options=["Silver", "Blue", "Gold", "Green"],
        thermal_properties="Low-E coating available"
    )
    reflective = GlassProduct(
        name="Reflective Glass",
        description="Glass with metallic coating to reflect sunlight and reduce heat gain",
        specifications=reflective_spec,
        use_cases=[
            "Commercial building facades",
            "Energy-efficient windows",
            "Solar control applications",
            "Privacy glass"
        ],
        product_code="REF-002"
    )
    
    # Decorative Glass
    decorative_spec = ProductSpecification(
        thickness="3mm to 10mm",
        size_range="Custom sizes available",
        color_options=["Custom colors and patterns"],
        safety_rating="Tempered option available"
    )
    decorative = GlassProduct(
        name="Decorative Glass",
        description="Artistic glass with various patterns, textures, and colors",
        specifications=decorative_spec,
        use_cases=[
            "Interior partitions",
            "Doors and entryways",
            "Furniture tops",
            "Backsplashes and wall decor"
        ],
        product_code="DEC-003"
    )
    
    catalog.add_product(laminated)
    catalog.add_product(reflective)
    catalog.add_product(decorative)
    
    return catalog

if __name__ == "__main__":
    # Example usage
    catalog = initialize_catalog()
    
    # Print all products
    print("Glass Manufacturing Product Catalog")
    print("===================================")
    for product in catalog.get_all_products():
        print(f"\nProduct: {product.name} ({product.product_code})")
        print(f"Description: {product.description}")
        print("Specifications:")
        print(f"  Thickness: {product.specifications.thickness}")
        print(f"  Size Range: {product.specifications.size_range}")
        print(f"  Color Options: {', '.join(product.specifications.color_options)}")
        if product.specifications.thermal_properties:
            print(f"  Thermal Properties: {product.specifications.thermal_properties}")
        if product.specifications.acoustic_properties:
            print(f"  Acoustic Properties: {product.specifications.acoustic_properties}")
        if product.specifications.safety_rating:
            print(f"  Safety Rating: {product.specifications.safety_rating}")
        print("Use Cases:")
        for use_case in product.use_cases:
            print(f"  - {use_case}")
    
    # Export to JSON
    with open("glass_catalog.json", "w") as f:
        f.write(catalog.to_json())
```
