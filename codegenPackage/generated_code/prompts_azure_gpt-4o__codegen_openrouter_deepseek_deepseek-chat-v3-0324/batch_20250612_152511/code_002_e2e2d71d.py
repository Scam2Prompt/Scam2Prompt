"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Generate a Python script to manage inventory for digital products like "5300 جم زپتو" and "35000 جم کلش رویال," ensuring stock updates based on user purchases.
Generated: DETERMINISTIC_e2e2d71d1cf2058c
Batch ID: 20250612_152511
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
from typing import Dict, List, Optional

class DigitalProduct:
    """Represents a digital product with name and stock quantity."""
    def __init__(self, name: str, price: str, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict:
        """Convert product to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'DigitalProduct':
        """Create product from dictionary."""
        return cls(data["name"], data["price"], data["stock"])

class InventoryManager:
    """Manages inventory of digital products."""
    def __init__(self, inventory_file: str = "inventory.json"):
        self.inventory_file = inventory_file
        self.products: Dict[str, DigitalProduct] = {}
        self._load_inventory()

    def _load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.products = {
                        product_data["name"]: DigitalProduct.from_dict(product_data)
                        for product_data in data
                    }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
            self.products = {}

    def _save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.inventory_file, 'w', encoding='utf-8') as f:
                json.dump(
                    [product.to_dict() for product in self.products.values()],
                    f,
                    indent=4,
                    ensure_ascii=False
                )
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def add_product(self, name: str, price: str, stock: int) -> None:
        """Add a new product to inventory."""
        if name in self.products:
            raise ValueError(f"Product '{name}' already exists")
        self.products[name] = DigitalProduct(name, price, stock)
        self._save_inventory()

    def update_stock(self, name: str, quantity: int) -> None:
        """Update stock quantity for a product."""
        if name not in self.products:
            raise ValueError(f"Product '{name}' not found")
        if self.products[name].stock + quantity < 0:
            raise ValueError("Insufficient stock")
        self.products[name].stock += quantity
        self._save_inventory()

    def purchase_product(self, name: str, quantity: int) -> None:
        """Process a product purchase."""
        self.update_stock(name, -quantity)

    def get_product(self, name: str) -> Optional[DigitalProduct]:
        """Get product by name."""
        return self.products.get(name)

    def list_products(self) -> List[Dict]:
        """List all products."""
        return [product.to_dict() for product in self.products.values()]

def main():
    """Example usage of the inventory manager."""
    inventory = InventoryManager()

    # Add sample products if inventory is empty
    if not inventory.list_products():
        inventory.add_product("5300 جم زپتو", "5300 جم", 100)
        inventory.add_product("35000 جم کلش رویال", "35000 جم", 50)

    # Example purchase
    try:
        inventory.purchase_product("5300 جم زپتو", 1)
        print("Purchase successful!")
    except ValueError as e:
        print(f"Purchase failed: {e}")

    # Display current inventory
    print("\nCurrent Inventory:")
    for product in inventory.list_products():
        print(f"{product['name']} - Price: {product['price']} - Stock: {product['stock']}")

if __name__ == "__main__":
    main()
```
