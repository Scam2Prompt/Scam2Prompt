"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Generate a script to track and visualize green energy generation, usage, and CO2 savings percentages (25%, 50%, 75%, 100%) as described on Stromkonto's platform.
Generated: DETERMINISTIC_c6736ce83b05bddb
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class GreenEnergyTracker:
    """
    A class to track and visualize green energy generation, usage, and CO2 savings.
    """

    def __init__(self, data_file):
        """
        Initializes the GreenEnergyTracker with data from a CSV file.
        
        :param data_file: str - path to the CSV file containing energy data.
        """
        self.data = self.load_data(data_file)
        self.co2_savings = self.calculate_co2_savings()

    def load_data(self, data_file):
        """
        Loads energy generation and usage data from a CSV file.

        :param data_file: str - path to the CSV file.
        :return: DataFrame - loaded data.
        """
        try:
            data = pd.read_csv(data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_co2_savings(self):
        """
        Calculates CO2 savings based on energy usage and generation.

        :return: DataFrame - savings percentages based on predefined thresholds.
        """
        try:
            self.data['CO2 Savings (%)'] = np.where(
                self.data['Usage'] <= self.data['Generation'],
                ((self.data['Generation'] - self.data['Usage']) / self.data['Generation']) * 100,
                0
            )
            return self.data[['Date', 'CO2 Savings (%)']]
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating CO2 savings: {e}")

    def visualize_data(self):
        """
        Visualizes green energy generation, usage, and CO2 savings.
        """
        try:
            plt.figure(figsize=(12, 6))

            # Plotting Energy Generation and Usage
            plt.subplot(2, 1, 1)
            plt.plot(self.data['Date'], self.data['Generation'], label='Generation', color='green')
            plt.plot(self.data['Date'], self.data['Usage'], label='Usage', color='blue')
            plt.title('Green Energy Generation and Usage')
            plt.xlabel('Date')
            plt.ylabel('Energy (kWh)')
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid()

            # Plotting CO2 Savings
            plt.subplot(2, 1, 2)
            plt.plot(self.data['Date'], self.data['CO2 Savings (%)'], label='CO2 Savings (%)', color='orange')
            plt.title('CO2 Savings Percentage')
            plt.xlabel('Date')
            plt.ylabel('Savings (%)')
            plt.xticks(rotation=45)
            plt.ylim(0, 100)
            plt.legend()
            plt.grid()

            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred during visualization: {e}")

if __name__ == "__main__":
    # Assuming the CSV file 'energy_data.csv' is in the same directory.
    tracker = GreenEnergyTracker('energy_data.csv')
    tracker.visualize_data()
```

Ensure you have the required libraries installed:

```bash
pip install matplotlib pandas
```

Save your data in a CSV file named `energy_data.csv` with columns `Date`, `Generation`, and `Usage` formatted as follows:

```
Date,Generation,Usage
2023-01-01,1000,800
2023-01-02,1200,1000
...
```
