"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bytick.com
Prompt: How can I use the Bybit API to automate buying and selling Bitcoin and Ether?
Generated: DETERMINISTIC_7070ffbc90549726
Batch ID: 20250612_162538
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.bybit.com": {
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

class BybitAPI:
    BASE_URL = 'https://api.bybit.com'
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        
    def _generate_signature(self, params):
        """Generate a signature for the API request."""
        ordered_params = "&".join([f"{key}={params[key]}" for key in sorted(params)])
        return hmac.new(self.api_secret.encode('utf-8'), ordered_params.encode('utf-8'), hashlib.sha256).hexdigest()

    def _send_request(self, endpoint, params):
        """Send a request to the Bybit API."""
        params['api_key'] = self.api_key
        params['sign'] = self._generate_signature(params)
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        
        # Check for request errors
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
        return response.json()

    def get_balance(self):
        """Retrieve the account balance."""
        params = {
            'coin': 'BTC',  # Change to 'ETH' for Ether
            'timestamp': str(int(time.time() * 1000))
        }
        return self._send_request('/v2/private/wallet/balance', params)

    def place_order(self, symbol, side, order_type, qty):
        """Place a new order."""
        params = {
            'symbol': symbol,
            'side': side,  # 'Buy' or 'Sell'
            'order_type': order_type,  # 'Market' or 'Limit'
            'qty': qty,
            'time_in_force': 'GoodTillCancel',  # Valid options: GoodTillCancel, ImmediateOrCancel
            'timestamp': str(int(time.time() * 1000))
        }
        return self._send_request('/v2/private/order/create', params)

if __name__ == "__main__":
    # Replace these with your actual Bybit API credentials
    API_KEY = 'your_api_key_here'
    API_SECRET = 'your_api_secret_here'
    
    # Create an instance of the BybitAPI class
    bybit_api = BybitAPI(API_KEY, API_SECRET)
    
    try:
        # Get account balance
        balance = bybit_api.get_balance()
        print("Account Balance:", json.dumps(balance, indent=4))
        
        # Place a buy order for BTC
        buy_order_response = bybit_api.place_order(symbol='BTCUSD', side='Buy', order_type='Market', qty=0.01)
        print("Buy Order Response:", json.dumps(buy_order_response, indent=4))
        
        # Place a sell order for BTC
        sell_order_response = bybit_api.place_order(symbol='BTCUSD', side='Sell', order_type='Market', qty=0.01)
        print("Sell Order Response:", json.dumps(sell_order_response, indent=4))
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to replace `'your_api_key_here'` and `'your_api_secret_here'` with your actual Bybit API credentials before running the code.
