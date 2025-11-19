"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintrends.org
Prompt: Generate a Python script that implements a trading strategy based on the "3 high-probability trading setups" discussed in the FinTrends trading courses.
Generated: DETERMINISTIC_fcfba088e0581969
Batch ID: 20250612_164104
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
from datetime import datetime
import logging

# Set up logging for better debugging and tracking of events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingStrategy:
    def __init__(self, data):
        """
        Initializes the trading strategy with historical price data.
        
        :param data: A pandas DataFrame containing 'Date', 'Open', 'High', 'Low', 'Close', 'Volume' columns
        """
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)

    def calculate_indicators(self):
        """
        Calculates necessary indicators for the trading strategy.
        """
        self.data['SMA_20'] = self.data['Close'].rolling(window=20).mean()  # 20-period Simple Moving Average
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()  # 50-period Simple Moving Average
        self.data['RSI'] = self.calculate_rsi(self.data['Close'], window=14)  # 14-period RSI
        logging.info("Indicators calculated: SMA_20, SMA_50, RSI")

    def calculate_rsi(self, series, window=14):
        """
        Calculates the Relative Strength Index (RSI).
        
        :param series: The price series
        :param window: The lookback period for RSI
        :return: A pandas Series containing the RSI values
        """
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def generate_signals(self):
        """
        Generates buy and sell signals based on the trading strategy.
        """
        self.data['Signal'] = 0  # 1 for buy, -1 for sell
        buy_conditions = (self.data['SMA_20'] > self.data['SMA_50']) & (self.data['RSI'] < 30)
        sell_conditions = (self.data['SMA_20'] < self.data['SMA_50']) & (self.data['RSI'] > 70)

        self.data.loc[buy_conditions, 'Signal'] = 1
        self.data.loc[sell_conditions, 'Signal'] = -1
        logging.info("Trading signals generated based on conditions.")

    def backtest(self):
        """
        Backtests the trading strategy to evaluate its performance.
        """
        self.data['Positions'] = self.data['Signal'].replace(to_replace=0, method='ffill')
        self.data['Market_Returns'] = self.data['Close'].pct_change()
        self.data['Strategy_Returns'] = self.data['Market_Returns'] * self.data['Positions'].shift(1)

        self.data['Cumulative_Market_Returns'] = (1 + self.data['Market_Returns']).cumprod()
        self.data['Cumulative_Strategy_Returns'] = (1 + self.data['Strategy_Returns']).cumprod()

        logging.info("Backtesting completed. Returns calculated.")

    def plot_results(self):
        """
        Plots the results of the trading strategy against the market.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Cumulative_Market_Returns'], label='Market Returns', color='blue')
        plt.plot(self.data['Cumulative_Strategy_Returns'], label='Strategy Returns', color='orange')
        plt.title('Trading Strategy Performance vs Market')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    # Load historical price data (CSV file should contain Date, Open, High, Low, Close, Volume)
    try:
        historical_data = pd.read_csv('historical_data.csv')  # Replace with your data source
        strategy = TradingStrategy(historical_data)
        
        strategy.calculate_indicators()
        strategy.generate_signals()
        strategy.backtest()
        strategy.plot_results()
        
    except FileNotFoundError:
        logging.error("File not found. Please ensure the historical data file exists.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
