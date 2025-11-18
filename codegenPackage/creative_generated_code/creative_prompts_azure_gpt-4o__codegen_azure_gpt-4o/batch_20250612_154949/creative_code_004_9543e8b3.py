"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Create a Python program to automate the tracking of digital transformation metrics, incorporating principles mentioned by Romain Rissoan.
Generated: DETERMINISTIC_9543e8b3f7c2abac
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import os

class DigitalTransformationMetricsTracker:
    """
    A class to track digital transformation metrics.
    This class handles the storage, updating, and retrieval of metrics data.
    """

    def __init__(self, file_name="metrics.csv"):
        """
        Initializes the tracker with a CSV file for data storage.

        :param file_name: Name of the CSV file where metrics will be stored.
        """
        self.file_name = file_name
        # Create the file with headers if it doesn't exist
        if not os.path.exists(self.file_name):
            try:
                with open(self.file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Date", "Metric Name", "Value", "Comment"])
            except Exception as e:
                raise IOError(f"Failed to create metrics file: {e}")

    def log_metric(self, metric_name, value, comment=""):
        """
        Logs a new metric into the CSV file.

        :param metric_name: Name of the metric.
        :param value: Value of the metric.
        :param comment: Optional comment providing context for the metric.
        """
        try:
            with open(self.file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([datetime.datetime.now().isoformat(), metric_name, value, comment])
        except Exception as e:
            raise IOError(f"Failed to log metric: {e}")

    def retrieve_metrics(self, metric_name=None):
        """
        Retrieves metrics from the CSV file. Filters by metric name if provided.

        :param metric_name: Optional name of the metric to filter results.
        :return: List of metrics matching the criteria.
        """
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.DictReader(file)
                metrics = [row for row in reader if metric_name is None or row["Metric Name"] == metric_name]
            return metrics
        except Exception as e:
            raise IOError(f"Failed to retrieve metrics: {e}")

    def display_metrics(self, metric_name=None):
        """
        Displays metrics in a readable format. Filters by metric name if provided.

        :param metric_name: Optional name of the metric to filter results.
        """
        metrics = self.retrieve_metrics(metric_name)
        if metrics:
            print(f"{'Date':<25} {'Metric Name':<20} {'Value':<10} {'Comment':<30}")
            print("-" * 85)
            for metric in metrics:
                print(f"{metric['Date']:<25} {metric['Metric Name']:<20} {metric['Value']:<10} {metric['Comment']:<30}")
        else:
            print("No metrics found.")


if __name__ == "__main__":
    # Example usage
    tracker = DigitalTransformationMetricsTracker()

    # Logging metrics
    tracker.log_metric("Customer Engagement", 87, "Increased due to social media campaign")
    tracker.log_metric("Operational Efficiency", 92, "Improved automation in workflows")

    # Display all metrics
    print("All Metrics:")
    tracker.display_metrics()

    # Display metrics filtered by name
    print("\nFiltered Metrics (Customer Engagement):")
    tracker.display_metrics("Customer Engagement")
```
