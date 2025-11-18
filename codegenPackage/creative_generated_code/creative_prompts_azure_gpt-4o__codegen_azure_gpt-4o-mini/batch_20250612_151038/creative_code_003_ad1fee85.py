"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orderly-network.pages.dev
Prompt: Provide an example of using the Orderly SDK to build a high-frequency trading bot that leverages deep liquidity.
Generated: DETERMINISTIC_ad1fee859c27436b
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
import random
import logging
from orderly_sdk import OrderlyAPI, OrderlyClient
from orderly_sdk.exceptions import OrderlyException

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO)

class HighFrequencyTradingBot:
    def __init__(self, api_key: str, api_secret: str, symbol: str):
        """
        Initialize the trading bot with API credentials and trading symbol.

        :param api_key: The API key for Orderly
        :param api_secret: The API secret for Orderly
        :param symbol: Trading symbol to buy/sell
        """
        self.client = OrderlyClient(api_key=api_key, api_secret=api_secret)
        self.symbol = symbol

    def get_market_data(self):
        """
        Fetch the latest market data for the specified symbol.
        
        :return: Market data as a dictionary or None on failure
        """
        try:
            market_data = self.client.get_market_data(self.symbol)
            return market_data
        except OrderlyException as e:
            logging.error(f"Failed to fetch market data: {e}")
            return None

    def place_order(self, order_type: str, quantity: float):
        """
        Place an order in the market.

        :param order_type: Type of order ('buy' or 'sell')
        :param quantity: Quantity of the asset to trade
        """
        try:
            if order_type == 'buy':
                response = self.client.place_order(symbol=self.symbol, side='buy', qty=quantity)
            elif order_type == 'sell':
                response = self.client.place_order(symbol=self.symbol, side='sell', qty=quantity)
            else:
                logging.error("Invalid order type specified.")
                return
            
            logging.info(f"Order placed successfully: {response}")
        except OrderlyException as e:
            logging.error(f"Failed to place order: {e}")

    def run(self):
        """
        Start the trading bot to execute high-frequency trading logic.
        The bot will run indefinitely until stopped.
        """
        while True:
            market_data = self.get_market_data()

            if market_data is None:
                time.sleep(1)  # Retry after a short delay
                continue

            # Example trading strategy: Buy if price is low, sell if price is high
            price = market_data['last_price']
            threshold_buy = market_data['bid'] * 0.99
            threshold_sell = market_data['ask'] * 1.01
            quantity = random.uniform(0.01, 1.0)  # Randomized quantity for demo purposes

            if price < threshold_buy:
                logging.info(f"Placing buy order at price {price}")
                self.place_order('buy', quantity)
            elif price > threshold_sell:
                logging.info(f"Placing sell order at price {price}")
                self.place_order('sell', quantity)

            time.sleep(0.5)  # Sleep to prevent overloading the API

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    API_SECRET = "your_api_secret_here"
    SYMBOL = "BTC/USD"
    
    trading_bot = HighFrequencyTradingBot(API_KEY, API_SECRET, SYMBOL)
    trading_bot.run()
```
