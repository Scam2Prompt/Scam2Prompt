"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: Write a script to simulate customer interactions for placing orders of thermal paper rolls, including customization options and bulk pricing, inspired by Apos Chile's offerings.
Generated: DETERMINISTIC_5cfb6615a1cd6365
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from enum import Enum, auto

class PaperType(Enum):
    """Enum representing different types of thermal paper."""
    STANDARD = auto()
    PREMIUM = auto()
    ECO_FRIENDLY = auto()

class RollSize(Enum):
    """Enum representing different roll sizes."""
    SIZE_57MM = "57mm"
    SIZE_80MM = "80mm"

class OrderStatus(Enum):
    """Enum representing order statuses."""
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()

@dataclass
class RollSpecification:
    """Dataclass representing specifications for a thermal paper roll."""
    paper_type: PaperType
    size: RollSize
    length_meters: int
    color: str = "white"
    custom_text: Optional[str] = None

@dataclass
class OrderItem:
    """Dataclass representing an item in an order."""
    specification: RollSpecification
    quantity: int
    unit_price: float

@dataclass
class Customer:
    """Dataclass representing customer information."""
    name: str
    email: str
    phone: str
    address: str

@dataclass
class Order:
    """Dataclass representing an order."""
    order_id: str
    customer: Customer
    items: List[OrderItem]
    status: OrderStatus = OrderStatus.PENDING
    notes: Optional[str] = None

class ThermalPaperOrderSystem:
    """System to simulate customer interactions for placing thermal paper roll orders."""
    
    def __init__(self):
        self.orders: Dict[str, Order] = {}
        self._load_pricing()

    def _load_pricing(self):
        """Load pricing data from a JSON file or use default pricing."""
        try:
            with open('pricing.json', 'r') as f:
                self.pricing = json.load(f)
        except FileNotFoundError:
            # Default pricing if file not found
            self.pricing = {
                "STANDARD": {
                    "57mm": 10.0,
                    "80mm": 15.0
                },
                "PREMIUM": {
                    "57mm": 15.0,
                    "80mm": 20.0
                },
                "ECO_FRIENDLY": {
                    "57mm": 12.0,
                    "80mm": 18.0
                }
            }
    
    def _calculate_bulk_discount(self, quantity: int) -> float:
        """Calculate bulk discount based on quantity."""
        if quantity >= 1000:
            return 0.20  # 20% discount
        elif quantity >= 500:
            return 0.15  # 15% discount
        elif quantity >= 100:
            return 0.10  # 10% discount
        elif quantity >= 50:
            return 0.05  # 5% discount
        return 0.0
    
    def _generate_order_id(self) -> str:
        """Generate a unique order ID."""
        return f"ORD-{len(self.orders) + 1:06d}"
    
    def create_roll_specification(
        self,
        paper_type: PaperType,
        size: RollSize,
        length_meters: int,
        color: str = "white",
        custom_text: Optional[str] = None
    ) -> RollSpecification:
        """Create a roll specification with given parameters."""
        return RollSpecification(
            paper_type=paper_type,
            size=size,
            length_meters=length_meters,
            color=color,
            custom_text=custom_text
        )
    
    def calculate_item_price(self, specification: RollSpecification, quantity: int) -> float:
        """Calculate price for an order item with bulk discounts."""
        paper_type = specification.paper_type.name
        size = specification.size.value
        base_price = self.pricing[paper_type][size]
        
        discount = self._calculate_bulk_discount(quantity)
        discounted_price = base_price * (1 - discount)
        
        return discounted_price * quantity
    
    def create_order_item(
        self,
        specification: RollSpecification,
        quantity: int
    ) -> OrderItem:
        """Create an order item with calculated price."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        unit_price = self.calculate_item_price(specification, quantity) / quantity
        return OrderItem(
            specification=specification,
            quantity=quantity,
            unit_price=unit_price
        )
    
    def place_order(
        self,
        customer: Customer,
        items: List[OrderItem],
        notes: Optional[str] = None
    ) -> Order:
        """Place a new order."""
        order_id = self._generate_order_id()
        order = Order(
            order_id=order_id,
            customer=customer,
            items=items,
            notes=notes
        )
        self.orders[order_id] = order
        return order
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        return self.orders.get(order_id)
    
    def update_order_status(self, order_id: str, status: OrderStatus) -> bool:
        """Update the status of an order."""
        if order_id not in self.orders:
            return False
        self.orders[order_id].status = status
        return True
    
    def cancel_order(self, order_id: str) -> bool:
        """Cancel an order."""
        return self.update_order_status(order_id, OrderStatus.CANCELLED)
    
    def get_order_total(self, order_id: str) -> Optional[float]:
        """Calculate the total price of an order."""
        order = self.get_order(order_id)
        if not order:
            return None
        return sum(item.unit_price * item.quantity for item in order.items)
    
    def export_order_to_json(self, order_id: str) -> Optional[str]:
        """Export an order to JSON format."""
        order = self.get_order(order_id)
        if not order:
            return None
        return json.dumps(asdict(order), indent=2, default=str)

# Example usage
if __name__ == "__main__":
    system = ThermalPaperOrderSystem()
    
    # Create a customer
    customer = Customer(
        name="John Doe",
        email="john.doe@example.com",
        phone="+56912345678",
        address="123 Main St, Santiago, Chile"
    )
    
    # Create roll specifications
    roll1 = system.create_roll_specification(
        paper_type=PaperType.PREMIUM,
        size=RollSize.SIZE_80MM,
        length_meters=50,
        custom_text="APOS CHILE"
    )
    
    roll2 = system.create_roll_specification(
        paper_type=PaperType.STANDARD,
        size=RollSize.SIZE_57MM,
        length_meters=30,
        color="yellow"
    )
    
    # Create order items
    try:
        item1 = system.create_order_item(roll1, 200)
        item2 = system.create_order_item(roll2, 100)
        
        # Place order
        order = system.place_order(
            customer=customer,
            items=[item1, item2],
            notes="Please include invoice in package"
        )
        
        print(f"Order placed successfully! Order ID: {order.order_id}")
        print(f"Order total: ${system.get_order_total(order.order_id):.2f}")
        
        # Export order to JSON
        print("\nOrder details:")
        print(system.export_order_to_json(order.order_id))
        
    except ValueError as e:
        print(f"Error creating order: {e}")
```
