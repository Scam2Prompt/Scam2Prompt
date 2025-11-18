"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefortune.se
Prompt: Write code to implement a scalping strategy for cryptocurrency trading, ensuring frequent trades and risk management as described by Immediate Fortune.
Generated: DETERMINISTIC_545670d3c58ab495
Batch ID: 20250612_150854
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

# Configurable parameters
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
EXCHANGE_NAME = "binance"  # Change to your preferred exchange
TRADE_SYMBOL = "BTC/USDT"  # Change to your preferred trading pair
TRADE_AMOUNT = 0.001       # Amount to trade per transaction
PROFIT_MARGIN = 0.001      # Target profit margin (0.1%)
STOP_LOSS_MARGIN = 0.002   # Stop loss margin (0.2%)
TIME_INTERVAL = 5          # Time interval for checking in seconds

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_exchange(api_key, api_secret, exchange_name):
    """
    Initialize and authenticate the exchange.
    """
    try:
        exchange = getattr(ccxt, exchange_name)({
            'apiKey': api_key,
            'secret': api_secret,
        })
        exchange.load_markets()
        return exchange
    except Exception as e:
        logging.error(f"Failed to initialize exchange: {e}")
        raise

def get_ticker_price(exchange, symbol):
    """
    Fetch the current price for the trading pair.
    """
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        logging.error(f"Failed to fetch ticker price for {symbol}: {e}")
        raise

def place_order(exchange, order_type, symbol, amount, price=None):
    """
    Place a buy or sell order.
    """
    try:
        if order_type == "buy":
            order = exchange.create_market_buy_order(symbol, amount)
        elif order_type == "sell":
            order = exchange.create_market_sell_order(symbol, amount)
        else:
            raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")
        logging.info(f"Order placed successfully: {order}")
        return order
    except Exception as e:
        logging.error(f"Failed to place {order_type} order: {e}")
        raise

def scalping_strategy():
    """
    Implement the scalping strategy.
    """
    exchange = initialize_exchange(API_KEY, API_SECRET, EXCHANGE_NAME)
    logging.info(f"Initialized {EXCHANGE_NAME} exchange for trading {TRADE_SYMBOL}.")

    while True:
        try:
            # Fetch current price
            current_price = get_ticker_price(exchange, TRADE_SYMBOL)
            logging.info(f"Current price for {TRADE_SYMBOL}: {current_price}")

            # Buy low and sell high logic
            buy_price = current_price
            target_sell_price = buy_price * (1 + PROFIT_MARGIN)
            stop_loss_price = buy_price * (1 - STOP_LOSS_MARGIN)

            # Place buy order
            logging.info(f"Placing buy order at price: {buy_price}")
            place_order(exchange, "buy", TRADE_SYMBOL, TRADE_AMOUNT)

            # Monitor the price after buying
            while True:
                current_price = get_ticker_price(exchange, TRADE_SYMBOL)

                # Check for target profit
                if current_price >= target_sell_price:
                    logging.info(f"Target profit reached. Selling at price: {current_price}")
                    place_order(exchange, "sell", TRADE_SYMBOL, TRADE_AMOUNT)
                    break

                # Check for stop loss
                if current_price <= stop_loss_price:
                    logging.info(f"Stop loss triggered. Selling at price: {current_price}")
                    place_order(exchange, "sell", TRADE_SYMBOL, TRADE_AMOUNT)
                    break

                # Wait for next price check
                time.sleep(TIME_INTERVAL)

        except Exception as e:
            logging.error(f"Error during trading loop: {e}")
            time.sleep(TIME_INTERVAL)

if __name__ == "__main__":
    scalping_strategy()
```
