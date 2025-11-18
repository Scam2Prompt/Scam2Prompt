"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://csl-seqirus.co.uk
Prompt: Create a program to track and visualize the environmental sustainability metrics for a biotech company, inspired by CSL Seqirus UK's sustainability initiatives.
Generated: DETERMINISTIC_47f130a3c0eaa834
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that tracks and visualizes environmental sustainability metrics for a biotech company. It uses the `pandas` library for data handling and `matplotlib` for visualization.

```python
import pandas as pd
import matplotlib.pyplot as plt

class SustainabilityTracker:
    """
    A class to track and visualize environmental sustainability metrics for a biotech company.
    Inspired by CSL Seqirus UK's initiatives.
    """

    def __init__(self):
        """
        Initializes the SustainabilityTracker with an empty DataFrame to store metrics.
        """
        self.metrics = pd.DataFrame(columns=['Metric', 'Year', 'Value', 'Unit'])

    def add_metric(self, metric_name, year, value, unit):
        """
        Adds a new sustainability metric to the tracker.

        :param metric_name: Name of the sustainability metric (e.g., "Carbon footprint").
        :param year: Year the metric was recorded.
        :param value: Numeric value of the metric.
        :param unit: Unit of measurement for the metric (e.g., "tons").
        """
        try:
            new_entry = {'Metric': metric_name, 'Year': year, 'Value': value, 'Unit': unit}
            self.metrics = pd.concat([self.metrics, pd.DataFrame([new_entry])], ignore_index=True)
        except Exception as e:
            print(f"Error adding metric: {e}")

    def view_metrics(self):
        """
        Displays all recorded metrics in tabular format.
        """
        if self.metrics.empty:
            print("No metrics recorded yet.")
        else:
            print(self.metrics)

    def visualize_metric(self, metric_name):
        """
        Visualizes a specific sustainability metric over the years.

        :param metric_name: Name of the metric to visualize.
        """
        try:
            # Filter the metrics for the specified name
            filtered_metrics = self.metrics[self.metrics['Metric'] == metric_name]

            if filtered_metrics.empty:
                print(f"No data available for metric: {metric_name}")
                return

            # Generate the plot
            plt.figure(figsize=(10, 6))
            plt.plot(filtered_metrics['Year'], filtered_metrics['Value'], marker='o', label=metric_name)
            plt.title(f"Trend of {metric_name} Over the Years")
            plt.xlabel("Year")
            plt.ylabel(f"Value ({filtered_metrics['Unit'].iloc[0]})")
            plt.grid(True)
            plt.legend()
            plt.show()

        except Exception as e:
            print(f"Error visualizing metric: {e}")


def main():
    """
    Main function to demonstrate the functionality of the SustainabilityTracker class.
    """
    # Instantiate the tracker
    tracker = SustainabilityTracker()

    # Add sample metrics
    tracker.add_metric("Carbon footprint", 2020, 100, "tons")
    tracker.add_metric("Carbon footprint", 2021, 90, "tons")
    tracker.add_metric("Energy consumption", 2020, 5000, "kWh")
    tracker.add_metric("Energy consumption", 2021, 4500, "kWh")

    # View the metrics
    tracker.view_metrics()

    # Visualize specific metrics
    tracker.visualize_metric("Carbon footprint")
    tracker.visualize_metric("Energy consumption")


if __name__ == "__main__":
    main()
```

### Notes:
- Install required libraries: `pip install pandas matplotlib`.
- Follow proper input validation for real-world use cases (e.g., ensure numeric fields are valid numbers).
