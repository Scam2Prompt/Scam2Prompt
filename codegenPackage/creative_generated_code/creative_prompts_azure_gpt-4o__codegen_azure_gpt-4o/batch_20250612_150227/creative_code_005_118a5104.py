"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitnexusai.com
Prompt: Provide a step-by-step guide to integrate an automated trading bot with major cryptocurrency exchanges like Binance and Coinbase, inspired by BitNexusAi's functionality.
Generated: DETERMINISTIC_118a51048f072099
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import ccxt  # Library to interact with crypto exchanges
import logging  # For logging errors and info
import time  # To implement delays between API requests

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("trading_bot.log"), logging.StreamHandler()]
)

class TradingBot:
    """
    A crypto trading bot that integrates with Binance and Coinbase Pro.
    """
    def __init__(self, exchange_name: str, api_key: str, api_secret: str):
        """
        Initialize the bot with exchange credentials.

        :param exchange_name: Name of the exchange ('binance' or 'coinbasepro')
        :param api_key: API key for the exchange
        :param api_secret: API secret for the exchange
        """
        self.exchange_name = exchange_name.lower()
        self.api_key = api_key
        self.api_secret = api_secret

        try:
            # Instantiate exchange object based on the name
            if self.exchange_name == 'binance':
                self.exchange = ccxt.binance({
                    'apiKey': self.api_key,
                    'secret': self.api_secret,
                })
            elif self.exchange_name == 'coinbasepro':
                self.exchange = ccxt.coinbasepro({
                    'apiKey': self.api_key,
                    'secret': self.api_secret,
                })
            else:
                raise ValueError("Unsupported exchange. Use 'binance' or 'coinbasepro'.")
            
            # Test API connectivity
            self.exchange.check_required_credentials()
            logging.info(f"Successfully connected to {self.exchange_name.capitalize()} exchange.")
        except Exception as e:
            logging.error(f"Error initializing exchange: {str(e)}")
            raise

    def fetch_balance(self):
        """
        Fetch account balance from the exchange.

        :return: Account balance dictionary
        """
        try:
            balance = self.exchange.fetch_balance()
            logging.info(f"Fetched balance successfully: {balance}")
            return balance
        except Exception as e:
            logging.error(f"Error fetching balance: {str(e)}")
            return None

    def fetch_market_data(self, symbol: str):
        """
        Fetch market data for a specific trading pair.

        :param symbol: Trading pair symbol (e.g., 'BTC/USDT')
        :return: Market ticker dictionary
        """
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            logging.info(f"Fetched ticker data for {symbol}: {ticker}")
            return ticker
        except Exception as e:
            logging.error(f"Error fetching market data for {symbol}: {str(e)}")
            return None

    def place_order(self, symbol: str, order_type: str, side: str, amount: float, price: float = None):
        """
        Place an order on the exchange.

        :param symbol: Trading pair symbol (e.g., 'BTC/USDT')
        :param order_type: Order type ('limit' or 'market')
        :param side: Order side ('buy' or 'sell')
        :param amount: Amount to trade
        :param price: Limit price for 'limit' orders (optional for 'market' orders)
        :return: Order confirmation dictionary
        """
        try:
            if order_type == 'market':
                order = self.exchange.create_order(symbol, order_type, side, amount)
            elif order_type == 'limit':
                if price is None:
                    raise ValueError("Price is required for limit orders.")
                order = self.exchange.create_order(symbol, order_type, side, amount, price)
            else:
                raise ValueError("Invalid order type. Use 'market' or 'limit'.")
            
            logging.info(f"Order placed successfully: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing order: {str(e)}")
            return None

    def run_bot(self, symbol: str, strategy_function):
        """
        Main method to run the trading bot and apply a custom strategy.

        :param symbol: Trading pair symbol (e.g., 'BTC/USDT')
        :param strategy_function: A user-defined function that implements the trading logic
        """
        try:
            while True:
                # Fetch market data
                market_data = self.fetch_market_data(symbol)
                if market_data is None:
                    logging.warning("Market data unavailable. Retrying...")
                    time.sleep(10)
                    continue
                
                # Apply user-defined trading strategy
                strategy_function(self, market_data)
                
                # Delay before the next iteration
                time.sleep(5)
        except KeyboardInterrupt:
            logging.info("Bot stopped by user.")
        except Exception as e:
            logging.error(f"Error running bot: {str(e)}")

# Example user-defined strategy
def sample_strategy(bot: TradingBot, market_data: dict):
    """
    A sample trading strategy that decides to buy or sell based on market data.

    :param bot: Instance of TradingBot
    :param market_data: Market data dictionary
    """
    try:
        # Example logic: Buy if price is below a threshold, sell if above a threshold
        price = market_data['last']
        logging.info(f"Current price: {price}")
        if price < 20000:  # Example threshold for buying
            bot.place_order('BTC/USDT', 'market', 'buy', 0.001)  # Buy 0.001 BTC
        elif price > 30000:  # Example threshold for selling
            bot.place_order('BTC/USDT', 'market', 'sell', 0.001)  # Sell 0.001 BTC
    except Exception as e:
        logging.error(f"Error in strategy function: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace with actual API keys and secrets
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"

    # Instantiate the bot for Binance
    bot = TradingBot(exchange_name='binance', api_key=API_KEY, api_secret=API_SECRET)

    # Run the bot with the sample strategy
    bot.run_bot(symbol='BTC/USDT', strategy_function=sample_strategy)
```
