"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: "Create a program for processing data from three-axis tests of soils as per the laboratory tests services offered by Научно-образовательный центр «Геотехника»."
Generated: DETERMINISTIC_592f3738b55a3d7b
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SoilTestProcessor:
    """
    A class to process three-axis test data for soil samples.
    """

    def __init__(self, data_file):
        """
        Initializes the SoilTestProcessor with the given data file.

        :param data_file: Path to the CSV file containing soil test data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads the soil test data from the specified CSV file.
        Raises an error if the file cannot be found or read.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("Error: The file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error: The file could not be parsed.")

    def process_data(self):
        """
        Processes the loaded data to calculate relevant soil properties.
        This method assumes the data contains columns for stress and strain.
        """
        if self.data is None:
            raise ValueError("Error: No data loaded. Please load data first.")

        # Example processing: Calculate the effective stress
        try:
            self.data['Effective_Stress'] = self.data['Total_Stress'] - self.data['Pore_Water_Pressure']
            print("Data processed successfully.")
        except KeyError as e:
            raise KeyError(f"Error: Missing expected column in data: {e}")

    def plot_results(self):
        """
        Plots the results of the three-axis tests.
        """
        if self.data is None:
            raise ValueError("Error: No data loaded. Please load data first.")

        try:
            plt.figure(figsize=(10, 6))
            plt.plot(self.data['Strain'], self.data['Effective_Stress'], label='Effective Stress vs Strain')
            plt.title('Three-Axis Test Results')
            plt.xlabel('Strain')
            plt.ylabel('Effective Stress')
            plt.legend()
            plt.grid()
            plt.show()
        except KeyError as e:
            raise KeyError(f"Error: Missing expected column in data for plotting: {e}")

def main():
    """
    Main function to execute the soil test processing.
    """
    data_file = 'soil_test_data.csv'  # Replace with your actual data file path
    processor = SoilTestProcessor(data_file)

    try:
        processor.load_data()
        processor.process_data()
        processor.plot_results()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
