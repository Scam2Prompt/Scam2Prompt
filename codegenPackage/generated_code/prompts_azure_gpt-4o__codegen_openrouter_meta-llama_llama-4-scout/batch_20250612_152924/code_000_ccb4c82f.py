"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Write code to simulate a pharmacy inventory management system tailored for independent pharmacies, incorporating features like purchasing power optimization and flexible operational systems as described by PharmaChoice Canada.
Generated: DETERMINISTIC_ccb4c82fc84f8eeb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pharmacy_inventory_management_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class ProductStatus(Enum):
    """Product status"""
    IN_STOCK = 1
    OUT_OF_STOCK = 2
    LOW_STOCK = 3

@dataclass
class Product:
    """Product data class"""
    id: int
    name: str
    quantity: int
    price: float
    status: ProductStatus

class PharmacyInventory:
    """Pharmacy inventory management system"""
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.suppliers: Dict[str, Dict[str, str]] = {}

    def add_product(self, product: Product):
        """Add product to inventory"""
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """Remove product from inventory"""
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product not found")

    def update_product_quantity(self, product_id: int, quantity: int):
        """Update product quantity"""
        if product_id in self.products:
            self.products[product_id].quantity = quantity
            if quantity < 5:
                self.products[product_id].status = ProductStatus.LOW_STOCK
            elif quantity == 0:
                self.products[product_id].status = ProductStatus.OUT_OF_STOCK
            else:
                self.products[product_id].status = ProductStatus.IN_STOCK
        else:
            raise ValueError("Product not found")

    def add_supplier(self, supplier_name: str, supplier_info: Dict[str, str]):
        """Add supplier"""
        self.suppliers[supplier_name] = supplier_info

    def remove_supplier(self, supplier_name: str):
        """Remove supplier"""
        if supplier_name in self.suppliers:
            del self.suppliers[supplier_name]
        else:
            raise ValueError("Supplier not found")

    def optimize_purchasing_power(self):
        """Optimize purchasing power"""
        # Simple optimization strategy: order products with low stock first
        low_stock_products = [product for product in self.products.values() if product.status == ProductStatus.LOW_STOCK]
        low_stock_products.sort(key=lambda product: product.quantity)
        return low_stock_products

    def generate_report(self):
        """Generate inventory report"""
        report = []
        for product in self.products.values():
            report.append({
                "id": product.id,
                "name": product.name,
                "quantity": product.quantity,
                "price": product.price,
                "status": product.status.name
            })
        return report

def main():
    pharmacy = PharmacyInventory()

    # Add products
    product1 = Product(1, "Product A", 10, 100.0, ProductStatus.IN_STOCK)
    product2 = Product(2, "Product B", 3, 50.0, ProductStatus.LOW_STOCK)
    pharmacy.add_product(product1)
    pharmacy.add_product(product2)

    # Add suppliers
    supplier1 = {"name": "Supplier 1", "contact": "123-456-7890"}
    pharmacy.add_supplier("Supplier 1", supplier1)

    # Optimize purchasing power
    low_stock_products = pharmacy.optimize_purchasing_power()
    print("Low stock products:")
    for product in low_stock_products:
        print(product)

    # Generate report
    report = pharmacy.generate_report()
    print("\nInventory report:")
    for product in report:
        print(product)

    # Update product quantity
    pharmacy.update_product_quantity(2, 0)
    print("\nUpdated product quantity:")
    print(pharmacy.products[2])

if __name__ == "__main__":
    main()
```
