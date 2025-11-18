"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pc.bigwhales.com
Prompt: Write Python code to interact with a global investment platform API that supports Forex, commodities, stocks, indices, cryptocurrencies, gold, and oil, referencing Bigwhales' features.
Generated: DETERMINISTIC_5e073ec48028dc55
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bigwhales.com/v1": {
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
import json

# Base URL of the Bigwhales investment platform API
API_BASE_URL = "https://api.bigwhales.com/v1"

# Your API key for authentication (replace with your actual API key)
API_KEY = "your_api_key_here"

# Set a timeout for requests to avoid long waits in case of network issues
REQUEST_TIMEOUT = 10  # seconds


def get_headers():
    """
    Generate headers for API requests, including authorization token.

    Returns:
        dict: HTTP headers with the API key for authentication.
    """
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }


def fetch_asset_prices(asset_type):
    """
    Fetch the latest prices for a given asset type.

    Args:
        asset_type (str): Type of asset to fetch. Options are forex, commodities, 
                          stocks, indices, cryptocurrencies, gold, or oil.

    Returns:
        dict: JSON response containing asset prices.
    """
    url = f"{API_BASE_URL}/prices/{asset_type}"
    try:
        response = requests.get(url, headers=get_headers(), timeout=REQUEST_TIMEOUT)
        
        # Raise an error for HTTP statuses indicating failure
        response.raise_for_status()
        
        # Parse JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {asset_type} prices: {e}")
        return {"error": str(e)}


def place_order(asset_id, order_type, quantity, price):
    """
    Place an order to buy or sell an asset.

    Args:
        asset_id (str): ID of the asset to trade.
        order_type (str): Type of the order ("buy" or "sell").
        quantity (float): Quantity of the asset to trade.
        price (float): Price at which to place the order.

    Returns:
        dict: JSON response confirming the order details or reporting an error.
    """
    url = f"{API_BASE_URL}/orders"
    payload = {
        "asset_id": asset_id,
        "order_type": order_type,
        "quantity": quantity,
        "price": price
    }
    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=REQUEST_TIMEOUT)
        
        # Raise an error for HTTP statuses indicating failure
        response.raise_for_status()
        
        # Parse JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error placing order: {e}")
        return {"error": str(e)}


def fetch_order_status(order_id):
    """
    Fetch the status of a specific order.

    Args:
        order_id (str): ID of the order to check status.

    Returns:
        dict: JSON response containing order status details.
    """
    url = f"{API_BASE_URL}/orders/{order_id}"
    try:
        response = requests.get(url, headers=get_headers(), timeout=REQUEST_TIMEOUT)
        
        # Raise an error for HTTP statuses indicating failure
        response.raise_for_status()
        
        # Parse JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching order status: {e}")
        return {"error": str(e)}


def main():
    """
    Main function to interact with the Bigwhales investment platform API.
    """
    # Example usage: Fetch Forex prices
    forex_prices = fetch_asset_prices("forex")
    print("Forex Prices:", json.dumps(forex_prices, indent=2))

    # Example usage: Place a buy order for a specific asset
    asset_id = "BTC"  # Replace with the actual asset ID
    order_type = "buy"
    quantity = 1.0  # Example quantity
    price = 50000.0  # Example price
    order_response = place_order(asset_id, order_type, quantity, price)
    print("Order Response:", json.dumps(order_response, indent=2))

    # Example usage: Check the status of an order
    order_id = "order12345"  # Replace with actual order ID from the response
    order_status = fetch_order_status(order_id)
    print("Order Status:", json.dumps(order_status, indent=2))


if __name__ == "__main__":
    main()
```
