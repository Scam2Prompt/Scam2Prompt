"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Write a Python code snippet to manage inventory for a luxury linen company like Regency Towel, including classes for Towels, Bedding, and Hotel Uniforms.
Generated: DETERMINISTIC_aca387a3e2d407d9
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

from typing import List, Dict
from enum import Enum

class ProductType(str, Enum):
    """Product type enumeration."""
    TOWEL = "towel"
    BEDDING = "bedding"
    HOTEL_UNIFORM = "hotel_uniform"

class Product:
    """Base product class."""
    def __init__(self, product_id: int, name: str, product_type: ProductType, quantity: int, price: float):
        """
        Initialize a product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - product_type (ProductType): Product type.
        - quantity (int): Initial quantity.
        - price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.product_type = product_type
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.product_type.value}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"

class Towel(Product):
    """Towel product class."""
    def __init__(self, product_id: int, name: str, size: str, material: str, quantity: int, price: float):
        """
        Initialize a towel product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - size (str): Towel size.
        - material (str): Towel material.
        - quantity (int): Initial quantity.
        - price (float): Product price.
        """
        super().__init__(product_id, name, ProductType.TOWEL, quantity, price)
        self.size = size
        self.material = material

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Material: {self.material}"

class Bedding(Product):
    """Bedding product class."""
    def __init__(self, product_id: int, name: str, thread_count: int, material: str, quantity: int, price: float):
        """
        Initialize a bedding product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - thread_count (int): Thread count.
        - material (str): Bedding material.
        - quantity (int): Initial quantity.
        - price (float): Product price.
        """
        super().__init__(product_id, name, ProductType.BEDDING, quantity, price)
        self.thread_count = thread_count
        self.material = material

    def __str__(self):
        return super().__str__() + f", Thread Count: {self.thread_count}, Material: {self.material}"

class HotelUniform(Product):
    """Hotel uniform product class."""
    def __init__(self, product_id: int, name: str, size: str, material: str, quantity: int, price: float):
        """
        Initialize a hotel uniform product.

        Args:
        - product_id (int): Unique product ID.
        - name (str): Product name.
        - size (str): Uniform size.
        - material (str): Uniform material.
        - quantity (int): Initial quantity.
        - price (float): Product price.
        """
        super().__init__(product_id, name, ProductType.HOTEL_UNIFORM, quantity, price)
        self.size = size
        self.material = material

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Material: {self.material}"

class Inventory:
    """Inventory management class."""
    def __init__(self):
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """Add a product to the inventory."""
        if product.product_id in self.products:
            raise ValueError("Product ID already exists in the inventory.")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int):
        """Remove a product from the inventory."""
        if product_id not in self.products:
            raise ValueError("Product ID does not exist in the inventory.")
        del self.products[product_id]

    def update_quantity(self, product_id: int, new_quantity: int):
        """Update the quantity of a product in the inventory."""
        if product_id not in self.products:
            raise ValueError("Product ID does not exist in the inventory.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """Get a product from the inventory."""
        return self.products.get(product_id)

    def __str__(self):
        inventory_list = "\n".join([str(product) for product in self.products.values()])
        return inventory_list

def main():
    # Example usage:
    inventory = Inventory()

    towel = Towel(1, "Luxury Towel", "Large", "Egyptian Cotton", 100, 19.99)
    bedding = Bedding(2, "Regency Bedding", 1000, "Cotton", 50, 99.99)
    uniform = HotelUniform(3, "Hotel Staff Uniform", "Medium", "Polyester", 200, 29.99)

    inventory.add_product(towel)
    inventory.add_product(bedding)
    inventory.add_product(uniform)

    print("Initial Inventory:")
    print(inventory)

    inventory.update_quantity(1, 50)
    print("\nUpdated Inventory:")
    print(inventory)

    print("\nGet Product:")
    print(inventory.get_product(2))

if __name__ == "__main__":
    main()
```
