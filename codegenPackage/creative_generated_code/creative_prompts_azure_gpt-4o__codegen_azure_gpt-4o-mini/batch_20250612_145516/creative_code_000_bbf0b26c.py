"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Write a Python script to simulate the investment strategy timeline described on the SUI Strategies website, including the percentage allocations for SUI, APT, SOL, BTC, and USD across different quarters from 2024 to 2026.
Generated: DETERMINISTIC_bbf0b26ce389b095
Batch ID: 20250612_145516
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


class InvestmentPortfolio:
    """
    A class to represent an investment portfolio with a specific allocation strategy.

    Attributes:
        start_date (str): The starting date for the investment simulation.
        end_date (str): The ending date for the investment simulation.
        allocations (dict): A dictionary containing the percentage allocations for each asset.
        timeline (DataFrame): A DataFrame to hold the investment timeline data.
    """

    def __init__(self, start_date: str, end_date: str, allocations: dict):
        """
        Initializes the InvestmentPortfolio with a start date, end date, and asset allocations.

        Parameters:
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.
            allocations (dict): Dictionary containing asset names and their corresponding allocation percentages.
        """
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)
        self.allocations = allocations
        self.timeline = self.create_timeline()

    def create_timeline(self) -> pd.DataFrame:
        """
        Creates a timeline of investment allocations from start_date to end_date.

        Returns:
            DataFrame: A DataFrame containing quarterly dates and corresponding allocations.
        """
        # Generate quarterly dates
        dates = pd.date_range(start=self.start_date, end=self.end_date, freq='Q')
        
        # Create a DataFrame with dates and allocations
        timeline = pd.DataFrame(dates, columns=['Date'])
        for asset, allocation in self.allocations.items():
            timeline[asset] = allocation

        return timeline

    def plot_allocations(self):
        """
        Plots the allocation of assets over the specified timeline.
        """
        # Set the index to Date for easier plotting
        self.timeline.set_index('Date', inplace=True)

        # Plotting the allocations
        plt.figure(figsize=(10, 6))
        for asset in self.allocations.keys():
            plt.plot(self.timeline.index, self.timeline[asset], label=asset)

        plt.title('Investment Strategy Timeline')
        plt.xlabel('Date')
        plt.ylabel('Allocation (%)')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # Define the investment allocations as per the user request
    allocations = {
        'SUI': [20, 25, 30, 35, 40, 30],
        'APT': [15, 10, 20, 15, 10, 15],
        'SOL': [30, 25, 20, 15, 10, 20],
        'BTC': [10, 15, 10, 15, 20, 25],
        'USD': [25, 25, 20, 20, 20, 10]
    }

    # Specify the start and end dates for the simulation
    start_date = '2024-01-01'
    end_date = '2026-12-31'

    try:
        # Create an instance of the InvestmentPortfolio
        portfolio = InvestmentPortfolio(start_date, end_date, allocations)

        # Plot the allocations
        portfolio.plot_allocations()

    except Exception as e:
        print(f"An error occurred: {e}")
```
