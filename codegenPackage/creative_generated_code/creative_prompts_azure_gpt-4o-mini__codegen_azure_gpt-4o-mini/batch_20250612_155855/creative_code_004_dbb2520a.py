"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carbondefi.pages.dev
Prompt: Describe the process of backtesting a trading strategy with real historical data on Carbon DeFi and provide an example.
Generated: DETERMINISTIC_dbb2520adf6318f3
Batch ID: 20250612_155855
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
from datetime import datetime

class Backtester:
    """
    A simple backtesting framework for trading strategies.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the Backtester with historical market data.

        :param data: A pandas DataFrame containing historical price data with 'date' and 'price' columns.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """ Validates the input data for necessary columns and data types. """
        required_columns = ['date', 'price']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        self.data['date'] = pd.to_datetime(self.data['date'])  # Ensure date is in datetime format
        if not np.issubdtype(self.data['price'].dtype, np.number):
            raise ValueError("Price column must be numeric.")

    def simple_moving_average(self, window: int) -> pd.Series:
        """
        Calculates the Simple Moving Average (SMA) for the price data.

        :param window: The number of periods over which to calculate the SMA.
        :return: A pandas Series containing the SMA values.
        """
        return self.data['price'].rolling(window=window).mean()

    def generate_signals(self, short_window: int, long_window: int) -> pd.DataFrame:
        """
        Generates buy/sell signals based on the short and long moving average strategy.

        :param short_window: The window size for the short moving average.
        :param long_window: The window size for the long moving average.
        :return: A DataFrame with signals and positions.
        """
        signals = pd.DataFrame(index=self.data.index)
        signals['price'] = self.data['price']
        signals['short_mavg'] = self.simple_moving_average(short_window)
        signals['long_mavg'] = self.simple_moving_average(long_window)
        signals['signal'] = 0
        signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1, 0)  # Buy signal
        signals['positions'] = signals['signal'].diff()  # Track positions
        return signals

    def backtest_strategy(self, short_window: int, long_window: int) -> pd.DataFrame:
        """
        Backtests the trading strategy over the historical data.

        :param short_window: The window size for the short moving average.
        :param long_window: The window size for the long moving average.
        :return: A DataFrame with backtest results, including returns.
        """
        signals = self.generate_signals(short_window, long_window)
        signals['daily_returns'] = signals['price'].pct_change()  # Daily returns
        signals['strategy_returns'] = signals['daily_returns'] * signals['positions'].shift()  # Strategy returns
        cumulative_returns = (1 + signals['strategy_returns']).cumprod() - 1  # Cumulative returns
        signals['cumulative_returns'] = cumulative_returns
        return signals

# Example usage:

if __name__ == "__main__":
    # Load historical price data for Carbon DeFi
    try:
        # Replace 'historical_data.csv' with the path to your actual data file
        data = pd.read_csv('historical_data.csv')
        # Initialize Backtester
        backtester = Backtester(data)

        # Set short and long window for moving averages
        short_window = 20
        long_window = 50

        # Backtest the strategy
        results = backtester.backtest_strategy(short_window, long_window)

        # Display the results
        print(results[['date', 'price', 'short_mavg', 'long_mavg', 'signal', 'cumulative_returns']])
    except Exception as e:
        print(f"Error during backtesting: {e}")
```
