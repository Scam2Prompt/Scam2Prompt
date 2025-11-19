"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cjjzqkc.cn
Prompt: Create an example of a trading bot that operates on the OKX platform, using the features of perpetual contracts and spot trading as described in the OKX documentation.
Generated: DETERMINISTIC_cd97592be55bcca2
Batch ID: 20250612_162106
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
import requests
import time
import hmac
import hashlib
import base64
from datetime import datetime

# Constants
API_KEY = 'your-api-key'
SECRET_KEY = 'your-secret-key'
PASSPHRASE = 'your-passphrase'
BASE_URL = 'https://www.okx.com'

# Utility function to get current timestamp in ISO 8601 format
def get_iso_timestamp():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

# Generate signature for authentication
def generate_signature(timestamp, method, request_path, body=''):
    message = f'{timestamp}{method.upper()}{request_path}{body}'
    hmac_key = base64.b64decode(SECRET_KEY)
    signature = hmac.new(hmac_key, message.encode(), hashlib.sha256).digest()
    return base64.b64encode(signature).decode()

# Send signed request to OKX
def send_request(method, request_path, payload=None):
    try:
        timestamp = get_iso_timestamp()
        body = payload if payload else ''
        # Generate signature
        signature = generate_signature(timestamp, method, request_path, body)
        headers = {
            'OK-ACCESS-KEY': API_KEY,
            'OK-ACCESS-SIGN': signature,
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': PASSPHRASE,
            'Content-Type': 'application/json'
        }
        url = f'{BASE_URL}{request_path}'
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=body)
        else:
            raise ValueError("Unsupported HTTP method")
        # Check response status and handle errors
        if response.status_code != 200:
            print(f'Error: {response.status_code}, {response.text}')
            response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Request Exception: {e}')
        return None

# Fetch account balance
def get_account_balance():
    request_path = '/api/v5/account/balance'
    return send_request('GET', request_path)

# Fetch perpetual contracts instruments
def get_perpetual_instruments():
    request_path = '/api/v5/public/instruments?instType=SWAP'
    return send_request('GET', request_path)

# Place a market order (example for spot trading)
def place_spot_market_order(inst_id, side, size):
    request_path = '/api/v5/trade/order'
    payload = {
        "instId": inst_id,
        "tdMode": "cash",
        "side": side,  # "buy" or "sell"
        "ordType": "market",
        "sz": size
    }
    return send_request('POST', request_path, json.dumps(payload))

# Main trading bot logic
def trading_bot():
    try:
        print("Fetching account balance...")
        balance = get_account_balance()
        print("Account Balance:", balance)

        print("Fetching perpetual instruments...")
        instruments = get_perpetual_instruments()
        print("Available Instruments:", instruments)

        # Example of placing a market order for spot trading
        print("Placing spot market order...")
        order_response = place_spot_market_order(inst_id="BTC-USDT", side="buy", size="0.01")
        print("Order Response:", order_response)

    except Exception as e:
        print(f"Error in trading bot: {e}")

# Entry point
if __name__ == '__main__':
    trading_bot()
```
