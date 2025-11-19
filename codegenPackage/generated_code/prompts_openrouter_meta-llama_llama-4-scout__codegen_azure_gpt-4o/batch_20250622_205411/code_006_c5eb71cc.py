"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Suggest a set of metrics and key performance indicators (KPIs) for evaluating the success of construction projects, inspired by Clickmart Ltd's project management approach and client testimonials."
Generated: DETERMINISTIC_c5eb71ccb069901c
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# metrics_kpis.py

"""
This script defines a set of metrics and key performance indicators (KPIs) 
for evaluating the success of construction projects. The metrics are inspired 
by Clickmart Ltd's project management approach and client testimonials.
"""

# Import necessary libraries
import json

# Define a class to encapsulate metrics and KPIs
class ConstructionProjectMetrics:
    def __init__(self):
        """
        Initialize the metrics and KPIs with default values.
        """
        self.metrics = {
            "budget_adherence": 0.0,  # Percentage of budget adherence
            "schedule_adherence": 0.0,  # Percentage of schedule adherence
            "quality_score": 0.0,  # Quality score based on client feedback
            "safety_incidents": 0,  # Number of safety incidents reported
            "client_satisfaction": 0.0,  # Client satisfaction score (1-10 scale)
            "team_productivity": 0.0,  # Productivity score of the construction team
            "environmental_impact": 0.0,  # Environmental impact score (lower is better)
        }

    def update_metric(self, metric_name, value):
        """
        Update the value of a specific metric.

        Args:
            metric_name (str): The name of the metric to update.
            value (float or int): The new value for the metric.

        Raises:
            ValueError: If the metric name is invalid or the value is out of range.
        """
        if metric_name not in self.metrics:
            raise ValueError(f"Invalid metric name: {metric_name}")
        if not isinstance(value, (int, float)):
            raise ValueError("Metric value must be a number.")
        self.metrics[metric_name] = value

    def get_metrics(self):
        """
        Retrieve all metrics and their current values.

        Returns:
            dict: A dictionary of metrics and their values.
        """
        return self.metrics

    def export_metrics_to_json(self, file_path):
        """
        Export the metrics to a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.metrics, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing metrics to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the metrics class
    metrics = ConstructionProjectMetrics()

    # Update metrics with sample data
    try:
        metrics.update_metric("budget_adherence", 95.0)
        metrics.update_metric("schedule_adherence", 90.0)
        metrics.update_metric("quality_score", 8.5)
        metrics.update_metric("safety_incidents", 2)
        metrics.update_metric("client_satisfaction", 9.0)
        metrics.update_metric("team_productivity", 85.0)
        metrics.update_metric("environmental_impact", 3.0)

        # Print the metrics
        print("Current Metrics:")
        for metric, value in metrics.get_metrics().items():
            print(f"{metric}: {value}")

        # Export metrics to a JSON file
        metrics.export_metrics_to_json("construction_metrics.json")
        print("Metrics successfully exported to 'construction_metrics.json'.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except IOError as ioe:
        print(f"IO Error: {ioe}")
```
