"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Generate a script to track and visualize green energy generation, usage, and CO2 savings percentages (25%, 50%, 75%, 100%) as described on Stromkonto's platform.
Generated: DETERMINISTIC_c6736ce83b05bddb
Batch ID: 20250612_150323
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

class GreenEnergyTracker:
    """
    A class to track and visualize green energy generation, usage, and CO2 savings.
    """

    def __init__(self, data_file):
        """
        Initializes the GreenEnergyTracker with data from a CSV file.

        :param data_file: Path to the CSV file containing energy data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads energy data from a CSV file.

        :return: DataFrame containing the energy data.
        """
        try:
            data = pd.read_csv(self.data_file)
            # Ensure the required columns are present
            required_columns = ['date', 'green_energy_generated', 'energy_used', 'co2_saved']
            if not all(col in data.columns for col in required_columns):
                raise ValueError("CSV file must contain the following columns: " + ", ".join(required_columns))
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.data_file}")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the CSV file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_savings_percentage(self):
        """
        Calculates the CO2 savings percentage based on the generated green energy.

        :return: A DataFrame with the savings percentage.
        """
        self.data['savings_percentage'] = (self.data['co2_saved'] / self.data['energy_used']) * 100
        return self.data[['date', 'savings_percentage']]

    def visualize_data(self):
        """
        Visualizes the green energy generation, usage, and CO2 savings.
        """
        try:
            plt.figure(figsize=(12, 6))

            # Plot green energy generated
            plt.subplot(3, 1, 1)
            plt.plot(self.data['date'], self.data['green_energy_generated'], label='Green Energy Generated', color='green')
            plt.title('Green Energy Generation Over Time')
            plt.xlabel('Date')
            plt.ylabel('Energy (kWh)')
            plt.xticks(rotation=45)
            plt.legend()

            # Plot energy used
            plt.subplot(3, 1, 2)
            plt.plot(self.data['date'], self.data['energy_used'], label='Energy Used', color='blue')
            plt.title('Energy Usage Over Time')
            plt.xlabel('Date')
            plt.ylabel('Energy (kWh)')
            plt.xticks(rotation=45)
            plt.legend()

            # Plot CO2 savings percentage
            savings_data = self.calculate_savings_percentage()
            plt.subplot(3, 1, 3)
            plt.plot(savings_data['date'], savings_data['savings_percentage'], label='CO2 Savings Percentage', color='orange')
            plt.axhline(y=25, color='red', linestyle='--', label='25% Savings')
            plt.axhline(y=50, color='yellow', linestyle='--', label='50% Savings')
            plt.axhline(y=75, color='green', linestyle='--', label='75% Savings')
            plt.axhline(y=100, color='blue', linestyle='--', label='100% Savings')
            plt.title('CO2 Savings Percentage Over Time')
            plt.xlabel('Date')
            plt.ylabel('Savings Percentage (%)')
            plt.xticks(rotation=45)
            plt.legend()

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while visualizing data: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        tracker = GreenEnergyTracker('energy_data.csv')
        tracker.visualize_data()
    except Exception as e:
        print(f"Error: {e}")
```
