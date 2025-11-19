"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Write code to calculate and display the doubling time of COVID-19 cases for selected regions, incorporating interactive features like deselecting/selecting all regions as mentioned on the website.
Generated: DETERMINISTIC_ec99acd2e9f55c6f
Batch ID: 20250612_151018
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

class Covid19DoublingTimeCalculator:
    def __init__(self, data):
        """
        Initialize the Covid19DoublingTimeCalculator with a pandas DataFrame.

        Parameters:
        data (pd.DataFrame): A DataFrame containing COVID-19 case data with columns 'Region', 'Date', and 'Cases'.
        """
        self.data = data

    def calculate_doubling_time(self, region):
        """
        Calculate the doubling time for a given region.

        Parameters:
        region (str): The name of the region.

        Returns:
        float: The doubling time in days.
        """
        region_data = self.data[self.data['Region'] == region]
        region_data.sort_values(by='Date', inplace=True)

        # Check if there are at least two data points
        if len(region_data) < 2:
            return np.nan

        # Calculate the daily growth rate
        region_data['Daily Growth Rate'] = region_data['Cases'].pct_change()

        # Calculate the average daily growth rate
        avg_daily_growth_rate = region_data['Daily Growth Rate'].mean()

        # Calculate the doubling time
        if avg_daily_growth_rate <= 0:
            return np.nan
        doubling_time = np.log(2) / np.log(1 + avg_daily_growth_rate)

        return doubling_time

    def display_doubling_times(self, regions):
        """
        Display the doubling times for a list of regions.

        Parameters:
        regions (list): A list of region names.
        """
        doubling_times = {}
        for region in regions:
            doubling_time = self.calculate_doubling_time(region)
            doubling_times[region] = doubling_time

        return doubling_times

    def plot_doubling_times(self, regions):
        """
        Plot the doubling times for a list of regions.

        Parameters:
        regions (list): A list of region names.
        """
        doubling_times = self.display_doubling_times(regions)

        plt.bar(doubling_times.keys(), doubling_times.values())
        plt.xlabel('Region')
        plt.ylabel('Doubling Time (days)')
        plt.title('COVID-19 Doubling Times')
        plt.show()

def main():
    # Sample data
    data = pd.DataFrame({
        'Region': ['USA', 'USA', 'USA', 'Canada', 'Canada', 'Canada'],
        'Date': ['2020-01-01', '2020-01-15', '2020-02-01', '2020-01-01', '2020-01-15', '2020-02-01'],
        'Cases': [100, 200, 400, 50, 100, 200]
    })

    calculator = Covid19DoublingTimeCalculator(data)

    # Interactive features
    regions = data['Region'].unique()
    selected_regions = []

    while True:
        print("\nOptions:")
        print("1. Select all regions")
        print("2. Deselect all regions")
        print("3. Select regions")
        print("4. Display doubling times")
        print("5. Plot doubling times")
        print("6. Exit")

        option = input("Choose an option: ")

        if option == "1":
            selected_regions = regions.tolist()
            print("All regions selected.")
        elif option == "2":
            selected_regions = []
            print("All regions deselected.")
        elif option == "3":
            selected_regions = input("Enter region names (comma-separated): ").split(',')
            selected_regions = [region.strip() for region in selected_regions]
            selected_regions = [region for region in selected_regions if region in regions]
            print("Regions selected:", selected_regions)
        elif option == "4":
            if not selected_regions:
                print("No regions selected.")
                continue
            doubling_times = calculator.display_doubling_times(selected_regions)
            print("Doubling Times:")
            for region, doubling_time in doubling_times.items():
                print(f"{region}: {doubling_time:.2f} days")
        elif option == "5":
            if not selected_regions:
                print("No regions selected.")
                continue
            calculator.plot_doubling_times(selected_regions)
        elif option == "6":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
