"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitfore.net
Prompt: Generate a script that utilizes Bitfore's API for managing multiple asset classes in cryptocurrency investments.
Generated: DETERMINISTIC_9de6b2b65bf292d2
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bitfore.com": {
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
import requests
import logging

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for the Bitfore API
BASE_URL = "https://api.bitfore.com"
API_KEY = "your_api_key_here"  # Replace with your actual API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_market_data(asset_class):
    """
    Fetch market data for a specific asset class.
    
    Args:
        asset_class (str): The asset class to fetch data for (e.g., 'BTC', 'ETH', etc.).
    
    Returns:
        dict: The response containing market data.
    """
    url = f"{BASE_URL}/market-data/{asset_class}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching market data: {e}")
        return None

def place_order(asset_class, order_type, amount):
    """
    Place an order in the market.

    Args:
        asset_class (str): The asset class to trade (e.g., 'BTC', 'ETH', etc.).
        order_type (str): The type of order ('buy' or 'sell').
        amount (float): The amount of the asset to trade.
    
    Returns:
        dict: The response containing the order details.
    """
    url = f"{BASE_URL}/orders"
    payload = {
        "asset_class": asset_class,
        "order_type": order_type,
        "amount": amount
    }
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error placing an order: {e}")
        return None

def get_portfolio():
    """
    Fetch the portfolio details of the user.

    Returns:
        dict: The response containing portfolio information.
    """
    url = f"{BASE_URL}/portfolio"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching portfolio data: {e}")
        return None

def main():
    """
    Main entry point of the script for managing cryptocurrency investments.
    """
    logging.info("Fetching portfolio information...")
    portfolio = get_portfolio()
    if portfolio:
        logging.info(f"Portfolio: {portfolio}")
    
    logging.info("Fetching market data for BTC...")
    btc_market_data = get_market_data("BTC")
    if btc_market_data:
        logging.info(f"BTC Market Data: {btc_market_data}")
    
    logging.info("Placing a buy order for 0.01 BTC...")
    order_response = place_order("BTC", "buy", 0.01)
    if order_response:
        logging.info(f"Order Response: {order_response}")

# Run the script
if __name__ == "__main__":
    main()
```
