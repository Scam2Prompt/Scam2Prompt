"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: Recommend tools or libraries for tracking sustainability metrics in architectural projects, inspired by Études' commitment to innovation and sustainability.
Generated: DETERMINISTIC_a2e924d26588b9b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sustainability_tracker.py

"""
A module for tracking sustainability metrics in architectural projects.
This module provides a simple interface to log and analyze sustainability metrics
inspired by Études' commitment to innovation and sustainability.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SustainabilityMetric:
    """
    A class to represent a sustainability metric for an architectural project.
    """

    def __init__(self, name, value, unit, timestamp=None):
        """
        Initializes a new sustainability metric.

        :param name: Name of the sustainability metric (e.g., 'Energy Consumption').
        :param value: Value of the metric (e.g., 150).
        :param unit: Unit of the metric (e.g., 'kWh').
        :param timestamp: Timestamp of when the metric was recorded (default is now).
        """
        self.name = name
        self.value = value
        self.unit = unit
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        """Converts the metric to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'value': self.value,
            'unit': self.unit,
            'timestamp': self.timestamp.isoformat()
        }

class SustainabilityTracker:
    """
    A class to track and store sustainability metrics.
    """

    def __init__(self, filename='sustainability_metrics.json'):
        """
        Initializes the sustainability tracker.

        :param filename: The filename where metrics will be stored.
        """
        self.filename = filename
        self.metrics = []
        self.load_metrics()

    def load_metrics(self):
        """Loads existing metrics from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.metrics = json.load(file)
                logging.info("Metrics loaded successfully.")
        except FileNotFoundError:
            logging.warning("Metrics file not found. Starting with an empty list.")
            self.metrics = []
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the metrics file. Starting fresh.")
            self.metrics = []

    def save_metrics(self):
        """Saves the current metrics to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.metrics, file, indent=4)
                logging.info("Metrics saved successfully.")
        except IOError as e:
            logging.error(f"Error saving metrics to file: {e}")

    def add_metric(self, metric):
        """
        Adds a new sustainability metric to the tracker.

        :param metric: An instance of SustainabilityMetric to add.
        """
        if not isinstance(metric, SustainabilityMetric):
            logging.error("Invalid metric type. Must be an instance of SustainabilityMetric.")
            return
        
        self.metrics.append(metric.to_dict())
        self.save_metrics()

    def get_metrics(self):
        """Returns the list of tracked sustainability metrics."""
        return self.metrics

# Example usage
if __name__ == "__main__":
    tracker = SustainabilityTracker()

    # Adding a sample metric
    energy_metric = SustainabilityMetric(name='Energy Consumption', value=150, unit='kWh')
    tracker.add_metric(energy_metric)

    # Retrieve and print all metrics
    all_metrics = tracker.get_metrics()
    print(json.dumps(all_metrics, indent=4))
```
