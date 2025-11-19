"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Illustrate how to implement a delivery scheduling feature for automotive parts orders using the services offered by Distribution Pièces Service.
Generated: DETERMINISTIC_3eadca9a4bbbf9a7
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import datetime
from typing import List, Dict, Any

class DeliveryScheduler:
    """
    A class to schedule deliveries for automotive parts orders.
    """

    def __init__(self):
        self.orders = []  # Holds scheduled orders

    def add_order(self, order: Dict[str, Any]):
        """
        Adds a new order to the schedule.
        
        :param order: A dictionary containing order details like 'order_id', 'delivery_date', and 'parts'.
        :raises ValueError: If the delivery date is in the past or if required fields are missing.
        """
        if not self.validate_order(order):
            raise ValueError("Order validation failed. Ensure order_id, delivery_date, and parts are provided.")

        delivery_date = self.parse_delivery_date(order['delivery_date'])
        if delivery_date < datetime.datetime.now():
            raise ValueError("Delivery date cannot be in the past.")

        self.orders.append(order)
        print(f"Order {order['order_id']} scheduled for delivery on {delivery_date.date()}.")

    @staticmethod
    def validate_order(order: Dict[str, Any]) -> bool:
        """
        Validates the order to ensure all required information is present.
        
        :param order: Order details dictionary.
        :return: True if valid, False otherwise.
        """
        required_fields = ['order_id', 'delivery_date', 'parts']
        return all(field in order for field in required_fields)

    @staticmethod
    def parse_delivery_date(date_str: str) -> datetime.datetime:
        """
        Parses a delivery date string into a datetime object.
        
        :param date_str: The delivery date in string format.
        :return: Parsed datetime object.
        :raises ValueError: If the date format is incorrect.
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.") from e

    def get_scheduled_deliveries(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of scheduled deliveries.
        
        :return: List of orders scheduled for delivery.
        """
        return self.orders

# Example usage
if __name__ == "__main__":
    scheduler = DeliveryScheduler()

    # Sample order to schedule
    order_example = {
        'order_id': '12345',
        'delivery_date': '2023-12-01',
        'parts': ['brake pads', 'oil filter']
    }

    try:
        scheduler.add_order(order_example)
    except ValueError as e:
        print(f"Error scheduling order: {e}")
    
    # Display scheduled deliveries
    scheduled_orders = scheduler.get_scheduled_deliveries()
    print("Scheduled Deliveries:")
    for order in scheduled_orders:
        print(order)
```
