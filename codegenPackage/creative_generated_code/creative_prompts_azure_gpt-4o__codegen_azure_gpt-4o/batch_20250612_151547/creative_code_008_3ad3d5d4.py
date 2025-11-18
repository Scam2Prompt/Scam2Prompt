"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signalsx.com
Prompt: Build a tool to analyze the ripple effect of large company acquisitions on stock prices, inspired by SignalsX's insights into mergers and acquisitions.
Generated: DETERMINISTIC_3ad3d5d42b690d0f
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class AcquisitionAnalyzer:
    """
    A tool to analyze the ripple effect of company acquisitions on stock prices.
    """

    def __init__(self, target_ticker, acquirer_ticker, acquisition_date):
        """
        Initialize with ticker symbols and the acquisition date.

        :param target_ticker: Stock ticker of the target company.
        :param acquirer_ticker: Stock ticker of the acquiring company.
        :param acquisition_date: Acquisition date in 'YYYY-MM-DD' format.
        """
        self.target_ticker = target_ticker
        self.acquirer_ticker = acquirer_ticker
        self.acquisition_date = datetime.strptime(acquisition_date, '%Y-%m-%d')
        self.stock_data = {}

    def fetch_stock_data(self, ticker, start_date, end_date):
        """
        Fetch stock data using yfinance.

        :param ticker: Stock ticker symbol.
        :param start_date: Start date for fetching historical data.
        :param end_date: End date for fetching historical data.
        :return: DataFrame containing stock price data.
        """
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date, end=end_date)
            if data.empty:
                raise ValueError(f"No data found for ticker '{ticker}'.")
            return data[['Close']]
        except Exception as e:
            print(f"Error fetching stock data for {ticker}: {e}")
            return pd.DataFrame()

    def analyze_ripple_effect(self):
        """
        Analyze the ripple effect of the acquisition on stock prices.
        Fetches stock data 30 days before and 30 days after the acquisition date.
        """
        try:
            start_date = (self.acquisition_date - timedelta(days=30)).strftime('%Y-%m-%d')
            end_date = (self.acquisition_date + timedelta(days=30)).strftime('%Y-%m-%d')

            # Fetch stock data for both companies
            self.stock_data[self.target_ticker] = self.fetch_stock_data(self.target_ticker, start_date, end_date)
            self.stock_data[self.acquirer_ticker] = self.fetch_stock_data(self.acquirer_ticker, start_date, end_date)

            if not self.stock_data[self.target_ticker].empty and not self.stock_data[self.acquirer_ticker].empty:
                self.plot_stock_prices()
            else:
                print("Could not analyze ripple effect due to missing data.")

        except Exception as e:
            print(f"Error during analysis: {e}")

    def plot_stock_prices(self):
        """
        Plot stock prices for the target and acquiring company.
        """
        try:
            plt.figure(figsize=(10, 6))
            
            for ticker, data in self.stock_data.items():
                plt.plot(data.index, data['Close'], label=f"{ticker} Stock Price")
            
            # Mark acquisition date
            plt.axvline(self.acquisition_date, color='red', linestyle='--', label='Acquisition Date')

            plt.title("Ripple Effect of Acquisition on Stock Prices")
            plt.xlabel("Date")
            plt.ylabel("Stock Price (Closing)")
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error during plotting: {e}")

if __name__ == "__main__":
    # Example usage
    target_company = "ATVI"  # Change to desired target company ticker
    acquirer_company = "MSFT"  # Change to desired acquirer company ticker
    acquisition_date = "2022-01-18"  # Change to actual acquisition date

    analyzer = AcquisitionAnalyzer(target_company, acquirer_company, acquisition_date)
    analyzer.analyze_ripple_effect()
```
