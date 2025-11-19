"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Generate a code snippet for an inventory management system that tracks high-quality hardware products like hinges, locks, and latches, similar to those offered by DEVA.
Generated: DETERMINISTIC_259af4a66f9d96cd
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Inventory Management System for High-Quality Hardware Products
"""

from dataclasses import dataclass
from typing import List, Optional
import datetime
import csv
import os
from enum import Enum, auto


class ProductCategory(Enum):
    HINGE = auto()
    LOCK = auto()
    LATCH = auto()
    OTHER = auto()


@dataclass
class Product:
    sku: str
    name: str
    category: ProductCategory
    quantity: int
    price: float
    weight: float  # in grams
    dimensions: str  # e.g., "100x50x20mm"
    material: str
    last_restocked: datetime.date
    minimum_stock: int = 10

    def needs_restock(self) -> bool:
        return self.quantity <= self.minimum_stock


class InventoryManager:
    def __init__(self, data_file: str = "inventory.csv"):
        self.products: List[Product] = []
        self.data_file = data_file
        self._load_inventory()

    def _load_inventory(self) -> None:
        if not os.path.exists(self.data_file):
            return

        with open(self.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    self.products.append(Product(
                        sku=row['sku'],
                        name=row['name'],
                        category=ProductCategory[row['category']],
                        quantity=int(row['quantity']),
                        price=float(row['price']),
                        weight=float(row['weight']),
                        dimensions=row['dimensions'],
                        material=row['material'],
                        last_restocked=datetime.datetime.strptime(
                            row['last_restocked'], '%Y-%m-%d').date(),
                        minimum_stock=int(row['minimum_stock'])
                    ))
                except (KeyError, ValueError) as e:
                    print(f"Error loading product {row.get('sku', 'unknown')}: {e}")

    def _save_inventory(self) -> None:
        with open(self.data_file, mode='w', newline='') as file:
            fieldnames = [
                'sku', 'name', 'category', 'quantity', 'price', 'weight',
                'dimensions', 'material', 'last_restocked', 'minimum_stock'
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in self.products:
                writer.writerow({
                    'sku': product.sku,
                    'name': product.name,
                    'category': product.category.name,
                    'quantity': product.quantity,
                    'price': product.price,
                    'weight': product.weight,
                    'dimensions': product.dimensions,
                    'material': product.material,
                    'last_restocked': product.last_restocked.strftime('%Y-%m-%d'),
                    'minimum_stock': product.minimum_stock
                })

    def add_product(self, product: Product) -> None:
        if any(p.sku == product.sku for p in self.products):
            raise ValueError(f"Product with SKU {product.sku} already exists")
        self.products.append(product)
        self._save_inventory()

    def update_product(self, sku: str, quantity: Optional[int] = None,
                       price: Optional[float] = None) -> None:
        product = self.find_product(sku)
        if not product:
            raise ValueError(f"Product with SKU {sku} not found")

        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price

        product.last_restocked = datetime.date.today()
        self._save_inventory()

    def find_product(self, sku: str) -> Optional[Product]:
        for product in self.products:
            if product.sku == sku:
                return product
        return None

    def get_low_stock_products(self) -> List[Product]:
        return [p for p in self.products if p.needs_restock()]

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        return [p for p in self.products if p.category == category]

    def delete_product(self, sku: str) -> None:
        product = self.find_product(sku)
        if not product:
            raise ValueError(f"Product with SKU {sku} not found")
        self.products.remove(product)
        self._save_inventory()


# Example usage
if __name__ == "__main__":
    inventory = InventoryManager()

    # Add sample products
    try:
        inventory.add_product(Product(
            sku="HNG-001",
            name="Stainless Steel Hinge",
            category=ProductCategory.HINGE,
            quantity=15,
            price=4.99,
            weight=150,
            dimensions="100x50x3mm",
            material="Stainless Steel",
            last_restocked=datetime.date.today(),
            minimum_stock=5
        ))

        inventory.add_product(Product(
            sku="LCK-001",
            name="Heavy Duty Door Lock",
            category=ProductCategory.LOCK,
            quantity=8,
            price=24.99,
            weight=450,
            dimensions="120x80x25mm",
            material="Brass",
            last_restocked=datetime.date.today(),
            minimum_stock=10
        ))
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Check low stock
    low_stock = inventory.get_low_stock_products()
    print(f"Products needing restock: {len(low_stock)}")

    # Update product
    try:
        inventory.update_product("LCK-001", quantity=12)
    except ValueError as e:
        print(f"Error updating product: {e}")
```
