"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delivery-services.online
Prompt: What are the best practices for implementing delivery services in an online business?
Generated: DETERMINISTIC_96ad3dc654d67b09
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This code implements a delivery service module for an online business. 
It includes functionality for handling delivery orders, calculating delivery costs, 
tracking delivery status, and managing errors effectively.
"""

import datetime

class DeliveryService:
    """
    A class to handle delivery services for an online business.
    """
    def __init__(self):
        # Initialize delivery service with an empty list of orders
        self.orders = []

    def add_order(self, order_id, delivery_address, delivery_distance):
        """
        Adds a new delivery order to the system.

        Args:
            order_id (str): Unique identifier for the order.
            delivery_address (str): Address to deliver the order.
            delivery_distance (float): Distance to the delivery location in kilometers.

        Returns:
            dict: The created order details.
        """
        if delivery_distance <= 0:
            raise ValueError("Delivery distance must be greater than zero.")

        order = {
            "order_id": order_id,
            "delivery_address": delivery_address,
            "delivery_distance": delivery_distance,
            "delivery_cost": self.calculate_delivery_cost(delivery_distance),
            "status": "Pending",
            "created_at": datetime.datetime.now()
        }

        self.orders.append(order)
        return order

    @staticmethod
    def calculate_delivery_cost(distance):
        """
        Calculates delivery cost based on distance.

        Args:
            distance (float): Distance in kilometers.

        Returns:
            float: Delivery cost in USD.
        """
        base_cost = 5.00  # Base cost in USD
        cost_per_km = 1.00  # Cost per kilometer in USD
        return base_cost + (cost_per_km * distance)

    def update_order_status(self, order_id, status):
        """
        Updates the delivery status of an order.

        Args:
            order_id (str): Unique identifier for the order.
            status (str): New status of the order (e.g., "Delivered", "In Transit").

        Returns:
            dict: The updated order details if successful.
        """
        order = self.get_order_by_id(order_id)
        if order is None:
            raise ValueError(f"Order with ID {order_id} not found.")

        order["status"] = status
        order["updated_at"] = datetime.datetime.now()
        return order

    def get_order_by_id(self, order_id):
        """
        Retrieves an order by its unique ID.

        Args:
            order_id (str): Unique identifier for the order.

        Returns:
            dict: The order details if found, or None if not found.
        """
        for order in self.orders:
            if order["order_id"] == order_id:
                return order
        return None

    def list_orders(self):
        """
        Lists all delivery orders in the system.

        Returns:
            list: A list of all orders.
        """
        return self.orders


# Example usage:
if __name__ == "__main__":
    try:
        delivery_service = DeliveryService()

        # Add a new order
        order = delivery_service.add_order(
            order_id="ORDER123",
            delivery_address="123 Main Street, Example City",
            delivery_distance=10.5
        )
        print("Order added:", order)

        # Update order status
        updated_order = delivery_service.update_order_status(order_id="ORDER123", status="In Transit")
        print("Order updated:", updated_order)

        # List all orders
        all_orders = delivery_service.list_orders()
        print("All orders:", all_orders)

    except Exception as e:
        print("An error occurred:", str(e))
```
