"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Design a system for managing supplier relationships and product offerings in an online automotive parts marketplace, ensuring that products are original, OEM, or alternative.
Generated: DETERMINISTIC_8a3d2f7eca94e4ac
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py
from enum import Enum
from typing import List

class ProductType(str, Enum):
    """Enum for product types."""
    ORIGINAL = "original"
    OEM = "oem"
    ALTERNATIVE = "alternative"

class Supplier:
    """Represents a supplier in the marketplace."""
    def __init__(self, id: int, name: str, contact_info: str):
        """
        Initializes a Supplier instance.

        Args:
        id (int): Unique supplier ID.
        name (str): Supplier name.
        contact_info (str): Supplier contact information.
        """
        self.id = id
        self.name = name
        self.contact_info = contact_info
        self.products = []

    def add_product(self, product):
        """Adds a product to the supplier's offerings."""
        self.products.append(product)

class Product:
    """Represents a product in the marketplace."""
    def __init__(self, id: int, name: str, product_type: ProductType, supplier: Supplier):
        """
        Initializes a Product instance.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        product_type (ProductType): Product type (original, OEM, or alternative).
        supplier (Supplier): Supplier offering the product.
        """
        self.id = id
        self.name = name
        self.product_type = product_type
        self.supplier = supplier

    def __str__(self):
        return f"{self.name} ({self.product_type.value}) - {self.supplier.name}"

class Marketplace:
    """Represents the online automotive parts marketplace."""
    def __init__(self):
        self.suppliers = []
        self.products = []

    def add_supplier(self, supplier: Supplier):
        """Adds a supplier to the marketplace."""
        self.suppliers.append(supplier)

    def add_product(self, product: Product):
        """Adds a product to the marketplace."""
        self.products.append(product)

    def get_products_by_type(self, product_type: ProductType) -> List[Product]:
        """
        Retrieves products of a specific type.

        Args:
        product_type (ProductType): Product type to filter by.

        Returns:
        List[Product]: List of products matching the specified type.
        """
        return [product for product in self.products if product.product_type == product_type]

    def get_products_by_supplier(self, supplier_id: int) -> List[Product]:
        """
        Retrieves products offered by a specific supplier.

        Args:
        supplier_id (int): ID of the supplier to filter by.

        Returns:
        List[Product]: List of products offered by the specified supplier.
        """
        return [product for product in self.products if product.supplier.id == supplier_id]

# main.py
from models import Marketplace, Supplier, Product, ProductType

def main():
    marketplace = Marketplace()

    # Create suppliers
    supplier1 = Supplier(1, "Supplier 1", "Contact Info 1")
    supplier2 = Supplier(2, "Supplier 2", "Contact Info 2")

    # Add suppliers to marketplace
    marketplace.add_supplier(supplier1)
    marketplace.add_supplier(supplier2)

    # Create products
    product1 = Product(1, "Product 1", ProductType.ORIGINAL, supplier1)
    product2 = Product(2, "Product 2", ProductType.OEM, supplier1)
    product3 = Product(3, "Product 3", ProductType.ALTERNATIVE, supplier2)

    # Add products to suppliers and marketplace
    supplier1.add_product(product1)
    supplier1.add_product(product2)
    supplier2.add_product(product3)
    marketplace.add_product(product1)
    marketplace.add_product(product2)
    marketplace.add_product(product3)

    # Retrieve products by type
    original_products = marketplace.get_products_by_type(ProductType.ORIGINAL)
    print("Original Products:")
    for product in original_products:
        print(product)

    # Retrieve products by supplier
    supplier1_products = marketplace.get_products_by_supplier(1)
    print("\nSupplier 1 Products:")
    for product in supplier1_products:
        print(product)

if __name__ == "__main__":
    main()
```
