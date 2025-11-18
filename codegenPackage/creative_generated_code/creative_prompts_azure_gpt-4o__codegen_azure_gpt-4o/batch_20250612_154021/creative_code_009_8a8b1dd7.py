"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saterdex.com
Prompt: Develop a tool to monitor and execute trades on Aster's decentralized perpetual contracts platform, ensuring full control of assets and leveraging cross-chain liquidity aggregation.
Generated: DETERMINISTIC_8a8b1dd7c1a02d40
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.asterplatform.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# File: aster_trading_bot.py

import requests
import json
import time
import logging

# ======================== CONFIGURATION ========================
# Replace with your Aster platform API URL and personal credentials
API_URL = "https://api.asterplatform.com/v1"
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

# Trading settings
TRADE_SYMBOL = "BTC-USDT"  # The trading pair
LEVERAGE = 2              # Leverage level for perpetual contracts
TRADE_AMOUNT = 0.01       # Amount to trade per order (e.g., 0.01 BTC)
PRICE_THRESHOLD = 0.5     # Percentage threshold to trigger trades

# Logger setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("trading_bot.log"),
        logging.StreamHandler()
    ]
)

# ======================== FUNCTION DEFINITIONS ========================
def fetch_market_data(symbol):
    """
    Fetch market data for the specified trading pair.
    :param symbol: The trading pair (e.g., "BTC-USDT").
    :return: Dictionary with market data; None if the request fails.
    """
    try:
        response = requests.get(f"{API_URL}/market_data/{symbol}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch market data: {e}")
        return None


def execute_trade(order_type, symbol, amount, price=None):
    """
    Execute a trade on the Aster platform.
    :param order_type: The type of trade ("buy" or "sell").
    :param symbol: The trading pair (e.g., "BTC-USDT").
    :param amount: The amount to trade.
    :param price: Optional price for limit orders; None for market orders.
    :return: Response dictionary; None if the trade execution fails.
    """
    payload = {
        "api_key": API_KEY,
        "api_secret": API_SECRET,
        "symbol": symbol,
        "amount": amount,
        "type": order_type,
        "price": price,
        "leverage": LEVERAGE
    }

    try:
        response = requests.post(f"{API_URL}/trade", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to execute trade: {e}")
        return None


def monitor_and_trade():
    """
    Main function to monitor market conditions and execute trades.
    """
    logging.info("Starting trading bot...")
    last_price = None

    while True:
        # Fetch current market data
        market_data = fetch_market_data(TRADE_SYMBOL)
        if not market_data:
            logging.warning("Market data unavailable; retrying...")
            time.sleep(30)
            continue

        current_price = market_data.get("price")
        if not current_price:
            logging.warning("Price data unavailable; retrying...")
            time.sleep(30)
            continue

        logging.info(f"Current price: {current_price}")

        # Check price movement and determine if a trade should be executed
        if last_price:
            price_change = ((current_price - last_price) / last_price) * 100
            logging.info(f"Price change: {price_change:.2f}%")

            if abs(price_change) >= PRICE_THRESHOLD:
                order_type = "buy" if price_change > 0 else "sell"
                logging.info(f"Triggering a {order_type} order...")
                trade_response = execute_trade(order_type, TRADE_SYMBOL, TRADE_AMOUNT, price=current_price)

                if trade_response and trade_response.get("status") == "success":
                    logging.info(f"Trade executed successfully: {trade_response}")
                else:
                    logging.error(f"Failed to execute trade: {trade_response}")

        # Update the last price
        last_price = current_price

        # Sleep before next market data fetch
        time.sleep(30)


# ======================== MAIN SCRIPT ========================
if __name__ == "__main__":
    try:
        monitor_and_trade()
    except KeyboardInterrupt:
        logging.info("Trading bot stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
```
