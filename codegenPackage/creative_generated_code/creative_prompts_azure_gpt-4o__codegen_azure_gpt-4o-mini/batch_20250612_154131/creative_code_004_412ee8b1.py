"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-axiomtrade.com
Prompt: Write a script to simulate day trading and swing trading strategies using historical price data, incorporating technical indicators like Bollinger Bands and RSI, as discussed on Ultronikclio.
Generated: DETERMINISTIC_412ee8b1501edb80
Batch ID: 20250612_154131
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
import yfinance as yf

class TradingSimulator:
    def __init__(self, ticker, start_date, end_date):
        """
        Initializes the TradingSimulator with historical price data.

        :param ticker: Stock ticker symbol
        :param start_date: Start date for fetching historical data
        :param end_date: End date for fetching historical data
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._fetch_data()
        self.signals = pd.DataFrame(index=self.data.index)

    def _fetch_data(self):
        """
        Fetches historical price data from Yahoo Finance.

        :return: DataFrame with historical price data
        """
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if data.empty:
                raise ValueError("No data fetched. Please check the ticker and date range.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def calculate_bollinger_bands(self, window=20, num_std=2):
        """
        Calculates Bollinger Bands.

        :param window: Number of periods for the moving average
        :param num_std: Number of standard deviations
        """
        rolling_mean = self.data['Close'].rolling(window).mean()
        rolling_std = self.data['Close'].rolling(window).std()
        self.signals['Upper Band'] = rolling_mean + (rolling_std * num_std)
        self.signals['Lower Band'] = rolling_mean - (rolling_std * num_std)

    def calculate_rsi(self, window=14):
        """
        Calculates the Relative Strength Index (RSI).

        :param window: Number of periods for RSI calculation
        """
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
        rs = gain / loss
        self.signals['RSI'] = 100 - (100 / (1 + rs))

    def generate_signals(self):
        """
        Generates buy/sell signals based on Bollinger Bands and RSI.
        """
        self.signals['Signal'] = 0
        self.signals['Signal'][self.signals['RSI'] < 30] = 1  # Buy signal
        self.signals['Signal'][self.signals['RSI'] > 70] = -1  # Sell signal
        self.signals['Position'] = self.signals['Signal'].replace(to_replace=0, method='ffill')

    def backtest_strategy(self):
        """
        Backtests the trading strategy based on generated signals.
        """
        self.data['Daily Returns'] = self.data['Close'].pct_change()
        self.data['Strategy Returns'] = self.data['Daily Returns'] * self.signals['Position'].shift(1)
        self.data['Cumulative Strategy Returns'] = (1 + self.data['Strategy Returns']).cumprod()
        self.data['Cumulative Market Returns'] = (1 + self.data['Daily Returns']).cumprod()

    def plot_results(self):
        """
        Plots the backtesting results.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Cumulative Market Returns'], label='Market Returns', color='blue')
        plt.plot(self.data['Cumulative Strategy Returns'], label='Strategy Returns', color='orange')
        plt.title(f'{self.ticker} Trading Strategy Performance')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.grid()
        plt.show()

    def run_simulation(self):
        """
        Runs the entire simulation process.
        """
        self.calculate_bollinger_bands()
        self.calculate_rsi()
        self.generate_signals()
        self.backtest_strategy()
        self.plot_results()


# Usage Example
if __name__ == "__main__":
    ticker = 'AAPL'  # Example: Apple Inc.
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    
    simulator = TradingSimulator(ticker, start_date, end_date)
    simulator.run_simulation()
```
