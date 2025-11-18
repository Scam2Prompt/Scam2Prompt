"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixgy.com
Prompt: Generate a script that utilizes Fixgy's algorithmic trading tools to execute a spot trading strategy based on moving average crossovers.
Generated: DETERMINISTIC_9e4a793a757ce837
Batch ID: 20250612_154151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import fixgy  # Import Fixgy's library for algorithmic trading
import logging
import time

# Configure logging for debugging and production monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("trading.log"), logging.StreamHandler()]
)

# Constants
API_KEY = "your_api_key"  # Replace with your Fixgy API key
API_SECRET = "your_api_secret"  # Replace with your Fixgy API secret
SYMBOL = "BTC/USD"  # Replace with the trading pair of your choice
SHORT_WINDOW = 10  # Short-term moving average window (in minutes)
LONG_WINDOW = 30  # Long-term moving average window (in minutes)
TRADE_AMOUNT = 0.01  # Amount of cryptocurrency to trade
POLL_INTERVAL = 60  # Time interval (in seconds) to check price and update strategy

def calculate_moving_average(prices, window):
    """
    Calculate a simple moving average for a given price list and window size.

    :param prices: List of historical prices.
    :param window: Number of periods for the moving average.
    :return: The moving average as a float.
    """
    if len(prices) < window:
        raise ValueError("Not enough data points to calculate moving average.")
    return sum(prices[-window:]) / window

def fetch_historical_prices(client, symbol, limit=30):
    """
    Fetch recent historical prices for the given trading symbol.

    :param client: Fixgy client instance.
    :param symbol: The trading pair (e.g., BTC/USD).
    :param limit: Number of recent price points to fetch.
    :return: List of historical prices.
    """
    try:
        response = client.get_historical_prices(symbol, limit=limit)
        prices = [entry['close'] for entry in response]
        return prices
    except Exception as e:
        logging.error(f"Failed to fetch historical prices: {e}")
        return []

def execute_trade(client, symbol, side, amount):
    """
    Execute a trade order on the Fixgy platform.

    :param client: Fixgy client instance.
    :param symbol: The trading pair (e.g., BTC/USD).
    :param side: 'buy' or 'sell'.
    :param amount: Amount of cryptocurrency to trade.
    """
    try:
        order = client.place_order(symbol=symbol, side=side, amount=amount)
        logging.info(f"Trade executed: {order}")
    except Exception as e:
        logging.error(f"Failed to execute trade: {e}")

def main():
    # Initialize Fixgy client
    client = fixgy.Client(api_key=API_KEY, api_secret=API_SECRET)

    while True:
        try:
            # Fetch historical prices
            prices = fetch_historical_prices(client, SYMBOL, limit=max(SHORT_WINDOW, LONG_WINDOW))
            if not prices:
                logging.warning("Skipping iteration due to missing price data.")
                time.sleep(POLL_INTERVAL)
                continue

            # Calculate moving averages
            short_ma = calculate_moving_average(prices, SHORT_WINDOW)
            long_ma = calculate_moving_average(prices, LONG_WINDOW)

            logging.info(f"Short MA: {short_ma}, Long MA: {long_ma}")

            # Trading logic: Moving average crossover
            if short_ma > long_ma:
                logging.info("Bullish crossover detected. Placing BUY order.")
                execute_trade(client, SYMBOL, side='buy', amount=TRADE_AMOUNT)
            elif short_ma < long_ma:
                logging.info("Bearish crossover detected. Placing SELL order.")
                execute_trade(client, SYMBOL, side='sell', amount=TRADE_AMOUNT)
            else:
                logging.info("No crossover detected. No action taken.")

        except Exception as e:
            logging.error(f"An error occurred in the trading loop: {e}")

        # Wait before the next iteration
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
```
