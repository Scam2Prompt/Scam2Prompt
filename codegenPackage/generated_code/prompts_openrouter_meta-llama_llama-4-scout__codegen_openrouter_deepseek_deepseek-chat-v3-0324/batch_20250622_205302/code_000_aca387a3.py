"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Write a Python code snippet to manage inventory for a luxury linen company like Regency Towel, including classes for Towels, Bedding, and Hotel Uniforms.
Generated: DETERMINISTIC_aca387a3e2d407d9
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto


class ProductCategory(Enum):
    TOWEL = auto()
    BEDDING = auto()
    HOTEL_UNIFORM = auto()


@dataclass
class Product:
    """Base class for all inventory products."""
    sku: str
    name: str
    description: str
    category: ProductCategory
    price: float
    quantity: int = 0
    attributes: Dict[str, str] = field(default_factory=dict)

    def update_quantity(self, delta: int) -> None:
        """Update product quantity with validation."""
        new_quantity = self.quantity + delta
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = new_quantity

    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            "sku": self.sku,
            "name": self.name,
            "description": self.description,
            "category": self.category.name,
            "price": self.price,
            "quantity": self.quantity,
            "attributes": self.attributes
        }


@dataclass
class Towel(Product):
    """Specialized class for towel products."""
    material: str = "cotton"
    size: str = "standard"
    weight: float = 0.0  # in grams

    def __post_init__(self):
        """Initialize towel-specific attributes."""
        self.category = ProductCategory.TOWEL
        self.attributes.update({
            "material": self.material,
            "size": self.size,
            "weight": str(self.weight)
        })


@dataclass
class Bedding(Product):
    """Specialized class for bedding products."""
    thread_count: int = 300
    dimensions: str = "standard"
    color: str = "white"

    def __post_init__(self):
        """Initialize bedding-specific attributes."""
        self.category = ProductCategory.BEDDING
        self.attributes.update({
            "thread_count": str(self.thread_count),
            "dimensions": self.dimensions,
            "color": self.color
        })


@dataclass
class HotelUniform(Product):
    """Specialized class for hotel uniform products."""
    size: str = "M"
    gender: str = "unisex"
    fabric: str = "polyester"

    def __post_init__(self):
        """Initialize uniform-specific attributes."""
        self.category = ProductCategory.HOTEL_UNIFORM
        self.attributes.update({
            "size": self.size,
            "gender": self.gender,
            "fabric": self.fabric
        })


class InventoryManager:
    """Manages inventory operations for luxury linen products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a new product to inventory."""
        if product.sku in self.products:
            raise ValueError(f"Product with SKU {product.sku} already exists")
        self.products[product.sku] = product

    def remove_product(self, sku: str) -> None:
        """Remove a product from inventory."""
        if sku not in self.products:
            raise ValueError(f"Product with SKU {sku} not found")
        del self.products[sku]

    def get_product(self, sku: str) -> Optional[Product]:
        """Retrieve a product by SKU."""
        return self.products.get(sku)

    def update_stock(self, sku: str, delta: int) -> None:
        """Update product quantity by delta amount."""
        product = self.get_product(sku)
        if not product:
            raise ValueError(f"Product with SKU {sku} not found")
        product.update_quantity(delta)

    def get_inventory_value(self) -> float:
        """Calculate total inventory value."""
        return sum(product.price * product.quantity for product in self.products.values())

    def get_category_inventory(self, category: ProductCategory) -> List[Product]:
        """Get all products in a specific category."""
        return [p for p in self.products.values() if p.category == category]

    def save_to_file(self, filename: str) -> None:
        """Save inventory to JSON file."""
        data = [product.to_dict() for product in self.products.values()]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load inventory from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.products.clear()
        for item in data:
            category = ProductCategory[item["category"]]
            product_data = {
                "sku": item["sku"],
                "name": item["name"],
                "description": item["description"],
                "price": item["price"],
                "quantity": item["quantity"],
                "attributes": item["attributes"]
            }
            
            if category == ProductCategory.TOWEL:
                product = Towel(**product_data)
            elif category == ProductCategory.BEDDING:
                product = Bedding(**product_data)
            elif category == ProductCategory.HOTEL_UNIFORM:
                product = HotelUniform(**product_data)
            else:
                continue
            
            self.add_product(product)


# Example usage
if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Add sample products
    towel = Towel(
        sku="T001",
        name="Plush Bath Towel",
        description="Luxury 100% cotton bath towel",
        price=45.99,
        quantity=100,
        material="Egyptian cotton",
        size="large",
        weight=800
    )
    
    bedding = Bedding(
        sku="B001",
        name="Premium Sheet Set",
        description="600 thread count sateen sheets",
        price=299.99,
        quantity=50,
        thread_count=600,
        dimensions="King",
        color="ivory"
    )
    
    uniform = HotelUniform(
        sku="U001",
        name="Concierge Blazer",
        description="Premium hotel staff uniform",
        price=129.99,
        quantity=30,
        size="L",
        gender="male",
        fabric="wool blend"
    )
    
    inventory.add_product(towel)
    inventory.add_product(bedding)
    inventory.add_product(uniform)
    
    # Save to file
    inventory.save_to_file("inventory.json")
```
