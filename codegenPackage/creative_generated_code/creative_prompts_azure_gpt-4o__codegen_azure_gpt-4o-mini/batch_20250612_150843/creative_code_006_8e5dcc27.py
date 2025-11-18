"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitlq-matrix.com
Prompt: Generate a Python script for auto-trading Bitcoin and other cryptocurrencies, allowing customization of trading preferences, as offered by BitLQ Matrix.
Generated: DETERMINISTIC_8e5dcc27514f3573
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

# Set up logging
logging.basicConfig(level=logging.INFO, filename='crypto_trader.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTrader:
    def __init__(self, exchange_id, api_key, secret, trading_pair, investment_amount, strategy):
        """
        Initialize the CryptoTrader with the exchange and trading preferences.

        :param exchange_id: The ID of the exchange (e.g., 'binance')
        :param api_key: Your API key for the exchange
        :param secret: Your API secret for the exchange
        :param trading_pair: The trading pair to trade (e.g., 'BTC/USDT')
        :param investment_amount: Amount of currency to invest in each trade
        :param strategy: Trading strategy function
        """
        self.exchange = self.connect_to_exchange(exchange_id, api_key, secret)
        self.trading_pair = trading_pair
        self.investment_amount = investment_amount
        self.strategy = strategy

    def connect_to_exchange(self, exchange_id, api_key, secret):
        """
        Connect to the specified exchange using ccxt.

        :param exchange_id: The ID of the exchange to connect to
        :param api_key: Your API key for the exchange
        :param secret: Your API secret for the exchange
        :return: An instance of the exchange
        """
        try:
            exchange_class = getattr(ccxt, exchange_id)
            return exchange_class({
                'apiKey': api_key,
                'secret': secret,
            })
        except Exception as e:
            logging.error(f"Error connecting to exchange: {str(e)}")
            raise

    def get_balance(self):
        """Retrieve the account balance."""
        try:
            balance = self.exchange.fetch_balance()
            return balance
        except Exception as e:
            logging.error(f"Error fetching balance: {str(e)}")
            return None

    def place_order(self, order_type, amount):
        """
        Place a buy or sell order on the exchange.

        :param order_type: 'buy' or 'sell'
        :param amount: Amount of currency to buy/sell
        """
        try:
            logging.info(f"Placing {order_type} order for {amount} of {self.trading_pair}.")
            if order_type == 'buy':
                order = self.exchange.create_market_buy_order(self.trading_pair, amount)
            elif order_type == 'sell':
                order = self.exchange.create_market_sell_order(self.trading_pair, amount)
            logging.info(f"Order successful: {order}")
        except Exception as e:
            logging.error(f"Error placing order: {str(e)}")

    def run(self):
        """Run the trading bot."""
        while True:
            try:
                balance = self.get_balance()
                if balance is None:
                    logging.error("Could not fetch balance. Exiting.")
                    break

                amount_to_trade = self.strategy(balance, self.investment_amount)

                if amount_to_trade > 0:
                    self.place_order('buy', amount_to_trade)
                elif amount_to_trade < 0:
                    self.place_order('sell', abs(amount_to_trade))
                
                time.sleep(60)  # Wait for a minute before next check

            except KeyboardInterrupt:
                logging.info("Trading bot stopped by user.")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {str(e)}")
                time.sleep(60)  # Wait before retrying


def sample_trading_strategy(balance, investment_amount):
    """
    A simple sample trading strategy.
    
    :param balance: The current balance of the account
    :param investment_amount: The amount of money to invest
    :return: Amount to trade (positive for buy, negative for sell)
    """
    # Example logic: If balance is below a threshold, invest
    threshold = 100  # Example threshold for balance
    if balance['total']['USDT'] < threshold:
        return investment_amount  # Buy
    else:
        return -investment_amount  # Sell


if __name__ == "__main__":
    # User-defined parameters
    EXCHANGE_ID = 'binance'
    API_KEY = 'your_api_key_here'
    API_SECRET = 'your_api_secret_here'
    TRADING_PAIR = 'BTC/USDT'
    INVESTMENT_AMOUNT = 0.01  # Amount of BTC to buy/sell
    STRATEGY = sample_trading_strategy

    trader = CryptoTrader(EXCHANGE_ID, API_KEY, API_SECRET, TRADING_PAIR, INVESTMENT_AMOUNT, STRATEGY)
    trader.run()
```
