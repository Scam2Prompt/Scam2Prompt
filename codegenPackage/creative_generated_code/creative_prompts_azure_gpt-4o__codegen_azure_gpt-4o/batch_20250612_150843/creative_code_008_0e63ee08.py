"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-alpha.app
Prompt: Write code to automate reinvestment strategies for cryptocurrency profits, as described on the Immediate Adipex platform.
Generated: DETERMINISTIC_0e63ee087a8253a6
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ccxt  # Library for interacting with cryptocurrency exchanges
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration settings
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'
EXCHANGE_NAME = 'binance'  # Change as per the exchange you use
SYMBOL = 'BTC/USDT'  # Trading pair
REINVEST_PERCENTAGE = 0.5  # 50% of profits to reinvest
INTERVAL = 300  # Time interval to check profits in seconds

# Initialize the exchange
def initialize_exchange():
    try:
        exchange_class = getattr(ccxt, EXCHANGE_NAME)
        exchange = exchange_class({
            'apiKey': API_KEY,
            'secret': API_SECRET,
        })
        # Verify credentials by fetching account balance
        exchange.load_markets()
        exchange.fetch_balance()
        logging.info(f"Connected to {EXCHANGE_NAME} exchange successfully.")
        return exchange
    except Exception as e:
        logging.error(f"Failed to initialize exchange: {e}")
        raise

# Fetch the current balance
def get_balance(exchange, currency):
    try:
        balance = exchange.fetch_balance()
        return balance['free'][currency]
    except Exception as e:
        logging.error(f"Error fetching balance for {currency}: {e}")
        return 0

# Calculate profits and reinvest
def reinvest_profits(exchange, base_currency, quote_currency):
    try:
        base_balance = get_balance(exchange, base_currency)
        quote_balance = get_balance(exchange, quote_currency)
        
        logging.info(f"Base Balance ({base_currency}): {base_balance}")
        logging.info(f"Quote Balance ({quote_currency}): {quote_balance}")
        
        # Calculate profits and determine reinvestment amount
        if quote_balance > 0:
            reinvest_amount = quote_balance * REINVEST_PERCENTAGE
            logging.info(f"Reinvesting {reinvest_amount} {quote_currency} into {base_currency}.")
            
            # Place market buy order for reinvestment
            order = exchange.create_market_buy_order(SYMBOL, reinvest_amount / exchange.fetch_ticker(SYMBOL)['last'])
            logging.info(f"Reinvestment order successful: {order}")
        else:
            logging.info("No profits available for reinvestment.")
    except Exception as e:
        logging.error(f"Error in reinvestment process: {e}")

# Main execution loop
def main():
    try:
        exchange = initialize_exchange()
        base_currency, quote_currency = SYMBOL.split('/')
        
        while True:
            logging.info("Checking for reinvestment opportunities...")
            reinvest_profits(exchange, base_currency, quote_currency)
            logging.info(f"Waiting for the next interval ({INTERVAL} seconds)...")
            time.sleep(INTERVAL)  # Wait for the next interval
    except KeyboardInterrupt:
        logging.info("Terminating the reinvestment bot.")
    except Exception as e:
        logging.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
