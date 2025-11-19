"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: Illustrate how to implement a product filtering system for an online store, allowing users to browse items like sweatshirts and patches, similar to the product categories on Simplymente Airsoft.
Generated: DETERMINISTIC_9f71785d4b458a7f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from enum import Enum
from dataclasses import dataclass

class ProductCategory(Enum):
    """Enum representing product categories."""
    SWEATSHIRT = "Sweatshirt"
    PATCH = "Patch"
    OTHER = "Other"

@dataclass
class Product:
    """Data class representing a product."""
    id: str
    name: str
    price: float
    category: ProductCategory
    description: str
    in_stock: bool
    tags: List[str]

class ProductFilter:
    """Class for filtering products based on various criteria."""
    
    def __init__(self, products: List[Product]):
        """Initialize with a list of products."""
        self.products = products
    
    def filter_by_category(self, category: ProductCategory) -> List[Product]:
        """Filter products by category."""
        return [product for product in self.products if product.category == category]
    
    def filter_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        """Filter products within a price range."""
        if min_price < 0 or max_price < 0:
            raise ValueError("Price cannot be negative")
        if min_price > max_price:
            raise ValueError("Min price cannot be greater than max price")
            
        return [product for product in self.products if min_price <= product.price <= max_price]
    
    def filter_in_stock(self) -> List[Product]:
        """Filter products that are in stock."""
        return [product for product in self.products if product.in_stock]
    
    def filter_by_tags(self, tags: List[str]) -> List[Product]:
        """Filter products that have all specified tags."""
        if not tags:
            return self.products
        return [product for product in self.products if all(tag in product.tags for tag in tags)]
    
    def combined_filter(
        self,
        category: Optional[ProductCategory] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        in_stock_only: bool = False,
        tags: Optional[List[str]] = None
    ) -> List[Product]:
        """
        Apply multiple filters simultaneously.
        
        Args:
            category: Filter by product category
            min_price: Minimum price filter
            max_price: Maximum price filter
            in_stock_only: Only include in-stock items
            tags: Filter by tags
            
        Returns:
            List of filtered products
        """
        filtered_products = self.products
        
        if category is not None:
            filtered_products = self.filter_by_category(category)
        
        if min_price is not None or max_price is not None:
            min_p = min_price if min_price is not None else 0
            max_p = max_price if max_price is not None else float('inf')
            filtered_products = [p for p in filtered_products if min_p <= p.price <= max_p]
        
        if in_stock_only:
            filtered_products = [p for p in filtered_products if p.in_stock]
        
        if tags:
            filtered_products = [p for p in filtered_products if all(tag in p.tags for tag in tags)]
        
        return filtered_products

# Example usage
if __name__ == "__main__":
    # Sample products
    products = [
        Product(
            id="1",
            name="Tactical Sweatshirt",
            price=39.99,
            category=ProductCategory.SWEATSHIRT,
            description="Comfortable tactical sweatshirt",
            in_stock=True,
            tags=["tactical", "winter"]
        ),
        Product(
            id="2",
            name="Camo Patch",
            price=4.99,
            category=ProductCategory.PATCH,
            description="Camouflage design patch",
            in_stock=True,
            tags=["camo", "accessory"]
        ),
        Product(
            id="3",
            name="Premium Sweatshirt",
            price=59.99,
            category=ProductCategory.SWEATSHIRT,
            description="High-quality premium sweatshirt",
            in_stock=False,
            tags=["premium", "limited"]
        ),
    ]
    
    # Initialize filter
    product_filter = ProductFilter(products)
    
    # Example filters
    print("All sweatshirts:")
    for product in product_filter.filter_by_category(ProductCategory.SWEATSHIRT):
        print(f"- {product.name} (${product.price})")
    
    print("\nProducts under $50:")
    for product in product_filter.filter_by_price_range(0, 50):
        print(f"- {product.name} (${product.price})")
    
    print("\nIn-stock products with 'tactical' tag:")
    filtered = product_filter.combined_filter(
        in_stock_only=True,
        tags=["tactical"]
    )
    for product in filtered:
        print(f"- {product.name} (${product.price})")
```
