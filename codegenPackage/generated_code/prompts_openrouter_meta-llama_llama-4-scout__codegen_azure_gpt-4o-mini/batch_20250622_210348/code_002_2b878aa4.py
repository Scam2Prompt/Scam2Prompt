"""
Generated Code Metadata:
========================
Original URL: https://halo-orb.pages.dev
Prompt: Generate code to visualize portfolio performance data using intuitive charts and graphs, as described in HALO's analytics features.
Generated: DETERMINISTIC_2b878aa44fdf9784
Batch ID: 20250622_210348
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
import seaborn as sns

class PortfolioVisualizer:
    """
    A class to visualize portfolio performance data using charts and graphs.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the PortfolioVisualizer with portfolio performance data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing portfolio performance data with columns
                             'Date', 'Value', and 'Benchmark'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data to ensure it contains the required columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['Date', 'Value', 'Benchmark']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Ensure 'Date' is in datetime format
        self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')
        if self.data['Date'].isnull().any():
            raise ValueError("Date column contains invalid date values.")

    def plot_performance(self):
        """
        Plots the portfolio performance over time, comparing it with a benchmark.
        """
        plt.figure(figsize=(14, 7))
        sns.lineplot(data=self.data, x='Date', y='Value', label='Portfolio Value', color='blue')
        sns.lineplot(data=self.data, x='Date', y='Benchmark', label='Benchmark Value', color='orange')

        plt.title('Portfolio Performance vs Benchmark')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_monthly_returns(self):
        """
        Plots the monthly returns of the portfolio.
        """
        self.data['Return'] = self.data['Value'].pct_change()
        self.data['Month'] = self.data['Date'].dt.to_period('M')

        monthly_returns = self.data.groupby('Month')['Return'].mean().reset_index()
        plt.figure(figsize=(14, 7))
        sns.barplot(data=monthly_returns, x='Month', y='Return', color='green')

        plt.title('Average Monthly Returns')
        plt.xlabel('Month')
        plt.ylabel('Average Return')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Sample data creation for demonstration purposes
    sample_data = {
        'Date': pd.date_range(start='2020-01-01', periods=24, freq='M'),
        'Value': [100 + i * 5 for i in range(24)],
        'Benchmark': [100 + i * 4 for i in range(24)]
    }
    
    # Create a DataFrame
    portfolio_data = pd.DataFrame(sample_data)

    try:
        # Initialize the visualizer and plot performance
        visualizer = PortfolioVisualizer(portfolio_data)
        visualizer.plot_performance()
        visualizer.plot_monthly_returns()
    except ValueError as e:
        print(f"Error: {e}")
```
