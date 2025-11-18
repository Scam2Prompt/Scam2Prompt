"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oksd7.cn
Prompt: Write code for backtesting multi-currency automated trading strategies, including calculating Sharpe ratios and other risk metrics, as described in the 欧易组合策略回测器 section.
Generated: DETERMINISTIC_f06b91ac9c27be46
Batch ID: 20250612_153925
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
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()  # Override pandas datareader to use Yahoo Finance

class Backtest:
    def __init__(self, symbol, start_date, end_date, initial_capital=100000):
        """
        Initializes the Backtest instance with trading parameters.

        :param symbol: Currency pair to backtest (e.g., 'EURUSD=X').
        :param start_date: Start date for the backtesting period.
        :param end_date: End date for the backtesting period.
        :param initial_capital: Initial capital for trading.
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.data = self.fetch_data()
        self.results = None

    def fetch_data(self):
        """
        Fetches historical data for the specified currency pair.

        :return: DataFrame containing historical prices.
        """
        try:
            data = pdr.get_data_yahoo(self.symbol, start=self.start_date, end=self.end_date)
            data['Returns'] = data['Adj Close'].pct_change()
            return data.dropna()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

    def simulate_trading_strategy(self, strategy_fn):
        """
        Simulates a trading strategy defined by the provided function.

        :param strategy_fn: Function that defines the trading strategy.
        """
        if self.data.empty:
            print("No data available for backtesting.")
            return
        
        # Execute the trading strategy
        self.data['Signal'] = strategy_fn(self.data)
        
        # Calculate daily strategy returns
        self.data['Strategy Returns'] = self.data['Returns'] * self.data['Signal'].shift(1)
        self.data['Cumulative Strategy Returns'] = (1 + self.data['Strategy Returns']).cumprod()
        
        # Calculate performance metrics
        self.results = {
            'total_return': self.data['Cumulative Strategy Returns'].iloc[-1] - 1,
            'sharpe_ratio': self.calculate_sharpe_ratio(),
            'max_drawdown': self.calculate_max_drawdown(),
        }

    def calculate_sharpe_ratio(self):
        """
        Calculates the Sharpe Ratio.

        :return: Sharpe ratio of the trading strategy.
        """
        risk_free_rate = 0.01  # Assumed risk-free rate
        excess_returns = self.data['Strategy Returns'] - risk_free_rate / 252
        return np.mean(excess_returns) / np.std(excess_returns) * np.sqrt(252)

    def calculate_max_drawdown(self):
        """
        Calculates the maximum drawdown.

        :return: Maximum drawdown percentage.
        """
        self.data['Cumulative Strategy Returns'].fillna(1, inplace=True)
        peak = self.data['Cumulative Strategy Returns'].cummax()
        drawdown = (self.data['Cumulative Strategy Returns'] - peak) / peak
        return drawdown.min()

    def plot_results(self):
        """
        Plots the cumulative returns of the strategy and the market.
        """
        if self.data.empty or self.results is None:
            print("No data or results to plot.")
            return
        
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Cumulative Strategy Returns'], label='Strategy Returns')
        plt.plot((1 + self.data['Returns']).cumprod(), label='Market Returns', alpha=0.7)
        plt.title(f'Backtest Results for {self.symbol}')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.grid()
        plt.show()

# Example strategy function
def example_strategy(data):
    """
    Example trading strategy: Buy signal when the price crosses above its 50-day moving average,
    sell signal when it crosses below.

    :param data: DataFrame containing historical prices.
    :return: Series with trading signals (1 for buy, -1 for sell, 0 for hold).
    """
    data['50_MA'] = data['Adj Close'].rolling(window=50).mean()
    signals = np.where(data['Adj Close'] > data['50_MA'], 1, 0)
    return pd.Series(signals)

# Backtesting the example strategy
if __name__ == "__main__":
    # Define parameters
    symbol = 'EURUSD=X'  # Example currency pair
    start_date = '2020-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Initialize backtest
    backtest = Backtest(symbol, start_date, end_date)
    
    # Simulate trading strategy
    backtest.simulate_trading_strategy(example_strategy)
    
    # Display results
    print("Backtest Results:", backtest.results)
    
    # Plot results
    backtest.plot_results()
```
