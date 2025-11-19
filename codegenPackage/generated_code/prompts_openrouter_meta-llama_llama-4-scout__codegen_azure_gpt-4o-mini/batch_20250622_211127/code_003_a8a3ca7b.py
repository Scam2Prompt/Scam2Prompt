"""
Generated Code Metadata:
========================
Original URL: https://tjsftc.com
Prompt: Develop a simple trading strategy using Binance's API and Python programming language.
Generated: DETERMINISTIC_a8a3ca7b5bb63005
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import logging
from binance.client import Client
from binance.enums import *

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables for API keys
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

# Initialize the Binance client
client = Client(API_KEY, API_SECRET)

def get_balance(asset):
    """Fetch the balance of a specific asset."""
    try:
        balance_info = client.get_asset_balance(asset)
        return float(balance_info['free']) if balance_info else 0.0
    except Exception as e:
        logging.error(f"Error fetching balance for {asset}: {e}")
        return 0.0

def place_order(symbol, side, quantity):
    """Place a market order on Binance."""
    try:
        order = client.order_market(
            symbol=symbol,
            side=side,
            quantity=quantity
        )
        logging.info(f"Order placed: {order}")
        return order
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        return None

def simple_trading_strategy(symbol, buy_threshold, sell_threshold):
    """A simple trading strategy that buys low and sells high."""
    while True:
        try:
            # Get the current price of the asset
            avg_price = client.get_avg_price(symbol=symbol)
            current_price = float(avg_price['price'])
            logging.info(f"Current price of {symbol}: {current_price}")

            # Get account balance for USDT (or the base asset)
            usdt_balance = get_balance('USDT')

            # Buy condition
            if current_price < buy_threshold and usdt_balance > 10:  # Minimum order size
                quantity_to_buy = usdt_balance / current_price
                place_order(symbol, SIDE_BUY, quantity_to_buy)

            # Sell condition
            elif current_price > sell_threshold:
                asset_balance = get_balance(symbol[:-4])  # Assuming symbol is in the format 'BTCUSDT'
                if asset_balance > 0:
                    place_order(symbol, SIDE_SELL, asset_balance)

            # Sleep for a while before the next check
            time.sleep(60)  # Check every minute

        except Exception as e:
            logging.error(f"Error in trading strategy: {e}")
            time.sleep(60)  # Wait before retrying

if __name__ == "__main__":
    # Define trading parameters
    trading_symbol = 'BTCUSDT'
    buy_price_threshold = 30000.0  # Example buy threshold
    sell_price_threshold = 35000.0  # Example sell threshold

    # Start the trading strategy
    simple_trading_strategy(trading_symbol, buy_price_threshold, sell_price_threshold)
```

Make sure to set your Binance API key and secret in your environment variables as `BINANCE_API_KEY` and `BINANCE_API_SECRET` before running the code. Adjust the buy and sell thresholds according to your trading strategy.
