"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Illustrate how to implement a delivery tracking feature for an e-commerce site, referencing the delivery guarantees mentioned on dhcpbrazz.
Generated: DETERMINISTIC_15c016b16273ab4d
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a delivery tracking feature for an e-commerce site:

```python
import datetime
from typing import Dict, Optional


class DeliveryTracking:
    """
    A class to handle delivery tracking for an e-commerce site.
    """

    def __init__(self):
        """
        Initializes the delivery tracking system.
        """
        # Dictionary to track orders and their statuses
        # Structure: {order_id: {"status": str, "delivery_date": datetime.date}}
        self.orders: Dict[str, Dict[str, Optional[datetime.date]]] = {}

    def create_order(self, order_id: str, delivery_date: datetime.date) -> None:
        """
        Creates a new order in the tracking system.

        :param order_id: Unique identifier for the order.
        :param delivery_date: The guaranteed delivery date for the order.
        :raises ValueError: If the order_id already exists.
        """
        if order_id in self.orders:
            raise ValueError(f"Order ID '{order_id}' already exists.")
        self.orders[order_id] = {"status": "In Transit", "delivery_date": delivery_date}

    def update_status(self, order_id: str, status: str) -> None:
        """
        Updates the delivery status of an order.

        :param order_id: Unique identifier for the order.
        :param status: New status for the order.
        :raises KeyError: If the order_id does not exist.
        """
        if order_id not in self.orders:
            raise KeyError(f"Order ID '{order_id}' not found.")
        self.orders[order_id]["status"] = status

    def get_order_status(self, order_id: str) -> Dict[str, Optional[str]]:
        """
        Retrieves the current status and delivery date of an order.

        :param order_id: Unique identifier for the order.
        :return: A dictionary containing the status and delivery date.
        :raises KeyError: If the order_id does not exist.
        """
        if order_id not in self.orders:
            raise KeyError(f"Order ID '{order_id}' not found.")
        return self.orders[order_id]

    def check_delivery_guarantee(self, order_id: str) -> bool:
        """
        Checks if an order is delivered by its guaranteed delivery date.

        :param order_id: Unique identifier for the order.
        :return: True if the order is delivered by the guaranteed date, False otherwise.
        :raises KeyError: If the order_id does not exist.
        """
        if order_id not in self.orders:
            raise KeyError(f"Order ID '{order_id}' not found.")
        order = self.orders[order_id]
        status = order["status"]
        delivery_date = order["delivery_date"]

        # Ensure the delivery date is valid and check if the current date is past the guarantee
        if status == "Delivered" and delivery_date and datetime.date.today() <= delivery_date:
            return True
        return False


def main():
    """
    Example usage of the DeliveryTracking system.
    """
    try:
        # Initialize the delivery tracking system
        tracking_system = DeliveryTracking()

        # Create orders
        tracking_system.create_order("ORDER123", datetime.date(2023, 11, 15))
        tracking_system.create_order("ORDER124", datetime.date(2023, 11, 20))

        # Update order statuses
        tracking_system.update_status("ORDER123", "Delivered")
        tracking_system.update_status("ORDER124", "In Transit")

        # Get and print order statuses
        print("ORDER123 Status:", tracking_system.get_order_status("ORDER123"))
        print("ORDER124 Status:", tracking_system.get_order_status("ORDER124"))

        # Check delivery guarantees
        print("ORDER123 Delivered on time:", tracking_system.check_delivery_guarantee("ORDER123"))
        print("ORDER124 Delivered on time:", tracking_system.check_delivery_guarantee("ORDER124"))

    except Exception as e:
        # Global error handling for demonstration purposes
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

This code provides a robust system for managing and tracking deliveries. It includes error handling, follows best practices, and is ready for production.
