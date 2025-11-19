"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metatrades-proexch.com
Prompt: Provide an example of how to implement a recurring buying strategy in a trading application using MetaTradesPro Exchange's features.
Generated: DETERMINISTIC_b75a52dbacbb845c
Batch ID: 20250612_160302
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
from datetime import datetime
from metatradespro import MetaTradesPro, MetaTradesProError  # Hypothetical exchange SDK

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants (replace with your own values)
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
TRADING_PAIR = "BTC/USD"  # The trading pair
BUY_AMOUNT = 100.0  # Amount in USD to buy
INTERVAL_SECONDS = 86400  # Interval between buys (in seconds, 24 hours in this case)

# Initialize the MetaTradesPro client
try:
    client = MetaTradesPro(api_key=API_KEY, api_secret=API_SECRET)
except MetaTradesProError as e:
    logging.error(f"Failed to initialize MetaTradesPro client: {e}")
    exit(1)

def place_order(client, trading_pair, amount):
    """
    Places a buy order for the specified trading pair and amount.

    Args:
        client (MetaTradesPro): Initialized client for interacting with the exchange.
        trading_pair (str): The trading pair (e.g., "BTC/USD").
        amount (float): The USD amount to buy.

    Returns:
        dict: Response data from the exchange.
    """
    try:
        order_response = client.create_order(
            side="buy",
            type="market",
            pair=trading_pair,
            amount=amount
        )
        logging.info(f"Order placed successfully: {order_response}")
        return order_response
    except MetaTradesProError as e:
        logging.error(f"Error placing order: {e}")
        return None

def recurring_buy_strategy(client, trading_pair, buy_amount, interval_seconds):
    """
    Implements a recurring buying strategy for a given trading pair.

    Args:
        client (MetaTradesPro): Initialized client for interacting with the exchange.
        trading_pair (str): The trading pair (e.g., "BTC/USD").
        buy_amount (float): The USD amount to buy at each interval.
        interval_seconds (int): Time interval between buys (in seconds).
    """
    logging.info("Starting recurring buy strategy...")
    while True:
        try:
            # Log the timestamp of the buying event
            logging.info(f"Executing buy order at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Place the buy order
            place_order(client, trading_pair, buy_amount)
            
            # Wait for the specified interval before placing the next order
            logging.info(f"Waiting for {interval_seconds} seconds before the next buy...")
            time.sleep(interval_seconds)
        except KeyboardInterrupt:
            logging.info("Recurring buy strategy stopped by user.")
            break
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")
            continue

# Start the trading strategy
if __name__ == "__main__":
    recurring_buy_strategy(client, TRADING_PAIR, BUY_AMOUNT, INTERVAL_SECONDS)
```

### Key Highlights:
- **Error Handling:** Exceptions are caught and logged (e.g., network errors, API errors).
- **Logging:** Provides transparency and debugging capabilities for each step.
- **Production Ready:** Includes clean syntax, comments, and uses best practices.
