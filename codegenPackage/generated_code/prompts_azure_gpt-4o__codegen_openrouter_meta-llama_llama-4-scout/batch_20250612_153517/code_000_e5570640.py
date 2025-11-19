"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write code to simulate a logistics management system for tracking the storage and transportation of cosmetic products, referencing the full-service solutions described by Fabricare Cosméticos.
Generated: DETERMINISTIC_e5570640b9c84520
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# logistics_management_system.py

from enum import Enum
from typing import List, Dict

class ProductStatus(Enum):
    """Enum for product status"""
    IN_STOCK = 1
    IN_TRANSIT = 2
    DELIVERED = 3
    DAMAGED = 4

class CosmeticProduct:
    """Class representing a cosmetic product"""
    def __init__(self, product_id: int, name: str, quantity: int):
        """
        Initialize a cosmetic product

        Args:
        - product_id (int): Unique product ID
        - name (str): Product name
        - quantity (int): Product quantity
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.status = ProductStatus.IN_STOCK

    def update_status(self, status: ProductStatus):
        """Update product status"""
        self.status = status

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}, Status: {self.status.name}"

class Warehouse:
    """Class representing a warehouse"""
    def __init__(self, warehouse_id: int, capacity: int):
        """
        Initialize a warehouse

        Args:
        - warehouse_id (int): Unique warehouse ID
        - capacity (int): Warehouse capacity
        """
        self.warehouse_id = warehouse_id
        self.capacity = capacity
        self.products: Dict[int, CosmeticProduct] = {}

    def add_product(self, product: CosmeticProduct):
        """Add a product to the warehouse"""
        if product.product_id in self.products:
            print("Product already exists in the warehouse.")
            return
        if sum(p.quantity for p in self.products.values()) + product.quantity > self.capacity:
            print("Warehouse is full. Cannot add product.")
            return
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        """Remove a product from the warehouse"""
        if product_id not in self.products:
            print("Product does not exist in the warehouse.")
            return
        del self.products[product_id]

    def __str__(self):
        warehouse_info = f"Warehouse ID: {self.warehouse_id}, Capacity: {self.capacity}\n"
        products_info = "\n".join(str(product) for product in self.products.values())
        return warehouse_info + products_info

class Transportation:
    """Class representing transportation"""
    def __init__(self):
        self.products: List[CosmeticProduct] = []

    def add_product(self, product: CosmeticProduct):
        """Add a product to transportation"""
        self.products.append(product)
        product.update_status(ProductStatus.IN_TRANSIT)

    def deliver_products(self):
        """Deliver products"""
        for product in self.products:
            product.update_status(ProductStatus.DELIVERED)
        self.products.clear()

    def __str__(self):
        products_info = "\n".join(str(product) for product in self.products)
        return products_info

def main():
    # Create warehouse
    warehouse = Warehouse(1, 1000)

    # Create products
    product1 = CosmeticProduct(1, "Shampoo", 100)
    product2 = CosmeticProduct(2, "Conditioner", 50)

    # Add products to warehouse
    warehouse.add_product(product1)
    warehouse.add_product(product2)

    # Print warehouse info
    print("Warehouse Info:")
    print(warehouse)

    # Create transportation
    transportation = Transportation()

    # Add products to transportation
    transportation.add_product(product1)
    transportation.add_product(product2)

    # Print transportation info
    print("\nTransportation Info:")
    print(transportation)

    # Deliver products
    transportation.deliver_products()

    # Print warehouse info after delivery
    print("\nWarehouse Info after Delivery:")
    print(warehouse)

if __name__ == "__main__":
    main()
```
