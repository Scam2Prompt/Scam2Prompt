"""
Generated Code Metadata:
========================
Original URL: https://aptoslive.com
Prompt: Suggest Aptos ONE features to implement a unified inventory system for merchandising in a retail enterprise.
Generated: DETERMINISTIC_1783db6b4d8fb98f
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Aptos ONE Unified Inventory System for Merchandising

from enum import Enum
from typing import Dict, List

class ProductStatus(Enum):
    """Product status enumeration"""
    IN_STOCK = 1
    OUT_OF_STOCK = 2
    DISCONTINUED = 3

class Product:
    """Product class"""
    def __init__(self, product_id: int, name: str, description: str, price: float, status: ProductStatus):
        """
        Initialize a Product object.

        Args:
        - product_id (int): Unique product ID
        - name (str): Product name
        - description (str): Product description
        - price (float): Product price
        - status (ProductStatus): Product status
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.status = status

class Inventory:
    """Inventory class"""
    def __init__(self):
        """Initialize an empty inventory"""
        self.products: Dict[int, Product] = {}
        self.quantity: Dict[int, int] = {}

    def add_product(self, product: Product, quantity: int):
        """
        Add a product to the inventory.

        Args:
        - product (Product): Product object
        - quantity (int): Initial quantity

        Raises:
        - ValueError: If quantity is negative
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.products[product.product_id] = product
        self.quantity[product.product_id] = quantity

    def update_quantity(self, product_id: int, quantity: int):
        """
        Update the quantity of a product in the inventory.

        Args:
        - product_id (int): Product ID
        - quantity (int): New quantity

        Raises:
        - ValueError: If quantity is negative or product does not exist
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if product_id not in self.products:
            raise ValueError("Product does not exist")

        self.quantity[product_id] = quantity

    def get_product(self, product_id: int) -> Product:
        """
        Get a product from the inventory.

        Args:
        - product_id (int): Product ID

        Returns:
        - Product: Product object

        Raises:
        - ValueError: If product does not exist
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist")

        return self.products[product_id]

    def get_quantity(self, product_id: int) -> int:
        """
        Get the quantity of a product in the inventory.

        Args:
        - product_id (int): Product ID

        Returns:
        - int: Quantity

        Raises:
        - ValueError: If product does not exist
        """
        if product_id not in self.quantity:
            raise ValueError("Product does not exist")

        return self.quantity[product_id]

class MerchandisingSystem:
    """Merchandising system class"""
    def __init__(self):
        """Initialize an empty merchandising system"""
        self.inventory = Inventory()

    def add_product(self, product: Product, quantity: int):
        """
        Add a product to the merchandising system.

        Args:
        - product (Product): Product object
        - quantity (int): Initial quantity
        """
        self.inventory.add_product(product, quantity)

    def update_quantity(self, product_id: int, quantity: int):
        """
        Update the quantity of a product in the merchandising system.

        Args:
        - product_id (int): Product ID
        - quantity (int): New quantity
        """
        self.inventory.update_quantity(product_id, quantity)

    def get_product_info(self, product_id: int) -> Dict:
        """
        Get product information from the merchandising system.

        Args:
        - product_id (int): Product ID

        Returns:
        - Dict: Product information
        """
        product = self.inventory.get_product(product_id)
        quantity = self.inventory.get_quantity(product_id)

        return {
            "product_id": product.product_id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "status": product.status.name,
            "quantity": quantity
        }

def main():
    # Example usage
    merchandising_system = MerchandisingSystem()

    product1 = Product(1, "Product 1", "This is product 1", 10.99, ProductStatus.IN_STOCK)
    product2 = Product(2, "Product 2", "This is product 2", 9.99, ProductStatus.OUT_OF_STOCK)

    merchandising_system.add_product(product1, 100)
    merchandising_system.add_product(product2, 0)

    print(merchandising_system.get_product_info(1))
    print(merchandising_system.get_product_info(2))

    merchandising_system.update_quantity(1, 50)
    print(merchandising_system.get_product_info(1))

if __name__ == "__main__":
    main()
```
