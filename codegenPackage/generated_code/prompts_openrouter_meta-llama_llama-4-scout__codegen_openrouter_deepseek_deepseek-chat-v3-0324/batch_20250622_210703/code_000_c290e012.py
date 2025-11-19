"""
Generated Code Metadata:
========================
Original URL: https://todobroncetb.com
Prompt: Write a Python code snippet to create a catalog system for a bathroom accessories company like Todo Bronce that manufactures bronze products.
Generated: DETERMINISTIC_c290e012a082d34f
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
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class ProductCategory(Enum):
    """Enumeration of product categories."""
    FAUCETS = "Faucets"
    SHOWER_HEADS = "Shower Heads"
    TOWEL_BARS = "Towel Bars"
    MIRRORS = "Mirrors"
    ACCESSORIES = "Accessories"


@dataclass
class Product:
    """Data class representing a product."""
    id: str
    name: str
    description: str
    category: ProductCategory
    price: float
    stock: int
    dimensions: Optional[Dict[str, float]] = None
    weight: Optional[float] = None

    def to_dict(self) -> Dict:
        """Convert product to dictionary."""
        product_dict = asdict(self)
        product_dict['category'] = self.category.value
        return product_dict


class Catalog:
    """Class representing a product catalog."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self._load_catalog()

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
        self._save_catalog()

    def update_product(self, product_id: str, **kwargs) -> None:
        """Update product attributes."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        for key, value in kwargs.items():
            if key == 'category' and isinstance(value, str):
                value = ProductCategory(value)
            setattr(product, key, value)
        
        self._save_catalog()

    def remove_product(self, product_id: str) -> None:
        """Remove a product from the catalog."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]
        self._save_catalog()

    def get_product(self, product_id: str) -> Product:
        """Get a product by ID."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        return self.products[product_id]

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Get all products in a specific category."""
        return [p for p in self.products.values() if p.category == category]

    def search_products(self, query: str) -> List[Product]:
        """Search products by name or description."""
        query = query.lower()
        return [
            p for p in self.products.values()
            if query in p.name.lower() or query in p.description.lower()
        ]

    def _save_catalog(self) -> None:
        """Save catalog to JSON file."""
        with open('catalog.json', 'w') as f:
            json.dump(
                [p.to_dict() for p in self.products.values()],
                f,
                indent=2
            )

    def _load_catalog(self) -> None:
        """Load catalog from JSON file."""
        try:
            with open('catalog.json', 'r') as f:
                products_data = json.load(f)
                for product_data in products_data:
                    product_data['category'] = ProductCategory(product_data['category'])
                    product = Product(**product_data)
                    self.products[product.id] = product
        except FileNotFoundError:
            pass


# Example usage
if __name__ == "__main__":
    catalog = Catalog()
    
    # Add sample products
    try:
        catalog.add_product(Product(
            id="001",
            name="Bronze Faucet",
            description="Handcrafted bronze faucet with modern design",
            category=ProductCategory.FAUCETS,
            price=249.99,
            stock=10,
            dimensions={"height": 5.5, "width": 3.2, "depth": 2.8},
            weight=2.3
        ))
        
        catalog.add_product(Product(
            id="002",
            name="Vintage Shower Head",
            description="Classic bronze shower head with adjustable settings",
            category=ProductCategory.SHOWER_HEADS,
            price=179.99,
            stock=15,
            dimensions={"height": 6.0, "width": 6.0, "depth": 3.5},
            weight=1.8
        ))
    except ValueError as e:
        print(f"Error adding product: {e}")
    
    # Search products
    results = catalog.search_products("bronze")
    print(f"Found {len(results)} products matching 'bronze'")
    
    # Get products by category
    faucets = catalog.get_products_by_category(ProductCategory.FAUCETS)
    print(f"Found {len(faucets)} faucets in catalog")
```
