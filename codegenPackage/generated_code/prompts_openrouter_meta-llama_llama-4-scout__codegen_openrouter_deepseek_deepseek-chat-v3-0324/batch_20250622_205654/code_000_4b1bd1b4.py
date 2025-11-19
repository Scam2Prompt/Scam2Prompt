"""
Generated Code Metadata:
========================
Original URL: https://shahkarco.com
Prompt: "Write a Python code snippet to manage an e-commerce inventory system for clothes racks, including product variations and pricing, similar to shahkarco.com."
Generated: DETERMINISTIC_4b1bd1b4b306e291
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class Size(Enum):
    """Available clothing sizes."""
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"


class Color(Enum):
    """Available clothing colors."""
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    BLACK = "Black"
    WHITE = "White"
    GRAY = "Gray"


@dataclass
class ProductVariant:
    """Represents a specific variant of a product."""
    size: Size
    color: Color
    price: float
    stock_quantity: int = 0
    sku: Optional[str] = None


@dataclass
class Product:
    """Represents a product in the inventory."""
    id: str
    name: str
    description: str
    category: str
    variants: List[ProductVariant] = field(default_factory=list)


class InventoryManager:
    """Manages the e-commerce inventory for clothing racks."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> None:
        """Add a product to the inventory."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists.")
        self.products[product.id] = product
    
    def remove_product(self, product_id: str) -> None:
        """Remove a product from the inventory."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        del self.products[product_id]
    
    def update_product(self, product_id: str, **kwargs) -> None:
        """Update product details."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise AttributeError(f"Product has no attribute {key}")
    
    def add_variant(self, product_id: str, variant: ProductVariant) -> None:
        """Add a variant to a product."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        product = self.products[product_id]
        for existing_variant in product.variants:
            if (existing_variant.size == variant.size and 
                existing_variant.color == variant.color):
                raise ValueError("Variant with same size and color already exists.")
        
        product.variants.append(variant)
    
    def update_variant_stock(self, product_id: str, size: Size, color: Color, quantity: int) -> None:
        """Update stock quantity for a product variant."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        
        product = self.products[product_id]
        for variant in product.variants:
            if variant.size == size and variant.color == color:
                variant.stock_quantity = quantity
                return
        
        raise ValueError("Variant not found.")
    
    def get_product(self, product_id: str) -> Product:
        """Get a product by ID."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found.")
        return self.products[product_id]
    
    def list_products(self) -> List[Product]:
        """List all products in inventory."""
        return list(self.products.values())
    
    def search_products(self, query: str) -> List[Product]:
        """Search products by name or description."""
        query = query.lower()
        return [
            product for product in self.products.values()
            if query in product.name.lower() or query in product.description.lower()
        ]
    
    def save_to_file(self, filename: str) -> None:
        """Save inventory to a JSON file."""
        data = {
            "products": [
                {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "category": product.category,
                    "variants": [
                        {
                            "size": variant.size.value,
                            "color": variant.color.value,
                            "price": variant.price,
                            "stock_quantity": variant.stock_quantity,
                            "sku": variant.sku
                        }
                        for variant in product.variants
                    ]
                }
                for product in self.products.values()
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.products = {}
        for product_data in data["products"]:
            variants = [
                ProductVariant(
                    size=Size(variant["size"]),
                    color=Color(variant["color"]),
                    price=variant["price"],
                    stock_quantity=variant["stock_quantity"],
                    sku=variant.get("sku")
                )
                for variant in product_data["variants"]
            ]
            
            product = Product(
                id=product_data["id"],
                name=product_data["name"],
                description=product_data["description"],
                category=product_data["category"],
                variants=variants
            )
            
            self.products[product.id] = product


# Example usage
if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Create a product
    t_shirt = Product(
        id="tshirt001",
        name="Premium Cotton T-Shirt",
        description="High quality cotton t-shirt for everyday wear",
        category="T-Shirts"
    )
    
    # Add variants
    t_shirt_variant1 = ProductVariant(
        size=Size.M,
        color=Color.BLACK,
        price=19.99,
        stock_quantity=50,
        sku="TSHIRT001-M-BLK"
    )
    
    t_shirt_variant2 = ProductVariant(
        size=Size.L,
        color=Color.WHITE,
        price=19.99,
        stock_quantity=30,
        sku="TSHIRT001-L-WHT"
    )
    
    # Add product to inventory
    inventory.add_product(t_shirt)
    inventory.add_variant(t_shirt.id, t_shirt_variant1)
    inventory.add_variant(t_shirt.id, t_shirt_variant2)
    
    # Save inventory to file
    inventory.save_to_file("inventory.json")
    
    # Load inventory from file
    new_inventory = InventoryManager()
    new_inventory.load_from_file("inventory.json")
    
    # Print loaded products
    for product in new_inventory.list_products():
        print(f"Product: {product.name}")
        for variant in product.variants:
            print(f"  Variant: {variant.size.value}, {variant.color.value} - ${variant.price} (Stock: {variant.stock_quantity})")
```
