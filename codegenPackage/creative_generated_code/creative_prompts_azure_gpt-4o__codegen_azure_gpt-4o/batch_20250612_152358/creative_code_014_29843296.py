"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-trades.org
Prompt: Write a program to track and visualize the growth of committed funds and supported countries, inspired by Lite Trade's statistics and facts section.
Generated: DETERMINISTIC_2984329637b7ebb8
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import json
import os

class FundGrowthTracker:
    """
    A class to track and visualize the growth of committed funds and supported countries.
    """
    def __init__(self, data_file='fund_growth_data.json'):
        """
        Initialize the tracker with a data file.

        :param data_file: Path to the JSON file storing data about fund growth and countries
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Load data from the JSON file. Create a default structure if the file does not exist.

        :return: A dictionary storing committed funds and supported countries
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Data file is corrupted. Starting with an empty dataset.")
        return {"funds": [], "countries": []}

    def add_data_point(self, funds, supported_countries):
        """
        Add a new data point to track fund growth and supported countries.

        :param funds: Total committed funds (in USD)
        :param supported_countries: Number of supported countries
        """
        if funds < 0 or supported_countries < 0:
            print("Error: Funds and supported countries must be non-negative.")
            return

        self.data['funds'].append(funds)
        self.data['countries'].append(supported_countries)
        self._save_data()

    def _save_data(self):
        """
        Save the current data into the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save data file. {str(e)}")

    def visualize_growth(self):
        """
        Generate a line chart visualizing the growth of funds and supported countries.
        """
        if not self.data['funds'] or not self.data['countries']:
            print("No data to visualize. Please add data points first.")
            return

        plt.figure(figsize=(10, 6))

        # Plotting committed funds
        plt.plot(self.data['funds'], label='Committed Funds (USD)', marker='o')

        # Plotting supported countries
        plt.plot(self.data['countries'], label='Supported Countries', marker='s')

        # Adding labels, title, legend, and grid
        plt.title("Growth of Committed Funds and Supported Countries")
        plt.xlabel("Time (Data Points)")
        plt.ylabel("Growth Metrics")
        plt.legend()
        plt.grid(True)

        # Display the plot
        plt.show()


# Example usage
if __name__ == "__main__":
    tracker = FundGrowthTracker()

    # Adding data points
    tracker.add_data_point(funds=100000, supported_countries=10)
    tracker.add_data_point(funds=200000, supported_countries=15)
    tracker.add_data_point(funds=300000, supported_countries=20)

    # Visualizing growth
    tracker.visualize_growth()
```
