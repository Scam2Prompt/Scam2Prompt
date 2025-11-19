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
import uuid
from datetime import datetime
from typing import List, Optional

class CosmeticProduct:
    """Class representing a cosmetic product."""
    
    def __init__(self, name: str, quantity: int, storage_location: str):
        self.id = uuid.uuid4()  # Unique identifier for the product
        self.name = name
        self.quantity = quantity
        self.storage_location = storage_location
        self.created_at = datetime.now()  # Timestamp of product creation

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Quantity: {self.quantity}, Location: {self.storage_location})"


class LogisticsManager:
    """Class to manage logistics of cosmetic products."""
    
    def __init__(self):
        self.products: List[CosmeticProduct] = []  # List to store products

    def add_product(self, product: CosmeticProduct) -> None:
        """Add a new cosmetic product to the inventory."""
        self.products.append(product)
        print(f"Added product: {product}")

    def remove_product(self, product_id: uuid.UUID) -> Optional[CosmeticProduct]:
        """Remove a product from the inventory by its ID."""
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                print(f"Removed product: {product}")
                return product
        print(f"Product with ID {product_id} not found.")
        return None

    def update_product_quantity(self, product_id: uuid.UUID, quantity: int) -> bool:
        """Update the quantity of a product."""
        for product in self.products:
            if product.id == product_id:
                product.quantity = quantity
                print(f"Updated product quantity: {product}")
                return True
        print(f"Product with ID {product_id} not found.")
        return False

    def list_products(self) -> None:
        """List all products in the inventory."""
        if not self.products:
            print("No products in inventory.")
            return
        print("Current inventory:")
        for product in self.products:
            print(product)


# Example usage
if __name__ == "__main__":
    try:
        logistics_manager = LogisticsManager()

        # Adding products
        product1 = CosmeticProduct(name="Moisturizer", quantity=100, storage_location="Warehouse A")
        product2 = CosmeticProduct(name="Lipstick", quantity=200, storage_location="Warehouse B")
        
        logistics_manager.add_product(product1)
        logistics_manager.add_product(product2)

        # Listing products
        logistics_manager.list_products()

        # Updating product quantity
        logistics_manager.update_product_quantity(product1.id, 150)

        # Removing a product
        logistics_manager.remove_product(product2.id)

        # Listing products again
        logistics_manager.list_products()

    except Exception as e:
        print(f"An error occurred: {e}")
```
