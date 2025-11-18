"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Write code to model the logistics and warehouse management system for delivering orders to customers' doorsteps, inspired by the infrastructure described on the Aayra International website.
Generated: DETERMINISTIC_d902d645c15416fb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from typing import List, Optional

class Item:
    """Class to represent an item in the warehouse."""
    def __init__(self, item_id: str, name: str, quantity: int):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}) - Quantity: {self.quantity}"

class Order:
    """Class to represent a customer order."""
    def __init__(self, customer_id: str, items: List[Item]):
        self.order_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.items = items
        self.status = "Pending"
        self.order_time = datetime.now()

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer ID: {self.customer_id}, Status: {self.status}, Order Time: {self.order_time}"

class Warehouse:
    """Class to represent a warehouse that holds items."""
    def __init__(self):
        self.inventory = {}

    def add_item(self, item: Item):
        """Add an item to the warehouse inventory."""
        if item.item_id in self.inventory:
            self.inventory[item.item_id].quantity += item.quantity
        else:
            self.inventory[item.item_id] = item

    def remove_item(self, item_id: str, quantity: int) -> Optional[Item]:
        """Remove an item from the warehouse inventory."""
        if item_id in self.inventory and self.inventory[item_id].quantity >= quantity:
            self.inventory[item_id].quantity -= quantity
            if self.inventory[item_id].quantity == 0:
                del self.inventory[item_id]
            return self.inventory.get(item_id)
        raise ValueError("Insufficient quantity or item not found in inventory.")

    def get_inventory(self) -> List[Item]:
        """Get a list of all items in the warehouse inventory."""
        return list(self.inventory.values())

class DeliveryService:
    """Class to handle the delivery of orders."""
    def __init__(self):
        self.deliveries = []

    def schedule_delivery(self, order: Order) -> str:
        """Schedule delivery for an order."""
        delivery_time = datetime.now() + timedelta(days=2)  # 2 days delivery
        self.deliveries.append((order, delivery_time))
        order.status = "Scheduled for Delivery"
        return f"Delivery scheduled for Order ID: {order.order_id} on {delivery_time}"

    def get_deliveries(self) -> List[str]:
        """Get all scheduled deliveries."""
        return [f"Order ID: {order.order_id}, Delivery Time: {delivery_time}" for order, delivery_time in self.deliveries]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the warehouse and delivery service
        warehouse = Warehouse()
        delivery_service = DeliveryService()

        # Add items to the warehouse
        warehouse.add_item(Item("1", "Laptop", 10))
        warehouse.add_item(Item("2", "Smartphone", 15))

        # Create an order
        order_items = [Item("1", "Laptop", 1), Item("2", "Smartphone", 2)]
        order = Order("customer_123", order_items)

        print(order)

        # Remove items from inventory
        for item in order.items:
            warehouse.remove_item(item.item_id, item.quantity)

        # Schedule delivery
        delivery_info = delivery_service.schedule_delivery(order)
        print(delivery_info)

        # List all deliveries
        print(delivery_service.get_deliveries())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
