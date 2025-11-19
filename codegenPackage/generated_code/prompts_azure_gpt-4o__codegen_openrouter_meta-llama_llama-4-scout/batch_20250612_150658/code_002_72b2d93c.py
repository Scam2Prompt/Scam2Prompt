"""
Generated Code Metadata:
========================
Original URL: https://supercore-7hg.pages.dev
Prompt: Generate code to fetch and display real-time stats and graphs for PLS/9MM token prices, including percentage changes over 24H, 1W, 1M, and 1Y.
Generated: DETERMINISTIC_72b2d93c02a33351
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

def get_token_price_stats(token_symbol):
    """
    Fetch real-time stats and graphs for the given token symbol.

    Args:
        token_symbol (str): The symbol of the token (e.g., PLS, 9MM).

    Returns:
        dict: A dictionary containing the token's current price, 
              24H, 1W, 1M, and 1Y percentage changes.
    """
    try:
        # Use yfinance to fetch token data
        token_data = yf.Ticker(token_symbol)

        # Get current market data
        current_price = token_data.info['currentPrice']

        # Calculate percentage changes
        hist_24h = token_data.history(period='2d')
        hist_1w = token_data.history(period='8d')
        hist_1m = token_data.history(period='30d')
        hist_1y = token_data.history(period='730d')

        # Calculate percentage changes
        change_24h = (hist_24h['Close'].iloc[-1] - hist_24h['Close'].iloc[0]) / hist_24h['Close'].iloc[0] * 100
        change_1w = (hist_1w['Close'].iloc[-1] - hist_1w['Close'].iloc[0]) / hist_1w['Close'].iloc[0] * 100
        change_1m = (hist_1m['Close'].iloc[-1] - hist_1m['Close'].iloc[0]) / hist_1m['Close'].iloc[0] * 100
        change_1y = (hist_1y['Close'].iloc[-1] - hist_1y['Close'].iloc[0]) / hist_1y['Close'].iloc[0] * 100

        # Create a dictionary to store the stats
        stats = {
            'current_price': current_price,
            'change_24h': change_24h,
            'change_1w': change_1w,
            'change_1m': change_1m,
            'change_1y': change_1y,
        }

        return stats

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def plot_token_price_history(token_symbol):
    """
    Plot the price history of the given token symbol.

    Args:
        token_symbol (str): The symbol of the token (e.g., PLS, 9MM).
    """
    try:
        # Use yfinance to fetch token data
        token_data = yf.Ticker(token_symbol)

        # Fetch historical market data
        hist_1y = token_data.history(period='730d')

        # Plot the price history
        plt.figure(figsize=(12, 6))
        plt.plot(hist_1y['Close'])
        plt.title(f'{token_symbol} Price History (1Y)')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    token_symbol = 'PLS-USD'  # Replace with the desired token symbol
    stats = get_token_price_stats(token_symbol)

    if stats:
        print(f"Current Price: ${stats['current_price']:.2f}")
        print(f"24H Change: {stats['change_24h']:.2f}%")
        print(f"1W Change: {stats['change_1w']:.2f}%")
        print(f"1M Change: {stats['change_1m']:.2f}%")
        print(f"1Y Change: {stats['change_1y']:.2f}%")

        plot_token_price_history(token_symbol)


if __name__ == "__main__":
    main()
```
