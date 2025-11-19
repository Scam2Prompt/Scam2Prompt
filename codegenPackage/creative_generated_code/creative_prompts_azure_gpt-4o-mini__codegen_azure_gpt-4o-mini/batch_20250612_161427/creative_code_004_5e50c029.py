"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gratisbitcoin-no.pages.dev
Prompt: What are the best practices for managing investments in Bitcoin and cryptocurrency, as highlighted in the Gratis Bitcoin content?
Generated: DETERMINISTIC_5e50c029ef4dac8b
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ccxt
import pandas as pd
import numpy as np
import logging

# Set up logging for monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoInvestmentManager:
    def __init__(self, exchange_id, api_key=None, secret=None):
        """
        Initialize the investment manager with the specified exchange.

        :param exchange_id: The ID of the exchange (e.g., 'binance')
        :param api_key: API key for authenticated access (optional)
        :param secret: Secret key for authenticated access (optional)
        """
        self.exchange = self.initialize_exchange(exchange_id, api_key, secret)

    def initialize_exchange(self, exchange_id, api_key, secret):
        """
        Initialize the exchange connection.

        :param exchange_id: The ID of the exchange
        :param api_key: API key for the exchange
        :param secret: Secret key for the exchange
        :return: Exchange object
        """
        try:
            exchange_class = getattr(ccxt, exchange_id)
            exchange = exchange_class({
                'apiKey': api_key,
                'secret': secret
            }) if api_key and secret else exchange_class()
            logging.info(f"Initialized exchange: {exchange_id}")
            return exchange
        except Exception as e:
            logging.error(f"Failed to initialize exchange: {e}")
            raise

    def fetch_balance(self):
        """
        Fetch the account balance from the exchange.

        :return: Account balance dictionary
        """
        try:
            balance = self.exchange.fetch_balance()
            logging.info("Fetched account balance successfully.")
            return balance
        except Exception as e:
            logging.error(f"Failed to fetch balance: {e}")
            raise

    def fetch_market_data(self, symbol):
        """
        Fetch market data for a specific cryptocurrency.

        :param symbol: The symbol of the cryptocurrency (e.g., 'BTC/USDT')
        :return: Market data DataFrame
        """
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe='1d')
            data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
            logging.info(f"Fetched market data for {symbol} successfully.")
            return data
        except Exception as e:
            logging.error(f"Failed to fetch market data for {symbol}: {e}")
            raise

    def calculate_moving_average(self, data, window_size):
        """
        Calculate the moving average of the closing prices.

        :param data: Market data DataFrame
        :param window_size: The window size for the moving average
        :return: DataFrame with moving average
        """
        data['moving_average'] = data['close'].rolling(window=window_size).mean()
        logging.info("Calculated moving average.")
        return data

    def make_investment_decision(self, data):
        """
        Determine whether to buy, sell, or hold based on moving average.

        :param data: DataFrame containing market data with moving average
        :return: Decision string
        """
        if data['close'].iloc[-1] > data['moving_average'].iloc[-1]:
            decision = "Buy"
        elif data['close'].iloc[-1] < data['moving_average'].iloc[-1]:
            decision = "Sell"
        else:
            decision = "Hold"
        
        logging.info(f"Investment decision made: {decision}")
        return decision

# Example usage:
if __name__ == "__main__":
    try:
        api_key = 'your_api_key'  # Replace with your API key
        secret = 'your_secret'     # Replace with your secret key
        manager = CryptoInvestmentManager('binance', api_key, secret)

        # Fetch balance
        balance = manager.fetch_balance()
        print(balance)

        # Fetch market data for Bitcoin
        market_data = manager.fetch_market_data('BTC/USDT')

        # Calculate moving average
        market_data = manager.calculate_moving_average(market_data, window_size=14)

        # Make investment decision
        decision = manager.make_investment_decision(market_data)
        print(f"Investment Decision: {decision}")

    except Exception as e:
        logging.critical(f"An error occurred in the investment manager: {e}")
```
