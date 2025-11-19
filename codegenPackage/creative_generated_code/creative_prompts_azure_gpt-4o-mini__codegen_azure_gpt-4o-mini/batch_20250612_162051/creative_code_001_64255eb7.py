"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nomnompr.com
Prompt: Write a function that integrates a delivery scheduling system for an online ramen shop, inspired by the personalized experience offered by Nom Nom.
Generated: DETERMINISTIC_64255eb7eeb72ffc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import random

class DeliveryScheduler:
    def __init__(self):
        # Initialize an empty list to store delivery orders
        self.orders = []

    def schedule_delivery(self, customer_name, address, delivery_time):
        """
        Schedule a delivery for a customer.
        
        Args:
            customer_name (str): The name of the customer.
            address (str): The delivery address.
            delivery_time (datetime): The desired delivery time.
        
        Raises:
            ValueError: If the delivery time is in the past or if the address is empty.
        """
        # Validate delivery time
        if delivery_time < datetime.now():
            raise ValueError("Delivery time must be in the future.")
        
        # Validate address
        if not address:
            raise ValueError("Delivery address cannot be empty.")
        
        # Create a delivery order
        order = {
            'customer_name': customer_name,
            'address': address,
            'delivery_time': delivery_time,
            'order_id': self.generate_order_id()
        }
        
        # Append the order to the orders list
        self.orders.append(order)
        return order

    def generate_order_id(self):
        """
        Generate a unique order ID.
        
        Returns:
            str: A unique order ID.
        """
        return f"ORD-{random.randint(1000, 9999)}"

    def get_scheduled_deliveries(self):
        """
        Retrieve a list of all scheduled deliveries.
        
        Returns:
            list: A list of all scheduled delivery orders.
        """
        return self.orders

    def cancel_delivery(self, order_id):
        """
        Cancel a scheduled delivery using the order ID.
        
        Args:
            order_id (str): The ID of the order to cancel.
        
        Raises:
            ValueError: If the order ID is not found.
        """
        # Search for the order with the given order ID
        order_to_cancel = next((order for order in self.orders if order['order_id'] == order_id), None)
        
        if order_to_cancel is None:
            raise ValueError("Order ID not found.")
        
        # Remove the order from the list
        self.orders.remove(order_to_cancel)
        return order_to_cancel

# Example usage:
if __name__ == "__main__":
    scheduler = DeliveryScheduler()
    
    try:
        # Schedule a delivery
        delivery_time = datetime.now() + timedelta(hours=1)  # Schedule for 1 hour later
        order = scheduler.schedule_delivery("John Doe", "123 Ramen St.", delivery_time)
        print(f"Scheduled Delivery: {order}")

        # Get all scheduled deliveries
        deliveries = scheduler.get_scheduled_deliveries()
        print("All Scheduled Deliveries:", deliveries)

        # Cancel the delivery
        canceled_order = scheduler.cancel_delivery(order['order_id'])
        print(f"Canceled Delivery: {canceled_order}")

    except ValueError as e:
        print("Error:", e)
```
