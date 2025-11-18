"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inceptiontrades.net
Prompt: Generate code to perform technical charting and fundamental research using tools similar to those provided by the Inception Trades platform.
Generated: DETERMINISTIC_8f0ae02d671e6c9f
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ta import trend, momentum, volume

# Define a class for technical and fundamental analysis
class InceptionTradesAnalysis:
    def __init__(self, ticker):
        """
        Initialize with the stock ticker symbol.
        :param ticker: Stock ticker string (e.g., 'AAPL', 'GOOG').
        """
        self.ticker = ticker
        self.data = None
        self.info = None

    def fetch_data(self, start_date, end_date):
        """
        Fetch historical stock data using Yahoo Finance.
        :param start_date: Start date for historical data (YYYY-MM-DD).
        :param end_date: End date for historical data (YYYY-MM-DD).
        """
        try:
            stock = yf.Ticker(self.ticker)
            self.data = stock.history(start=start_date, end=end_date)
            self.info = stock.info  # Fetch fundamental data
            if self.data.empty:
                raise ValueError("No historical data found for the given dates.")
        except Exception as e:
            print(f"Error fetching data: {e}")
            self.data = None

    def plot_technical_chart(self):
        """
        Plot technical chart with moving averages and RSI.
        """
        if self.data is None:
            print("No data available for technical charting.")
            return

        try:
            # Calculate Moving Averages
            self.data["SMA20"] = self.data["Close"].rolling(window=20).mean()
            self.data["SMA50"] = self.data["Close"].rolling(window=50).mean()

            # Calculate Relative Strength Index (RSI)
            self.data["RSI"] = momentum.rsi(self.data["Close"])

            # Plotting the data
            plt.figure(figsize=(14, 10))

            # Plot Closing Price and Moving Averages
            plt.subplot(2, 1, 1)
            plt.plot(self.data["Close"], label="Closing Price", color="blue")
            plt.plot(self.data["SMA20"], label="20-Day SMA", color="green")
            plt.plot(self.data["SMA50"], label="50-Day SMA", color="red")
            plt.title(f"{self.ticker} - Closing Price and Moving Averages")
            plt.legend()
            plt.grid()

            # Plot RSI
            plt.subplot(2, 1, 2)
            plt.plot(self.data["RSI"], label="RSI", color="purple")
            plt.axhline(70, linestyle="--", color="red")  # Overbought threshold
            plt.axhline(30, linestyle="--", color="green")  # Oversold threshold
            plt.title(f"{self.ticker} - Relative Strength Index (RSI)")
            plt.legend()
            plt.grid()

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting technical chart: {e}")

    def display_fundamental_data(self):
        """
        Display key fundamental data.
        """
        if self.info is None:
            print("No fundamental data available.")
            return

        try:
            fundamental_keys = [
                "marketCap", "forwardPE", "dividendYield", "beta", "earningsGrowth",
                "revenueGrowth", "currentPrice", "sector", "industry"
            ]

            print(f"Fundamental Data for {self.ticker}:")
            for key in fundamental_keys:
                value = self.info.get(key, "N/A")
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Error displaying fundamental data: {e}")


# Example usage of the class
if __name__ == "__main__":
    ticker = "AAPL"  # Replace with desired stock ticker
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    analysis = InceptionTradesAnalysis(ticker)
    analysis.fetch_data(start_date, end_date)
    analysis.plot_technical_chart()
    analysis.display_fundamental_data()
```

### Requirements:
1. Install dependencies using pip:
   ```bash
   pip install yfinance matplotlib pandas numpy ta
   ```
2. Ensure that `ta` (technical analysis library) is installed for RSI and other indicators.
