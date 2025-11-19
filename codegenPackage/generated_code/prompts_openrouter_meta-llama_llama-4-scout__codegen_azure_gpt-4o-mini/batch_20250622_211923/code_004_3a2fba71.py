"""
Generated Code Metadata:
========================
Original URL: https://fiboex.com
Prompt: Generate code to create a simple Fibonacci-based trading strategy backtester using Python and relevant libraries.
Generated: DETERMINISTIC_3a2fba718c073906
Batch ID: 20250622_211923
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

class FibonacciTradingStrategy:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the FibonacciTradingStrategy with historical price data.

        :param data: A pandas DataFrame containing historical price data with a 'Close' column.
        """
        if 'Close' not in data.columns:
            raise ValueError("DataFrame must contain a 'Close' column.")
        
        self.data = data
        self.fibonacci_levels = self.calculate_fibonacci_levels()

    def calculate_fibonacci_levels(self) -> dict:
        """
        Calculate Fibonacci retracement levels based on the historical price data.

        :return: A dictionary containing Fibonacci levels.
        """
        max_price = self.data['Close'].max()
        min_price = self.data['Close'].min()
        difference = max_price - min_price

        levels = {
            'level_0': max_price,
            'level_236': max_price - difference * 0.236,
            'level_382': max_price - difference * 0.382,
            'level_618': max_price - difference * 0.618,
            'level_100': min_price
        }
        return levels

    def generate_signals(self) -> pd.DataFrame:
        """
        Generate buy and sell signals based on Fibonacci levels.

        :return: A DataFrame with signals.
        """
        signals = pd.DataFrame(index=self.data.index)
        signals['Close'] = self.data['Close']
        signals['Signal'] = 0  # Default to no signal

        # Generate buy signals
        signals.loc[signals['Close'] <= self.fibonacci_levels['level_382'], 'Signal'] = 1  # Buy signal
        # Generate sell signals
        signals.loc[signals['Close'] >= self.fibonacci_levels['level_236'], 'Signal'] = -1  # Sell signal

        return signals

    def backtest(self) -> pd.DataFrame:
        """
        Backtest the trading strategy and calculate returns.

        :return: A DataFrame with the backtest results.
        """
        signals = self.generate_signals()
        signals['Position'] = signals['Signal'].replace(to_replace=0, method='ffill')  # Forward fill positions
        signals['Market Return'] = self.data['Close'].pct_change()
        signals['Strategy Return'] = signals['Market Return'] * signals['Position'].shift(1)  # Shift position for next day

        # Calculate cumulative returns
        signals['Cumulative Market Return'] = (1 + signals['Market Return']).cumprod()
        signals['Cumulative Strategy Return'] = (1 + signals['Strategy Return']).cumprod()

        return signals

    def plot_results(self, results: pd.DataFrame):
        """
        Plot the backtest results.

        :param results: A DataFrame containing the backtest results.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(results['Cumulative Market Return'], label='Market Return', color='blue')
        plt.plot(results['Cumulative Strategy Return'], label='Strategy Return', color='orange')
        plt.title('Fibonacci Trading Strategy Backtest Results')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Load historical price data (ensure 'Close' column exists)
    try:
        data = pd.read_csv('historical_price_data.csv', parse_dates=True, index_col='Date')
        strategy = FibonacciTradingStrategy(data)
        results = strategy.backtest()
        strategy.plot_results(results)
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to have the required libraries installed (`pandas`, `numpy`, `matplotlib`) and replace `'historical_price_data.csv'` with the path to your actual historical price data file. The CSV file should contain a 'Close' column with the closing prices of the asset.
