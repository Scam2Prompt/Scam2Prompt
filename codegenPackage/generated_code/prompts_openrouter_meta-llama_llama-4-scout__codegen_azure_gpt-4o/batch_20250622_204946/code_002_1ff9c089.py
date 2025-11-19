"""
Generated Code Metadata:
========================
Original URL: https://fintrends.org
Prompt: Generate a high-probability trading setup using Trend Analysis and technical indicators, and provide a code example in Python for backtesting the strategy.
Generated: DETERMINISTIC_1ff9c089877759bc
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
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf

# Backtesting a trading strategy based on Moving Average Crossover and RSI

# Function to fetch historical data
def fetch_data(ticker, start_date, end_date):
    """
    Fetch historical stock data using yfinance.
    :param ticker: Stock ticker symbol (e.g., 'AAPL').
    :param start_date: Start date for historical data (e.g., '2020-01-01').
    :param end_date: End date for historical data (e.g., '2023-01-01').
    :return: DataFrame containing historical stock data.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            raise ValueError("No data fetched. Check ticker or date range.")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Function to calculate technical indicators
def calculate_indicators(data, short_window=50, long_window=200, rsi_period=14):
    """
    Calculate Moving Averages and RSI for trend analysis.
    :param data: DataFrame containing historical stock data.
    :param short_window: Window size for short-term moving average.
    :param long_window: Window size for long-term moving average.
    :param rsi_period: Period for RSI calculation.
    :return: DataFrame with added indicator columns.
    """
    data['SMA50'] = data['Close'].rolling(window=short_window).mean()
    data['SMA200'] = data['Close'].rolling(window=long_window).mean()
    
    # RSI Calculation
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    return data

# Function to generate trading signals
def generate_signals(data):
    """
    Generate buy and sell signals based on Moving Average Crossover and RSI.
    :param data: DataFrame containing historical stock data with indicators.
    :return: DataFrame with added signal column.
    """
    data['Signal'] = 0  # Default signal is 0 (no action)
    
    # Buy signal: SMA50 crosses above SMA200 and RSI is below 30 (oversold)
    data.loc[(data['SMA50'] > data['SMA200']) & (data['RSI'] < 30), 'Signal'] = 1
    
    # Sell signal: SMA50 crosses below SMA200 and RSI is above 70 (overbought)
    data.loc[(data['SMA50'] < data['SMA200']) & (data['RSI'] > 70), 'Signal'] = -1
    
    return data

# Backtesting function
def backtest_strategy(data, initial_balance=10000):
    """
    Backtest the trading strategy and calculate portfolio performance.
    :param data: DataFrame containing historical stock data with signals.
    :param initial_balance: Initial portfolio balance.
    :return: Final portfolio balance and performance metrics.
    """
    balance = initial_balance
    position = 0  # Number of shares held
    for index, row in data.iterrows():
        if row['Signal'] == 1:  # Buy signal
            if balance > row['Close']:  # Ensure we have enough balance to buy
                position += balance // row['Close']  # Buy as many shares as possible
                balance -= position * row['Close']  # Deduct cost from balance
        elif row['Signal'] == -1:  # Sell signal
            if position > 0:  # Ensure we have shares to sell
                balance += position * row['Close']  # Add proceeds to balance
                position = 0  # Reset position
    
    # Final portfolio value
    final_balance = balance + (position * data.iloc[-1]['Close'])
    return final_balance

# Main function
def main():
    """
    Main function to execute the trading strategy and backtest.
    """
    # Parameters
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    
    # Fetch data
    data = fetch_data(ticker, start_date, end_date)
    if data is None:
        return
    
    # Calculate indicators
    data = calculate_indicators(data)
    
    # Generate signals
    data = generate_signals(data)
    
    # Backtest strategy
    final_balance = backtest_strategy(data)
    print(f"Final Portfolio Balance: ${final_balance:.2f}")
    
    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', alpha=0.5)
    plt.plot(data['SMA50'], label='SMA50', alpha=0.75)
    plt.plot(data['SMA200'], label='SMA200', alpha=0.75)
    plt.scatter(data.index[data['Signal'] == 1], data['Close'][data['Signal'] == 1], label='Buy Signal', marker='^', color='green')
    plt.scatter(data.index[data['Signal'] == -1], data['Close'][data['Signal'] == -1], label='Sell Signal', marker='v', color='red')
    plt.title(f"{ticker} Trading Strategy")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# Run the program
if __name__ == "__main__":
    main()
```
