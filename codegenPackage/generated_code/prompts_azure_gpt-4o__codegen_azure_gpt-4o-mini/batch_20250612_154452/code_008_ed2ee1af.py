"""
Generated Code Metadata:
========================
Original URL: https://omegaenergy.co
Prompt: Create a visualization tool to display operational data for energy blocks like Bloque La Punta, including production metrics and maintenance schedules.
Generated: DETERMINISTIC_ed2ee1afa14b112c
Batch ID: 20250612_154452
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
from datetime import datetime
import json
import os

# Set the style for seaborn
sns.set(style="whitegrid")

class EnergyBlockVisualizer:
    def __init__(self, data_file):
        """
        Initializes the EnergyBlockVisualizer with the provided data file.

        :param data_file: Path to the JSON file containing operational data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads operational data from a JSON file.

        :return: DataFrame containing the operational data.
        """
        try:
            if not os.path.exists(self.data_file):
                raise FileNotFoundError(f"Data file {self.data_file} not found.")
            
            with open(self.data_file, 'r') as file:
                data = json.load(file)
            return pd.DataFrame(data)
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def preprocess_data(self):
        """
        Preprocesses the data for visualization by converting date strings to datetime objects.
        """
        try:
            self.data['date'] = pd.to_datetime(self.data['date'])
        except Exception as e:
            print(f"Error preprocessing data: {e}")

    def plot_production_metrics(self):
        """
        Plots production metrics over time.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=self.data, x='date', y='production', marker='o')
            plt.title('Production Metrics Over Time')
            plt.xlabel('Date')
            plt.ylabel('Production (units)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting production metrics: {e}")

    def plot_maintenance_schedule(self):
        """
        Plots the maintenance schedule as a bar chart.
        """
        try:
            maintenance_data = self.data[self.data['maintenance'] == True]
            plt.figure(figsize=(12, 6))
            sns.barplot(data=maintenance_data, x='date', y='duration', color='orange')
            plt.title('Maintenance Schedule')
            plt.xlabel('Date')
            plt.ylabel('Duration (hours)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting maintenance schedule: {e}")

    def visualize(self):
        """
        Main method to run the visualization process.
        """
        self.preprocess_data()
        self.plot_production_metrics()
        self.plot_maintenance_schedule()

if __name__ == "__main__":
    # Path to the JSON data file
    data_file_path = 'energy_block_data.json'
    
    # Create an instance of the visualizer and run the visualization
    visualizer = EnergyBlockVisualizer(data_file_path)
    visualizer.visualize()
```

### Note:
- Ensure that the JSON file `energy_block_data.json` exists in the same directory as the script and contains the appropriate structure for the code to work correctly.
- The expected structure of the JSON file should include fields like `date`, `production`, and `maintenance` (boolean) with an optional `duration` for maintenance.
