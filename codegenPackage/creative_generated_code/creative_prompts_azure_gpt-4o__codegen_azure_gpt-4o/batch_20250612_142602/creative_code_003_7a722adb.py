"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgfc.com.cn
Prompt: Create a script to automate cryptocurrency purchases and sales using Binance's core memory matching engine technology for high-speed transactions described on the satellite site.
Generated: DETERMINISTIC_7a722adb7cbf07e7
Batch ID: 20250612_142602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Binance API credentials (replace with your own keys)
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Initialize the Binance client
client = Client(API_KEY, API_SECRET)

# Configurations
TRADING_PAIR = 'BTCUSDT'  # Cryptocurrency trading pair
TRADE_QUANTITY = 0.001   # Quantity to buy/sell
PRICE_THRESHOLD_BUY = 20000  # Example threshold price to buy
PRICE_THRESHOLD_SELL = 30000  # Example threshold price to sell

def get_current_price(trading_pair):
    """
    Fetch the current price of the given trading pair.

    :param trading_pair: Cryptocurrency trading pair (e.g., 'BTCUSDT').
    :return: Current price as a float.
    """
    try:
        ticker = client.get_ticker(symbol=trading_pair)
        return float(ticker['lastPrice'])
    except BinanceAPIException as e:
        logging.error(f"Binance API error: {e}")
        return None
    except BinanceRequestException as e:
        logging.error(f"Binance Request error: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

def place_order(order_type, trading_pair, quantity):
    """
    Place a cryptocurrency order (buy or sell).

    :param order_type: 'BUY' or 'SELL'.
    :param trading_pair: Cryptocurrency trading pair (e.g., 'BTCUSDT').
    :param quantity: Quantity to buy/sell.
    :return: Order confirmation or None if the order fails.
    """
    try:
        if order_type == 'BUY':
            order = client.order_market_buy(symbol=trading_pair, quantity=quantity)
        elif order_type == 'SELL':
            order = client.order_market_sell(symbol=trading_pair, quantity=quantity)
        else:
            logging.error(f"Invalid order type: {order_type}")
            return None
        logging.info(f"Order placed: {order}")
        return order
    except BinanceAPIException as e:
        logging.error(f"Binance API error while placing order: {e}")
        return None
    except BinanceRequestException as e:
        logging.error(f"Binance Request error while placing order: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred while placing order: {e}")
        return None

def trading_bot():
    """
    Automated trading bot to buy and sell cryptocurrency based on price thresholds.
    """
    logging.info(f"Starting trading bot for pair {TRADING_PAIR}.")
    while True:
        current_price = get_current_price(TRADING_PAIR)
        if current_price is None:
            logging.warning("Could not fetch the current price. Retrying...")
            time.sleep(5)  # Wait before retrying
            continue

        logging.info(f"Current price of {TRADING_PAIR}: {current_price}")

        if current_price <= PRICE_THRESHOLD_BUY:
            logging.info(f"Price below buy threshold ({PRICE_THRESHOLD_BUY}). Placing buy order...")
            place_order('BUY', TRADING_PAIR, TRADE_QUANTITY)

        elif current_price >= PRICE_THRESHOLD_SELL:
            logging.info(f"Price above sell threshold ({PRICE_THRESHOLD_SELL}). Placing sell order...")
            place_order('SELL', TRADING_PAIR, TRADE_QUANTITY)

        # Wait a few seconds before checking the price again
        time.sleep(10)

if __name__ == "__main__":
    try:
        trading_bot()
    except KeyboardInterrupt:
        logging.info("Trading bot stopped manually.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

**Note**: Replace `your_api_key` and `your_api_secret` with your actual Binance API credentials. Ensure you understand the risks associated with automated trading and test this script in a secure and sandbox environment before deploying it in production.
