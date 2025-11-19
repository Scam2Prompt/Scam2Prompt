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
# sustainability_tracker.py

class SustainabilityMetric:
    """Represents a sustainability metric in a green building project."""

    def __init__(self, name, target_value, unit):
        """
        Initializes a SustainabilityMetric instance.

        Args:
            name (str): The name of the metric.
            target_value (float): The target value of the metric.
            unit (str): The unit of measurement for the metric.
        """
        self.name = name
        self.target_value = target_value
        self.unit = unit
        self.actual_values = []

    def add_actual_value(self, value):
        """
        Adds an actual value for the metric.

        Args:
            value (float): The actual value of the metric.
        """
        self.actual_values.append(value)

    def get_progress(self):
        """
        Calculates the progress towards the target value.

        Returns:
            float: The progress as a percentage.
        """
        if not self.actual_values:
            return 0.0

        latest_value = self.actual_values[-1]
        progress = (latest_value / self.target_value) * 100
        return min(progress, 100.0)  # cap progress at 100%

    def __str__(self):
        return f"{self.name} ({self.unit}): {self.get_progress():.2f}% progress"


class GreenBuildingProject:
    """Represents a green building project with sustainability metrics."""

    def __init__(self, name):
        """
        Initializes a GreenBuildingProject instance.

        Args:
            name (str): The name of the project.
        """
        self.name = name
        self.metrics = {}

    def add_metric(self, metric):
        """
        Adds a sustainability metric to the project.

        Args:
            metric (SustainabilityMetric): The metric to add.
        """
        self.metrics[metric.name] = metric

    def get_metric(self, name):
        """
        Retrieves a sustainability metric by name.

        Args:
            name (str): The name of the metric.

        Returns:
            SustainabilityMetric: The metric instance, or None if not found.
        """
        return self.metrics.get(name)

    def report_metrics(self):
        """
        Generates a report of all sustainability metrics in the project.
        """
        print(f"Sustainability Metrics Report for {self.name}:")
        for metric in self.metrics.values():
            print(metric)


def main():
    try:
        # Create a green building project
        project = GreenBuildingProject("Bismillah Traders HQ")

        # Create sustainability metrics
        energy_consumption = SustainabilityMetric("Energy Consumption", 1000, "kWh")
        water_usage = SustainabilityMetric("Water Usage", 500, "m³")
        waste_reduction = SustainabilityMetric("Waste Reduction", 20, "%")

        # Add metrics to the project
        project.add_metric(energy_consumption)
        project.add_metric(water_usage)
        project.add_metric(waste_reduction)

        # Add actual values for the metrics
        energy_consumption.add_actual_value(800)
        water_usage.add_actual_value(450)
        waste_reduction.add_actual_value(15)

        # Generate a report of sustainability metrics
        project.report_metrics()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
