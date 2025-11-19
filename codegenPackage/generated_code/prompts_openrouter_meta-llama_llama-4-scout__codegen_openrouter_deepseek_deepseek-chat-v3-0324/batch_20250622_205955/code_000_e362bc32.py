"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Write a Python code snippet to manage an e-commerce inventory system for a beauty store like Eclat, including products such as nail polish, nail art supplies, and eyelash extensions.
Generated: DETERMINISTIC_e362bc32664413e7
Batch ID: 20250622_205955
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
import uuid


@dataclass
class Product:
    """Represents a product in the inventory."""
    id: str
    name: str
    category: str
    price: float
    quantity: int
    description: Optional[str] = None
    brand: Optional[str] = None
    sku: Optional[str] = None


class InventoryManager:
    """Manages the e-commerce inventory system."""
    
    def __init__(self, inventory_file: str = "inventory.json"):
        self.inventory_file = inventory_file
        self.products: Dict[str, Product] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """Load inventory data from file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    data = json.load(f)
                    self.products = {
                        pid: Product(**product_data) 
                        for pid, product_data in data.items()
                    }
        except Exception as e:
            raise Exception(f"Error loading inventory: {str(e)}")

    def _save_inventory(self) -> None:
        """Save inventory data to file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(
                    {pid: asdict(product) for pid, product in self.products.items()},
                    f,
                    indent=2
                )
        except Exception as e:
            raise Exception(f"Error saving inventory: {str(e)}")

    def add_product(
        self,
        name: str,
        category: str,
        price: float,
        quantity: int,
        description: Optional[str] = None,
        brand: Optional[str] = None,
        sku: Optional[str] = None
    ) -> str:
        """Add a new product to inventory."""
        product_id = str(uuid.uuid4())
        product = Product(
            id=product_id,
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            description=description,
            brand=brand,
            sku=sku
        )
        self.products[product_id] = product
        self._save_inventory()
        return product_id

    def update_product(
        self,
        product_id: str,
        name: Optional[str] = None,
        category: Optional[str] = None,
        price: Optional[float] = None,
        quantity: Optional[int] = None,
        description: Optional[str] = None,
        brand: Optional[str] = None,
        sku: Optional[str] = None
    ) -> bool:
        """Update an existing product."""
        if product_id not in self.products:
            return False
        
        product = self.products[product_id]
        if name is not None:
            product.name = name
        if category is not None:
            product.category = category
        if price is not None:
            product.price = price
        if quantity is not None:
            product.quantity = quantity
        if description is not None:
            product.description = description
        if brand is not None:
            product.brand = brand
        if sku is not None:
            product.sku = sku
        
        self._save_inventory()
        return True

    def remove_product(self, product_id: str) -> bool:
        """Remove a product from inventory."""
        if product_id in self.products:
            del self.products[product_id]
            self._save_inventory()
            return True
        return False

    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by ID."""
        return self.products.get(product_id)

    def list_products(self, category: Optional[str] = None) -> List[Product]:
        """List all products or filter by category."""
        if category:
            return [
                product for product in self.products.values() 
                if product.category == category
            ]
        return list(self.products.values())

    def update_stock(self, product_id: str, quantity_change: int) -> bool:
        """Update product stock quantity."""
        if product_id not in self.products:
            return False
        
        new_quantity = self.products[product_id].quantity + quantity_change
        if new_quantity < 0:
            return False
        
        self.products[product_id].quantity = new_quantity
        self._save_inventory()
        return True


# Example usage
if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Add sample products
    nail_polish_id = inventory.add_product(
        name="Gel Nail Polish",
        category="Nail Polish",
        price=12.99,
        quantity=50,
        brand="Eclat",
        description="Long-lasting gel nail polish"
    )
    
    lash_id = inventory.add_product(
        name="Volume Eyelash Extensions",
        category="Eyelashes",
        price=24.99,
        quantity=30,
        brand="Eclat",
        description="Premium volume eyelash extensions"
    )
    
    # Update product
    inventory.update_product(
        product_id=nail_polish_id,
        price=14.99,
        quantity=45
    )
    
    # List products
    print("All Products:")
    for product in inventory.list_products():
        print(f"{product.name} - ${product.price} ({product.quantity} in stock)")
    
    print("\nNail Products:")
    for product in inventory.list_products(category="Nail Polish"):
        print(f"{product.name} - ${product.price}")
```
