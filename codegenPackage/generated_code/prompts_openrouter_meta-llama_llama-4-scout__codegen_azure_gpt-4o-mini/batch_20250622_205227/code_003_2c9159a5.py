"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: "Design a data model to store and manage warehouse inventory for a logistics company like Fealty Worldwide."
Generated: DETERMINISTIC_2c9159a5f5585c6d
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# warehouse_inventory.py

from typing import List, Optional
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Product:
    """Represents a product in the warehouse."""
    product_id: str
    name: str
    description: str
    quantity: int
    unit_price: float
    last_updated: datetime = field(default_factory=datetime.now)

    def update_quantity(self, amount: int) -> None:
        """Update the quantity of the product."""
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount
        self.last_updated = datetime.now()

    def update_price(self, new_price: float) -> None:
        """Update the price of the product."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.unit_price = new_price
        self.last_updated = datetime.now()

@dataclass
class Warehouse:
    """Represents a warehouse that holds products."""
    warehouse_id: str
    location: str
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> None:
        """Add a new product to the warehouse."""
        if any(p.product_id == product.product_id for p in self.products):
            raise ValueError("Product with this ID already exists.")
        self.products.append(product)

    def remove_product(self, product_id: str) -> None:
        """Remove a product from the warehouse by its ID."""
        self.products = [p for p in self.products if p.product_id != product_id]

    def find_product(self, product_id: str) -> Optional[Product]:
        """Find a product by its ID."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def total_inventory_value(self) -> float:
        """Calculate the total value of the inventory in the warehouse."""
        return sum(product.quantity * product.unit_price for product in self.products)

# Example usage
if __name__ == "__main__":
    try:
        # Create a warehouse
        warehouse = Warehouse(warehouse_id="WH001", location="New York")

        # Create products
        product1 = Product(product_id="P001", name="Widget A", description="A useful widget", quantity=100, unit_price=2.50)
        product2 = Product(product_id="P002", name="Widget B", description="Another useful widget", quantity=200, unit_price=3.00)

        # Add products to the warehouse
        warehouse.add_product(product1)
        warehouse.add_product(product2)

        # Update product quantity
        product1.update_quantity(-10)  # Sell 10 units of Widget A

        # Calculate total inventory value
        total_value = warehouse.total_inventory_value()
        print(f"Total inventory value: ${total_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
