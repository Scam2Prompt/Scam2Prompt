"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Write a Python script to manage inventory for a menuiserie distribution company like Distribution Menuiserie, including classes for products (e.g., Fenêtres, Portes, Volets) and methods for tracking stock levels."
Generated: DETERMINISTIC_5ba35bc78ec29057
Batch ID: 20250622_205436
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
from enum import Enum, auto


class ProductCategory(Enum):
    """Enumeration of product categories."""
    WINDOW = auto()  # Fenêtres
    DOOR = auto()    # Portes
    SHUTTER = auto() # Volets


@dataclass
class Product:
    """Class representing a product in inventory."""
    id: str
    name: str
    category: ProductCategory
    price: float
    quantity: int
    description: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convert Product instance to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create Product instance from dictionary."""
        return cls(
            id=data['id'],
            name=data['name'],
            category=ProductCategory[data['category']],
            price=data['price'],
            quantity=data['quantity'],
            description=data.get('description')
        )


class InventoryManager:
    """Class to manage inventory operations."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """Initialize inventory manager with storage file path."""
        self.file_path = file_path
        self.products: Dict[str, Product] = {}
        self.load_inventory()

    def add_product(self, product: Product) -> None:
        """Add a new product to inventory."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
        self._save_inventory()

    def update_product(self, product_id: str, quantity: int = None, 
                       price: float = None, description: str = None) -> None:
        """Update existing product information."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price
        if description is not None:
            product.description = description
        
        self._save_inventory()

    def remove_product(self, product_id: str) -> None:
        """Remove product from inventory."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]
        self._save_inventory()

    def get_product(self, product_id: str) -> Product:
        """Get product by ID."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        return self.products[product_id]

    def list_products(self, category: Optional[ProductCategory] = None) -> List[Product]:
        """List all products, optionally filtered by category."""
        if category:
            return [p for p in self.products.values() if p.category == category]
        return list(self.products.values())

    def _save_inventory(self) -> None:
        """Save inventory to file."""
        data = {
            'products': [product.to_dict() for product in self.products.values()]
        }
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def load_inventory(self) -> None:
        """Load inventory from file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.products = {
                    p['id']: Product.from_dict(p) 
                    for p in data.get('products', [])
                }
        except FileNotFoundError:
            self.products = {}
        except json.JSONDecodeError:
            raise ValueError("Inventory file is corrupted")

    def get_low_stock_products(self, threshold: int = 5) -> List[Product]:
        """Get products with quantity below threshold."""
        return [p for p in self.products.values() if p.quantity < threshold]


# Example usage
if __name__ == "__main__":
    try:
        manager = InventoryManager()
        
        # Add sample products
        manager.add_product(Product(
            id="win001",
            name="Fenêtre PVC Blanche",
            category=ProductCategory.WINDOW,
            price=350.00,
            quantity=10,
            description="Fenêtre en PVC blanc, dimensions 120x90cm"
        ))
        
        manager.add_product(Product(
            id="door001",
            name="Porte d'entrée Bois",
            category=ProductCategory.DOOR,
            price=1200.00,
            quantity=3,
            description="Porte d'entrée en chêne massif"
        ))
        
        # List all windows
        print("Windows in inventory:")
        for product in manager.list_products(ProductCategory.WINDOW):
            print(f"- {product.name} (Qty: {product.quantity})")
        
        # Update product quantity
        manager.update_product("win001", quantity=8)
        
        # Check low stock
        print("\nLow stock products:")
        for product in manager.get_low_stock_products(5):
            print(f"- {product.name} (Qty: {product.quantity})")
            
    except Exception as e:
        print(f"Error occurred: {e}")
```
