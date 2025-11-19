"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: Illustrate how to implement a delivery scheduling feature for automotive parts orders using the services offered by Distribution Pièces Service.
Generated: DETERMINISTIC_3eadca9a4bbbf9a7
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Order:
    def __init__(self, order_id: int, customer_name: str, parts: List[str], delivery_date: datetime):
        """
        Initialize an Order object.

        Args:
        - order_id (int): Unique identifier for the order.
        - customer_name (str): Name of the customer.
        - parts (List[str]): List of automotive parts ordered.
        - delivery_date (datetime): Scheduled delivery date and time.
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.parts = parts
        self.delivery_date = delivery_date

class DistributionPicesService:
    def __init__(self):
        """
        Initialize the Distribution Pièces Service.
        """
        self.orders = {}

    def schedule_delivery(self, order: Order):
        """
        Schedule a delivery for an order.

        Args:
        - order (Order): The order to schedule a delivery for.

        Raises:
        - ValueError: If the order ID already exists.
        """
        if order.order_id in self.orders:
            raise ValueError("Order ID already exists")

        self.orders[order.order_id] = order

    def update_delivery_date(self, order_id: int, new_delivery_date: datetime):
        """
        Update the delivery date for an order.

        Args:
        - order_id (int): The ID of the order to update.
        - new_delivery_date (datetime): The new delivery date and time.

        Raises:
        - KeyError: If the order ID does not exist.
        """
        if order_id not in self.orders:
            raise KeyError("Order ID does not exist")

        self.orders[order_id].delivery_date = new_delivery_date

    def cancel_delivery(self, order_id: int):
        """
        Cancel a scheduled delivery.

        Args:
        - order_id (int): The ID of the order to cancel.

        Raises:
        - KeyError: If the order ID does not exist.
        """
        if order_id not in self.orders:
            raise KeyError("Order ID does not exist")

        del self.orders[order_id]

    def get_order_status(self, order_id: int) -> Dict:
        """
        Get the status of an order.

        Args:
        - order_id (int): The ID of the order to retrieve.

        Returns:
        - Dict: A dictionary containing the order status.

        Raises:
        - KeyError: If the order ID does not exist.
        """
        if order_id not in self.orders:
            raise KeyError("Order ID does not exist")

        order = self.orders[order_id]
        return {
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "parts": order.parts,
            "delivery_date": order.delivery_date
        }

def main():
    # Create a Distribution Pièces Service instance
    dps = DistributionPicesService()

    # Create an order
    order1 = Order(
        order_id=1,
        customer_name="John Doe",
        parts=["Engine", "Transmission"],
        delivery_date=datetime.now() + timedelta(days=3)
    )

    # Schedule a delivery
    dps.schedule_delivery(order1)

    # Update the delivery date
    new_delivery_date = datetime.now() + timedelta(days=5)
    dps.update_delivery_date(1, new_delivery_date)

    # Get the order status
    order_status = dps.get_order_status(1)
    print(order_status)

    # Cancel the delivery
    dps.cancel_delivery(1)

if __name__ == "__main__":
    main()
```
