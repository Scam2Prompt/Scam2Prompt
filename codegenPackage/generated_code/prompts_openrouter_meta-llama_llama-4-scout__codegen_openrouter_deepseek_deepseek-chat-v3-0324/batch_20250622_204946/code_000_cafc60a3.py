"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Write a Python script to implement a simple Forex trading strategy using technical indicators, such as moving averages and RSI, for a beginner trader.
Generated: DETERMINISTIC_cafc60a3d17bb641
Batch ID: 20250622_204946
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
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class ForexTradingStrategy:
    """
    A simple Forex trading strategy using SMA and RSI indicators.
    """
    
    def __init__(self, symbol, start_date, end_date, short_window=20, long_window=50, rsi_window=14, rsi_buy_threshold=30, rsi_sell_threshold=70):
        """
        Initialize the trading strategy.
        
        Parameters:
        - symbol: Forex pair symbol (e.g., 'EURUSD=X')
        - start_date: Start date for historical data
        - end_date: End date for historical data
        - short_window: Short-term SMA window
        - long_window: Long-term SMA window
        - rsi_window: RSI calculation window
        - rsi_buy_threshold: RSI threshold for buy signal
        - rsi_sell_threshold: RSI threshold for sell signal
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.short_window = short_window
        self.long_window = long_window
        self.rsi_window = rsi_window
        self.rsi_buy_threshold = rsi_buy_threshold
        self.rsi_sell_threshold = rsi_sell_threshold
        self.data = None
        
    def fetch_data(self):
        """Fetch historical forex data from Yahoo Finance."""
        try:
            self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            if self.data.empty:
                raise ValueError("No data fetched for the given symbol and date range.")
            self.data['SMA_short'] = self.data['Close'].rolling(window=self.short_window).mean()
            self.data['SMA_long'] = self.data['Close'].rolling(window=self.long_window).mean()
            self._calculate_rsi()
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise

    def _calculate_rsi(self):
        """Calculate Relative Strength Index (RSI)."""
        delta = self.data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=self.rsi_window).mean()
        avg_loss = loss.rolling(window=self.rsi_window).mean()
        
        rs = avg_gain / avg_loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
        
    def generate_signals(self):
        """Generate trading signals based on SMA crossover and RSI."""
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        # Initialize signals column
        self.data['Signal'] = 0
        
        # SMA crossover signals
        self.data.loc[self.data['SMA_short'] > self.data['SMA_long'], 'Signal'] = 1
        self.data.loc[self.data['SMA_short'] < self.data['SMA_long'], 'Signal'] = -1
        
        # RSI signals
        self.data.loc[self.data['RSI'] < self.rsi_buy_threshold, 'Signal'] = 1
        self.data.loc[self.data['RSI'] > self.rsi_sell_threshold, 'Signal'] = -1
        
    def backtest(self):
        """Backtest the trading strategy."""
        if 'Signal' not in self.data.columns:
            raise ValueError("Signals not generated. Call generate_signals() first.")
            
        # Calculate daily returns
        self.data['Daily_Return'] = self.data['Close'].pct_change()
        
        # Calculate strategy returns
        self.data['Strategy_Return'] = self.data['Signal'].shift(1) * self.data['Daily_Return']
        
        # Calculate cumulative returns
        self.data['Cumulative_Market'] = (1 + self.data['Daily_Return']).cumprod()
        self.data['Cumulative_Strategy'] = (1 + self.data['Strategy_Return']).cumprod()
        
        return self.data[['Cumulative_Market', 'Cumulative_Strategy']].iloc[-1]
    
    def plot_results(self):
        """Plot the cumulative returns of the strategy vs. market."""
        if 'Cumulative_Market' not in self.data.columns:
            raise ValueError("Backtest not performed. Call backtest() first.")
            
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Cumulative_Market'], label='Market Returns', alpha=0.5)
        plt.plot(self.data['Cumulative_Strategy'], label='Strategy Returns', alpha=0.5)
        plt.title('Forex Trading Strategy Backtest')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Set parameters
        symbol = 'EURUSD=X'
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        
        # Initialize strategy
        strategy = ForexTradingStrategy(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            short_window=10,
            long_window=30,
            rsi_window=14,
            rsi_buy_threshold=30,
            rsi_sell_threshold=70
        )
        
        # Execute strategy
        strategy.fetch_data()
        strategy.generate_signals()
        results = strategy.backtest()
        
        print(f"Market Return: {results['Cumulative_Market']:.2f}")
        print(f"Strategy Return: {results['Cumulative_Strategy']:.2f}")
        
        # Plot results
        strategy.plot_results()
        
    except Exception as e:
        print(f"Error running strategy: {e}")
```
