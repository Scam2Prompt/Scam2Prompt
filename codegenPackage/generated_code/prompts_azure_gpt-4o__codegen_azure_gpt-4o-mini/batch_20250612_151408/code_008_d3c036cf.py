"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Create a Python script to analyze Engel fridge freezer energy consumption, factoring in 12v power usage and cooling efficiency.
Generated: DETERMINISTIC_d3c036cfeb5c41eb
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class EngelFridgeAnalyzer:
    """
    A class to analyze the energy consumption of an Engel fridge freezer.
    """

    def __init__(self, data_file):
        """
        Initializes the EngelFridgeAnalyzer with a data file.

        :param data_file: Path to the CSV file containing energy consumption data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads energy consumption data from a CSV file.

        :return: DataFrame containing the energy consumption data.
        """
        try:
            data = pd.read_csv(self.data_file)
            # Ensure the necessary columns are present
            if not all(col in data.columns for col in ['timestamp', 'power_usage', 'cooling_efficiency']):
                raise ValueError("CSV must contain 'timestamp', 'power_usage', and 'cooling_efficiency' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_energy_consumption(self):
        """
        Calculates the total energy consumption based on power usage and cooling efficiency.

        :return: Total energy consumption in kWh.
        """
        try:
            # Calculate energy consumption (kWh) = Power Usage (W) * Time (h) / 1000
            self.data['time_diff'] = self.data['timestamp'].diff().dt.total_seconds() / 3600
            self.data['energy_consumption'] = (self.data['power_usage'] * self.data['time_diff']) / 1000
            total_energy = self.data['energy_consumption'].sum()
            return total_energy
        except Exception as e:
            raise Exception(f"An error occurred during energy consumption calculation: {e}")

    def analyze_efficiency(self):
        """
        Analyzes the cooling efficiency of the fridge.

        :return: Average cooling efficiency.
        """
        try:
            average_efficiency = self.data['cooling_efficiency'].mean()
            return average_efficiency
        except Exception as e:
            raise Exception(f"An error occurred during efficiency analysis: {e}")

    def run_analysis(self):
        """
        Runs the complete analysis and prints the results.
        """
        try:
            total_energy = self.calculate_energy_consumption()
            average_efficiency = self.analyze_efficiency()
            print(f"Total Energy Consumption: {total_energy:.2f} kWh")
            print(f"Average Cooling Efficiency: {average_efficiency:.2f}")
        except Exception as e:
            print(f"Analysis failed: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = EngelFridgeAnalyzer('energy_data.csv')
        analyzer.run_analysis()
    except Exception as e:
        print(f"Error: {e}")
```

Make sure to replace `'energy_data.csv'` with the actual path to your CSV file containing the energy consumption data. The CSV should have columns named `timestamp`, `power_usage`, and `cooling_efficiency`.
