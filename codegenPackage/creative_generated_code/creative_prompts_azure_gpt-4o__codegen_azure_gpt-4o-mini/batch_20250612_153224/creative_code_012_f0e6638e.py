"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vidaglobaltrade.com
Prompt: Develop a program to track and report on the performance of a distribution network, incorporating metrics like on-time deliveries and customer satisfaction, inspired by VIDA TRADE LLC’s impact statistics.
Generated: DETERMINISTIC_f0e6638e89b86e5d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Delivery:
    """Class representing a delivery in the distribution network."""

    def __init__(self, delivery_id: str, customer_id: str, delivery_date: str, status: str, satisfaction: float):
        self.delivery_id = delivery_id
        self.customer_id = customer_id
        self.delivery_date = datetime.strptime(delivery_date, "%Y-%m-%d")
        self.status = status  # e.g., "on-time", "delayed"
        self.satisfaction = satisfaction  # Customer satisfaction score from 0 to 100

    def is_on_time(self) -> bool:
        """Check if the delivery was on time."""
        return self.status == "on-time"

class DistributionNetwork:
    """Class to manage and report on delivery metrics."""

    def __init__(self):
        self.deliveries: List[Delivery] = []

    def add_delivery(self, delivery: Delivery) -> None:
        """Add a new delivery to the network."""
        self.deliveries.append(delivery)

    def calculate_metrics(self) -> Dict[str, Any]:
        """Calculate performance metrics for the distribution network."""
        if not self.deliveries:
            raise ValueError("No deliveries recorded.")

        total_deliveries = len(self.deliveries)
        on_time_deliveries = sum(1 for d in self.deliveries if d.is_on_time())
        average_satisfaction = sum(d.satisfaction for d in self.deliveries) / total_deliveries

        metrics = {
            "total_deliveries": total_deliveries,
            "on_time_deliveries": on_time_deliveries,
            "on_time_percentage": (on_time_deliveries / total_deliveries) * 100,
            "average_satisfaction": average_satisfaction
        }

        return metrics

    def report_metrics(self) -> None:
        """Print the performance metrics in a readable format."""
        try:
            metrics = self.calculate_metrics()
            metrics_report = json.dumps(metrics, indent=4)
            print("Distribution Network Performance Metrics:")
            print(metrics_report)
        except ValueError as e:
            print(f"Error: {e}")

def main():
    # Create a distribution network instance
    network = DistributionNetwork()

    # Sample deliveries (in a real application, this data might come from a database)
    deliveries_data = [
        {"delivery_id": "D1", "customer_id": "C1", "delivery_date": "2023-10-01", "status": "on-time", "satisfaction": 95},
        {"delivery_id": "D2", "customer_id": "C2", "delivery_date": "2023-10-02", "status": "delayed", "satisfaction": 80},
        {"delivery_id": "D3", "customer_id": "C3", "delivery_date": "2023-10-03", "status": "on-time", "satisfaction": 90},
    ]

    # Add deliveries to the network
    for delivery_data in deliveries_data:
        delivery = Delivery(**delivery_data)
        network.add_delivery(delivery)

    # Report the performance metrics
    network.report_metrics()

if __name__ == "__main__":
    main()
```
