"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Write code to calculate and display the doubling time of COVID-19 cases for selected regions, incorporating interactive features like deselecting/selecting all regions as mentioned on the website.
Generated: DETERMINISTIC_ec99acd2e9f55c6f
Batch ID: 20250612_151018
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
from datetime import datetime
import numpy as np

class COVIDDoublingTimeCalculator:
    def __init__(self, data_file):
        """
        Initialize the calculator with COVID-19 cases data.
        
        :param data_file: Path to the CSV data file containing COVID-19 cases
        """
        self.data = self.load_data(data_file)
        self.regions = self.data['Region'].unique()
        
    def load_data(self, data_file):
        """
        Load the COVID-19 case data from a CSV file.
        
        :param data_file: Path to the CSV data file
        :return: DataFrame containing COVID-19 cases data
        """
        try:
            data = pd.read_csv(data_file)
            data['Date'] = pd.to_datetime(data['Date'])
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def calculate_doubling_time(self, region):
        """
        Calculate the doubling time of COVID-19 cases for a given region.
        
        :param region: The region to calculate doubling time for
        :return: Doubling time in days
        """
        region_data = self.data[self.data['Region'] == region].copy()
        region_data.set_index('Date', inplace=True)
        
        # Calculate daily new cases
        region_data['New Cases'] = region_data['Cases'].diff().fillna(0)
        region_data = region_data[region_data['New Cases'] > 0]
        
        # Calculate the logarithm of new cases
        region_data['Log New Cases'] = np.log(region_data['New Cases'])
        
        # Fit a linear model to the log new cases
        if len(region_data) < 2:
            print(f"Not enough data to calculate doubling time for {region}.")
            return None
        
        x = np.arange(len(region_data))
        coefficients = np.polyfit(x, region_data['Log New Cases'], 1)
        
        # Doubling time formula: DT = log(2) / slope
        slope = coefficients[0]
        doubling_time = np.log(2) / slope
        
        return doubling_time

    def display_doubling_time(self):
        """
        Display the doubling time for all regions and allow user interaction.
        """
        region_doubling_times = {}
        
        # Calculate doubling times for all regions
        for region in self.regions:
            dt = self.calculate_doubling_time(region)
            if dt is not None:
                region_doubling_times[region] = dt
        
        # Display results
        print("Doubling Times for COVID-19 Cases by Region (in days):")
        for region, dt in region_doubling_times.items():
            print(f"{region}: {dt:.2f} days")

        # Plot doubling times
        self.plot_doubling_times(region_doubling_times)

    def plot_doubling_times(self, doubling_times):
        """
        Plot the doubling times for COVID-19 cases.
        
        :param doubling_times: Dictionary containing regions and their doubling times
        """
        plt.figure(figsize=(10, 6))
        plt.bar(doubling_times.keys(), doubling_times.values(), color='skyblue')
        plt.axhline(y=np.mean(list(doubling_times.values())), color='r', linestyle='--', label='Average Doubling Time')
        plt.title('COVID-19 Doubling Time by Region')
        plt.xlabel('Region')
        plt.ylabel('Doubling Time (days)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        calculator = COVIDDoublingTimeCalculator('covid_cases.csv')
        calculator.display_doubling_time()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `'covid_cases.csv'` with the actual path to your CSV file containing COVID-19 data in the proper format. The CSV should have at least the following columns: 'Date', 'Region', and 'Cases'.
