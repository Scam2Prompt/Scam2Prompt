"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoin-optimizer-pro.com
Prompt: Develop a Python script for backtesting trading strategies using historical data, ensuring the strategies align with the customization capabilities mentioned in Bitcoin Optimizer.
Generated: DETERMINISTIC_0e4c3038d6174bd6
Batch ID: 20250612_151126
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

class Backtester:
    """
    A simple backtesting framework for trading strategies.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the Backtester with historical data.

        :param data: A pandas DataFrame containing historical price data with a datetime index.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame")
        self.data = data
        self.signals = pd.Series(index=data.index)

    def moving_average_strategy(self, short_window: int, long_window: int):
        """
        Implement a moving average crossover strategy.

        :param short_window: The number of periods for the short moving average.
        :param long_window: The number of periods for the long moving average.
        """
        self.data['Short_MA'] = self.data['Close'].rolling(window=short_window).mean()
        self.data['Long_MA'] = self.data['Close'].rolling(window=long_window).mean()

        # Generate signals
        self.signals = np.where(self.data['Short_MA'] > self.data['Long_MA'], 1.0, 0.0)
        self.signals = pd.Series(self.signals, index=self.data.index)

    def backtest(self, initial_capital: float):
        """
        Backtest the trading strategy and calculate performance metrics.

        :param initial_capital: The initial amount of capital to start with.
        :return: A DataFrame containing the portfolio value over time.
        """
        # Create a DataFrame to track portfolio value
        portfolio = pd.DataFrame(index=self.data.index)
        portfolio['Holdings'] = self.signals.shift(1) * self.data['Close']  # Buy at close of the day
        portfolio['Cash'] = initial_capital - (self.signals.shift(1) * self.data['Close']).cumsum()
        portfolio['Total_Value'] = portfolio['Holdings'] + portfolio['Cash']

        # Handle case where cash goes negative (not enough capital)
        if (portfolio['Cash'] < 0).any():
            raise ValueError("Insufficient capital for the trades suggested by the strategy")

        return portfolio

    def plot_results(self, portfolio: pd.DataFrame):
        """
        Plot the results of the backtest.

        :param portfolio: The portfolio DataFrame returned by the backtest method.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(portfolio['Total_Value'], label='Portfolio Value', color='blue')
        plt.title('Backtest Results')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.legend()
        plt.grid()
        plt.show()


def main():
    # Load historical data
    try:
        # Replace with your actual data source
        data = pd.read_csv('historical_data.csv', parse_dates=True, index_col='Date')
        if 'Close' not in data.columns:
            raise ValueError("'Close' column is required in the historical data")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Initialize Backtester
    backtester = Backtester(data)

    # Set strategy parameters
    short_window = 40
    long_window = 100

    # Run the moving average strategy
    backtester.moving_average_strategy(short_window, long_window)

    # Backtest the strategy
    try:
        portfolio = backtester.backtest(initial_capital=10000)
    except ValueError as e:
        print(f"Backtest error: {e}")
        return

    # Plot the results
    backtester.plot_results(portfolio)


if __name__ == '__main__':
    main()
```
