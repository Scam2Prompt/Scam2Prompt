"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateplatform.org
Prompt: Write code to simulate swing trading strategies using historical price data and trend lines, incorporating the technical analysis tools highlighted on MarvexTrader.
Generated: DETERMINISTIC_ff14947855b0a8da
Batch ID: 20250612_150854
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
from sklearn.linear_model import LinearRegression
import yfinance as yf

# Function to download historical price data
def download_data(ticker, start, end):
    """
    Downloads historical price data for the given ticker between start and end dates.

    :param ticker: Stock ticker symbol
    :param start: Start date (YYYY-MM-DD)
    :param end: End date (YYYY-MM-DD)
    :return: DataFrame containing historical price data
    """
    try:
        data = yf.download(ticker, start=start, end=end)
        return data
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None

# Function to calculate moving averages
def calculate_moving_average(data, window):
    """
    Calculates the moving average for a given window size.

    :param data: DataFrame containing price data
    :param window: Window size for moving average
    :return: Series with the moving average
    """
    return data['Close'].rolling(window=window).mean()

# Function to identify buy and sell signals
def identify_signals(data, short_window, long_window):
    """
    Identifies buy and sell signals based on moving averages.

    :param data: DataFrame containing price data
    :param short_window: Short moving average window
    :param long_window: Long moving average window
    :return: DataFrame with buy/sell signals
    """
    signals = pd.DataFrame(index=data.index)
    signals['Close'] = data['Close']
    signals['Short_MA'] = calculate_moving_average(data, short_window)
    signals['Long_MA'] = calculate_moving_average(data, long_window)

    # Creating buy (1) and sell (-1) signals
    signals['Signal'] = 0
    signals['Signal'][short_window:] = np.where(
        signals['Short_MA'][short_window:] > signals['Long_MA'][short_window:], 1, -1
    )
    return signals

# Function to visualize the trading signals
def plot_signals(data, signals):
    """
    Plots the closing prices with buy/sell signals and moving averages.

    :param data: DataFrame containing price data
    :param signals: DataFrame containing signals
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.5)
    plt.plot(signals['Short_MA'], label='Short Moving Average', color='red', alpha=0.75)
    plt.plot(signals['Long_MA'], label='Long Moving Average', color='green', alpha=0.75)

    # Plot buy signals
    plt.plot(signals[signals['Signal'] == 1].index,
             signals['Short_MA'][signals['Signal'] == 1],
             '^', markersize=10, color='g', label='Buy Signal')
    
    # Plot sell signals
    plt.plot(signals[signals['Signal'] == -1].index,
             signals['Short_MA'][signals['Signal'] == -1],
             'v', markersize=10, color='r', label='Sell Signal')

    plt.title('Swing Trading Strategy with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# Main function to execute the trading strategy simulation
def main(ticker, start_date, end_date, short_window, long_window):
    """
    Executes the swing trading strategy simulation.

    :param ticker: Stock ticker symbol
    :param start_date: Start date for the historical data
    :param end_date: End date for the historical data
    :param short_window: Short moving average window
    :param long_window: Long moving average window
    """
    # Download historical data
    data = download_data(ticker, start_date, end_date)

    if data is not None:
        # Identify buy/sell signals
        signals = identify_signals(data, short_window, long_window)

        # Visualize the signals
        plot_signals(data, signals)
    else:
        print("No data to analyze.")

# Example usage
if __name__ == "__main__":
    TICKER = 'AAPL'
    START_DATE = '2021-01-01'
    END_DATE = '2023-01-01'
    SHORT_WINDOW = 20
    LONG_WINDOW = 50
    
    main(TICKER, START_DATE, END_DATE, SHORT_WINDOW, LONG_WINDOW)
```
