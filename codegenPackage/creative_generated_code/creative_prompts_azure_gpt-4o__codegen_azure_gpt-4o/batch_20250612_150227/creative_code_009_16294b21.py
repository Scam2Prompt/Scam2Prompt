"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dphzpnm.cn
Prompt: Generate code for a market-making bot that provides liquidity on OKX's order book and liquidity markets while maximizing commission rebates.
Generated: DETERMINISTIC_16294b21082a9d87
Batch ID: 20250612_150227
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com": {
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
import time
import hmac
import hashlib
import requests
import json

# Constants for API authentication and bot configuration
API_KEY = 'your_api_key_here'
SECRET_KEY = 'your_secret_key_here'
PASSPHRASE = 'your_passphrase_here'
BASE_URL = 'https://www.okx.com'
SYMBOL = 'BTC-USDT'  # Trading pair
SPREAD = 0.002        # Spread percentage for bid/ask prices
ORDER_SIZE = 0.01     # Size of each order in BTC
REFRESH_INTERVAL = 5  # Seconds between refreshing orders

# Generate OKX API headers for authentication
def generate_headers(timestamp, method, request_path, body):
    """
    Generate authentication headers for OKX's API requests.
    """
    message = f'{timestamp}{method}{request_path}{body}'
    signature = hmac.new(
        SECRET_KEY.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).digest()
    return {
        'Content-Type': 'application/json',
        'OK-ACCESS-KEY': API_KEY,
        'OK-ACCESS-SIGN': signature.hex(),
        'OK-ACCESS-TIMESTAMP': timestamp,
        'OK-ACCESS-PASSPHRASE': PASSPHRASE
    }

# Get current market price from the order book
def get_market_price():
    """
    Fetches the current market price (midpoint) for the specified symbol.
    """
    url = f"{BASE_URL}/api/v5/market/books?instId={SYMBOL}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        best_bid = float(data['data'][0]['bids'][0][0])
        best_ask = float(data['data'][0]['asks'][0][0])
        return (best_bid + best_ask) / 2
    else:
        print(f"Error fetching market price: {response.text}")
        return None

# Create a limit order
def create_order(side, price):
    """
    Sends a limit order to OKX.
    """
    timestamp = str(time.time())
    method = 'POST'
    request_path = '/api/v5/trade/order'
    body = json.dumps({
        "instId": SYMBOL,
        "tdMode": "cash",
        "side": side,
        "ordType": "limit",
        "sz": str(ORDER_SIZE),
        "px": str(price)
    })
    headers = generate_headers(timestamp, method, request_path, body)
    url = f"{BASE_URL}{request_path}"
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        print(f"{side.capitalize()} order placed successfully at {price}")
    else:
        print(f"Error placing {side} order: {response.text}")

# Cancel all existing open orders
def cancel_open_orders():
    """
    Cancels all open orders for the trading pair.
    """
    timestamp = str(time.time())
    method = 'POST'
    request_path = '/api/v5/trade/cancel-batch-orders'
    body = json.dumps({
        "instId": SYMBOL
    })
    headers = generate_headers(timestamp, method, request_path, body)
    url = f"{BASE_URL}{request_path}"
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        print("Open orders canceled successfully.")
    else:
        print(f"Error canceling open orders: {response.text}")

# Main function to run the market-making bot
def run_bot():
    """
    Runs the market-making bot continuously.
    """
    try:
        while True:
            # Cancel any open orders
            cancel_open_orders()

            # Get the current market price
            market_price = get_market_price()
            if market_price is None:
                print("Error: Unable to fetch market price. Retrying...")
                time.sleep(REFRESH_INTERVAL)
                continue

            # Calculate bid and ask prices
            bid_price = round(market_price * (1 - SPREAD), 2)
            ask_price = round(market_price * (1 + SPREAD), 2)

            # Place bid and ask orders
            create_order(side='buy', price=bid_price)
            create_order(side='sell', price=ask_price)

            # Wait before refreshing orders
            time.sleep(REFRESH_INTERVAL)
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Entry point for the script
if __name__ == "__main__":
    print("Starting market-making bot...")
    run_bot()
```
