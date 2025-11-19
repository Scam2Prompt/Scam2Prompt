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
# delivery_tracking_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class OrderStatus(Enum):
    """Enum for order status"""
    PENDING = 1
    IN_TRANSIT = 2
    DELIVERED = 3
    LOST = 4

class Order:
    """Class representing an order"""
    def __init__(self, order_id: int, customer_name: str, delivery_address: str, 
                 order_date: datetime, expected_delivery_date: datetime):
        self.order_id = order_id
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.order_date = order_date
        self.expected_delivery_date = expected_delivery_date
        self.status = OrderStatus.PENDING
        self.tracking_info = []

    def update_status(self, status: OrderStatus):
        """Update the order status"""
        self.status = status

    def add_tracking_info(self, location: str, timestamp: datetime):
        """Add tracking information"""
        self.tracking_info.append((location, timestamp))

class DeliveryTrackingSystem:
    """Class representing the delivery tracking system"""
    def __init__(self):
        self.orders: Dict[int, Order] = {}

    def place_order(self, order_id: int, customer_name: str, delivery_address: str, 
                    order_date: datetime, expected_delivery_date: datetime):
        """Place a new order"""
        if order_id in self.orders:
            raise ValueError("Order ID already exists")
        self.orders[order_id] = Order(order_id, customer_name, delivery_address, 
                                      order_date, expected_delivery_date)

    def update_order_status(self, order_id: int, status: OrderStatus):
        """Update the status of an existing order"""
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist")
        self.orders[order_id].update_status(status)

    def add_tracking_info(self, order_id: int, location: str, timestamp: datetime):
        """Add tracking information for an existing order"""
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist")
        self.orders[order_id].add_tracking_info(location, timestamp)

    def get_order_status(self, order_id: int) -> OrderStatus:
        """Get the status of an existing order"""
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist")
        return self.orders[order_id].status

    def get_tracking_info(self, order_id: int) -> List[tuple]:
        """Get the tracking information for an existing order"""
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist")
        return self.orders[order_id].tracking_info

def main():
    # Create a delivery tracking system
    tracking_system = DeliveryTrackingSystem()

    # Place an order
    order_id = 12345
    customer_name = "John Doe"
    delivery_address = "123 Main St"
    order_date = datetime.now()
    expected_delivery_date = order_date + timedelta(days=3)
    tracking_system.place_order(order_id, customer_name, delivery_address, 
                                order_date, expected_delivery_date)

    # Update order status
    tracking_system.update_order_status(order_id, OrderStatus.IN_TRANSIT)

    # Add tracking information
    tracking_system.add_tracking_info(order_id, "Warehouse", datetime.now())
    tracking_system.add_tracking_info(order_id, "Shipping Hub", datetime.now() + timedelta(hours=2))

    # Get order status and tracking information
    status = tracking_system.get_order_status(order_id)
    tracking_info = tracking_system.get_tracking_info(order_id)

    print(f"Order {order_id} status: {status.name}")
    print("Tracking Information:")
    for location, timestamp in tracking_info:
        print(f"{location} - {timestamp}")

if __name__ == "__main__":
    main()
```
