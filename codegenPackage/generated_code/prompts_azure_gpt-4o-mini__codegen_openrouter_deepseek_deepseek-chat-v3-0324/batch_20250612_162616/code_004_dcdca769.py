"""
Generated Code Metadata:
========================
Original URL: https://zellerscanada.ca
Prompt: Illustrate how to implement a search functionality for an e-commerce platform that categorizes products like Zellers does, including features for limited-time offers.
Generated: DETERMINISTIC_dcdca769c26c74fc
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum
import json

class ProductCategory(Enum):
    ELECTRONICS = "Electronics"
    CLOTHING = "Clothing"
    GROCERY = "Grocery"
    HOME = "Home"
    TOYS = "Toys"

class Product:
    def __init__(self, id: int, name: str, price: float, category: ProductCategory, 
                 description: str = "", offer_end_time: Optional[datetime] = None):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        self.offer_end_time = offer_end_time

    def is_on_offer(self) -> bool:
        """Check if the product is currently on a limited-time offer."""
        if self.offer_end_time is None:
            return False
        return datetime.now() < self.offer_end_time

    def to_dict(self) -> Dict:
        """Convert product to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category.value,
            "description": self.description,
            "is_on_offer": self.is_on_offer(),
            "offer_end_time": self.offer_end_time.isoformat() if self.offer_end_time else None
        }

class ProductInventory:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a product to the inventory."""
        self.products.append(product)

    def search_products(self, query: str = "", category: Optional[ProductCategory] = None, 
                        on_offer: bool = False) -> List[Product]:
        """
        Search products by query, category, and offer status.
        
        Args:
            query: Search term to match against product name/description
            category: Filter by product category
            on_offer: Only return products with active offers
            
        Returns:
            List of matching products
        """
        results = self.products
        
        if query:
            query = query.lower()
            results = [p for p in results 
                      if query in p.name.lower() or query in p.description.lower()]
        
        if category is not None:
            results = [p for p in results if p.category == category]
            
        if on_offer:
            results = [p for p in results if p.is_on_offer()]
            
        return results

    def get_categories(self) -> List[ProductCategory]:
        """Get all unique product categories in inventory."""
        return list(set(p.category for p in self.products))

    def to_json(self) -> str:
        """Serialize inventory to JSON."""
        return json.dumps([p.to_dict() for p in self.products], indent=2)

# Example usage
if __name__ == "__main__":
    # Create inventory
    inventory = ProductInventory()
    
    # Add sample products
    inventory.add_product(Product(
        id=1,
        name="Smart TV",
        price=799.99,
        category=ProductCategory.ELECTRONICS,
        description="55-inch 4K Smart TV",
        offer_end_time=datetime.now() + timedelta(days=3)
    ))
    
    inventory.add_product(Product(
        id=2,
        name="T-Shirt",
        price=19.99,
        category=ProductCategory.CLOTHING,
        description="Cotton crew neck t-shirt"
    ))
    
    inventory.add_product(Product(
        id=3,
        name="Coffee Maker",
        price=49.99,
        category=ProductCategory.HOME,
        description="12-cup programmable coffee maker",
        offer_end_time=datetime.now() + timedelta(hours=12)
    ))
    
    # Search examples
    print("All products:")
    print(inventory.to_json())
    
    print("\nElectronics products:")
    electronics = inventory.search_products(category=ProductCategory.ELECTRONICS)
    print(json.dumps([p.to_dict() for p in electronics], indent=2))
    
    print("\nProducts on offer:")
    offers = inventory.search_products(on_offer=True)
    print(json.dumps([p.to_dict() for p in offers], indent=2))
    
    print("\nSearch for 'coffee':")
    coffee = inventory.search_products(query="coffee")
    print(json.dumps([p.to_dict() for p in coffee], indent=2))
```
