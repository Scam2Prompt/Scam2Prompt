"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://algotech-trade-en.web.app
Prompt: Describe how to implement a mean reversion strategy on Algotech and provide an example of the code needed.
Generated: DETERMINISTIC_1b3c30a690b02152
Batch ID: 20250612_161353
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
import yfinance as yf

class MeanReversionStrategy:
    """
    A class to implement a mean reversion trading strategy.
    This strategy identifies when a stock price deviates significantly from its moving average (mean)
    and assumes it will revert back to the mean over time.
    """

    def __init__(self, symbol, start_date, end_date, window_size, threshold):
        """
        Initializes the MeanReversionStrategy instance.
        
        Parameters:
            symbol (str): The stock ticker symbol (e.g., 'AAPL').
            start_date (str): The start date for historical data in 'YYYY-MM-DD' format.
            end_date (str): The end date for historical data in 'YYYY-MM-DD' format.
            window_size (int): The moving average window size (e.g., 20 for 20-day SMA).
            threshold (float): The percentage threshold for mean reversion (e.g., 0.02 for 2%).
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.window_size = window_size
        self.threshold = threshold
        self.data = None

    def fetch_data(self):
        """
        Fetch historical stock data using Yahoo Finance.
        """
        try:
            self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        except Exception as e:
            print(f"Error fetching data for {self.symbol}: {e}")
            self.data = None

    def calculate_indicators(self):
        """
        Calculate the moving average and percentage deviations from the mean.
        """
        if self.data is not None:
            self.data['SMA'] = self.data['Close'].rolling(window=self.window_size).mean()
            self.data['Deviation'] = (self.data['Close'] - self.data['SMA']) / self.data['SMA']
        else:
            raise ValueError("Data not loaded. Ensure fetch_data() is called first.")

    def generate_signals(self):
        """
        Generate buy and sell signals based on the mean reversion strategy.
        Buy when the price is below the lower threshold, sell when above the upper threshold.
        """
        if self.data is not None:
            self.data['Signal'] = 0  # Default no signal
            self.data.loc[self.data['Deviation'] < -self.threshold, 'Signal'] = 1  # Buy signal
            self.data.loc[self.data['Deviation'] > self.threshold, 'Signal'] = -1  # Sell signal
        else:
            raise ValueError("Indicators not calculated. Ensure calculate_indicators() is called first.")

    def plot_signals(self):
        """
        Plot closing prices, moving average, and buy/sell signals for visualization.
        """
        if self.data is not None:
            plt.figure(figsize=(12, 6))
            plt.plot(self.data['Close'], label='Closing Price', alpha=0.6)
            plt.plot(self.data['SMA'], label=f'{self.window_size}-Day SMA', alpha=0.8)
            plt.scatter(self.data.index[self.data['Signal'] == 1], 
                        self.data['Close'][self.data['Signal'] == 1], 
                        label='Buy Signal', marker='^', color='green')
            plt.scatter(self.data.index[self.data['Signal'] == -1], 
                        self.data['Close'][self.data['Signal'] == -1], 
                        label='Sell Signal', marker='v', color='red')
            plt.title(f'Mean Reversion Strategy for {self.symbol}')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.show()
        else:
            raise ValueError("Signals not generated. Ensure generate_signals() is called first.")

# Example Usage
if __name__ == "__main__":
    # Define parameters for the strategy
    stock_symbol = 'AAPL'         # Stock symbol
    start_date = '2021-01-01'     # Start date for data
    end_date = '2023-01-01'       # End date for data
    moving_avg_window = 20        # 20-day moving average
    deviation_threshold = 0.02    # 2% deviation threshold

    # Initialize the strategy
    strategy = MeanReversionStrategy(stock_symbol, start_date, end_date, moving_avg_window, deviation_threshold)
    
    # Fetch data and process the strategy
    strategy.fetch_data()
    strategy.calculate_indicators()
    strategy.generate_signals()
    
    # Visualize the results
    strategy.plot_signals()
```
