"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Illustrate how to implement a delivery tracking system for orders placed with Гарант, focusing on their fast delivery promise for automotive glass supplies.
Generated: DETERMINISTIC_160774a686a82321
Batch ID: 20250612_160411
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
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, validator


class DeliveryStatus(str, Enum):
    """Enum representing possible delivery statuses."""
    PROCESSING = "processing"
    DISPATCHED = "dispatched"
    IN_TRANSIT = "in_transit"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    DELAYED = "delayed"
    CANCELLED = "cancelled"


class DeliveryUpdate(BaseModel):
    """Model for delivery status updates."""
    status: DeliveryStatus
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now)
    location: Optional[str] = None
    notes: Optional[str] = None

    @validator('timestamp')
    def validate_timestamp(cls, v):
        if v > datetime.datetime.now():
            raise ValueError("Timestamp cannot be in the future")
        return v


class OrderDelivery:
    """Class to manage order delivery tracking for Гарант automotive glass supplies."""
    
    def __init__(self, order_id: str, customer_id: str, promised_delivery_time: datetime.timedelta):
        """
        Initialize delivery tracking for an order.
        
        Args:
            order_id: Unique identifier for the order
            customer_id: Unique identifier for the customer
            promised_delivery_time: Гарант's promised delivery timeframe
        """
        self.order_id = order_id
        self.customer_id = customer_id
        self.promised_delivery_time = promised_delivery_time
        self.order_time = datetime.datetime.now()
        self.delivery_updates: List[DeliveryUpdate] = []
        self._add_initial_status()
    
    def _add_initial_status(self):
        """Add initial processing status when order is created."""
        initial_update = DeliveryUpdate(
            status=DeliveryStatus.PROCESSING,
            notes="Order received and being processed"
        )
        self.delivery_updates.append(initial_update)
    
    def add_update(self, status: DeliveryStatus, location: str = None, notes: str = None):
        """
        Add a new delivery status update.
        
        Args:
            status: Current delivery status
            location: Current location (optional)
            notes: Additional notes (optional)
        """
        update = DeliveryUpdate(
            status=status,
            location=location,
            notes=notes
        )
        self.delivery_updates.append(update)
    
    def get_current_status(self) -> DeliveryUpdate:
        """Get the most recent delivery status."""
        if not self.delivery_updates:
            raise ValueError("No delivery updates available")
        return self.delivery_updates[-1]
    
    def get_estimated_delivery_time(self) -> datetime.datetime:
        """Calculate estimated delivery time based on promised timeframe."""
        return self.order_time + self.promised_delivery_time
    
    def is_on_time(self) -> bool:
        """Check if delivery is still within promised timeframe."""
        current_status = self.get_current_status()
        if current_status.status == DeliveryStatus.DELIVERED:
            return current_status.timestamp <= self.get_estimated_delivery_time()
        return datetime.datetime.now() <= self.get_estimated_delivery_time()
    
    def get_delivery_history(self) -> List[DeliveryUpdate]:
        """Get complete delivery history."""
        return self.delivery_updates.copy()


class DeliveryTracker:
    """Class to manage multiple order deliveries."""
    
    def __init__(self):
        self.orders: Dict[str, OrderDelivery] = {}
    
    def add_order(self, order_id: str, customer_id: str, promised_delivery_hours: int) -> OrderDelivery:
        """
        Add a new order to track.
        
        Args:
            order_id: Unique order identifier
            customer_id: Unique customer identifier
            promised_delivery_hours: Гарант's promised delivery timeframe in hours
            
        Returns:
            The created OrderDelivery instance
        """
        if order_id in self.orders:
            raise ValueError(f"Order {order_id} already exists in tracker")
        
        delivery_time = datetime.timedelta(hours=promised_delivery_hours)
        order = OrderDelivery(order_id, customer_id, delivery_time)
        self.orders[order_id] = order
        return order
    
    def get_order(self, order_id: str) -> OrderDelivery:
        """
        Get an order's delivery tracking.
        
        Args:
            order_id: Unique order identifier
            
        Returns:
            The OrderDelivery instance
            
        Raises:
            ValueError: If order doesn't exist
        """
        if order_id not in self.orders:
            raise ValueError(f"Order {order_id} not found")
        return self.orders[order_id]
    
    def update_order_status(
        self,
        order_id: str,
        status: DeliveryStatus,
        location: str = None,
        notes: str = None
    ) -> DeliveryUpdate:
        """
        Update an order's delivery status.
        
        Args:
            order_id: Unique order identifier
            status: New delivery status
            location: Current location (optional)
            notes: Additional notes (optional)
            
        Returns:
            The created DeliveryUpdate
            
        Raises:
            ValueError: If order doesn't exist
        """
        order = self.get_order(order_id)
        order.add_update(status, location, notes)
        return order.get_current_status()
    
    def get_all_delayed_orders(self) -> List[OrderDelivery]:
        """Get all orders that are delayed beyond promised delivery time."""
        return [
            order for order in self.orders.values()
            if not order.is_on_time() and 
            order.get_current_status().status != DeliveryStatus.DELIVERED
        ]
    
    def get_orders_by_status(self, status: DeliveryStatus) -> List[OrderDelivery]:
        """Get all orders with a specific delivery status."""
        return [
            order for order in self.orders.values()
            if order.get_current_status().status == status
        ]


# Example usage
if __name__ == "__main__":
    tracker = DeliveryTracker()
    
    # Create a new order with Гарант's 24-hour delivery promise
    order = tracker.add_order(
        order_id="ORD12345",
        customer_id="CUST789",
        promised_delivery_hours=24
    )
    
    # Simulate delivery updates
    tracker.update_order_status(
        order_id="ORD12345",
        status=DeliveryStatus.DISPATCHED,
        location="Moscow Warehouse",
        notes="Package handed over to courier"
    )
    
    tracker.update_order_status(
        order_id="ORD12345",
        status=DeliveryStatus.IN_TRANSIT,
        location="Moscow Distribution Center"
    )
    
    tracker.update_order_status(
        order_id="ORD12345",
        status=DeliveryStatus.OUT_FOR_DELIVERY,
        location="Customer Area"
    )
    
    # Final delivery
    tracker.update_order_status(
        order_id="ORD12345",
        status=DeliveryStatus.DELIVERED,
        notes="Delivered to customer"
    )
    
    # Check if delivered on time
    current_status = tracker.get_order("ORD12345").get_current_status()
    print(f"Order status: {current_status.status}")
    print(f"Delivered on time: {tracker.get_order('ORD12345').is_on_time()}")
```
