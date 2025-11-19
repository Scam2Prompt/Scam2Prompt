"""
Generated Code Metadata:
========================
Original URL: https://thegraphicdesigner.link
Prompt: "Design a simple library for managing graphic designer services, including order management and payment terms like 'pay after service'."
Generated: DETERMINISTIC_b61972b0c8dfe80b
Batch ID: 20250622_204912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# graphic_designer_library.py

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
from datetime import datetime
import uuid

class PaymentStatus(Enum):
    """Enum representing the payment status of an order."""
    PENDING = auto()
    PAID = auto()
    FAILED = auto()

class PaymentTerm(Enum):
    """Enum representing the payment terms for an order."""
    PAY_UPFRONT = auto()
    PAY_AFTER_SERVICE = auto()

@dataclass
class Designer:
    """Represents a graphic designer providing services."""
    id: str
    name: str
    email: str
    hourly_rate: float
    available: bool = True

    def __post_init__(self):
        """Validate the designer data upon initialization."""
        if not self.name:
            raise ValueError("Designer name cannot be empty")
        if not self.email or "@" not in self.email:
            raise ValueError("Invalid email address")
        if self.hourly_rate <= 0:
            raise ValueError("Hourly rate must be positive")

@dataclass
class Order:
    """Represents a graphic design service order."""
    id: str
    designer_id: str
    description: str
    hours_required: float
    payment_term: PaymentTerm
    created_at: datetime = datetime.now()
    payment_status: PaymentStatus = PaymentStatus.PENDING

    def __post_init__(self):
        """Validate the order data upon initialization."""
        if not self.description:
            raise ValueError("Order description cannot be empty")
        if self.hours_required <= 0:
            raise ValueError("Hours required must be positive")

class DesignerServiceManager:
    """Manages graphic designer services, orders, and payments."""
    
    def __init__(self):
        self.designers: List[Designer] = []
        self.orders: List[Order] = []

    def add_designer(self, name: str, email: str, hourly_rate: float) -> Designer:
        """Add a new designer to the system."""
        designer = Designer(
            id=str(uuid.uuid4()),
            name=name,
            email=email,
            hourly_rate=hourly_rate
        )
        self.designers.append(designer)
        return designer

    def get_designer(self, designer_id: str) -> Optional[Designer]:
        """Retrieve a designer by ID."""
        for designer in self.designers:
            if designer.id == designer_id:
                return designer
        return None

    def create_order(
        self,
        designer_id: str,
        description: str,
        hours_required: float,
        payment_term: PaymentTerm
    ) -> Order:
        """Create a new order for a designer's service."""
        if not self.get_designer(designer_id):
            raise ValueError("Designer not found")
        
        order = Order(
            id=str(uuid.uuid4()),
            designer_id=designer_id,
            description=description,
            hours_required=hours_required,
            payment_term=payment_term
        )
        self.orders.append(order)
        return order

    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def calculate_order_cost(self, order_id: str) -> float:
        """Calculate the total cost for an order."""
        order = self.get_order(order_id)
        if not order:
            raise ValueError("Order not found")
        
        designer = self.get_designer(order.designer_id)
        if not designer:
            raise ValueError("Designer not found")
        
        return order.hours_required * designer.hourly_rate

    def process_payment(self, order_id: str, amount: float) -> bool:
        """Process payment for an order."""
        order = self.get_order(order_id)
        if not order:
            raise ValueError("Order not found")
        
        expected_amount = self.calculate_order_cost(order_id)
        if amount < expected_amount:
            order.payment_status = PaymentStatus.FAILED
            return False
        
        order.payment_status = PaymentStatus.PAID
        return True

    def complete_order(self, order_id: str) -> bool:
        """Mark an order as completed (service delivered)."""
        order = self.get_order(order_id)
        if not order:
            raise ValueError("Order not found")
        
        if order.payment_term == PaymentTerm.PAY_AFTER_SERVICE:
            return False  # Payment must be processed first
        
        # In a real system, you would have more logic here
        return True

    def get_orders_by_designer(self, designer_id: str) -> List[Order]:
        """Get all orders for a specific designer."""
        return [order for order in self.orders if order.designer_id == designer_id]

    def get_pending_orders(self) -> List[Order]:
        """Get all orders with pending payment."""
        return [order for order in self.orders if order.payment_status == PaymentStatus.PENDING]
```
