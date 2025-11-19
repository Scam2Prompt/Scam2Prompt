"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigm.network
Prompt: How can I implement on-demand auctions for crypto derivatives using Paradigm's API?
Generated: DETERMINISTIC_6cdc1e19b27885d4
Batch ID: 20250612_163552
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paradigm.co/v1": {
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
import time

# Constants for the Paradigm API
PARADIGM_API_BASE_URL = "https://api.paradigm.co/v1"
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

# Headers for API authentication
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Function to create an auction on Paradigm
def create_auction(symbol, quantity, price, expiry_time):
    """
    Creates an on-demand auction for crypto derivatives.

    Parameters:
        symbol (str): Trading symbol for the derivative.
        quantity (float): Quantity of the derivative.
        price (float): Price per unit of the derivative.
        expiry_time (int): Time in seconds until the auction expires.

    Returns:
        dict: Response from the Paradigm API.
    """
    url = f"{PARADIGM_API_BASE_URL}/auctions"
    payload = {
        "symbol": symbol,
        "quantity": quantity,
        "price": price,
        "expiry_time": int(time.time()) + expiry_time  # Auction expiry timestamp
    }

    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        return response.json()  # Parse and return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error creating auction: {e}")
        return {"error": str(e)}

# Function to fetch auction details
def get_auction_details(auction_id):
    """
    Retrieves details of an existing auction.

    Parameters:
        auction_id (str): Unique ID of the auction.

    Returns:
        dict: Response from the Paradigm API.
    """
    url = f"{PARADIGM_API_BASE_URL}/auctions/{auction_id}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching auction details: {e}")
        return {"error": str(e)}

# Function to cancel an auction
def cancel_auction(auction_id):
    """
    Cancels an existing auction.

    Parameters:
        auction_id (str): Unique ID of the auction to cancel.

    Returns:
        dict: Response from the Paradigm API.
    """
    url = f"{PARADIGM_API_BASE_URL}/auctions/{auction_id}/cancel"

    try:
        response = requests.post(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error cancelling auction: {e}")
        return {"error": str(e)}

# Example Usage
if __name__ == "__main__":
    # Create an auction
    auction_response = create_auction(symbol="BTC-USD", quantity=1.0, price=50000.0, expiry_time=3600)
    if "error" not in auction_response:
        auction_id = auction_response.get("auction_id")
        print(f"Auction created successfully. Auction ID: {auction_id}")
        
        # Fetch auction details
        details = get_auction_details(auction_id)
        print("Auction Details:", details)
        
        # Cancel the auction
        cancel_response = cancel_auction(auction_id)
        print("Cancel Response:", cancel_response)
    else:
        print("Failed to create auction:", auction_response)
```

Note: Replace `your_api_key_here` and `your_api_secret_here` with your actual Paradigm API key and secret.
