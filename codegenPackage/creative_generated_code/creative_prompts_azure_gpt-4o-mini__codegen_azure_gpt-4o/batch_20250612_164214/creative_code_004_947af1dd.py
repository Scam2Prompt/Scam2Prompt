"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ftx-trading.com
Prompt: Create an example of a quantitative trading strategy that synthesizes principles from mathematics and computer science, reflecting FTX's investment philosophy.
Generated: DETERMINISTIC_947af1ddafd090e0
Batch ID: 20250612_164214
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression
from scipy.stats import zscore
import logging

# Set up logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantitativeTradingStrategy:
    def __init__(self, tickers, lookback_period=252, zscore_threshold=2.0, capital=100000):
        """
        Initialize the trading strategy with given parameters.

        :param tickers: List of stock tickers to trade.
        :param lookback_period: Number of trading days for historical analysis.
        :param zscore_threshold: Threshold for z-score to trigger trades.
        :param capital: Starting capital for the strategy.
        """
        self.tickers = tickers
        self.lookback_period = lookback_period
        self.zscore_threshold = zscore_threshold
        self.capital = capital
        self.positions = {ticker: 0 for ticker in tickers}  # No initial positions

    def fetch_data(self, ticker):
        """
        Fetch historical stock data from Yahoo Finance.

        :param ticker: Stock ticker symbol.
        :return: Pandas DataFrame with historical prices.
        """
        logging.info(f"Fetching data for {ticker}.")
        try:
            data = yf.download(ticker, period=f"{self.lookback_period}d", interval="1d")
            data = data[['Adj Close']].rename(columns={'Adj Close': 'price'})
            return data
        except Exception as e:
            logging.error(f"Failed to fetch data for {ticker}: {e}")
            return None

    def compute_mean_reversion_signal(self, prices):
        """
        Compute the mean-reversion signal using z-score of price deviations.

        :param prices: Pandas Series of historical prices.
        :return: Z-score values.
        """
        mean_price = prices.rolling(window=self.lookback_period).mean()
        stddev_price = prices.rolling(window=self.lookback_period).std()
        zscores = (prices - mean_price) / stddev_price
        return zscores

    def generate_signals(self, data):
        """
        Generate trading signals based on z-score thresholds.

        :param data: Pandas DataFrame containing the prices and z-scores.
        :return: A list of trading signals.
        """
        data['zscore'] = zscore(data['price'])
        data['signal'] = 0
        data.loc[data['zscore'] > self.zscore_threshold, 'signal'] = -1  # Sell signal
        data.loc[data['zscore'] < -self.zscore_threshold, 'signal'] = 1  # Buy signal
        return data

    def backtest(self, data):
        """
        Backtest the strategy using historical data.

        :param data: Pandas DataFrame with prices and signals.
        :return: Final portfolio value.
        """
        cash = self.capital
        position = 0

        for index, row in data.iterrows():
            if row['signal'] == 1 and cash > row['price']:  # Buy signal
                position += 1
                cash -= row['price']
                logging.info(f"Bought 1 unit at {row['price']} on {index}.")

            elif row['signal'] == -1 and position > 0:  # Sell signal
                position -= 1
                cash += row['price']
                logging.info(f"Sold 1 unit at {row['price']} on {index}.")

        final_portfolio_value = cash + position * data.iloc[-1]['price']
        logging.info(f"Final portfolio value: {final_portfolio_value}")
        return final_portfolio_value

    def execute(self):
        """
        Execute the trading strategy for the specified tickers.
        """
        for ticker in self.tickers:
            data = self.fetch_data(ticker)
            if data is not None:
                data = self.generate_signals(data)
                final_value = self.backtest(data)
                logging.info(f"Final portfolio value for {ticker}: {final_value}")


if __name__ == "__main__":
    # Example tickers: Replace with desired symbols
    tickers_list = ["AAPL", "GOOGL", "MSFT"]
    strategy = QuantitativeTradingStrategy(tickers=tickers_list, lookback_period=252, zscore_threshold=2.0, capital=100000)
    strategy.execute()
```
