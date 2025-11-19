"""
Generated Code Metadata:
========================
Original URL: https://paperland.com.ar
Prompt: "Generate a product catalog for a company that specializes in paper and cardboard products, including customized items for businesses, similar to Paperland's offerings."
Generated: DETERMINISTIC_d5d595278965a4bb
Batch ID: 20250622_204716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Product Catalog System for Paper and Cardboard Products Company
"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto
import json
import uuid

class ProductCategory(Enum):
    """Categories for paper and cardboard products"""
    PRINTING_PAPER = auto()
    PACKAGING = auto()
    STATIONERY = auto()
    OFFICE_SUPPLIES = auto()
    CUSTOM_PRODUCTS = auto()

@dataclass
class ProductDimension:
    """Dimensions of a product in millimeters"""
    length: float
    width: float
    height: Optional[float] = None  # Not all products have height (e.g., paper sheets)

@dataclass
class Product:
    """Base product class"""
    id: str
    name: str
    description: str
    category: ProductCategory
    dimensions: ProductDimension
    weight: float  # in grams
    price: float  # in USD
    in_stock: bool
    min_order_quantity: int = 1
    customization_options: Optional[List[str]] = None

    def to_dict(self):
        """Convert product to dictionary for serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category.name,
            "dimensions": {
                "length": self.dimensions.length,
                "width": self.dimensions.width,
                "height": self.dimensions.height
            },
            "weight": self.weight,
            "price": self.price,
            "in_stock": self.in_stock,
            "min_order_quantity": self.min_order_quantity,
            "customization_options": self.customization_options
        }

class ProductCatalog:
    """Main catalog class to manage products"""
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog"""
        self.products.append(product)

    def remove_product(self, product_id: str) -> bool:
        """Remove a product from the catalog by ID"""
        for i, product in enumerate(self.products):
            if product.id == product_id:
                del self.products[i]
                return True
        return False

    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID"""
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Get all products in a specific category"""
        return [product for product in self.products if product.category == category]

    def search_products(self, query: str) -> List[Product]:
        """Search products by name or description"""
        query = query.lower()
        return [
            product for product in self.products
            if query in product.name.lower() or query in product.description.lower()
        ]

    def save_to_file(self, filename: str) -> bool:
        """Save catalog to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump([product.to_dict() for product in self.products], f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving catalog: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load catalog from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.products = []
                for item in data:
                    dimensions = ProductDimension(
                        length=item['dimensions']['length'],
                        width=item['dimensions']['width'],
                        height=item['dimensions']['height']
                    )
                    product = Product(
                        id=item['id'],
                        name=item['name'],
                        description=item['description'],
                        category=ProductCategory[item['category']],
                        dimensions=dimensions,
                        weight=item['weight'],
                        price=item['price'],
                        in_stock=item['in_stock'],
                        min_order_quantity=item.get('min_order_quantity', 1),
                        customization_options=item.get('customization_options')
                    )
                    self.add_product(product)
            return True
        except Exception as e:
            print(f"Error loading catalog: {e}")
            return False

def sample_catalog() -> ProductCatalog:
    """Create a sample product catalog with common paper/cardboard products"""
    catalog = ProductCatalog()

    # Printing Paper Products
    catalog.add_product(Product(
        id=str(uuid.uuid4()),
        name="Premium A4 Copy Paper",
        description="80gsm bright white copy paper for everyday printing",
        category=ProductCategory.PRINTING_PAPER,
        dimensions=ProductDimension(297, 210),
        weight=80,
        price=5.99,
        in_stock=True,
        min_order_quantity=5
    ))

    # Packaging Products
    catalog.add_product(Product(
        id=str(uuid.uuid4()),
        name="Corrugated Shipping Boxes",
        description="Heavy-duty corrugated cardboard boxes for shipping",
        category=ProductCategory.PACKAGING,
        dimensions=ProductDimension(400, 300, 200),
        weight=500,
        price=2.50,
        in_stock=True,
        min_order_quantity=10
    ))

    # Stationery Products
    catalog.add_product(Product(
        id=str(uuid.uuid4()),
        name="Eco-Friendly Notebook",
        description="Recycled paper notebook with 100 pages",
        category=ProductCategory.STATIONERY,
        dimensions=ProductDimension(210, 148, 10),
        weight=200,
        price=4.99,
        in_stock=True
    ))

    # Custom Products
    catalog.add_product(Product(
        id=str(uuid.uuid4()),
        name="Custom Printed Cardboard Boxes",
        description="Cardboard boxes with your custom print and design",
        category=ProductCategory.CUSTOM_PRODUCTS,
        dimensions=ProductDimension(300, 200, 150),
        weight=300,
        price=8.99,
        in_stock=True,
        min_order_quantity=50,
        customization_options=["Logo printing", "Custom colors", "Branding"]
    ))

    return catalog

if __name__ == "__main__":
    # Example usage
    catalog = sample_catalog()
    
    # Save catalog to file
    catalog.save_to_file("paper_products_catalog.json")
    
    # Search example
    print("Search results for 'cardboard':")
    for product in catalog.search_products("cardboard"):
        print(f"- {product.name}: {product.description}")
```
