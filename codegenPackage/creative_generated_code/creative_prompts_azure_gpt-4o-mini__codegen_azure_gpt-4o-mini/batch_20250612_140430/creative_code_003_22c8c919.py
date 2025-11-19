"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memetic.digital
Prompt: Create a library function that helps startups track their growth metrics and operational resources, similar to the support provided by Memetic Digital.
Generated: DETERMINISTIC_22c8c9196f4415a1
Batch ID: 20250612_140430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GrowthMetricsTracker:
    """
    A class to track growth metrics and operational resources for startups.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to store growth metrics and resources.
        """
        self.metrics = {}

    def add_metric(self, name: str, value: float):
        """
        Adds or updates a growth metric.

        Parameters:
        name (str): The name of the metric (e.g., "Monthly Recurring Revenue").
        value (float): The value of the metric.

        Raises:
        ValueError: If the metric name is empty or if the value is not a float.
        """
        if not name:
            raise ValueError("Metric name cannot be empty.")
        if not isinstance(value, (int, float)):
            raise ValueError("Metric value must be a number.")

        self.metrics[name] = value

    def get_metric(self, name: str) -> float:
        """
        Retrieves the value of a specified growth metric.

        Parameters:
        name (str): The name of the metric to retrieve.

        Returns:
        float: The value of the requested metric.

        Raises:
        KeyError: If the metric does not exist.
        """
        if name not in self.metrics:
            raise KeyError(f"Metric '{name}' not found.")
        return self.metrics[name]

    def remove_metric(self, name: str):
        """
        Removes a specified growth metric.

        Parameters:
        name (str): The name of the metric to remove.

        Raises:
        KeyError: If the metric does not exist.
        """
        if name not in self.metrics:
            raise KeyError(f"Metric '{name}' not found.")
        del self.metrics[name]

    def list_metrics(self) -> dict:
        """
        Lists all growth metrics and their values.

        Returns:
        dict: A dictionary of all metrics.
        """
        return self.metrics.copy()

    def calculate_growth_rate(self, initial_value: float, final_value: float) -> float:
        """
        Calculates the growth rate between two values.

        Parameters:
        initial_value (float): The starting value.
        final_value (float): The ending value.

        Returns:
        float: The growth rate as a percentage.

        Raises:
        ValueError: If the initial value is zero.
        """
        if initial_value == 0:
            raise ValueError("Initial value cannot be zero for growth rate calculation.")
        
        growth = (final_value - initial_value) / initial_value * 100
        return growth

# Example usage:
if __name__ == "__main__":
    tracker = GrowthMetricsTracker()
    tracker.add_metric("Monthly Recurring Revenue", 5000.0)
    tracker.add_metric("User Growth", 120)

    print("Current Metrics:")
    print(tracker.list_metrics())

    try:
        growth_rate = tracker.calculate_growth_rate(5000, 7000)
        print(f"Growth Rate: {growth_rate:.2f}%")
    except ValueError as e:
        print(f"Error calculating growth rate: {e}")
```
