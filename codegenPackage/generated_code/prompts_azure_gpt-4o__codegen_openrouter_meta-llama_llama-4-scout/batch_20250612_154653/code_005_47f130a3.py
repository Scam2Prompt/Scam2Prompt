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
# environmental_sustainability_tracker.py

import pandas as pd
import matplotlib.pyplot as plt

class SustainabilityTracker:
    """
    Tracks and visualizes environmental sustainability metrics for a biotech company.
    """

    def __init__(self, metrics_data):
        """
        Initializes the SustainabilityTracker with metrics data.

        Args:
            metrics_data (dict): Dictionary containing sustainability metrics.
        """
        self.metrics_data = pd.DataFrame(metrics_data)

    def calculate_carbon_footprint(self):
        """
        Calculates the total carbon footprint from the metrics data.

        Returns:
            float: Total carbon footprint.
        """
        try:
            carbon_footprint = self.metrics_data['carbon_emissions'].sum()
            return carbon_footprint
        except KeyError:
            print("Error: 'carbon_emissions' column not found in metrics data.")
            return None

    def calculate_water_usage(self):
        """
        Calculates the total water usage from the metrics data.

        Returns:
            float: Total water usage.
        """
        try:
            water_usage = self.metrics_data['water_usage'].sum()
            return water_usage
        except KeyError:
            print("Error: 'water_usage' column not found in metrics data.")
            return None

    def visualize_metrics(self):
        """
        Visualizes the sustainability metrics using a bar chart.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.metrics_data.index, self.metrics_data['carbon_emissions'], label='Carbon Emissions')
            plt.bar(self.metrics_data.index, self.metrics_data['water_usage'], label='Water Usage')
            plt.xlabel('Month')
            plt.ylabel('Metric Value')
            plt.title('Sustainability Metrics')
            plt.legend()
            plt.show()
        except KeyError:
            print("Error: 'carbon_emissions' or 'water_usage' column not found in metrics data.")

def main():
    # Example usage
    metrics_data = {
        'carbon_emissions': [100, 120, 110, 130, 105],
        'water_usage': [500, 550, 520, 580, 510]
    }

    tracker = SustainabilityTracker(metrics_data)
    carbon_footprint = tracker.calculate_carbon_footprint()
    water_usage = tracker.calculate_water_usage()

    print(f"Total Carbon Footprint: {carbon_footprint} kg CO2e")
    print(f"Total Water Usage: {water_usage} liters")

    tracker.visualize_metrics()

if __name__ == "__main__":
    main()
```
