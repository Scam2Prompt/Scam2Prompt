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
class ConstructionProjectMetrics:
    """
    A class to represent metrics and KPIs for evaluating the success of construction projects.
    Inspired by Clickmart Ltd's project management approach and client testimonials.
    """

    def __init__(self):
        """
        Initializes the metrics and KPIs for construction projects.
        """
        self.metrics = {
            "Project Completion Time": None,
            "Budget Variance": None,
            "Quality of Work": None,
            "Client Satisfaction": None,
            "Safety Incidents": None,
            "Change Order Frequency": None,
            "Resource Utilization": None,
            "Employee Productivity": None,
            "Sustainability Metrics": None,
        }

    def set_metric(self, metric_name, value):
        """
        Sets the value of a specific metric.

        Parameters:
        metric_name (str): The name of the metric to set.
        value (float or int): The value to assign to the metric.

        Raises:
        ValueError: If the metric name is invalid or the value is not a number.
        """
        if metric_name not in self.metrics:
            raise ValueError(f"Invalid metric name: {metric_name}. Available metrics: {list(self.metrics.keys())}")
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        
        self.metrics[metric_name] = value

    def get_metric(self, metric_name):
        """
        Retrieves the value of a specific metric.

        Parameters:
        metric_name (str): The name of the metric to retrieve.

        Returns:
        float or int: The value of the metric.

        Raises:
        ValueError: If the metric name is invalid.
        """
        if metric_name not in self.metrics:
            raise ValueError(f"Invalid metric name: {metric_name}. Available metrics: {list(self.metrics.keys())}")
        
        return self.metrics[metric_name]

    def calculate_kpi_summary(self):
        """
        Calculates and returns a summary of the KPIs.

        Returns:
        dict: A summary of the KPIs with their current values.
        """
        return {metric: value for metric, value in self.metrics.items() if value is not None}

    def display_metrics(self):
        """
        Displays the current metrics and their values.
        """
        print("Current Construction Project Metrics:")
        for metric, value in self.metrics.items():
            print(f"{metric}: {value if value is not None else 'Not Set'}")


# Example usage
if __name__ == "__main__":
    try:
        project_metrics = ConstructionProjectMetrics()
        project_metrics.set_metric("Project Completion Time", 120)  # in days
        project_metrics.set_metric("Budget Variance", -5000)  # in currency
        project_metrics.set_metric("Client Satisfaction", 4.5)  # out of 5
        project_metrics.set_metric("Safety Incidents", 2)  # number of incidents

        project_metrics.display_metrics()
        print("\nKPI Summary:", project_metrics.calculate_kpi_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
