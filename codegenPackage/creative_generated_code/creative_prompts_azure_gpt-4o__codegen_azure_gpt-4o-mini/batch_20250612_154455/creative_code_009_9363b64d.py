"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financestargate.com
Prompt: Write a Python script to analyze the energy consumption of AI models at scale, inspired by Finance StarGate's exploration of AI's energy appetite.
Generated: DETERMINISTIC_9363b64dc3843866
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

class EnergyConsumptionAnalyzer:
    """
    A class to analyze the energy consumption of AI models at scale.
    """

    def __init__(self, data_file):
        """
        Initializes the EnergyConsumptionAnalyzer with the given data file.

        Parameters:
            data_file (str): Path to the CSV file containing energy consumption data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads energy consumption data from a CSV file.

        Returns:
            DataFrame: Pandas DataFrame containing the loaded data.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"The specified file does not exist: {self.data_file}")

        try:
            data = pd.read_csv(self.data_file)
            return data
        except Exception as e:
            raise RuntimeError(f"Error loading data: {e}")

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and converting data types.

        Returns:
            DataFrame: Preprocessed DataFrame.
        """
        # Fill missing values with the mean of the column
        self.data.fillna(self.data.mean(), inplace=True)

        # Ensure correct data types
        self.data['energy_consumed'] = self.data['energy_consumed'].astype(float)
        self.data['model_id'] = self.data['model_id'].astype(str)

    def analyze_consumption(self):
        """
        Analyzes energy consumption by plotting the results.

        Generates and saves plots of energy consumption per model.
        """
        plt.figure(figsize=(12, 6))
        sns.barplot(data=self.data, x='model_id', y='energy_consumed', estimator=np.sum, ci=None)
        plt.title('Total Energy Consumption per AI Model')
        plt.xlabel('Model ID')
        plt.ylabel('Total Energy Consumed (kWh)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('energy_consumption_analysis.png')
        plt.show()

    def summarize_consumption(self):
        """
        Summarizes the overall energy consumption statistics.

        Returns:
            dict: Summary statistics including total energy consumption,
            average energy per model, and model count.
        """
        total_consumption = self.data['energy_consumed'].sum()
        average_consumption = self.data['energy_consumed'].mean()
        model_count = self.data['model_id'].nunique()

        summary = {
            'total_energy_consumed': total_consumption,
            'average_energy_per_model': average_consumption,
            'model_count': model_count
        }

        # Save summary to a JSON file
        with open('energy_consumption_summary.json', 'w') as f:
            json.dump(summary, f, indent=4)

        return summary

    def run_analysis(self):
        """
        Executes the complete analysis pipeline.
        """
        self.preprocess_data()
        self.analyze_consumption()
        summary = self.summarize_consumption()
        print("Analysis complete. Summary saved to 'energy_consumption_summary.json'.")
        return summary


if __name__ == "__main__":
    # Define the path to the energy consumption data file
    DATA_FILE = 'energy_consumption_data.csv'

    # Create an instance of EnergyConsumptionAnalyzer and run the analysis
    analyzer = EnergyConsumptionAnalyzer(DATA_FILE)
    try:
        analyzer.run_analysis()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```
