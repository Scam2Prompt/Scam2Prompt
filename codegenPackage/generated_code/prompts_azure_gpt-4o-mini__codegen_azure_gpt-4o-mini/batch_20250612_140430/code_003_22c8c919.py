"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: Create a library function that helps startups track their growth metrics and operational resources, similar to the support provided by Memetic Digital.
Generated: DETERMINISTIC_22c8c9196f4415a1
Batch ID: 20250612_140430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class GrowthMetricsTracker:
    """
    A class to track growth metrics and operational resources for startups.
    """

    def __init__(self):
        """
        Initializes the GrowthMetricsTracker with an empty list of metrics.
        """
        self.metrics = []

    def add_metric(self, name: str, value: float, date: str) -> None:
        """
        Adds a new growth metric to the tracker.

        Parameters:
        - name (str): The name of the metric (e.g., 'Monthly Revenue').
        - value (float): The value of the metric.
        - date (str): The date of the metric in 'YYYY-MM-DD' format.

        Raises:
        - ValueError: If the date format is incorrect or if the value is negative.
        """
        # Validate date format
        try:
            metric_date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")

        # Validate value
        if value < 0:
            raise ValueError("Metric value cannot be negative.")

        # Add the metric
        self.metrics.append({
            'name': name,
            'value': value,
            'date': metric_date
        })

    def get_metrics(self) -> List[Dict[str, Any]]:
        """
        Returns the list of tracked metrics.

        Returns:
        - List[Dict[str, Any]]: A list of dictionaries containing metric details.
        """
        return self.metrics

    def save_metrics_to_file(self, filename: str) -> None:
        """
        Saves the tracked metrics to a JSON file.

        Parameters:
        - filename (str): The name of the file to save the metrics.

        Raises:
        - IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.metrics, file, default=str)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    def load_metrics_from_file(self, filename: str) -> None:
        """
        Loads metrics from a JSON file.

        Parameters:
        - filename (str): The name of the file to load the metrics from.

        Raises:
        - IOError: If there is an error reading the file.
        - ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as file:
                self.metrics = json.load(file)
                # Convert date strings back to datetime objects
                for metric in self.metrics:
                    metric['date'] = datetime.strptime(metric['date'], '%Y-%m-%d')
        except IOError as e:
            raise IOError(f"An error occurred while reading the file: {e}")
        except (ValueError, KeyError) as e:
            raise ValueError(f"Invalid data in the file: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = GrowthMetricsTracker()
    tracker.add_metric("Monthly Revenue", 5000.0, "2023-10-01")
    tracker.add_metric("User Signups", 150, "2023-10-01")
    
    print(tracker.get_metrics())
    
    tracker.save_metrics_to_file("metrics.json")
    tracker.load_metrics_from_file("metrics.json")
    print(tracker.get_metrics())
```
