"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Create a program to track the on-time delivery rate (e.g., 95%) for a fleet of refrigerated transport vehicles, as described on RefrigeratorTransport.com.
Generated: DETERMINISTIC_a94f79ef713b2287
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class Delivery:
    def __init__(self, delivery_id: str, scheduled_time: datetime.datetime, actual_time: datetime.datetime):
        self.delivery_id = delivery_id
        self.scheduled_time = scheduled_time
        self.actual_time = actual_time

    def is_on_time(self) -> bool:
        """Check if the delivery was on time."""
        return self.actual_time <= self.scheduled_time

class DeliveryTracker:
    def __init__(self):
        self.deliveries: List[Delivery] = []

    def add_delivery(self, delivery_id: str, scheduled_time: datetime.datetime, actual_time: datetime.datetime) -> None:
        """Add a new delivery to the tracker."""
        if actual_time < scheduled_time:
            raise ValueError("Actual delivery time cannot be earlier than scheduled time.")
        self.deliveries.append(Delivery(delivery_id, scheduled_time, actual_time))

    def calculate_on_time_rate(self) -> float:
        """Calculate the on-time delivery rate as a percentage."""
        if not self.deliveries:
            return 0.0  # Avoid division by zero

        on_time_deliveries = sum(delivery.is_on_time() for delivery in self.deliveries)
        return (on_time_deliveries / len(self.deliveries)) * 100

    def get_delivery_report(self) -> Dict[str, float]:
        """Generate a report of the on-time delivery rate."""
        return {
            "total_deliveries": len(self.deliveries),
            "on_time_rate": self.calculate_on_time_rate(),
        }

# Example usage
if __name__ == "__main__":
    tracker = DeliveryTracker()
    
    # Adding deliveries with scheduled and actual times
    try:
        tracker.add_delivery("D001", datetime.datetime(2023, 10, 1, 14, 0), datetime.datetime(2023, 10, 1, 14, 10))
        tracker.add_delivery("D002", datetime.datetime(2023, 10, 1, 15, 0), datetime.datetime(2023, 10, 1, 15, 0))
        tracker.add_delivery("D003", datetime.datetime(2023, 10, 1, 16, 0), datetime.datetime(2023, 10, 1, 16, 30))  # Late delivery
        tracker.add_delivery("D004", datetime.datetime(2023, 10, 1, 17, 0), datetime.datetime(2023, 10, 1, 17, 0))

        # Generate and print delivery report
        report = tracker.get_delivery_report()
        print(f"Total Deliveries: {report['total_deliveries']}")
        print(f"On-Time Delivery Rate: {report['on_time_rate']:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
```
