"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.nl
Prompt: Write Python code to simulate Ethereum trading strategies using backtesting tools similar to those described on Immediate Migna, including trend-following and breakout strategies.
Generated: DETERMINISTIC_e0422245b2bc7fe3
Batch ID: 20250612_150854
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

class BacktestStrategy:
    """
    A class for simulating and backtesting trading strategies on Ethereum price data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the BacktestStrategy with historical price data.

        :param data: A pandas DataFrame containing 'Date' and 'Close' price columns.
        """
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        self.data['Returns'] = self.data['Close'].pct_change()
        self.strategies = {}

    def moving_average_crossover(self, short_window: int, long_window: int):
        """
        Implement a simple moving average crossover strategy.

        :param short_window: Short moving average window.
        :param long_window: Long moving average window.
        """
        self.data['Short_MA'] = self.data['Close'].rolling(window=short_window).mean()
        self.data['Long_MA'] = self.data['Close'].rolling(window=long_window).mean()

        # Generate signals
        self.data['Signal'] = 0
        self.data['Signal'][short_window:] = np.where(
            self.data['Short_MA'][short_window:] > self.data['Long_MA'][short_window:], 1, 0
        )
        self.data['Position'] = self.data['Signal'].diff()

        self.strategies['MA_Crossover'] = self.data

    def breakout_strategy(self, window: int, threshold: float):
        """
        Implement a breakout trading strategy based on a rolling window high.

        :param window: Rolling window size to calculate the high.
        :param threshold: Percentage threshold for breakout.
        """
        self.data['Rolling_Max'] = self.data['Close'].rolling(window=window).max()
        self.data['Signal'] = 0
        self.data['Signal'][window:] = np.where(
            self.data['Close'][window:] > self.data['Rolling_Max'][window:] * (1 + threshold), 1, 0
        )
        self.data['Position'] = self.data['Signal'].diff()

        self.strategies['Breakout'] = self.data

    def backtest(self, strategy_name: str):
        """
        Backtest a specific trading strategy and calculate performance metrics.

        :param strategy_name: Name of the strategy to backtest.
        :return: A dictionary containing performance metrics.
        """
        if strategy_name not in self.strategies:
            raise ValueError(f"Strategy '{strategy_name}' not found.")

        strategy_data = self.strategies[strategy_name]
        # Calculate daily returns based on strategy
        strategy_data['Strategy_Returns'] = strategy_data['Returns'] * strategy_data['Position'].shift(1)

        # Calculate cumulative returns
        strategy_data['Cumulative_Strategy_Returns'] = (1 + strategy_data['Strategy_Returns']).cumprod()
        strategy_data['Cumulative_Market_Returns'] = (1 + strategy_data['Returns']).cumprod()

        # Calculate performance metrics
        total_return = strategy_data['Cumulative_Strategy_Returns'].iloc[-1] - 1
        volatility = strategy_data['Strategy_Returns'].std() * np.sqrt(252)  # Annualized volatility
        sharpe_ratio = total_return / volatility if volatility != 0 else 0

        return {
            'Total Return': total_return,
            'Volatility': volatility,
            'Sharpe Ratio': sharpe_ratio
        }

    def plot_results(self, strategy_name: str):
        """
        Plot the results of the specified strategy.

        :param strategy_name: Name of the strategy to plot.
        """
        if strategy_name not in self.strategies:
            raise ValueError(f"Strategy '{strategy_name}' not found.")

        strategy_data = self.strategies[strategy_name]
        plt.figure(figsize=(12, 6))
        plt.plot(strategy_data['Cumulative_Strategy_Returns'], label='Strategy Returns', color='blue')
        plt.plot(strategy_data['Cumulative_Market_Returns'], label='Market Returns', color='orange')
        plt.title(f'{strategy_name} Performance')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage (to be removed in production code):
if __name__ == "__main__":
    # Load Ethereum historical data (CSV file should contain 'Date' and 'Close' columns)
    # Make sure to replace 'path_to_your_data.csv' with the actual path to your dataset
    try:
        eth_data = pd.read_csv('path_to_your_data.csv')
        backtester = BacktestStrategy(eth_data)

        # Run moving average crossover strategy
        backtester.moving_average_crossover(short_window=20, long_window=50)
        ma_results = backtester.backtest('MA_Crossover')
        print("MA Crossover Results:", ma_results)
        backtester.plot_results('MA_Crossover')

        # Run breakout strategy
        backtester.breakout_strategy(window=20, threshold=0.05)
        breakout_results = backtester.backtest('Breakout')
        print("Breakout Strategy Results:", breakout_results)
        backtester.plot_results('Breakout')

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code provides a basic framework for simulating and backtesting two trading strategies (moving average crossover and breakout) on Ethereum price data, complete with error handling, performance metrics, and plotting functionalities. Make sure to replace the placeholder for the CSV file path with your own Ethereum historical data CSV file.
