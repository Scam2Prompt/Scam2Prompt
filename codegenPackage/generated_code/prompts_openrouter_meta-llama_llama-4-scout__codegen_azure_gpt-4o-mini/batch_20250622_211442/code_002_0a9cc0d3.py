"""
Generated Code Metadata:
========================
Original URL: https://paperhanded-checker.pages.dev
Prompt: Generate code to visualize portfolio performance data using intuitive charts and graphs, inspired by Halo's analytics tools.
Generated: DETERMINISTIC_0a9cc0d3247b1904
Batch ID: 20250622_211442
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

# Set the style for seaborn
sns.set(style="whitegrid")

class PortfolioVisualizer:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the PortfolioVisualizer with the provided data.

        :param data: A pandas DataFrame containing portfolio performance data.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the necessary columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['Date', 'Portfolio Value', 'Benchmark Value']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def plot_performance(self):
        """
        Plots the portfolio performance over time, comparing it to a benchmark.
        """
        self.validate_data()

        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Date'], self.data['Portfolio Value'], label='Portfolio Value', color='blue')
        plt.plot(self.data['Date'], self.data['Benchmark Value'], label='Benchmark Value', color='orange')
        
        plt.title('Portfolio Performance Over Time', fontsize=16)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Value', fontsize=14)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_returns(self):
        """
        Plots the returns of the portfolio and benchmark.
        """
        self.validate_data()

        # Calculate daily returns
        self.data['Portfolio Returns'] = self.data['Portfolio Value'].pct_change()
        self.data['Benchmark Returns'] = self.data['Benchmark Value'].pct_change()

        plt.figure(figsize=(14, 7))
        sns.lineplot(data=self.data, x='Date', y='Portfolio Returns', label='Portfolio Returns', color='blue')
        sns.lineplot(data=self.data, x='Date', y='Benchmark Returns', label='Benchmark Returns', color='orange')

        plt.title('Portfolio vs Benchmark Returns', fontsize=16)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Returns', fontsize=14)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data creation for demonstration purposes
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'Portfolio Value': pd.Series(range(100, 200)).cumsum() + (pd.Series(range(100)).apply(lambda x: x * 0.5).cumsum()),
        'Benchmark Value': pd.Series(range(100, 200)).cumsum() + (pd.Series(range(100)).apply(lambda x: x * 0.3).cumsum())
    }
    
    # Create a DataFrame
    portfolio_data = pd.DataFrame(data)

    # Initialize the visualizer
    visualizer = PortfolioVisualizer(portfolio_data)

    # Plot performance and returns
    visualizer.plot_performance()
    visualizer.plot_returns()
```
