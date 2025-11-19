"""
Generated Code Metadata:
========================
Original URL: https://global-group.uk
Prompt: "Write a Python script to manage inventory for a food distribution company like Global Group, including tracking products, shipments, and warehouse locations."
Generated: DETERMINISTIC_7f1d8b53323c4879
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class ProductStatus(str, Enum):
    """Product status"""
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    DISCONTINUED = "discontinued"

@dataclass
class Product:
    """Product details"""
    id: int
    name: str
    description: str
    quantity: int
    status: ProductStatus

@dataclass
class Shipment:
    """Shipment details"""
    id: int
    product_id: int
    shipment_date: datetime
    quantity: int
    warehouse_location: str

@dataclass
class Warehouse:
    """Warehouse details"""
    location: str
    capacity: int
    available_space: int

class InventoryManager:
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.shipments: Dict[int, Shipment] = {}
        self.warehouses: Dict[str, Warehouse] = {}

    def add_product(self, product: Product):
        """Add a product to the inventory"""
        self.products[product.id] = product

    def update_product(self, product_id: int, quantity: int):
        """Update product quantity"""
        if product_id in self.products:
            self.products[product_id].quantity = quantity
        else:
            raise ValueError("Product not found")

    def add_shipment(self, shipment: Shipment):
        """Add a shipment to the inventory"""
        self.shipments[shipment.id] = shipment
        self.update_warehouse_space(shipment.warehouse_location, -shipment.quantity)

    def update_warehouse_space(self, warehouse_location: str, quantity: int):
        """Update warehouse available space"""
        if warehouse_location in self.warehouses:
            self.warehouses[warehouse_location].available_space += quantity
        else:
            raise ValueError("Warehouse not found")

    def add_warehouse(self, warehouse: Warehouse):
        """Add a warehouse to the inventory"""
        self.warehouses[warehouse.location] = warehouse

    def get_product(self, product_id: int) -> Product:
        """Get a product by ID"""
        return self.products.get(product_id)

    def get_shipment(self, shipment_id: int) -> Shipment:
        """Get a shipment by ID"""
        return self.shipments.get(shipment_id)

    def get_warehouse(self, warehouse_location: str) -> Warehouse:
        """Get a warehouse by location"""
        return self.warehouses.get(warehouse_location)

def main():
    # Initialize inventory manager
    inventory_manager = InventoryManager()

    # Add warehouses
    warehouse1 = Warehouse("WH1", 1000, 1000)
    warehouse2 = Warehouse("WH2", 500, 500)
    inventory_manager.add_warehouse(warehouse1)
    inventory_manager.add_warehouse(warehouse2)

    # Add products
    product1 = Product(1, "Product A", "Description A", 100, ProductStatus.IN_STOCK)
    product2 = Product(2, "Product B", "Description B", 50, ProductStatus.IN_STOCK)
    inventory_manager.add_product(product1)
    inventory_manager.add_product(product2)

    # Add shipments
    shipment1 = Shipment(1, 1, datetime.now(), 20, "WH1")
    shipment2 = Shipment(2, 2, datetime.now(), 10, "WH2")
    inventory_manager.add_shipment(shipment1)
    inventory_manager.add_shipment(shipment2)

    # Get product
    product = inventory_manager.get_product(1)
    print(f"Product {product.id}: {product.name}, Quantity: {product.quantity}")

    # Get shipment
    shipment = inventory_manager.get_shipment(1)
    print(f"Shipment {shipment.id}: Product ID {shipment.product_id}, Quantity: {shipment.quantity}")

    # Get warehouse
    warehouse = inventory_manager.get_warehouse("WH1")
    print(f"Warehouse {warehouse.location}: Available Space {warehouse.available_space}")

if __name__ == "__main__":
    main()
```
