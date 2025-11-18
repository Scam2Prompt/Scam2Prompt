"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi.net
Prompt: Develop a dashboard to track the Savings Rate over different time periods (1M, 3M, 1Y) using SparkFi.net's data.
Generated: DETERMINISTIC_e705c84565bf1226
Batch ID: 20250612_154115
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
from datetime import datetime, timedelta

class SavingsRateDashboard:
    """A class to track and visualize the Savings Rate over different time periods."""

    def __init__(self, data_source):
        """
        Initializes the SavingsRateDashboard with a data source.

        Args:
            data_source (str): The file path or URL to the data source containing Savings Rate data.
        """
        self.data_source = data_source
        self.savings_data = None

    def load_data(self):
        """Loads the savings rate data from the specified data source."""
        try:
            self.savings_data = pd.read_csv(self.data_source)
            # Parse dates and ensure the data is sorted
            self.savings_data['date'] = pd.to_datetime(self.savings_data['date'])
            self.savings_data.sort_values('date', inplace=True)
        except FileNotFoundError:
            print("Error: The data source file was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The data source file is empty.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def calculate_savings_rate(self, period):
        """
        Calculates the average savings rate over a specified period.

        Args:
            period (str): The time period for calculating the savings rate ('1M', '3M', '1Y').

        Returns:
            float: The average savings rate over the specified period.
        """
        end_date = self.savings_data['date'].max()
        start_date = self._get_start_date(period, end_date)

        period_data = self.savings_data[
            (self.savings_data['date'] >= start_date) & 
            (self.savings_data['date'] <= end_date)
        ]

        if period_data.empty:
            print(f"No data available for the period: {period}")
            return None

        average_rate = period_data['savings_rate'].mean()
        return average_rate

    def _get_start_date(self, period, end_date):
        """Helper method to determine the start date based on the given period."""
        if period == '1M':
            return end_date - timedelta(days=30)
        elif period == '3M':
            return end_date - timedelta(days=90)
        elif period == '1Y':
            return end_date - timedelta(days=365)
        else:
            raise ValueError("Invalid period specified. Use '1M', '3M', or '1Y'.")

    def plot_savings_rate(self):
        """Generates a plot of the savings rate over time."""
        if self.savings_data is None:
            print("No data available to plot.")
            return

        plt.figure(figsize=(12, 6))
        plt.plot(self.savings_data['date'], self.savings_data['savings_rate'], marker='o')
        plt.title('Savings Rate Over Time')
        plt.xlabel('Date')
        plt.ylabel('Savings Rate (%)')
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    dashboard = SavingsRateDashboard("savings_rate_data.csv")
    dashboard.load_data()

    # Calculate and print savings rates for different periods
    for period in ['1M', '3M', '1Y']:
        savings_rate = dashboard.calculate_savings_rate(period)
        if savings_rate is not None:
            print(f"Average Savings Rate for {period}: {savings_rate:.2f}%")

    # Plot the savings rate over time
    dashboard.plot_savings_rate()
```
