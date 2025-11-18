"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: Create a Python script to analyze the socio-environmental impact of using laminated glass in construction projects, incorporating data on material recycling and energy savings.
Generated: DETERMINISTIC_5cf7c4e40f35c915
Batch ID: 20250612_142645
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

class LaminatedGlassAnalysis:
    """
    A class to analyze the socio-environmental impact of using laminated glass in construction projects.
    """

    def __init__(self, data_file):
        """
        Initializes the analysis with a data file containing information on laminated glass usage, recycling rates, and energy savings.

        :param data_file: str, path to the CSV data file
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads data from the specified CSV file into a pandas DataFrame.
        
        :return: DataFrame containing the data
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} does not exist.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def analyze_recycling(self):
        """
        Analyzes the recycling rates of laminated glass in the dataset and outputs statistics.
        """
        recycling_rate_mean = self.data['recycling_rate'].mean()
        recycling_rate_median = self.data['recycling_rate'].median()

        print(f"Average Recycling Rate: {recycling_rate_mean:.2f}%")
        print(f"Median Recycling Rate: {recycling_rate_median:.2f}%")

    def analyze_energy_savings(self):
        """
        Analyzes the energy savings associated with using laminated glass and outputs statistics.
        """
        energy_savings_mean = self.data['energy_savings'].mean()
        energy_savings_median = self.data['energy_savings'].median()

        print(f"Average Energy Savings: {energy_savings_mean:.2f} kWh/m²")
        print(f"Median Energy Savings: {energy_savings_median:.2f} kWh/m²")

    def plot_data(self):
        """
        Plots the recycling rates and energy savings for visual analysis.
        """
        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.bar(self.data['project_name'], self.data['recycling_rate'], color='g', alpha=0.6, label='Recycling Rate (%)')
        ax2.plot(self.data['project_name'], self.data['energy_savings'], color='b', marker='o', label='Energy Savings (kWh/m²)')

        ax1.set_xlabel('Project Name')
        ax1.set_ylabel('Recycling Rate (%)', color='g')
        ax2.set_ylabel('Energy Savings (kWh/m²)', color='b')

        ax1.tick_params(axis='y', labelcolor='g')
        ax2.tick_params(axis='y', labelcolor='b')

        plt.title('Recycling Rates and Energy Savings of Laminated Glass Projects')
        plt.xticks(rotation=45)
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Path to the data file
    data_file_path = 'laminated_glass_data.csv'
    
    # Initialize the analysis
    analysis = LaminatedGlassAnalysis(data_file_path)
    
    # Perform analyses
    analysis.analyze_recycling()
    analysis.analyze_energy_savings()
    
    # Plot the results
    analysis.plot_data()
```
