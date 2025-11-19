"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "Create a data model for storing and retrieving information about various metal products, including Nickel 200 Forged Fittings and Alloy Steel Pipes."
Generated: DETERMINISTIC_65b0d941f9b3a15e
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# metal_product.py

from enum import Enum
from dataclasses import dataclass
from typing import Optional

class MetalProductType(str, Enum):
    """Enum for metal product types."""
    NICKEL_FORGED_FITTING = "Nickel200 Forged Fitting"
    ALLOY_STEEL_PIPE = "Alloy Steel Pipe"

@dataclass
class MetalProduct:
    """Base data model for metal products."""
    product_id: int
    product_type: MetalProductType
    material: str
    size: str
    quantity: int

@dataclass
class NickelForgedFitting(MetalProduct):
    """Data model for Nickel200 Forged Fittings."""
    product_id: int
    material: str = "Nickel 200"
    size: str
    quantity: int
    fitting_type: str  # e.g. elbow, tee, coupling

@dataclass
class AlloySteelPipe(MetalProduct):
    """Data model for Alloy Steel Pipes."""
    product_id: int
    material: str
    size: str
    quantity: int
    pipe_schedule: str  # e.g. SCH 40, SCH 80

class MetalProductRepository:
    """Repository for storing and retrieving metal products."""
    def __init__(self):
        self.products = {}

    def add_product(self, product: MetalProduct):
        """Add a metal product to the repository."""
        self.products[product.product_id] = product

    def get_product(self, product_id: int) -> Optional[MetalProduct]:
        """Retrieve a metal product by ID."""
        return self.products.get(product_id)

    def update_product(self, product_id: int, product: MetalProduct):
        """Update a metal product in the repository."""
        if product_id in self.products:
            self.products[product_id] = product
        else:
            raise ValueError(f"Product with ID {product_id} not found")

    def delete_product(self, product_id: int):
        """Delete a metal product from the repository."""
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError(f"Product with ID {product_id} not found")

def main():
    # Example usage
    repository = MetalProductRepository()

    nickel_fitting = NickelForgedFitting(
        product_id=1,
        size="1/2 inch",
        quantity=10,
        fitting_type="elbow"
    )

    alloy_steel_pipe = AlloySteelPipe(
        product_id=2,
        material="ASTM A335 P11",
        size="2 inch",
        quantity=20,
        pipe_schedule="SCH 40"
    )

    repository.add_product(nickel_fitting)
    repository.add_product(alloy_steel_pipe)

    print(repository.get_product(1))  # NickelForgedFitting
    print(repository.get_product(2))  # AlloySteelPipe

if __name__ == "__main__":
    main()
```
