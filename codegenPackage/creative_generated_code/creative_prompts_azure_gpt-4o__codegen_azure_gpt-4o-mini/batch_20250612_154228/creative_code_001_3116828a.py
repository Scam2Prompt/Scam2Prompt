"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitget.fi
Prompt: Generate a script to automate cryptocurrency trades using the Bitget platform API, including setting stop-loss and take-profit orders.
Generated: DETERMINISTIC_3116828a8db15b40
Batch ID: 20250612_154228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bitget.com/api/v1": {
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
import time
import hmac
import hashlib
import json

class BitgetAPI:
    BASE_URL = "https://api.bitget.com/api/v1"
    
    def __init__(self, api_key, api_secret, passphrase):
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase

    def _get_headers(self, method, endpoint, params={}):
        # Create the signature for the request
        timestamp = str(int(time.time() * 1000))
        param_str = json.dumps(params) if params else ""
        signature = self._generate_signature(timestamp, method, endpoint, param_str)
        
        # Set the headers for the request
        headers = {
            "Content-Type": "application/json",
            "X-BG-APIKEY": self.api_key,
            "X-BG-SIGN": signature,
            "X-BG-TIMESTAMP": timestamp,
            "X-BG-PASSPHRASE": self.passphrase,
        }
        return headers

    def _generate_signature(self, timestamp, method, endpoint, params):
        # Prepare the data to be signed
        payload = f"{timestamp}{method}{endpoint}{params}"
        return hmac.new(self.api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

    def place_order(self, symbol, side, order_type, price, size, stop_loss=None, take_profit=None):
        endpoint = "/order"
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "price": price,
            "size": size,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
        }
        
        # Send the request to place an order
        try:
            response = requests.post(self.BASE_URL + endpoint, headers=self._get_headers("POST", endpoint, params), data=json.dumps(params))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error placing order: {e}")
            return None

    def get_account_info(self):
        endpoint = "/account"
        
        # Send the request to get account information
        try:
            response = requests.get(self.BASE_URL + endpoint, headers=self._get_headers("GET", endpoint))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving account info: {e}")
            return None

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"
    PASSPHRASE = "your_passphrase"

    # Initialize the Bitget API client
    bitget = BitgetAPI(API_KEY, API_SECRET, PASSPHRASE)

    # Place a trade with stop-loss and take-profit
    symbol = "BTCUSDT"
    side = "buy"  # or "sell"
    order_type = "limit"
    price = 60000  # Target price for the order
    size = 0.01  # Size of the trade
    stop_loss = 59000  # Stop-loss price
    take_profit = 61000  # Take-profit price

    order_response = bitget.place_order(symbol, side, order_type, price, size, stop_loss, take_profit)
    if order_response:
        print("Order placed successfully:", order_response)

    # Get account information
    account_info = bitget.get_account_info()
    if account_info:
        print("Account info retrieved successfully:", account_info)
```
