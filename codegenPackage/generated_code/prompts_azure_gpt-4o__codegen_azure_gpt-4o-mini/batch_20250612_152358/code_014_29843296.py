"""
Generated Code Metadata:
========================
Original URL: https://lite-trades.org
Prompt: Write a program to track and visualize the growth of committed funds and supported countries, inspired by Lite Trade's statistics and facts section.
Generated: DETERMINISTIC_2984329637b7ebb8
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd

class FundTracker:
    def __init__(self):
        """Initialize the FundTracker with empty data."""
        self.data = pd.DataFrame(columns=['Year', 'Committed Funds', 'Supported Countries'])

    def add_data(self, year, committed_funds, supported_countries):
        """
        Add a new entry to the tracker.

        Parameters:
        year (int): The year of the data entry.
        committed_funds (float): The amount of committed funds.
        supported_countries (int): The number of supported countries.
        """
        if year in self.data['Year'].values:
            raise ValueError(f"Data for year {year} already exists.")
        
        new_entry = {'Year': year, 'Committed Funds': committed_funds, 'Supported Countries': supported_countries}
        self.data = self.data.append(new_entry, ignore_index=True)

    def visualize_growth(self):
        """Visualize the growth of committed funds and supported countries over the years."""
        if self.data.empty:
            raise ValueError("No data available to visualize.")

        # Set the figure size
        plt.figure(figsize=(12, 6))

        # Plot committed funds
        plt.subplot(1, 2, 1)
        plt.plot(self.data['Year'], self.data['Committed Funds'], marker='o', color='b', label='Committed Funds')
        plt.title('Growth of Committed Funds')
        plt.xlabel('Year')
        plt.ylabel('Committed Funds ($)')
        plt.grid()
        plt.legend()

        # Plot supported countries
        plt.subplot(1, 2, 2)
        plt.plot(self.data['Year'], self.data['Supported Countries'], marker='o', color='g', label='Supported Countries')
        plt.title('Growth of Supported Countries')
        plt.xlabel('Year')
        plt.ylabel('Number of Supported Countries')
        plt.grid()
        plt.legend()

        # Show the plots
        plt.tight_layout()
        plt.show()

def main():
    """Main function to run the FundTracker."""
    tracker = FundTracker()

    # Example data entries
    try:
        tracker.add_data(2020, 1000000, 5)
        tracker.add_data(2021, 1500000, 8)
        tracker.add_data(2022, 2000000, 10)
        tracker.add_data(2023, 2500000, 12)

        # Visualize the growth
        tracker.visualize_growth()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
