"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Provide code to implement a system for tracking and improving recruitment metrics (quality, time, and cost) using Kaizen principles, as described in Terawit's Tera Recruit service.
Generated: DETERMINISTIC_622990b7e0082b02
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import List, Dict, Any

class RecruitmentMetric:
    """
    A class to represent recruitment metrics.
    """

    def __init__(self, quality: float, time: float, cost: float):
        """
        Initialize the recruitment metrics.

        :param quality: Quality of hire metric (0-100 scale)
        :param time: Time to hire in days
        :param cost: Cost per hire in currency units
        """
        self.quality = quality
        self.time = time
        self.cost = cost
        self.timestamp = datetime.datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the metrics to a dictionary for easy serialization.

        :return: Dictionary representation of the metrics
        """
        return {
            "quality": self.quality,
            "time": self.time,
            "cost": self.cost,
            "timestamp": self.timestamp.isoformat()
        }


class RecruitmentTracker:
    """
    A class to track and improve recruitment metrics using Kaizen principles.
    """

    def __init__(self):
        """
        Initialize the recruitment tracker with an empty metrics list.
        """
        self.metrics: List[RecruitmentMetric] = []

    def add_metric(self, quality: float, time: float, cost: float) -> None:
        """
        Add a new recruitment metric to the tracker.

        :param quality: Quality of hire metric (0-100 scale)
        :param time: Time to hire in days
        :param cost: Cost per hire in currency units
        """
        if not (0 <= quality <= 100):
            raise ValueError("Quality must be between 0 and 100.")
        if time < 0:
            raise ValueError("Time cannot be negative.")
        if cost < 0:
            raise ValueError("Cost cannot be negative.")

        metric = RecruitmentMetric(quality, time, cost)
        self.metrics.append(metric)

    def calculate_average_metrics(self) -> Dict[str, float]:
        """
        Calculate average recruitment metrics.

        :return: Dictionary with average quality, time, and cost
        """
        if not self.metrics:
            raise ValueError("No metrics available to calculate averages.")

        total_quality = sum(metric.quality for metric in self.metrics)
        total_time = sum(metric.time for metric in self.metrics)
        total_cost = sum(metric.cost for metric in self.metrics)

        average_metrics = {
            "average_quality": total_quality / len(self.metrics),
            "average_time": total_time / len(self.metrics),
            "average_cost": total_cost / len(self.metrics)
        }

        return average_metrics

    def save_metrics_to_file(self, filename: str) -> None:
        """
        Save the recruitment metrics to a JSON file.

        :param filename: The name of the file to save the metrics
        """
        try:
            with open(filename, 'w') as file:
                json.dump([metric.to_dict() for metric in self.metrics], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write to file {filename}: {e}")

    def load_metrics_from_file(self, filename: str) -> None:
        """
        Load recruitment metrics from a JSON file.

        :param filename: The name of the file to load the metrics from
        """
        try:
            with open(filename, 'r') as file:
                metrics_data = json.load(file)
                for data in metrics_data:
                    self.add_metric(data['quality'], data['time'], data['cost'])
        except (IOError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to read from file {filename}: {e}")


# Example usage
if __name__ == "__main__":
    tracker = RecruitmentTracker()
    
    # Adding some metrics
    tracker.add_metric(85, 30, 5000)
    tracker.add_metric(90, 25, 4500)
    
    # Calculate and print average metrics
    averages = tracker.calculate_average_metrics()
    print("Average Recruitment Metrics:", averages)
    
    # Save metrics to a file
    tracker.save_metrics_to_file("recruitment_metrics.json")
    
    # Load metrics from a file
    tracker.load_metrics_from_file("recruitment_metrics.json")
```
