"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learnatcheap.com
Prompt: Generate code to backtest price action trading strategies based on the MG Mentorship 2023 course listed on LearningAtCheap.com.
Generated: DETERMINISTIC_7692e705c5542572
Batch ID: 20250612_153224
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

class PriceActionBacktester:
    """
    A class to backtest price action trading strategies.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the backtester with historical price data.

        :param data: DataFrame containing historical price data with 'Date', 'Open', 'High', 'Low', 'Close'.
        """
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)

    def simple_moving_average(self, period: int):
        """
        Computes the Simple Moving Average (SMA) for a specified period.

        :param period: The period for which to calculate the SMA.
        :return: Series containing the SMA values.
        """
        return self.data['Close'].rolling(window=period).mean()

    def backtest_strategy(self, sma_period: int):
        """
        Backtests a simple price action strategy based on SMA crossover.

        :param sma_period: The period of the Simple Moving Average to determine buy/sell signals.
        :return: A DataFrame with the strategy results.
        """
        # Calculate SMA
        self.data['SMA'] = self.simple_moving_average(sma_period)

        # Create signals: buy (1) when price is above SMA, sell (-1) when below
        self.data['Signal'] = np.where(self.data['Close'] > self.data['SMA'], 1, -1)

        # Calculate daily returns
        self.data['Daily_Return'] = self.data['Close'].pct_change()

        # Calculate strategy returns
        self.data['Strategy_Return'] = self.data['Signal'].shift(1) * self.data['Daily_Return']

        return self.data

    def plot_results(self):
        """
        Plots the closing price, SMA, and buy/sell signals.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', color='blue', alpha=0.5)
        plt.plot(self.data['SMA'], label='SMA', color='orange', alpha=0.5)

        # Plot buy signals
        plt.plot(self.data[self.data['Signal'] == 1].index, 
                 self.data['SMA'][self.data['Signal'] == 1],
                 '^', markersize=10, color='g', label='Buy Signal')

        # Plot sell signals
        plt.plot(self.data[self.data['Signal'] == -1].index, 
                 self.data['SMA'][self.data['Signal'] == -1],
                 'v', markersize=10, color='r', label='Sell Signal')

        plt.title('Price Action Strategy Backtest Results')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

    def calculate_performance(self):
        """
        Calculates and prints the overall performance of the strategy.

        :return: None
        """
        total_return = self.data['Strategy_Return'].sum() * 100  # Convert to percentage
        print(f"Total Strategy Return: {total_return:.2f}%")
        print(f"Final Portfolio Value: {100 * (1 + self.data['Strategy_Return'].cumsum().iloc[-1]):.2f}")

# Example usage
if __name__ == '__main__':
    # Load your historical price data here
    # Data should have columns: 'Date', 'Open', 'High', 'Low', 'Close'
    try:
        historical_data = pd.read_csv('path_to_your_price_data.csv')  # Adjust path as necessary
        backtester = PriceActionBacktester(historical_data)
        results = backtester.backtest_strategy(sma_period=20)
        backtester.plot_results()
        backtester.calculate_performance()
    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
