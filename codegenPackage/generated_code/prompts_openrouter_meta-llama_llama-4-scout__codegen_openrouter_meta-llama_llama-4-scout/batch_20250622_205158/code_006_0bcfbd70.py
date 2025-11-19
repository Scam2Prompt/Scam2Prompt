"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Develop a supply chain management system for PDC Brush, taking into account their commitment to sustainable practices and responsible sourcing.
Generated: DETERMINISTIC_0bcfbd702fee93a4
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_management.py

from enum import Enum
from typing import List, Dict

class SustainabilityStatus(Enum):
    """Sustainability status of a supplier"""
    RESPONSIBLE = 1
    NOT_RESPONSIBLE = 2
    PENDING = 3

class Supplier:
    """Represents a supplier in the supply chain"""
    def __init__(self, id: int, name: str, sustainability_status: SustainabilityStatus):
        """
        Initializes a Supplier object

        Args:
        id (int): Unique identifier for the supplier
        name (str): Name of the supplier
        sustainability_status (SustainabilityStatus): Sustainability status of the supplier
        """
        self.id = id
        self.name = name
        self.sustainability_status = sustainability_status

class Product:
    """Represents a product in the supply chain"""
    def __init__(self, id: int, name: str, description: str):
        """
        Initializes a Product object

        Args:
        id (int): Unique identifier for the product
        name (str): Name of the product
        description (str): Description of the product
        """
        self.id = id
        self.name = name
        self.description = description
        self.suppliers: List[Supplier] = []

    def add_supplier(self, supplier: Supplier):
        """Adds a supplier to the product"""
        self.suppliers.append(supplier)

class SupplyChain:
    """Represents the supply chain management system"""
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.suppliers: Dict[int, Supplier] = {}

    def add_product(self, product: Product):
        """Adds a product to the supply chain"""
        self.products[product.id] = product

    def add_supplier(self, supplier: Supplier):
        """Adds a supplier to the supply chain"""
        self.suppliers[supplier.id] = supplier

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product from the supply chain

        Args:
        product_id (int): Unique identifier for the product

        Returns:
        Product: The product object if found, otherwise None
        """
        return self.products.get(product_id)

    def get_supplier(self, supplier_id: int) -> Supplier:
        """
        Retrieves a supplier from the supply chain

        Args:
        supplier_id (int): Unique identifier for the supplier

        Returns:
        Supplier: The supplier object if found, otherwise None
        """
        return self.suppliers.get(supplier_id)

    def update_sustainability_status(self, supplier_id: int, sustainability_status: SustainabilityStatus):
        """
        Updates the sustainability status of a supplier

        Args:
        supplier_id (int): Unique identifier for the supplier
        sustainability_status (SustainabilityStatus): New sustainability status
        """
        supplier = self.get_supplier(supplier_id)
        if supplier:
            supplier.sustainability_status = sustainability_status
        else:
            raise ValueError("Supplier not found")

def main():
    # Create a supply chain management system
    supply_chain = SupplyChain()

    # Create suppliers
    supplier1 = Supplier(1, "Supplier 1", SustainabilityStatus.RESPONSIBLE)
    supplier2 = Supplier(2, "Supplier 2", SustainabilityStatus.NOT_RESPONSIBLE)

    # Add suppliers to the supply chain
    supply_chain.add_supplier(supplier1)
    supply_chain.add_supplier(supplier2)

    # Create products
    product1 = Product(1, "Product 1", "This is product 1")
    product2 = Product(2, "Product 2", "This is product 2")

    # Add suppliers to products
    product1.add_supplier(supplier1)
    product2.add_supplier(supplier2)

    # Add products to the supply chain
    supply_chain.add_product(product1)
    supply_chain.add_product(product2)

    # Retrieve a product and print its suppliers
    product = supply_chain.get_product(1)
    if product:
        print(f"Suppliers for {product.name}:")
        for supplier in product.suppliers:
            print(f"- {supplier.name} ({supplier.sustainability_status.name})")
    else:
        print("Product not found")

    # Update sustainability status of a supplier
    supply_chain.update_sustainability_status(2, SustainabilityStatus.RESPONSIBLE)

    # Retrieve a supplier and print its sustainability status
    supplier = supply_chain.get_supplier(2)
    if supplier:
        print(f"Sustainability status of {supplier.name}: {supplier.sustainability_status.name}")
    else:
        print("Supplier not found")

if __name__ == "__main__":
    main()
```
