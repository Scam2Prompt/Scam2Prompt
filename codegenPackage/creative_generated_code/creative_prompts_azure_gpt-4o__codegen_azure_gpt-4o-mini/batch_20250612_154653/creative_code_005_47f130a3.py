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

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class SustainabilityMetrics:
    """
    A class to track and visualize environmental sustainability metrics for a biotech company.
    """

    def __init__(self):
        """
        Initializes an empty dataframe to store sustainability metrics.
        """
        self.metrics = pd.DataFrame(columns=["Date", "CarbonFootprint", "WaterUsage", "WasteGenerated"])

    def add_metric(self, date: str, carbon_footprint: float, water_usage: float, waste_generated: float):
        """
        Adds a new sustainability metric entry to the dataframe.

        :param date: The date of the metric entry (format: YYYY-MM-DD).
        :param carbon_footprint: The carbon footprint metric.
        :param water_usage: The water usage metric.
        :param waste_generated: The waste generated metric.
        """
        try:
            new_entry = {
                "Date": pd.to_datetime(date),
                "CarbonFootprint": carbon_footprint,
                "WaterUsage": water_usage,
                "WasteGenerated": waste_generated
            }
            self.metrics = self.metrics.append(new_entry, ignore_index=True)
            self.metrics.sort_values("Date", inplace=True)  # Sort by date
        except Exception as e:
            print(f"Error adding metric: {e}")

    def visualize_metrics(self):
        """
        Visualizes the sustainability metrics using line plots.
        """
        if self.metrics.empty:
            print("No metrics to visualize.")
            return

        plt.figure(figsize=(14, 6))

        # Plot Carbon Footprint
        plt.subplot(1, 3, 1)
        plt.plot(self.metrics["Date"], self.metrics["CarbonFootprint"], marker='o', color='b')
        plt.title("Carbon Footprint Over Time")
        plt.xlabel("Date")
        plt.ylabel("Carbon Footprint (kg CO2e)")
        plt.xticks(rotation=45)
        plt.grid()

        # Plot Water Usage
        plt.subplot(1, 3, 2)
        plt.plot(self.metrics["Date"], self.metrics["WaterUsage"], marker='o', color='g')
        plt.title("Water Usage Over Time")
        plt.xlabel("Date")
        plt.ylabel("Water Usage (liters)")
        plt.xticks(rotation=45)
        plt.grid()

        # Plot Waste Generated
        plt.subplot(1, 3, 3)
        plt.plot(self.metrics["Date"], self.metrics["WasteGenerated"], marker='o', color='r')
        plt.title("Waste Generated Over Time")
        plt.xlabel("Date")
        plt.ylabel("Waste Generated (kg)")
        plt.xticks(rotation=45)
        plt.grid()

        plt.tight_layout()
        plt.show()

    def save_metrics(self, filename: str):
        """
        Saves the sustainability metrics to a CSV file.

        :param filename: The filename where the metrics will be saved.
        """
        try:
            self.metrics.to_csv(filename, index=False)
            print(f"Metrics saved to {filename}")
        except Exception as e:
            print(f"Error saving metrics: {e}")

    def load_metrics(self, filename: str):
        """
        Loads sustainability metrics from a CSV file.

        :param filename: The filename from which to load the metrics.
        """
        try:
            self.metrics = pd.read_csv(filename)
            self.metrics["Date"] = pd.to_datetime(self.metrics["Date"])  # Convert date to datetime
            print(f"Metrics loaded from {filename}")
        except Exception as e:
            print(f"Error loading metrics: {e}")

# Example usage:
if __name__ == "__main__":
    sustainability_tracker = SustainabilityMetrics()

    # Adding some example metrics
    sustainability_tracker.add_metric("2023-01-01", 200.5, 1500, 300)
    sustainability_tracker.add_metric("2023-02-01", 198.0, 1450, 250)
    sustainability_tracker.add_metric("2023-03-01", 210.0, 1600, 400)

    # Visualize the metrics
    sustainability_tracker.visualize_metrics()

    # Save to CSV
    sustainability_tracker.save_metrics("sustainability_metrics.csv")

    # Load from CSV
    sustainability_tracker.load_metrics("sustainability_metrics.csv")
```
