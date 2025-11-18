"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bit-turbo-pro.com
Prompt: Develop a customizable trading bot that allows users to set autonomy and support levels for trading Bitcoin and other cryptocurrencies, inspired by the features of Bit Turbo Pro.
Generated: DETERMINISTIC_e7e596d93419229b
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ccxt
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTradingBot:
    """
    A customizable trading bot for Bitcoin and other cryptocurrencies.
    Allows users to set autonomy and support levels for trading.
    """
    def __init__(self, exchange_name, api_key, api_secret, trading_pair, support_level, resistance_level, autonomy_level):
        """
        Initialize the trading bot with user-defined parameters.
        :param exchange_name: Name of the cryptocurrency exchange (e.g., 'binance').
        :param api_key: API key for the exchange.
        :param api_secret: API secret for the exchange.
        :param trading_pair: Trading pair (e.g., 'BTC/USDT').
        :param support_level: Price level to buy at.
        :param resistance_level: Price level to sell at.
        :param autonomy_level: Trading autonomy level (e.g., 'low', 'medium', 'high').
        """
        self.exchange_name = exchange_name
        self.api_key = api_key
        self.api_secret = api_secret
        self.trading_pair = trading_pair
        self.support_level = support_level
        self.resistance_level = resistance_level
        self.autonomy_level = autonomy_level
        
        # Initialize exchange instance
        self.exchange = self._initialize_exchange()
    
    def _initialize_exchange(self):
        """
        Initialize the exchange object using ccxt.
        :return: Exchange instance.
        """
        try:
            exchange_class = getattr(ccxt, self.exchange_name)
            exchange = exchange_class({
                'apiKey': self.api_key,
                'secret': self.api_secret,
                'enableRateLimit': True,
            })
            logging.info(f"Connected to {self.exchange_name} exchange.")
            return exchange
        except Exception as e:
            logging.error(f"Failed to initialize exchange: {e}")
            raise
    
    def fetch_market_price(self):
        """
        Fetch the current market price for the trading pair.
        :return: Current price.
        """
        try:
            ticker = self.exchange.fetch_ticker(self.trading_pair)
            current_price = ticker['last']
            logging.info(f"Current market price for {self.trading_pair}: {current_price}")
            return current_price
        except Exception as e:
            logging.error(f"Failed to fetch market price: {e}")
            raise
    
    def place_order(self, order_type, amount):
        """
        Place a buy or sell order.
        :param order_type: 'buy' or 'sell'.
        :param amount: Amount of cryptocurrency to trade.
        :return: Order details.
        """
        try:
            if order_type == 'buy':
                order = self.exchange.create_market_buy_order(self.trading_pair, amount)
            elif order_type == 'sell':
                order = self.exchange.create_market_sell_order(self.trading_pair, amount)
            else:
                raise ValueError("Invalid order type. Use 'buy' or 'sell'.")
            
            logging.info(f"Successfully placed {order_type} order: {order}")
            return order
        except Exception as e:
            logging.error(f"Failed to place {order_type} order: {e}")
            raise
    
    def calculate_trade_amount(self, current_price):
        """
        Calculate the trade amount based on autonomy level and current price.
        :param current_price: Current market price.
        :return: Trade amount.
        """
        # Example logic: Higher autonomy levels trade larger percentages of the balance
        autonomy_multiplier = {'low': 0.01, 'medium': 0.05, 'high': 0.1}
        try:
            balance = self.exchange.fetch_balance()
            quote_currency = self.trading_pair.split('/')[-1]
            available_balance = balance['free'][quote_currency]
            trade_amount = available_balance * autonomy_multiplier[self.autonomy_level]
            trade_amount /= current_price  # Convert to base currency amount
            logging.info(f"Calculated trade amount: {trade_amount} (Autonomy level: {self.autonomy_level})")
            return trade_amount
        except Exception as e:
            logging.error(f"Failed to calculate trade amount: {e}")
            raise
    
    def execute_trade_strategy(self):
        """
        Execute the trading strategy based on support and resistance levels.
        """
        try:
            current_price = self.fetch_market_price()
            trade_amount = self.calculate_trade_amount(current_price)
            
            if current_price <= self.support_level:
                logging.info("Current price is below support level. Placing buy order...")
                self.place_order('buy', trade_amount)
            elif current_price >= self.resistance_level:
                logging.info("Current price is above resistance level. Placing sell order...")
                self.place_order('sell', trade_amount)
            else:
                logging.info("Current price is within range. No action taken.")
        except Exception as e:
            logging.error(f"Error executing trade strategy: {e}")
    
    def start_trading(self, interval=60):
        """
        Start the trading bot and execute strategy periodically.
        :param interval: Time interval between strategy executions (in seconds).
        """
        logging.info("Starting trading bot...")
        try:
            while True:
                self.execute_trade_strategy()
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Trading bot stopped by user.")
        except Exception as e:
            logging.error(f"Error in trading bot: {e}")
            raise


# Example usage:
# Replace with your own exchange name, API credentials, and desired parameters.
if __name__ == "__main__":
    bot = CryptoTradingBot(
        exchange_name='binance',
        api_key='your_api_key',
        api_secret='your_api_secret',
        trading_pair='BTC/USDT',
        support_level=30000,  # Example support level
        resistance_level=40000,  # Example resistance level
        autonomy_level='medium'  # Trading autonomy level
    )
    bot.start_trading(interval=60)  # Check market conditions every 60 seconds
```
