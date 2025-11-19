"""
Generated Code Metadata:
========================
Original URL: https://ircmhealth.com
Prompt: Create a sample code for tracking revenue cycle metrics in a healthcare application.
Generated: DETERMINISTIC_33ecb6d524744e4b
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class RevenueCycleMetric:
    """
    A class to represent a revenue cycle metric in a healthcare application.
    """

    def __init__(self, date: datetime.date, total_revenue: float, total_expenses: float):
        """
        Initializes a new instance of RevenueCycleMetric.

        :param date: The date of the metric.
        :param total_revenue: Total revenue for the day.
        :param total_expenses: Total expenses for the day.
        """
        self.date = date
        self.total_revenue = total_revenue
        self.total_expenses = total_expenses

    @property
    def net_revenue(self) -> float:
        """
        Calculates the net revenue.

        :return: Net revenue (total revenue - total expenses).
        """
        return self.total_revenue - self.total_expenses


class RevenueCycleTracker:
    """
    A class to track revenue cycle metrics over time.
    """

    def __init__(self):
        """
        Initializes a new instance of RevenueCycleTracker with an empty metrics list.
        """
        self.metrics: List[RevenueCycleMetric] = []

    def add_metric(self, metric: RevenueCycleMetric) -> None:
        """
        Adds a new revenue cycle metric to the tracker.

        :param metric: An instance of RevenueCycleMetric to add.
        """
        self.metrics.append(metric)

    def get_metrics(self) -> List[Dict[str, Optional[float]]]:
        """
        Retrieves all metrics in a structured format.

        :return: A list of dictionaries containing date, total revenue, total expenses, and net revenue.
        """
        return [
            {
                "date": metric.date,
                "total_revenue": metric.total_revenue,
                "total_expenses": metric.total_expenses,
                "net_revenue": metric.net_revenue
            }
            for metric in self.metrics
        ]

    def calculate_average_net_revenue(self) -> float:
        """
        Calculates the average net revenue across all metrics.

        :return: Average net revenue.
        :raises ValueError: If there are no metrics to calculate the average.
        """
        if not self.metrics:
            raise ValueError("No metrics available to calculate average net revenue.")
        
        total_net_revenue = sum(metric.net_revenue for metric in self.metrics)
        return total_net_revenue / len(self.metrics)


# Example usage
if __name__ == "__main__":
    tracker = RevenueCycleTracker()

    # Adding sample metrics
    try:
        tracker.add_metric(RevenueCycleMetric(datetime.date(2023, 10, 1), 10000.0, 7000.0))
        tracker.add_metric(RevenueCycleMetric(datetime.date(2023, 10, 2), 15000.0, 8000.0))
        tracker.add_metric(RevenueCycleMetric(datetime.date(2023, 10, 3), 12000.0, 6000.0))

        # Retrieving metrics
        metrics = tracker.get_metrics()
        for metric in metrics:
            print(metric)

        # Calculating average net revenue
        average_net_revenue = tracker.calculate_average_net_revenue()
        print(f"Average Net Revenue: {average_net_revenue:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
