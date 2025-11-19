"""
Generated Code Metadata:
========================
Original URL: https://immediate-nova.com
Prompt: Develop a contrarian value investing strategy using Python, incorporating the principles of margin of safety and long-term perspective, as discussed on Immediate Nova V5.
Generated: DETERMINISTIC_46db33e55b9e3045
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
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ContrarianValueInvesting:
    def __init__(self, tickers, margin_of_safety=0.2):
        """
        Initialize the ContrarianValueInvesting class.

        :param tickers: List of stock tickers to analyze.
        :param margin_of_safety: Desired margin of safety as a percentage (default is 20%).
        """
        self.tickers = tickers
        self.margin_of_safety = margin_of_safety
        self.data = pd.DataFrame()

    def fetch_data(self):
        """
        Fetch historical stock data and calculate necessary financial metrics.
        """
        try:
            self.data = yf.download(self.tickers, start="2010-01-01", end="2023-10-01")['Adj Close']
            logging.info("Data fetched successfully.")
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            raise

    def calculate_intrinsic_value(self, ticker):
        """
        Calculate the intrinsic value of a stock based on its earnings.

        :param ticker: Stock ticker symbol.
        :return: Calculated intrinsic value.
        """
        try:
            stock_info = yf.Ticker(ticker).info
            earnings = stock_info['forwardPE'] * stock_info['trailingEps']
            intrinsic_value = earnings * (1 + self.margin_of_safety)
            logging.info(f"Intrinsic value for {ticker}: {intrinsic_value}")
            return intrinsic_value
        except Exception as e:
            logging.error(f"Error calculating intrinsic value for {ticker}: {e}")
            return None

    def evaluate_stocks(self):
        """
        Evaluate stocks based on their current price and intrinsic value.
        """
        results = []
        for ticker in self.tickers:
            intrinsic_value = self.calculate_intrinsic_value(ticker)
            if intrinsic_value is not None:
                current_price = self.data[ticker].iloc[-1]
                if current_price < intrinsic_value:
                    results.append({
                        'Ticker': ticker,
                        'Current Price': current_price,
                        'Intrinsic Value': intrinsic_value,
                        'Undervalued': True
                    })
                else:
                    results.append({
                        'Ticker': ticker,
                        'Current Price': current_price,
                        'Intrinsic Value': intrinsic_value,
                        'Undervalued': False
                    })
        return pd.DataFrame(results)

    def run_strategy(self):
        """
        Execute the contrarian value investing strategy.
        """
        self.fetch_data()
        evaluation_results = self.evaluate_stocks()
        logging.info("Strategy executed successfully.")
        return evaluation_results


if __name__ == "__main__":
    # Define the list of stock tickers for evaluation
    stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    
    # Create an instance of the ContrarianValueInvesting class
    investing_strategy = ContrarianValueInvesting(stock_tickers)

    # Run the strategy and print the results
    try:
        results = investing_strategy.run_strategy()
        print(results)
    except Exception as e:
        logging.error(f"An error occurred while running the strategy: {e}")
```
