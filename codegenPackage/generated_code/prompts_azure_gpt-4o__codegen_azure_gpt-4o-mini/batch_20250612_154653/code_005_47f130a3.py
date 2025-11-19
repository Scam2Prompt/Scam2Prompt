"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Create a program to track and visualize the environmental sustainability metrics for a biotech company, inspired by CSL Seqirus UK's sustainability initiatives.
Generated: DETERMINISTIC_47f130a3c0eaa834
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SustainabilityTracker:
    """
    A class to track and visualize environmental sustainability metrics for a biotech company.
    """

    def __init__(self):
        """
        Initializes the SustainabilityTracker with an empty DataFrame.
        """
        self.metrics = pd.DataFrame(columns=['Date', 'Metric', 'Value'])

    def add_metric(self, date: str, metric: str, value: float):
        """
        Adds a sustainability metric to the tracker.

        Parameters:
        date (str): The date of the metric in 'YYYY-MM-DD' format.
        metric (str): The name of the sustainability metric.
        value (float): The value of the sustainability metric.

        Raises:
        ValueError: If the date format is incorrect or if the value is negative.
        """
        # Validate date format
        try:
            pd.to_datetime(date)
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")

        # Validate value
        if value < 0:
            raise ValueError("Metric value cannot be negative.")

        # Append the new metric to the DataFrame
        self.metrics = self.metrics.append({'Date': date, 'Metric': metric, 'Value': value}, ignore_index=True)

    def visualize_metrics(self):
        """
        Visualizes the sustainability metrics using a line plot.

        Raises:
        ValueError: If there are no metrics to visualize.
        """
        if self.metrics.empty:
            raise ValueError("No metrics available to visualize.")

        # Set the style for the plot
        sns.set(style="whitegrid")

        # Create a pivot table for better visualization
        pivot_metrics = self.metrics.pivot(index='Date', columns='Metric', values='Value')

        # Plot the metrics
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=pivot_metrics)
        plt.title('Environmental Sustainability Metrics Over Time')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.xticks(rotation=45)
        plt.legend(title='Metrics')
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    tracker = SustainabilityTracker()
    
    # Adding some sample metrics
    try:
        tracker.add_metric('2023-01-01', 'Carbon Emissions (tonnes)', 150.0)
        tracker.add_metric('2023-02-01', 'Water Usage (litres)', 20000.0)
        tracker.add_metric('2023-03-01', 'Waste Generated (kg)', 500.0)
        
        # Visualize the metrics
        tracker.visualize_metrics()
    except ValueError as e:
        print(f"Error: {e}")
```
