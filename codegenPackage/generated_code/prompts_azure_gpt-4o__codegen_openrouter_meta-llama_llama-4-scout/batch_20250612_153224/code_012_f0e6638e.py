"""
Generated Code Metadata:
========================
Original URL: https://www.vidaglobaltrade.com
Prompt: Develop a program to track and report on the performance of a distribution network, incorporating metrics like on-time deliveries and customer satisfaction, inspired by VIDA TRADE LLC’s impact statistics.
Generated: DETERMINISTIC_f0e6638e89b86e5d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# distribution_network_tracker.py

import datetime
from typing import Dict, List

class Delivery:
    """Represents a delivery with its status and customer satisfaction."""

    def __init__(self, delivery_id: int, expected_date: datetime.date, actual_date: datetime.date = None, customer_satisfaction: int = None):
        """
        Initializes a Delivery object.

        Args:
        - delivery_id (int): Unique identifier for the delivery.
        - expected_date (datetime.date): Expected date of delivery.
        - actual_date (datetime.date, optional): Actual date of delivery. Defaults to None.
        - customer_satisfaction (int, optional): Customer satisfaction rating (1-5). Defaults to None.
        """
        self.delivery_id = delivery_id
        self.expected_date = expected_date
        self.actual_date = actual_date
        self.customer_satisfaction = customer_satisfaction

    def is_on_time(self) -> bool:
        """Checks if the delivery was on time."""
        return self.actual_date == self.expected_date

    def __repr__(self):
        return f"Delivery(delivery_id={self.delivery_id}, expected_date={self.expected_date}, actual_date={self.actual_date}, customer_satisfaction={self.customer_satisfaction})"


class DistributionNetwork:
    """Tracks and reports on the performance of a distribution network."""

    def __init__(self):
        """Initializes a DistributionNetwork object."""
        self.deliveries: List[Delivery] = []

    def add_delivery(self, delivery: Delivery):
        """
        Adds a delivery to the distribution network.

        Args:
        - delivery (Delivery): Delivery object to add.
        """
        self.deliveries.append(delivery)

    def get_on_time_deliveries(self) -> int:
        """Gets the number of on-time deliveries."""
        return sum(1 for delivery in self.deliveries if delivery.is_on_time())

    def get_total_deliveries(self) -> int:
        """Gets the total number of deliveries."""
        return len(self.deliveries)

    def get_on_time_delivery_rate(self) -> float:
        """Gets the on-time delivery rate."""
        total_deliveries = self.get_total_deliveries()
        if total_deliveries == 0:
            return 0.0
        return self.get_on_time_deliveries() / total_deliveries

    def get_average_customer_satisfaction(self) -> float:
        """Gets the average customer satisfaction rating."""
        satisfaction_ratings = [delivery.customer_satisfaction for delivery in self.deliveries if delivery.customer_satisfaction is not None]
        if not satisfaction_ratings:
            return 0.0
        return sum(satisfaction_ratings) / len(satisfaction_ratings)

    def generate_report(self) -> Dict[str, str]:
        """
        Generates a performance report for the distribution network.

        Returns:
        - Dict[str, str]: Performance report with metrics.
        """
        report = {
            "Total Deliveries": str(self.get_total_deliveries()),
            "On-Time Deliveries": str(self.get_on_time_deliveries()),
            "On-Time Delivery Rate": f"{self.get_on_time_delivery_rate():.2%}",
            "Average Customer Satisfaction": f"{self.get_average_customer_satisfaction():.2f}/5"
        }
        return report


def main():
    # Example usage
    network = DistributionNetwork()

    delivery1 = Delivery(1, datetime.date(2024, 9, 1), datetime.date(2024, 9, 1), 5)
    delivery2 = Delivery(2, datetime.date(2024, 9, 2), datetime.date(2024, 9, 3), 4)
    delivery3 = Delivery(3, datetime.date(2024, 9, 3), datetime.date(2024, 9, 3), 5)

    network.add_delivery(delivery1)
    network.add_delivery(delivery2)
    network.add_delivery(delivery3)

    report = network.generate_report()

    print("Distribution Network Performance Report:")
    for metric, value in report.items():
        print(f"{metric}: {value}")


if __name__ == "__main__":
    main()
```
