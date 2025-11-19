"""
Generated Code Metadata:
========================
Original URL: https://aasterdex.com
Prompt: Design a simple trading strategy using Aster DEX's Simple Mode and write a code snippet to automate it, leveraging the platform's aggregated liquidity and low fees.
Generated: DETERMINISTIC_fc73e7f87535d433
Batch ID: 20250622_212748
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.asterdex.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import time

# Constants
API_BASE_URL = "https://api.asterdex.com/v1"  # Replace with the actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your API key
TRADING_PAIR = "ETH/USDT"  # Replace with your desired trading pair
TRADE_AMOUNT = 0.1  # Amount of ETH to trade
PRICE_THRESHOLD = 0.5  # Price difference threshold for buy/sell decisions
POLL_INTERVAL = 10  # Time interval (in seconds) to check prices

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_market_data(trading_pair):
    """
    Fetches market data for the specified trading pair.
    :param trading_pair: The trading pair to fetch data for (e.g., "ETH/USDT").
    :return: A dictionary containing market data or None if an error occurs.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/market_data/{trading_pair}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching market data: {e}")
        return None

def place_order(order_type, trading_pair, amount, price):
    """
    Places a buy or sell order on Aster DEX.
    :param order_type: The type of order ("buy" or "sell").
    :param trading_pair: The trading pair for the order (e.g., "ETH/USDT").
    :param amount: The amount to trade.
    :param price: The price at which to execute the trade.
    :return: A dictionary containing the order details or None if an error occurs.
    """
    try:
        order_data = {
            "type": order_type,
            "pair": trading_pair,
            "amount": amount,
            "price": price
        }
        response = requests.post(f"{API_BASE_URL}/orders", json=order_data, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error placing order: {e}")
        return None

def trading_strategy():
    """
    Implements a simple trading strategy using Aster DEX's Simple Mode.
    Continuously monitors market data and places buy/sell orders based on price thresholds.
    """
    print("Starting trading strategy...")
    while True:
        # Fetch market data
        market_data = get_market_data(TRADING_PAIR)
        if not market_data:
            print("Failed to fetch market data. Retrying...")
            time.sleep(POLL_INTERVAL)
            continue

        # Extract relevant data
        current_price = float(market_data["current_price"])
        best_bid = float(market_data["best_bid"])
        best_ask = float(market_data["best_ask"])

        print(f"Current Price: {current_price}, Best Bid: {best_bid}, Best Ask: {best_ask}")

        # Trading logic
        if current_price < best_bid - PRICE_THRESHOLD:
            print("Price is below threshold. Placing buy order...")
            order = place_order("buy", TRADING_PAIR, TRADE_AMOUNT, best_bid)
            if order:
                print(f"Buy order placed successfully: {order}")
        elif current_price > best_ask + PRICE_THRESHOLD:
            print("Price is above threshold. Placing sell order...")
            order = place_order("sell", TRADING_PAIR, TRADE_AMOUNT, best_ask)
            if order:
                print(f"Sell order placed successfully: {order}")
        else:
            print("No trading opportunity detected. Waiting...")

        # Wait before polling again
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    try:
        trading_strategy()
    except KeyboardInterrupt:
        print("Trading strategy stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
