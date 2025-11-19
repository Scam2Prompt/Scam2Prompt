"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lumos-airdrop.pages.dev
Prompt: Design a financial dashboard that visualizes the performance of digital asset investments, incorporating features highlighted in Lumos Capital's approach to client engagement and transparency.
Generated: DETERMINISTIC_a99e53e003423959
Batch ID: 20250612_161035
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
import numpy as np

class AssetDashboard:
    """
    A class to represent a financial dashboard for visualizing digital asset investments.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the dashboard with asset data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing asset investment data with 'date', 'asset', 'value'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validate the input data to ensure it contains necessary columns.
        Raises ValueError if validation fails.
        """
        required_columns = {'date', 'asset', 'value'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")

        # Ensure 'date' is a datetime type and 'value' is numeric
        self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce')
        if self.data['date'].isnull().any():
            raise ValueError("Date column contains invalid date values.")
        
        if not np.issubdtype(self.data['value'].dtype, np.number):
            raise ValueError("Value column must be numeric.")

    def plot_investment_performance(self):
        """
        Visualize the performance of investments over time.
        Creates a line plot for each asset in the dataset.
        """
        plt.figure(figsize=(12, 6))
        
        # Grouping data by asset and date
        grouped_data = self.data.groupby(['date', 'asset'])['value'].sum().unstack()

        # Plotting each asset's performance
        for asset in grouped_data.columns:
            plt.plot(grouped_data.index, grouped_data[asset], marker='', label=asset)

        plt.title('Digital Asset Investment Performance')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.grid()
        plt.tight_layout()
        
        # Save plot to a file
        plt.savefig('investment_performance.png')
        plt.show()

    def calculate_performance_metrics(self):
        """
        Calculate key performance metrics for the investments.

        Returns:
        dict: A dictionary with performance metrics for each asset.
        """
        metrics = {}
        grouped_data = self.data.groupby('asset')['value'].sum()
        
        for asset, total_value in grouped_data.items():
            metrics[asset] = {
                'total_invested': total_value,
                'return_on_investment': (total_value - self.data[self.data['asset'] == asset]['value'].min()) / total_value
            }
        
        return metrics
        
# Example Usage
if __name__ == "__main__":
    # Sample Data
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'asset': ['Bitcoin', 'Bitcoin', 'Ethereum', 'Ethereum'],
        'value': [50000, 52000, 3000, 3200]
    }

    df = pd.DataFrame(data)

    try:
        dashboard = AssetDashboard(df)
        dashboard.plot_investment_performance()
        metrics = dashboard.calculate_performance_metrics()
        print(metrics)
    except ValueError as e:
        print(f"Error: {e}")
```
