"""
Generated Code Metadata:
========================
Original URL: https://www.napatablets.com
Prompt: Create a tutorial on how to use the Delivery Tracker for tracking deliveries and analyzing performance metrics in an auto parts business.
Generated: DETERMINISTIC_3383e1f9900a5f7e
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# delivery_tracker.py

class Delivery:
    """Represents a delivery with its status and metrics."""

    def __init__(self, order_id, customer_name, delivery_date, status="pending"):
        """
        Initializes a Delivery object.

        Args:
            order_id (int): Unique identifier for the order.
            customer_name (str): Name of the customer.
            delivery_date (str): Scheduled date of delivery.
            status (str, optional): Status of the delivery. Defaults to "pending".
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.delivery_date = delivery_date
        self.status = status
        self.actual_delivery_date = None

    def update_status(self, status):
        """Updates the status of the delivery."""
        self.status = status

    def record_actual_delivery_date(self, date):
        """Records the actual date of delivery."""
        self.actual_delivery_date = date


class DeliveryTracker:
    """Tracks deliveries and analyzes performance metrics."""

    def __init__(self):
        """Initializes a DeliveryTracker object."""
        self.deliveries = {}

    def add_delivery(self, delivery):
        """Adds a delivery to the tracker."""
        self.deliveries[delivery.order_id] = delivery

    def update_delivery_status(self, order_id, status):
        """Updates the status of a delivery."""
        if order_id in self.deliveries:
            self.deliveries[order_id].update_status(status)
        else:
            raise ValueError("Delivery not found")

    def record_actual_delivery_date(self, order_id, date):
        """Records the actual date of delivery."""
        if order_id in self.deliveries:
            self.deliveries[order_id].record_actual_delivery_date(date)
        else:
            raise ValueError("Delivery not found")

    def get_delivery(self, order_id):
        """Gets a delivery by its order ID."""
        return self.deliveries.get(order_id)

    def calculate_on_time_delivery_rate(self):
        """Calculates the on-time delivery rate."""
        total_deliveries = len(self.deliveries)
        on_time_deliveries = sum(
            1
            for delivery in self.deliveries.values()
            if delivery.actual_delivery_date == delivery.delivery_date
        )
        return (on_time_deliveries / total_deliveries) * 100 if total_deliveries > 0 else 0

    def calculate_average_delivery_time(self):
        """Calculates the average delivery time."""
        total_deliveries = len(self.deliveries)
        total_days = sum(
            (
                datetime.strptime(delivery.actual_delivery_date, "%Y-%m-%d")
                - datetime.strptime(delivery.delivery_date, "%Y-%m-%d")
            ).days
            for delivery in self.deliveries.values()
            if delivery.actual_delivery_date
        )
        return total_days / total_deliveries if total_deliveries > 0 else 0


from datetime import datetime


def main():
    tracker = DeliveryTracker()

    # Create deliveries
    delivery1 = Delivery(1, "John Doe", "2024-09-15")
    delivery2 = Delivery(2, "Jane Doe", "2024-09-16")

    # Add deliveries to tracker
    tracker.add_delivery(delivery1)
    tracker.add_delivery(delivery2)

    # Update delivery status
    tracker.update_delivery_status(1, "shipped")

    # Record actual delivery date
    tracker.record_actual_delivery_date(1, "2024-09-15")
    tracker.record_actual_delivery_date(2, "2024-09-17")

    # Calculate performance metrics
    on_time_delivery_rate = tracker.calculate_on_time_delivery_rate()
    average_delivery_time = tracker.calculate_average_delivery_time()

    print(f"On-time delivery rate: {on_time_delivery_rate}%")
    print(f"Average delivery time: {average_delivery_time} days")


if __name__ == "__main__":
    main()
```
