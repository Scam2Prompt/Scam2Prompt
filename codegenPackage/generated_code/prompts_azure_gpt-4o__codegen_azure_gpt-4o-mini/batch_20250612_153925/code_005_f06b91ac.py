"""
Generated Code Metadata:
========================
Original URL: https://oksd7.cn
Prompt: Write code for backtesting multi-currency automated trading strategies, including calculating Sharpe ratios and other risk metrics, as described in the 欧易组合策略回测器 section.
Generated: DETERMINISTIC_f06b91ac9c27be46
Batch ID: 20250612_153925
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
from datetime import datetime
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Backtester:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the Backtester with historical price data.

        :param data: DataFrame containing historical price data with columns ['Date', 'Currency', 'Close']
        """
        self.data = data
        self.results = pd.DataFrame()

    def calculate_returns(self):
        """
        Calculate daily returns for each currency in the dataset.
        """
        self.data['Return'] = self.data.groupby('Currency')['Close'].pct_change()
        logging.info("Calculated daily returns.")

    def calculate_sharpe_ratio(self, risk_free_rate: float = 0.01):
        """
        Calculate the Sharpe Ratio for the strategy.

        :param risk_free_rate: The risk-free rate to use in the calculation
        :return: Sharpe Ratio
        """
        mean_return = self.data['Return'].mean()
        std_dev = self.data['Return'].std()
        sharpe_ratio = (mean_return - risk_free_rate) / std_dev
        logging.info(f"Calculated Sharpe Ratio: {sharpe_ratio}")
        return sharpe_ratio

    def calculate_max_drawdown(self):
        """
        Calculate the maximum drawdown of the strategy.

        :return: Maximum drawdown as a percentage
        """
        self.data['Cumulative_Return'] = (1 + self.data['Return']).cumprod()
        self.data['Peak'] = self.data['Cumulative_Return'].cummax()
        self.data['Drawdown'] = (self.data['Cumulative_Return'] - self.data['Peak']) / self.data['Peak']
        max_drawdown = self.data['Drawdown'].min()
        logging.info(f"Calculated Maximum Drawdown: {max_drawdown}")
        return max_drawdown

    def backtest_strategy(self):
        """
        Run the backtest and calculate performance metrics.
        """
        self.calculate_returns()
        sharpe_ratio = self.calculate_sharpe_ratio()
        max_drawdown = self.calculate_max_drawdown()

        self.results = pd.DataFrame({
            'Sharpe Ratio': [sharpe_ratio],
            'Max Drawdown': [max_drawdown]
        })

    def plot_results(self):
        """
        Plot the cumulative returns and drawdown.
        """
        plt.figure(figsize=(14, 7))
        plt.subplot(2, 1, 1)
        plt.plot(self.data['Cumulative_Return'], label='Cumulative Returns')
        plt.title('Cumulative Returns Over Time')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(self.data['Drawdown'], label='Drawdown', color='red')
        plt.title('Drawdown Over Time')
        plt.legend()

        plt.tight_layout()
        plt.show()

def main():
    # Load historical data (example CSV file)
    try:
        data = pd.read_csv('historical_data.csv', parse_dates=['Date'])
        data = data.sort_values(by='Date')
        logging.info("Loaded historical data successfully.")
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return

    # Initialize the backtester
    backtester = Backtester(data)

    # Run the backtest
    backtester.backtest_strategy()

    # Display results
    print(backtester.results)

    # Plot results
    backtester.plot_results()

if __name__ == "__main__":
    main()
```

Make sure to have a CSV file named `historical_data.csv` with the appropriate structure (columns: 'Date', 'Currency', 'Close') in the same directory as this script for it to run successfully.
