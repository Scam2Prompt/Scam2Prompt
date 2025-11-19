"""
Generated Code Metadata:
========================
Original URL: https://the-bitcoin-optimizer-pro.com
Prompt: Develop a Python script for backtesting trading strategies using historical data, ensuring the strategies align with the customization capabilities mentioned in Bitcoin Optimizer.
Generated: DETERMINISTIC_0e4c3038d6174bd6
Batch ID: 20250612_151126
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

class Backtester:
    """
    A class to backtest trading strategies using historical data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the Backtester with historical data.

        :param data: A pandas DataFrame containing historical price data with 'Date', 'Open', 'High', 'Low', 'Close', 'Volume' columns.
        """
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)

    def moving_average_strategy(self, short_window: int, long_window: int):
        """
        Implements a moving average crossover strategy.

        :param short_window: The short moving average window.
        :param long_window: The long moving average window.
        :return: A DataFrame with signals and strategy returns.
        """
        # Calculate moving averages
        self.data['Short_MA'] = self.data['Close'].rolling(window=short_window, min_periods=1).mean()
        self.data['Long_MA'] = self.data['Close'].rolling(window=long_window, min_periods=1).mean()

        # Generate signals
        self.data['Signal'] = 0
        self.data['Signal'][short_window:] = np.where(
            self.data['Short_MA'][short_window:] > self.data['Long_MA'][short_window:], 1, 0
        )
        self.data['Position'] = self.data['Signal'].diff()

        # Calculate returns
        self.data['Strategy_Returns'] = self.data['Close'].pct_change() * self.data['Signal'].shift(1)

        return self.data

    def plot_results(self):
        """
        Plots the backtest results including price, moving averages, and buy/sell signals.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        plt.plot(self.data['Short_MA'], label='Short Moving Average', alpha=0.75)
        plt.plot(self.data['Long_MA'], label='Long Moving Average', alpha=0.75)

        # Plot buy signals
        plt.plot(self.data[self.data['Position'] == 1].index,
                 self.data['Short_MA'][self.data['Position'] == 1],
                 '^', markersize=10, color='g', lw=0, label='Buy Signal')

        # Plot sell signals
        plt.plot(self.data[self.data['Position'] == -1].index,
                 self.data['Short_MA'][self.data['Position'] == -1],
                 'v', markersize=10, color='r', lw=0, label='Sell Signal')

        plt.title('Backtest Results')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

    def calculate_performance(self):
        """
        Calculates and prints the performance metrics of the strategy.

        :return: A dictionary containing performance metrics.
        """
        total_return = self.data['Strategy_Returns'].sum()
        annualized_return = (1 + total_return) ** (252 / len(self.data)) - 1
        annualized_volatility = self.data['Strategy_Returns'].std() * np.sqrt(252)
        sharpe_ratio = annualized_return / annualized_volatility if annualized_volatility != 0 else 0

        performance_metrics = {
            'Total Return': total_return,
            'Annualized Return': annualized_return,
            'Annualized Volatility': annualized_volatility,
            'Sharpe Ratio': sharpe_ratio
        }

        print("Performance Metrics:")
        for key, value in performance_metrics.items():
            print(f"{key}: {value:.2%}")

        return performance_metrics

def main():
    # Load historical data
    try:
        data = pd.read_csv('historical_data.csv')  # Ensure the CSV file exists in the same directory
    except FileNotFoundError:
        print("Error: The historical data file was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The historical data file is empty.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Initialize the backtester
    backtester = Backtester(data)

    # Define moving average windows
    short_window = 20
    long_window = 50

    # Run the moving average strategy
    backtester.moving_average_strategy(short_window, long_window)

    # Plot the results
    backtester.plot_results()

    # Calculate and display performance metrics
    backtester.calculate_performance()

if __name__ == "__main__":
    main()
```
