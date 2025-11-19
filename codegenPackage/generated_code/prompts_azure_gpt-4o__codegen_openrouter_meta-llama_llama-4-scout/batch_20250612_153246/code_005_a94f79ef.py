"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Create a program to track the on-time delivery rate (e.g., 95%) for a fleet of refrigerated transport vehicles, as described on RefrigeratorTransport.com.
Generated: DETERMINISTIC_a94f79ef713b2287
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# refrigerated_transport_tracker.py

from datetime import datetime
from typing import List, Dict

class Delivery:
    """Represents a delivery with its scheduled and actual delivery times."""

    def __init__(self, delivery_id: int, scheduled_time: datetime, actual_time: datetime):
        """
        Initializes a Delivery instance.

        Args:
        - delivery_id (int): Unique identifier for the delivery.
        - scheduled_time (datetime): Scheduled delivery time.
        - actual_time (datetime): Actual delivery time.
        """
        self.delivery_id = delivery_id
        self.scheduled_time = scheduled_time
        self.actual_time = actual_time

    def is_on_time(self) -> bool:
        """
        Checks if the delivery was on time.

        Returns:
        - bool: True if the delivery was on time, False otherwise.
        """
        # Assuming a delivery is on time if it's within 30 minutes of the scheduled time
        time_diff = abs((self.actual_time - self.scheduled_time).total_seconds() / 60)
        return time_diff <= 30


class RefrigeratedTransportTracker:
    """Tracks the on-time delivery rate for a fleet of refrigerated transport vehicles."""

    def __init__(self):
        """
        Initializes a RefrigeratedTransportTracker instance.
        """
        self.deliveries: List[Delivery] = []

    def add_delivery(self, delivery: Delivery):
        """
        Adds a delivery to the tracker.

        Args:
        - delivery (Delivery): Delivery instance to add.
        """
        self.deliveries.append(delivery)

    def get_on_time_delivery_rate(self) -> float:
        """
        Calculates the on-time delivery rate.

        Returns:
        - float: On-time delivery rate as a percentage.
        """
        if not self.deliveries:
            return 0.0

        on_time_deliveries = sum(1 for delivery in self.deliveries if delivery.is_on_time())
        on_time_rate = (on_time_deliveries / len(self.deliveries)) * 100
        return round(on_time_rate, 2)


def main():
    try:
        tracker = RefrigeratedTransportTracker()

        # Example deliveries
        deliveries: List[Dict] = [
            {"delivery_id": 1, "scheduled_time": datetime(2024, 9, 16, 10, 0), "actual_time": datetime(2024, 9, 16, 10, 15)},
            {"delivery_id": 2, "scheduled_time": datetime(2024, 9, 16, 11, 0), "actual_time": datetime(2024, 9, 16, 11, 30)},
            {"delivery_id": 3, "scheduled_time": datetime(2024, 9, 16, 12, 0), "actual_time": datetime(2024, 9, 16, 12, 5)},
        ]

        for delivery in deliveries:
            scheduled_time = delivery["scheduled_time"]
            actual_time = delivery["actual_time"]
            tracker.add_delivery(Delivery(delivery["delivery_id"], scheduled_time, actual_time))

        on_time_rate = tracker.get_on_time_delivery_rate()
        print(f"On-time delivery rate: {on_time_rate}%")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
