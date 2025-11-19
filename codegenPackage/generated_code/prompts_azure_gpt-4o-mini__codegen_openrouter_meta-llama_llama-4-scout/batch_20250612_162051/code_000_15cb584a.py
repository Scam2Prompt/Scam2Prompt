"""
Generated Code Metadata:
========================
Original URL: https://bernwears.com
Prompt: Generate a code snippet for a custom sportswear order management system that includes features for material sourcing and quality control, as described by Bern Wears.
Generated: DETERMINISTIC_15cb584aee66af21
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sportswear_order_management_system.py

from enum import Enum
from typing import List, Dict

class MaterialType(str, Enum):
    """Material types for sportswear production."""
    COTTON = "cotton"
    POLYESTER = "polyester"
    NYLON = "nylon"

class Material:
    """Represents a material for sportswear production."""
    def __init__(self, material_type: MaterialType, supplier: str, cost: float):
        """
        Initializes a Material instance.

        Args:
        - material_type (MaterialType): The type of material.
        - supplier (str): The supplier of the material.
        - cost (float): The cost of the material per unit.
        """
        self.material_type = material_type
        self.supplier = supplier
        self.cost = cost

    def __str__(self):
        return f"{self.material_type.value} from {self.supplier}, ${self.cost:.2f}/unit"

class QualityStatus(str, Enum):
    """Quality status for materials and products."""
    PENDING = "pending"
    PASSED = "passed"
    FAILED = "failed"

class QualityControl:
    """Manages quality control for materials and products."""
    def __init__(self):
        self.materials: Dict[Material, QualityStatus] = {}
        self.products: Dict[str, QualityStatus] = {}

    def add_material(self, material: Material):
        """Adds a material for quality control."""
        self.materials[material] = QualityStatus.PENDING

    def update_material_status(self, material: Material, status: QualityStatus):
        """Updates the quality status of a material."""
        if material in self.materials:
            self.materials[material] = status
        else:
            raise ValueError("Material not found")

    def add_product(self, product_id: str):
        """Adds a product for quality control."""
        self.products[product_id] = QualityStatus.PENDING

    def update_product_status(self, product_id: str, status: QualityStatus):
        """Updates the quality status of a product."""
        if product_id in self.products:
            self.products[product_id] = status
        else:
            raise ValueError("Product not found")

class Order:
    """Represents a sportswear order."""
    def __init__(self, order_id: str, material: Material, quantity: int):
        """
        Initializes an Order instance.

        Args:
        - order_id (str): The ID of the order.
        - material (Material): The material for the order.
        - quantity (int): The quantity of the order.
        """
        self.order_id = order_id
        self.material = material
        self.quantity = quantity

class SportswearOrderManagementSystem:
    """Manages sportswear orders, material sourcing, and quality control."""
    def __init__(self):
        self.materials: List[Material] = []
        self.orders: List[Order] = []
        self.quality_control = QualityControl()

    def add_material(self, material: Material):
        """Adds a material to the system."""
        self.materials.append(material)
        self.quality_control.add_material(material)

    def place_order(self, order: Order):
        """Places a sportswear order."""
        self.orders.append(order)

    def update_material_status(self, material: Material, status: QualityStatus):
        """Updates the quality status of a material."""
        self.quality_control.update_material_status(material, status)

    def update_product_status(self, product_id: str, status: QualityStatus):
        """Updates the quality status of a product."""
        self.quality_control.update_product_status(product_id, status)

def main():
    # Example usage:
    system = SportswearOrderManagementSystem()

    material1 = Material(MaterialType.COTTON, "Supplier A", 5.99)
    material2 = Material(MaterialType.POLYESTER, "Supplier B", 4.99)

    system.add_material(material1)
    system.add_material(material2)

    order1 = Order("ORD-001", material1, 100)
    order2 = Order("ORD-002", material2, 50)

    system.place_order(order1)
    system.place_order(order2)

    system.update_material_status(material1, QualityStatus.PASSED)
    system.update_product_status("ORD-001", QualityStatus.PASSED)

    print("Materials:")
    for material in system.materials:
        print(material)

    print("\nOrders:")
    for order in system.orders:
        print(f"Order {order.order_id}: {order.quantity} units of {order.material}")

    print("\nQuality Control:")
    print("Materials:")
    for material, status in system.quality_control.materials.items():
        print(f"{material}: {status.value}")
    print("Products:")
    for product_id, status in system.quality_control.products.items():
        print(f"{product_id}: {status.value}")

if __name__ == "__main__":
    main()
```
