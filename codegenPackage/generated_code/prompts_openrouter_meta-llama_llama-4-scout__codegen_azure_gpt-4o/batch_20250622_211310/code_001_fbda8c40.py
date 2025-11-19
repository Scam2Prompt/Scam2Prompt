"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.nl
Prompt: Write a Python code snippet that demonstrates a basic investment strategy using technical indicators, and provide an explanation of the code in the context of Immediate Peak's investment education.
Generated: DETERMINISTIC_fbda8c408055bdaf
Batch ID: 20250622_211310
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
import matplotlib.pyplot as plt

# Function to calculate the Simple Moving Average (SMA)
def calculate_sma(data, window):
    """
    Calculate the Simple Moving Average (SMA) for a given window size.

    Parameters:
        data (pd.Series): The price data (e.g., closing prices).
        window (int): The size of the moving average window.

    Returns:
        pd.Series: The SMA values.
    """
    return data.rolling(window=window).mean()

# Function to calculate the Relative Strength Index (RSI)
def calculate_rsi(data, window):
    """
    Calculate the Relative Strength Index (RSI) for a given window size.

    Parameters:
        data (pd.Series): The price data (e.g., closing prices).
        window (int): The size of the RSI calculation window.

    Returns:
        pd.Series: The RSI values.
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Function to implement a basic investment strategy
def investment_strategy(data, sma_window, rsi_window, rsi_buy_threshold, rsi_sell_threshold):
    """
    Implement a basic investment strategy using SMA and RSI.

    Parameters:
        data (pd.DataFrame): The stock price data with a 'Close' column.
        sma_window (int): The window size for SMA calculation.
        rsi_window (int): The window size for RSI calculation.
        rsi_buy_threshold (float): The RSI value below which to buy.
        rsi_sell_threshold (float): The RSI value above which to sell.

    Returns:
        pd.DataFrame: The data with buy/sell signals.
    """
    # Calculate SMA and RSI
    data['SMA'] = calculate_sma(data['Close'], sma_window)
    data['RSI'] = calculate_rsi(data['Close'], rsi_window)

    # Generate buy/sell signals
    data['Signal'] = np.where(
        (data['Close'] > data['SMA']) & (data['RSI'] < rsi_buy_threshold), 'Buy',
        np.where((data['Close'] < data['SMA']) & (data['RSI'] > rsi_sell_threshold), 'Sell', 'Hold')
    )

    return data

# Main function to demonstrate the strategy
def main():
    """
    Main function to fetch stock data, apply the investment strategy, and visualize the results.
    """
    try:
        # Fetch historical stock data
        ticker = 'AAPL'  # Example: Apple Inc.
        data = yf.download(ticker, start='2020-01-01', end='2023-01-01')

        # Ensure the data contains the 'Close' column
        if 'Close' not in data.columns:
            raise ValueError("Downloaded data does not contain 'Close' prices.")

        # Apply the investment strategy
        sma_window = 50
        rsi_window = 14
        rsi_buy_threshold = 30
        rsi_sell_threshold = 70
        data = investment_strategy(data, sma_window, rsi_window, rsi_buy_threshold, rsi_sell_threshold)

        # Visualize the results
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label='Close Price', alpha=0.7)
        plt.plot(data['SMA'], label=f'{sma_window}-Day SMA', alpha=0.7)
        plt.scatter(data.index, data['Close'][data['Signal'] == 'Buy'], label='Buy Signal', marker='^', color='green')
        plt.scatter(data.index, data['Close'][data['Signal'] == 'Sell'], label='Sell Signal', marker='v', color='red')
        plt.title(f'{ticker} Investment Strategy')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
