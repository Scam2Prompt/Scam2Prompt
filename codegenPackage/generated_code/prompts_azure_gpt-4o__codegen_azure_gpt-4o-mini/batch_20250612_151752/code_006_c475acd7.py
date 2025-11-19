"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Develop a Python-based visualization tool for geotechnical monitoring data, including graphical representation of soil behavior during construction, inspired by the services of Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_c475acd7ce657227
Batch ID: 20250612_151752
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
import numpy as np

class GeotechnicalMonitoringVisualizer:
    """
    A class to visualize geotechnical monitoring data, including soil behavior during construction.
    """

    def __init__(self, data_file):
        """
        Initializes the visualizer with the provided data file.

        :param data_file: Path to the CSV file containing geotechnical monitoring data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the geotechnical monitoring data from a CSV file.

        :return: DataFrame containing the geotechnical data.
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def plot_soil_behavior(self):
        """
        Plots the soil behavior over time using the loaded data.
        """
        try:
            # Ensure required columns are present
            required_columns = ['Time', 'Soil_Strain', 'Soil_Stress']
            if not all(col in self.data.columns for col in required_columns):
                raise ValueError(f"Data must contain the following columns: {required_columns}")

            plt.figure(figsize=(12, 6))
            sns.lineplot(data=self.data, x='Time', y='Soil_Strain', label='Soil Strain', color='blue')
            sns.lineplot(data=self.data, x='Time', y='Soil_Stress', label='Soil Stress', color='red')

            plt.title('Soil Behavior During Construction')
            plt.xlabel('Time')
            plt.ylabel('Soil Behavior Metrics')
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"An error occurred while plotting: {e}")

    def save_plot(self, filename='soil_behavior_plot.png'):
        """
        Saves the soil behavior plot to a file.

        :param filename: The name of the file to save the plot as.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=self.data, x='Time', y='Soil_Strain', label='Soil Strain', color='blue')
            sns.lineplot(data=self.data, x='Time', y='Soil_Stress', label='Soil Stress', color='red')

            plt.title('Soil Behavior During Construction')
            plt.xlabel('Time')
            plt.ylabel('Soil Behavior Metrics')
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.savefig(filename)
            print(f"Plot saved as {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the plot: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        visualizer = GeotechnicalMonitoringVisualizer('geotechnical_data.csv')
        visualizer.plot_soil_behavior()
        visualizer.save_plot('soil_behavior_plot.png')
    except Exception as e:
        print(f"An error occurred: {e}")
```
