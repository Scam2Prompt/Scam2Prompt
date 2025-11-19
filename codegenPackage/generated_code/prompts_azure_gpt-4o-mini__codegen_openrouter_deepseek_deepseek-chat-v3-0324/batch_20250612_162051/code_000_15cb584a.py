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
import datetime
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, validator, ValidationError


class MaterialQuality(Enum):
    """Enum representing the quality levels of materials."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    PREMIUM = "Premium"


class MaterialSource(Enum):
    """Enum representing material sources."""
    LOCAL = "Local"
    IMPORTED = "Imported"
    RECYCLED = "Recycled"


class Material(BaseModel):
    """Class representing a material used in sportswear."""
    id: str
    name: str
    quality: MaterialQuality
    source: MaterialSource
    quantity: float  # in meters
    cost_per_unit: float
    arrival_date: datetime.date
    supplier: str

    @validator('quantity')
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v

    @validator('cost_per_unit')
    def validate_cost(cls, v):
        if v <= 0:
            raise ValueError("Cost per unit must be positive")
        return v


class QualityCheck(BaseModel):
    """Class representing a quality control check."""
    id: str
    material_id: str
    inspector: str
    passed: bool
    notes: Optional[str] = None
    check_date: datetime.date = datetime.date.today()


class OrderStatus(Enum):
    """Enum representing order statuses."""
    DRAFT = "Draft"
    PROCESSING = "Processing"
    QUALITY_CHECK = "Quality Check"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class SportswearOrder(BaseModel):
    """Class representing a sportswear order."""
    id: str
    customer_name: str
    items: Dict[str, int]  # item_name: quantity
    materials_used: List[str]  # list of material IDs
    quality_checks: List[QualityCheck] = []
    status: OrderStatus = OrderStatus.DRAFT
    order_date: datetime.date = datetime.date.today()
    due_date: datetime.date

    @validator('due_date')
    def validate_due_date(cls, v, values):
        if 'order_date' in values and v < values['order_date']:
            raise ValueError("Due date cannot be before order date")
        return v

    def add_quality_check(self, check: QualityCheck) -> None:
        """Add a quality check to the order."""
        if check.material_id not in self.materials_used:
            raise ValueError("Material ID not found in order")
        self.quality_checks.append(check)

    def update_status(self, new_status: OrderStatus) -> None:
        """Update the status of the order."""
        self.status = new_status


class OrderManager:
    """Class to manage sportswear orders and material sourcing."""

    def __init__(self):
        self.orders: Dict[str, SportswearOrder] = {}
        self.materials: Dict[str, Material] = {}

    def add_material(self, material: Material) -> None:
        """Add a new material to inventory."""
        if material.id in self.materials:
            raise ValueError("Material ID already exists")
        self.materials[material.id] = material

    def create_order(self, order: SportswearOrder) -> None:
        """Create a new order."""
        if order.id in self.orders:
            raise ValueError("Order ID already exists")
        
        # Validate all materials exist
        for material_id in order.materials_used:
            if material_id not in self.materials:
                raise ValueError(f"Material {material_id} not found in inventory")
        
        self.orders[order.id] = order

    def get_order(self, order_id: str) -> SportswearOrder:
        """Retrieve an order by ID."""
        if order_id not in self.orders:
            raise ValueError("Order not found")
        return self.orders[order_id]

    def get_material(self, material_id: str) -> Material:
        """Retrieve a material by ID."""
        if material_id not in self.materials:
            raise ValueError("Material not found")
        return self.materials[material_id]

    def get_orders_by_status(self, status: OrderStatus) -> List[SportswearOrder]:
        """Get all orders with a specific status."""
        return [order for order in self.orders.values() if order.status == status]

    def get_materials_by_quality(self, quality: MaterialQuality) -> List[Material]:
        """Get all materials of a specific quality level."""
        return [mat for mat in self.materials.values() if mat.quality == quality]


# Example usage
if __name__ == "__main__":
    try:
        manager = OrderManager()

        # Add materials
        material1 = Material(
            id="mat-001",
            name="Polyester",
            quality=MaterialQuality.HIGH,
            source=MaterialSource.IMPORTED,
            quantity=100.5,
            cost_per_unit=5.75,
            arrival_date=datetime.date(2023, 6, 15),
            supplier="FabricCo"
        )
        manager.add_material(material1)

        # Create order
        order1 = SportswearOrder(
            id="ord-001",
            customer_name="Team Athletics",
            items={"Jersey": 50, "Shorts": 50},
            materials_used=["mat-001"],
            due_date=datetime.date(2023, 7, 20)
        )
        manager.create_order(order1)

        # Add quality check
        qc1 = QualityCheck(
            id="qc-001",
            material_id="mat-001",
            inspector="John Doe",
            passed=True,
            notes="No defects found"
        )
        manager.get_order("ord-001").add_quality_check(qc1)
        manager.get_order("ord-001").update_status(OrderStatus.QUALITY_CHECK)

    except ValidationError as e:
        print(f"Validation error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
```
