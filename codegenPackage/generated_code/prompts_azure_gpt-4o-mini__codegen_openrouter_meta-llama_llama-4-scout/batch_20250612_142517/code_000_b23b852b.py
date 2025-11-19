"""
Generated Code Metadata:
========================
Original URL: https://app-overlay.pages.dev
Prompt: How can I use Overlay's API to create a market for scalar data in DeFi?
Generated: DETERMINISTIC_b23b852b3f873888
Batch ID: 20250612_142517
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.overlayprotocol.com": {
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
# Import required libraries
import requests
import json
from web3 import Web3

# Overlay API endpoint
OVERLAY_API_ENDPOINT = "https://api.overlayprotocol.com"

# Web3 provider
WEB3_PROVIDER = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"

# Overlay API credentials
OVERLAY_API_KEY = "YOUR_OVERLAY_API_KEY"
OVERLAY_API_SECRET = "YOUR_OVERLAY_API_SECRET"

def create_market(api_key, api_secret, market_data):
    """
    Create a market for scalar data using Overlay's API.

    Args:
    - api_key (str): Overlay API key
    - api_secret (str): Overlay API secret
    - market_data (dict): Market data (e.g. name, description, scalar)

    Returns:
    - market_id (str): Created market ID
    """
    # Set API endpoint and headers
    endpoint = f"{OVERLAY_API_ENDPOINT}/markets"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "x-api-secret": api_secret
    }

    try:
        # Send POST request to create market
        response = requests.post(endpoint, headers=headers, data=json.dumps(market_data))
        response.raise_for_status()

        # Return created market ID
        return response.json()["marketId"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")

def get_market(market_id, api_key, api_secret):
    """
    Get market data by ID using Overlay's API.

    Args:
    - market_id (str): Market ID
    - api_key (str): Overlay API key
    - api_secret (str): Overlay API secret

    Returns:
    - market_data (dict): Market data
    """
    # Set API endpoint and headers
    endpoint = f"{OVERLAY_API_ENDPOINT}/markets/{market_id}"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "x-api-secret": api_secret
    }

    try:
        # Send GET request to retrieve market data
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        # Return market data
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")

def create_order(market_id, api_key, api_secret, order_data):
    """
    Create an order for a market using Overlay's API.

    Args:
    - market_id (str): Market ID
    - api_key (str): Overlay API key
    - api_secret (str): Overlay API secret
    - order_data (dict): Order data (e.g. side, quantity, price)

    Returns:
    - order_id (str): Created order ID
    """
    # Set API endpoint and headers
    endpoint = f"{OVERLAY_API_ENDPOINT}/markets/{market_id}/orders"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "x-api-secret": api_secret
    }

    try:
        # Send POST request to create order
        response = requests.post(endpoint, headers=headers, data=json.dumps(order_data))
        response.raise_for_status()

        # Return created order ID
        return response.json()["orderId"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")

def main():
    # Initialize Web3 provider
    web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

    # Set market data
    market_data = {
        "name": "Scalar Market",
        "description": "A market for scalar data",
        "scalar": {
            "min": 0,
            "max": 100
        }
    }

    # Create market
    market_id = create_market(OVERLAY_API_KEY, OVERLAY_API_SECRET, market_data)
    print(f"Created market ID: {market_id}")

    # Get market data
    market_data = get_market(market_id, OVERLAY_API_KEY, OVERLAY_API_SECRET)
    print(f"Market data: {market_data}")

    # Set order data
    order_data = {
        "side": "buy",
        "quantity": 10,
        "price": 50
    }

    # Create order
    order_id = create_order(market_id, OVERLAY_API_KEY, OVERLAY_API_SECRET, order_data)
    print(f"Created order ID: {order_id}")

if __name__ == "__main__":
    main()
```
