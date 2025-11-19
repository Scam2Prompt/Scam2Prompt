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
# Import necessary libraries
from typing import List, Dict, Optional
import uuid

# Define a class to represent a Supplier
class Supplier:
    def __init__(self, name: str, contact_info: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the supplier
        self.name = name
        self.contact_info = contact_info

    def __repr__(self):
        return f"Supplier(id={self.id}, name={self.name}, contact_info={self.contact_info})"

# Define a class to represent a Product
class Product:
    def __init__(self, name: str, category: str, price: float, supplier: Supplier, product_type: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the product
        self.name = name
        self.category = category
        self.price = price
        self.supplier = supplier
        self.product_type = product_type  # 'OEM', 'Original', or 'Alternative'

    def __repr__(self):
        return (f"Product(id={self.id}, name={self.name}, category={self.category}, "
                f"price={self.price}, supplier={self.supplier.name}, product_type={self.product_type})")

# Define a class to manage the Supplier and Product relationships
class Marketplace:
    def __init__(self):
        self.suppliers: Dict[str, Supplier] = {}  # Dictionary to store suppliers by ID
        self.products: Dict[str, Product] = {}  # Dictionary to store products by ID

    def add_supplier(self, name: str, contact_info: str) -> Supplier:
        """Add a new supplier to the marketplace."""
        supplier = Supplier(name, contact_info)
        self.suppliers[supplier.id] = supplier
        return supplier

    def add_product(self, name: str, category: str, price: float, supplier_id: str, product_type: str) -> Optional[Product]:
        """Add a new product to the marketplace."""
        if supplier_id not in self.suppliers:
            raise ValueError(f"Supplier with ID {supplier_id} does not exist.")
        
        product = Product(name, category, price, self.suppliers[supplier_id], product_type)
        self.products[product.id] = product
        return product

    def get_supplier(self, supplier_id: str) -> Optional[Supplier]:
        """Retrieve a supplier by ID."""
        return self.suppliers.get(supplier_id)

    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by ID."""
        return self.products.get(product_id)

    def list_suppliers(self) -> List[Supplier]:
        """List all suppliers in the marketplace."""
        return list(self.suppliers.values())

    def list_products(self) -> List[Product]:
        """List all products in the marketplace."""
        return list(self.products.values())

# Example usage
if __name__ == "__main__":
    marketplace = Marketplace()

    # Adding suppliers
    supplier1 = marketplace.add_supplier("Auto Parts Co.", "contact@autopartsco.com")
    supplier2 = marketplace.add_supplier("OEM Parts Inc.", "support@oemparts.com")

    # Adding products
    try:
        product1 = marketplace.add_product("Brake Pad", "Brakes", 49.99, supplier1.id, "OEM")
        product2 = marketplace.add_product("Oil Filter", "Filters", 19.99, supplier2.id, "Original")
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Listing suppliers and products
    print("Suppliers:")
    for supplier in marketplace.list_suppliers():
        print(supplier)

    print("\nProducts:")
    for product in marketplace.list_products():
        print(product)
```
