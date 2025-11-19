"""
Generated Code Metadata:
========================
Original URL: https://tudulcepecado.cl
Prompt: Write a Python script to manage an e-commerce inventory system for a sex toy store like Tu Dulce Pecado, including product categorization and pricing.
Generated: DETERMINISTIC_f221a764ac983357
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum, auto
import uuid


class ProductCategory(Enum):
    """Enumeration of product categories."""
    VIBRATORS = auto()
    DILDOS = auto()
    ANAL_TOYS = auto()
    BDSM = auto()
    LUBRICANTS = auto()
    COSTUMES = auto()
    OTHER = auto()


@dataclass
class Product:
    """Class representing a product in inventory."""
    id: str
    name: str
    description: str
    category: ProductCategory
    price: float
    quantity: int
    is_adult: bool = True
    is_bestseller: bool = False

    def to_dict(self) -> Dict:
        """Convert Product instance to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create Product instance from dictionary."""
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            category=ProductCategory[data['category']],
            price=data['price'],
            quantity=data['quantity'],
            is_adult=data.get('is_adult', True),
            is_bestseller=data.get('is_bestseller', False)
        )


class InventoryManager:
    """Class to manage e-commerce inventory operations."""
    
    def __init__(self, inventory_file: str = 'inventory.json'):
        """Initialize inventory manager with storage file."""
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Product] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    data = json.load(f)
                    self.inventory = {
                        product_id: Product.from_dict(product_data)
                        for product_id, product_data in data.items()
                    }
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading inventory: {str(e)}")

    def _save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(
                    {product_id: product.to_dict() 
                     for product_id, product in self.inventory.items()},
                    f,
                    indent=4
                )
        except IOError as e:
            raise Exception(f"Error saving inventory: {str(e)}")

    def add_product(
        self,
        name: str,
        description: str,
        category: ProductCategory,
        price: float,
        quantity: int,
        is_adult: bool = True,
        is_bestseller: bool = False
    ) -> str:
        """Add a new product to inventory."""
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        product_id = str(uuid.uuid4())
        product = Product(
            id=product_id,
            name=name,
            description=description,
            category=category,
            price=price,
            quantity=quantity,
            is_adult=is_adult,
            is_bestseller=is_bestseller
        )
        
        self.inventory[product_id] = product
        self._save_inventory()
        return product_id

    def update_product(
        self,
        product_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        category: Optional[ProductCategory] = None,
        price: Optional[float] = None,
        quantity: Optional[int] = None,
        is_adult: Optional[bool] = None,
        is_bestseller: Optional[bool] = None
    ) -> None:
        """Update existing product details."""
        if product_id not in self.inventory:
            raise ValueError("Product not found")
        
        product = self.inventory[product_id]
        
        if name is not None:
            product.name = name
        if description is not None:
            product.description = description
        if category is not None:
            product.category = category
        if price is not None:
            if price <= 0:
                raise ValueError("Price must be positive")
            product.price = price
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            product.quantity = quantity
        if is_adult is not None:
            product.is_adult = is_adult
        if is_bestseller is not None:
            product.is_bestseller = is_bestseller
            
        self._save_inventory()

    def remove_product(self, product_id: str) -> None:
        """Remove product from inventory."""
        if product_id not in self.inventory:
            raise ValueError("Product not found")
        
        del self.inventory[product_id]
        self._save_inventory()

    def get_product(self, product_id: str) -> Product:
        """Get product by ID."""
        if product_id not in self.inventory:
            raise ValueError("Product not found")
        return self.inventory[product_id]

    def list_products(self, category: Optional[ProductCategory] = None) -> List[Product]:
        """List all products or filter by category."""
        products = list(self.inventory.values())
        if category is not None:
            products = [p for p in products if p.category == category]
        return products

    def update_stock(self, product_id: str, quantity_change: int) -> None:
        """Update product quantity (add or subtract)."""
        if product_id not in self.inventory:
            raise ValueError("Product not found")
        
        new_quantity = self.inventory[product_id].quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        self.inventory[product_id].quantity = new_quantity
        self._save_inventory()

    def search_products(
        self,
        query: str,
        category: Optional[ProductCategory] = None
    ) -> List[Product]:
        """Search products by name or description."""
        query = query.lower()
        products = self.list_products(category)
        return [
            p for p in products
            if query in p.name.lower() or query in p.description.lower()
        ]


# Example usage
if __name__ == "__main__":
    try:
        manager = InventoryManager()
        
        # Add a new product
        product_id = manager.add_product(
            name="Premium Vibrator",
            description="High-quality silicone vibrator with multiple settings",
            category=ProductCategory.VIBRATORS,
            price=49.99,
            quantity=50,
            is_bestseller=True
        )
        
        # Update product
        manager.update_product(
            product_id=product_id,
            price=45.99,
            quantity=40
        )
        
        # List all vibrators
        vibrators = manager.list_products(ProductCategory.VIBRATORS)
        print(f"Vibrators in stock: {len(vibrators)}")
        
        # Search products
        results = manager.search_products("silicone")
        print(f"Found {len(results)} matching products")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
