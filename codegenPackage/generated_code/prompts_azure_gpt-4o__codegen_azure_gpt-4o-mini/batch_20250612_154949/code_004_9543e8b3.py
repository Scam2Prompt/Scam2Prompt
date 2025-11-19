"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Create a Python program to automate the tracking of digital transformation metrics, incorporating principles mentioned by Romain Rissoan.
Generated: DETERMINISTIC_9543e8b3f7c2abac
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import Dict, Any, List

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DigitalTransformationMetrics:
    """
    A class to track and manage digital transformation metrics.
    """

    def __init__(self, metrics_file: str):
        """
        Initializes the DigitalTransformationMetrics with a specified metrics file.

        :param metrics_file: Path to the JSON file where metrics will be stored.
        """
        self.metrics_file = metrics_file
        self.metrics_data = self.load_metrics()

    def load_metrics(self) -> Dict[str, Any]:
        """
        Loads metrics from the JSON file.

        :return: A dictionary containing the metrics data.
        """
        try:
            with open(self.metrics_file, 'r') as file:
                metrics = json.load(file)
                logging.info("Metrics loaded successfully.")
                return metrics
        except FileNotFoundError:
            logging.warning("Metrics file not found. Initializing with empty metrics.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from metrics file. Initializing with empty metrics.")
            return {}

    def save_metrics(self) -> None:
        """
        Saves the current metrics data to the JSON file.
        """
        try:
            with open(self.metrics_file, 'w') as file:
                json.dump(self.metrics_data, file, indent=4)
                logging.info("Metrics saved successfully.")
        except IOError as e:
            logging.error(f"Error saving metrics to file: {e}")

    def add_metric(self, name: str, value: Any) -> None:
        """
        Adds a new metric or updates an existing one.

        :param name: The name of the metric.
        :param value: The value of the metric.
        """
        self.metrics_data[name] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }
        logging.info(f"Metric '{name}' added/updated with value: {value}.")
        self.save_metrics()

    def get_metric(self, name: str) -> Any:
        """
        Retrieves the value of a specified metric.

        :param name: The name of the metric to retrieve.
        :return: The value of the metric or None if not found.
        """
        metric = self.metrics_data.get(name)
        if metric:
            logging.info(f"Retrieved metric '{name}': {metric['value']} at {metric['timestamp']}.")
            return metric['value']
        else:
            logging.warning(f"Metric '{name}' not found.")
            return None

    def list_metrics(self) -> List[str]:
        """
        Lists all the metrics currently being tracked.

        :return: A list of metric names.
        """
        metrics_list = list(self.metrics_data.keys())
        logging.info(f"Current metrics: {metrics_list}.")
        return metrics_list

if __name__ == "__main__":
    # Example usage of the DigitalTransformationMetrics class
    metrics_tracker = DigitalTransformationMetrics('metrics.json')

    # Adding some metrics
    metrics_tracker.add_metric('customer_satisfaction', 85)
    metrics_tracker.add_metric('digital_engagement', 75)

    # Retrieving a metric
    satisfaction = metrics_tracker.get_metric('customer_satisfaction')

    # Listing all metrics
    all_metrics = metrics_tracker.list_metrics()
```
