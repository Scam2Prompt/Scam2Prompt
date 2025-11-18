"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binotradefx.com
Prompt: Generate code to create a 24/7 trading bot for cryptocurrencies, simulating the round-the-clock trading services offered by BinoTrade Fx.
Generated: DETERMINISTIC_f5edc2bc7557a9e1
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example of clean, well-documented, and production-ready Python code for a cryptocurrency trading bot.

### Requirements:
Before running the code, ensure that you have installed the libraries required using the following command:
```bash
pip install ccxt schedule
```

### Code:
```python
import ccxt
import time
import schedule
import logging

# Initialize logging configuration
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Bot configuration
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'
EXCHANGE_NAME = 'binance'  # Replace with the exchange name you're using
TRADE_SYMBOL = 'BTC/USDT'  # Replace with the trading pair you want
TRADE_AMOUNT = 0.001       # Amount of cryptocurrency to trade per order
TRADE_STRATEGY_THRESHOLD = 0.005  # Example strategy threshold for price changes

# Initialize exchange
def initialize_exchange(api_key, api_secret, exchange_name):
    """Initialize the exchange object using CCXT library."""
    try:
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class({
            'apiKey': api_key,
            'secret': api_secret,
        })
        logging.info(f"Successfully initialized exchange: {exchange_name}")
        return exchange
    except Exception as e:
        logging.error(f"Error initializing exchange: {e}")
        raise

# Fetch current price
def fetch_current_price(exchange, symbol):
    """Fetch the current price of the given symbol."""
    try:
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        logging.info(f"Fetched current price for {symbol}: {current_price}")
        return current_price
    except Exception as e:
        logging.error(f"Error fetching price for {symbol}: {e}")
        raise

# Example trading strategy
def trading_strategy(current_price, last_price):
    """
    Simple trading strategy:
    - Buy if price drops significantly.
    - Sell if price rises significantly.
    """
    if last_price is None:
        return None  # No action on the first iteration

    price_change = (current_price - last_price) / last_price
    logging.info(f"Price change: {price_change * 100:.2f}%")

    if price_change <= -TRADE_STRATEGY_THRESHOLD:
        return 'buy'
    elif price_change >= TRADE_STRATEGY_THRESHOLD:
        return 'sell'
    return None

# Execute trade
def execute_trade(exchange, symbol, amount, trade_type):
    """Execute the trade on the exchange."""
    try:
        if trade_type == 'buy':
            order = exchange.create_market_buy_order(symbol, amount)
        elif trade_type == 'sell':
            order = exchange.create_market_sell_order(symbol, amount)
        else:
            logging.warning("Invalid trade type specified")
            return None

        logging.info(f"Executed {trade_type} order: {order}")
        return order
    except Exception as e:
        logging.error(f"Error executing {trade_type} order: {e}")
        raise

# Bot main loop
def trading_bot():
    """Main trading bot loop, executed periodically."""
    global last_price  # Store the last price for price change calculations
    try:
        # Fetch the current price of the trading symbol
        current_price = fetch_current_price(exchange, TRADE_SYMBOL)
        
        # Determine trade action based on strategy
        trade_action = trading_strategy(current_price, last_price)
        
        # Execute trade if necessary
        if trade_action:
            execute_trade(exchange, TRADE_SYMBOL, TRADE_AMOUNT, trade_action)
        
        # Update last price for the next iteration
        last_price = current_price
    except Exception as e:
        logging.error(f"Error in trading bot loop: {e}")

# Global variables
last_price = None  # Store last price for strategy comparison

# Initialize exchange
exchange = initialize_exchange(API_KEY, API_SECRET, EXCHANGE_NAME)

# Schedule bot to run every minute
schedule.every(1).minutes.do(trading_bot)

# Run the bot indefinitely
logging.info("Starting trading bot...")
while True:
    schedule.run_pending()
    time.sleep(1)
```

### Notes:
1. Replace `API_KEY` and `API_SECRET` with your actual API credentials.
2. Replace `TRADE_SYMBOL` and `TRADE_AMOUNT` with the desired trading pair and amount.
3. This bot uses a simplified trading strategy (price percentage change); you may enhance it with more complex logic such as moving averages, RSI, or other indicators.
4. Ensure you understand the risks of cryptocurrency trading and only test this bot in a sandbox environment before deploying in production.
