"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikqmph.firebaseapp.com
Prompt: Design a portfolio management tool for tracking cryptocurrency investments, including features like real-time price updates, portfolio diversification analysis, and alert systems for significant market changes.
Generated: DETERMINISTIC_d07d628b4b60ae0e
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_management_tool.py

import ccxt
import time
import pandas as pd
from datetime import datetime
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PortfolioManagementTool:
    def __init__(self, exchange_id, api_key, api_secret):
        """
        Initialize the portfolio management tool.

        Args:
        - exchange_id (str): The ID of the cryptocurrency exchange.
        - api_key (str): The API key for the exchange.
        - api_secret (str): The API secret for the exchange.
        """
        self.exchange_id = exchange_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'apiSecret': api_secret,
        })
        self.portfolio = {}

    def get_real_time_prices(self, symbols):
        """
        Get real-time prices for the given cryptocurrency symbols.

        Args:
        - symbols (list): A list of cryptocurrency symbols.

        Returns:
        - A dictionary with symbol as key and price as value.
        """
        prices = {}
        for symbol in symbols:
            try:
                ticker = self.exchange.fetch_ticker(symbol)
                prices[symbol] = ticker['close']
            except Exception as e:
                logger.error(f"Failed to get price for {symbol}: {str(e)}")
        return prices

    def update_portfolio(self, symbol, amount):
        """
        Update the portfolio with the given cryptocurrency symbol and amount.

        Args:
        - symbol (str): The cryptocurrency symbol.
        - amount (float): The amount of cryptocurrency.
        """
        if symbol in self.portfolio:
            self.portfolio[symbol] += amount
        else:
            self.portfolio[symbol] = amount

    def get_portfolio_value(self, prices):
        """
        Calculate the total value of the portfolio.

        Args:
        - prices (dict): A dictionary with symbol as key and price as value.

        Returns:
        - The total value of the portfolio.
        """
        total_value = 0
        for symbol, amount in self.portfolio.items():
            if symbol in prices:
                total_value += amount * prices[symbol]
        return total_value

    def diversification_analysis(self):
        """
        Perform portfolio diversification analysis.

        Returns:
        - A dictionary with symbol as key and diversification metrics as value.
        """
        analysis = {}
        total_value = self.get_portfolio_value(self.get_real_time_prices(self.portfolio.keys()))
        for symbol, amount in self.portfolio.items():
            price = self.get_real_time_prices([symbol])[symbol]
            value = amount * price
            analysis[symbol] = {
                'value': value,
                'percentage': (value / total_value) * 100
            }
        return analysis

    def set_alert(self, symbol, threshold):
        """
        Set an alert for significant market changes.

        Args:
        - symbol (str): The cryptocurrency symbol.
        - threshold (float): The threshold percentage.
        """
        current_price = self.get_real_time_prices([symbol])[symbol]
        previous_price = None
        while True:
            time.sleep(60)  # Check every minute
            new_price = self.get_real_time_prices([symbol])[symbol]
            if previous_price is not None:
                percentage_change = ((new_price - previous_price) / previous_price) * 100
                if abs(percentage_change) > threshold:
                    logger.warning(f"Alert: {symbol} price changed by {percentage_change}%")
            previous_price = new_price

def main():
    exchange_id = 'binance'
    api_key = 'YOUR_API_KEY'
    api_secret = 'YOUR_API_SECRET'

    tool = PortfolioManagementTool(exchange_id, api_key, api_secret)

    # Update portfolio
    tool.update_portfolio('BTC/USDT', 1.0)
    tool.update_portfolio('ETH/USDT', 5.0)

    # Get real-time prices
    symbols = ['BTC/USDT', 'ETH/USDT']
    prices = tool.get_real_time_prices(symbols)
    logger.info(f"Real-time prices: {prices}")

    # Get portfolio value
    portfolio_value = tool.get_portfolio_value(prices)
    logger.info(f"Portfolio value: {portfolio_value}")

    # Diversification analysis
    analysis = tool.diversification_analysis()
    logger.info(f"Diversification analysis: {analysis}")

    # Set alert
    tool.set_alert('BTC/USDT', 5.0)

if __name__ == '__main__':
    main()
```
