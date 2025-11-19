"""
Generated Code Metadata:
========================
Original URL: https://cm-canada.ca
Prompt: "Generate a Python code snippet to manage inventory for a construction supply company like One World Supply, including product categories such as valves, couplings, and plumbing fixtures."
Generated: DETERMINISTIC_ebaa9e61860a371b
Batch ID: 20250622_212444
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
from dataclasses import dataclass, asdict
import os


@dataclass
class Product:
    """Represents a construction supply product."""
    id: str
    name: str
    category: str  # e.g., 'valve', 'coupling', 'plumbing fixture'
    quantity: int
    price: float
    supplier: str
    minimum_stock_level: int = 10

    def to_dict(self) -> Dict:
        """Convert Product instance to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create Product instance from dictionary."""
        return cls(**data)


class InventoryManager:
    """Manages inventory for construction supply products."""
    
    def __init__(self, data_file: str = 'inventory.json'):
        """Initialize inventory manager with data file."""
        self.data_file = data_file
        self.products: Dict[str, Product] = {}
        self.load_inventory()

    def add_product(self, product: Product) -> None:
        """Add a new product to inventory."""
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
        self._save_inventory()

    def update_product(self, product_id: str, quantity: Optional[int] = None, 
                      price: Optional[float] = None) -> None:
        """Update product quantity or price."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price
        
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

    def get_low_stock_products(self) -> List[Product]:
        """Get products below minimum stock level."""
        return [p for p in self.products.values() 
                if p.quantity < p.minimum_stock_level]

    def get_products_by_category(self, category: str) -> List[Product]:
        """Get all products in a specific category."""
        return [p for p in self.products.values() 
                if p.category.lower() == category.lower()]

    def _save_inventory(self) -> None:
        """Save inventory to file."""
        with open(self.data_file, 'w') as f:
            json.dump(
                {pid: p.to_dict() for pid, p in self.products.items()}, 
                f, 
                indent=4
            )

    def load_inventory(self) -> None:
        """Load inventory from file."""
        if not os.path.exists(self.data_file):
            return
            
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.products = {
                    pid: Product.from_dict(p_data) 
                    for pid, p_data in data.items()
                }
        except json.JSONDecodeError:
            raise ValueError("Invalid inventory file format")
        except Exception as e:
            raise ValueError(f"Error loading inventory: {str(e)}")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self._save_inventory()


# Example usage
if __name__ == "__main__":
    with InventoryManager() as manager:
        # Add sample products
        try:
            manager.add_product(Product(
                id="V001",
                name="Ball Valve",
                category="valve",
                quantity=25,
                price=12.99,
                supplier="ValveCo"
            ))
            
            manager.add_product(Product(
                id="C001",
                name="PVC Coupling",
                category="coupling",
                quantity=8,  # Below minimum stock level
                price=4.50,
                supplier="PipeMasters"
            ))
            
            manager.add_product(Product(
                id="P001",
                name="Faucet Set",
                category="plumbing fixture",
                quantity=15,
                price=45.75,
                supplier="PlumbRight"
            ))
            
            # Get low stock products
            low_stock = manager.get_low_stock_products()
            print("Low stock items:")
            for product in low_stock:
                print(f"{product.name} ({product.quantity} remaining)")
            
            # Get products by category
            valves = manager.get_products_by_category("valve")
            print("\nValves in inventory:")
            for valve in valves:
                print(valve.name)
                
        except ValueError as e:
            print(f"Error: {str(e)}")
```
