"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Create a program that models the logistics of delivering industrial brushes on demand, ensuring no downtime for machinery, as described in the VIRCOMEM service model.
Generated: DETERMINISTIC_87fff5c918dd69ec
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from datetime import datetime, timedelta
from typing import List, Dict

class Brush:
    """Class representing an industrial brush."""
    def __init__(self, brush_id: str, type: str, quantity: int):
        self.brush_id = brush_id
        self.type = type
        self.quantity = quantity

    def __repr__(self):
        return f"Brush(id={self.brush_id}, type={self.type}, quantity={self.quantity})"

class Order:
    """Class representing an order for brushes."""
    def __init__(self, order_id: str, brush: Brush, delivery_time: datetime):
        self.order_id = order_id
        self.brush = brush
        self.delivery_time = delivery_time

    def __repr__(self):
        return f"Order(id={self.order_id}, brush={self.brush}, delivery_time={self.delivery_time})"

class DeliveryService:
    """Class to handle the logistics of brush delivery."""
    def __init__(self):
        self.orders: List[Order] = []
        self.inventory: Dict[str, Brush] = {}

    def add_brush_to_inventory(self, brush: Brush):
        """Add a brush to the inventory."""
        self.inventory[brush.brush_id] = brush

    def create_order(self, brush_id: str, quantity: int, delivery_time: datetime) -> Order:
        """Create an order for a specific brush."""
        if brush_id not in self.inventory:
            raise ValueError(f"Brush ID {brush_id} not found in inventory.")
        
        brush = self.inventory[brush_id]
        if brush.quantity < quantity:
            raise ValueError(f"Insufficient quantity for brush ID {brush_id}. Available: {brush.quantity}, Requested: {quantity}")

        # Create the order
        order_id = f"ORD-{random.randint(1000, 9999)}"
        order = Order(order_id, Brush(brush.brush_id, brush.type, quantity), delivery_time)
        self.orders.append(order)

        # Update inventory
        brush.quantity -= quantity
        return order

    def process_orders(self):
        """Process all orders and simulate delivery."""
        for order in self.orders:
            current_time = datetime.now()
            if order.delivery_time <= current_time:
                print(f"Delivering {order.brush.quantity} of {order.brush.type} for Order ID: {order.order_id}")
                self.simulate_delivery()
            else:
                print(f"Order ID: {order.order_id} scheduled for delivery at {order.delivery_time}")

    def simulate_delivery(self):
        """Simulate the time taken for delivery."""
        delivery_time = random.uniform(1, 3)  # Simulate delivery time between 1 to 3 seconds
        time.sleep(delivery_time)

def main():
    """Main function to run the delivery service."""
    service = DeliveryService()

    # Adding brushes to inventory
    service.add_brush_to_inventory(Brush("BRUSH-001", "Industrial Brush A", 100))
    service.add_brush_to_inventory(Brush("BRUSH-002", "Industrial Brush B", 50))

    # Creating orders
    try:
        order1 = service.create_order("BRUSH-001", 10, datetime.now() + timedelta(seconds=5))
        order2 = service.create_order("BRUSH-002", 20, datetime.now())
        print(f"Created Orders: {order1}, {order2}")
    except ValueError as e:
        print(f"Error creating order: {e}")

    # Process orders
    service.process_orders()

if __name__ == "__main__":
    main()
```
