"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Provide a Python implementation for tracking and reporting transparency metrics based on Omega Energy's Programa de Transparencia y Ética Empresarial (PTEE).
Generated: DETERMINISTIC_53ef13241729eb0e
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging for tracking and error reporting
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("transparency_metrics.log"),
        logging.StreamHandler()
    ]
)

class TransparencyMetricsTracker:
    """
    A class to track and report transparency metrics 
    as per Omega Energy's Programa de Transparencia y Ética Empresarial (PTEE).
    """

    def __init__(self, metrics_file="metrics.json"):
        """
        Initialize the tracker with a specified metrics file.
        
        Args:
            metrics_file (str): Path to the JSON file where metrics are stored.
        """
        self.metrics_file = metrics_file
        self.metrics = self._load_metrics()

    def _load_metrics(self):
        """
        Load transparency metrics from the JSON file.

        Returns:
            dict: Loaded metrics data.
        """
        try:
            with open(self.metrics_file, "r") as file:
                logging.info("Metrics file loaded successfully.")
                return json.load(file)
        except FileNotFoundError:
            logging.warning(f"{self.metrics_file} not found. Creating new metrics file.")
            return {}
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from {self.metrics_file}. Starting with empty metrics.")
            return {}

    def _save_metrics(self):
        """
        Save transparency metrics to the JSON file.
        """
        try:
            with open(self.metrics_file, "w") as file:
                json.dump(self.metrics, file, indent=4)
                logging.info("Metrics successfully saved.")
        except Exception as e:
            logging.error(f"Error saving metrics: {e}")

    def add_metric(self, name, value, description=""):
        """
        Add or update a transparency metric.
        
        Args:
            name (str): Name of the metric.
            value (any): Value of the metric.
            description (str): Optional description of the metric.
        """
        self.metrics[name] = {
            "value": value,
            "description": description,
            "last_updated": datetime.now().isoformat()
        }
        logging.info(f"Metric '{name}' updated: {value}")
        self._save_metrics()

    def get_metric(self, name):
        """
        Retrieve a transparency metric by name.
        
        Args:
            name (str): Name of the metric.
        
        Returns:
            dict: Metric details or None if not found.
        """
        metric = self.metrics.get(name)
        if metric:
            logging.info(f"Metric '{name}' retrieved.")
            return metric
        else:
            logging.warning(f"Metric '{name}' not found.")
            return None

    def report_metrics(self):
        """
        Generate a report of all transparency metrics.
        
        Returns:
            str: Formatted report of all metrics.
        """
        if not self.metrics:
            logging.info("No metrics to report.")
            return "No metrics available."
        
        report = ["Transparency Metrics Report:"]
        for name, details in self.metrics.items():
            report.append(
                f"Metric: {name}\n"
                f"  Value: {details['value']}\n"
                f"  Description: {details['description']}\n"
                f"  Last Updated: {details['last_updated']}\n"
            )
        logging.info("Metrics report generated.")
        return "\n".join(report)


# Example usage of the TransparencyMetricsTracker class
if __name__ == "__main__":
    try:
        tracker = TransparencyMetricsTracker()

        # Add metrics
        tracker.add_metric("Integrity Index", 95, "Score indicating ethical compliance.")
        tracker.add_metric("Whistleblower Cases", 4, "Number of whistleblower cases resolved.")

        # Retrieve a specific metric
        metric = tracker.get_metric("Integrity Index")
        if metric:
            print("Retrieved Metric:", metric)

        # Generate a full report
        print(tracker.report_metrics())

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
```
