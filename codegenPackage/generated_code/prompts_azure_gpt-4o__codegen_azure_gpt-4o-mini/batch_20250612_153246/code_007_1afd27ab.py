"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Provide a Python-based solution for tracking and reporting sustainability metrics in green building projects, inspired by the offerings of Bismillah Traders.
Generated: DETERMINISTIC_1afd27ab08b7df76
Batch ID: 20250612_153246
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SustainabilityMetric:
    """Class to represent a sustainability metric for a green building project."""
    
    def __init__(self, name, value, unit, date_recorded=None):
        """
        Initialize a sustainability metric.

        :param name: Name of the sustainability metric (e.g., 'Energy Consumption').
        :param value: Value of the metric.
        :param unit: Unit of measurement (e.g., 'kWh', 'kg CO2').
        :param date_recorded: Date when the metric was recorded. Defaults to today.
        """
        self.name = name
        self.value = value
        self.unit = unit
        self.date_recorded = date_recorded or datetime.now().isoformat()

    def to_dict(self):
        """Convert the metric to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'value': self.value,
            'unit': self.unit,
            'date_recorded': self.date_recorded
        }

class SustainabilityTracker:
    """Class to track and report sustainability metrics for green building projects."""
    
    def __init__(self):
        """Initialize the tracker with an empty list of metrics."""
        self.metrics = []

    def add_metric(self, metric):
        """
        Add a sustainability metric to the tracker.

        :param metric: An instance of SustainabilityMetric to add.
        """
        if not isinstance(metric, SustainabilityMetric):
            logging.error("Invalid metric type. Must be an instance of SustainabilityMetric.")
            raise ValueError("Invalid metric type. Must be an instance of SustainabilityMetric.")
        
        self.metrics.append(metric)
        logging.info(f"Added metric: {metric.to_dict()}")

    def report_metrics(self):
        """Generate a report of all tracked sustainability metrics."""
        report = [metric.to_dict() for metric in self.metrics]
        logging.info("Generated report of sustainability metrics.")
        return json.dumps(report, indent=4)

    def save_report(self, filename):
        """
        Save the report of sustainability metrics to a JSON file.

        :param filename: The name of the file to save the report to.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.report_metrics())
            logging.info(f"Report saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save report to {filename}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    tracker = SustainabilityTracker()
    
    # Adding some sample metrics
    try:
        tracker.add_metric(SustainabilityMetric("Energy Consumption", 1500, "kWh"))
        tracker.add_metric(SustainabilityMetric("Water Usage", 300, "liters"))
        tracker.add_metric(SustainabilityMetric("CO2 Emissions", 200, "kg"))
        
        # Generate and save the report
        tracker.save_report("sustainability_report.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
