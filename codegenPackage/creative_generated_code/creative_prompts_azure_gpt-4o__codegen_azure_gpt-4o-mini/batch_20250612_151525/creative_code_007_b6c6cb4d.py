"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Create a Python program that models Tesla's stock performance over the last 12 months, using the data trends discussed in Ahmeti Wealth Management's blog.
Generated: DETERMINISTIC_b6c6cb4d143c81d8
Batch ID: 20250612_151525
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
from datetime import datetime, timedelta

# Define the main function to model Tesla's stock performance
def model_tesla_stock_performance():
    """
    Fetches Tesla's stock data for the last 12 months, analyzes performance trends,
    and visualizes the stock price along with moving averages.
    """

    # Define the stock ticker and time frame
    ticker = 'TSLA'
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    try:
        # Fetch Tesla stock data from Yahoo Finance
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        
        # Check if data is retrieved
        if stock_data.empty:
            raise ValueError("No data retrieved for the stock. Please check the ticker symbol.")

        # Calculate moving averages
        stock_data['20_MA'] = stock_data['Close'].rolling(window=20).mean()
        stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()

        # Plotting the stock performance
        plt.figure(figsize=(14, 7))
        plt.plot(stock_data['Close'], label='TSLA Close Price', color='blue')
        plt.plot(stock_data['20_MA'], label='20-Day Moving Average', color='orange', linestyle='--')
        plt.plot(stock_data['50_MA'], label='50-Day Moving Average', color='green', linestyle='--')

        # Adding titles and labels
        plt.title('Tesla (TSLA) Stock Performance Over the Last 12 Months', fontsize=16)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Price (USD)', fontsize=14)
        plt.legend()
        plt.grid()
        plt.tight_layout()

        # Save the plot as an image
        plt.savefig('tesla_stock_performance.png')
        plt.show()

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == '__main__':
    model_tesla_stock_performance()
```
