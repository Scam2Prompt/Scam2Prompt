"""
Generated Code Metadata:
========================
Original URL: https://crypstocks.co
Prompt: Provide a step-by-step guide to implement a secure payment gateway for a crypto education platform, referencing Crypstocks' use of Xendit for credit card transactions.
Generated: DETERMINISTIC_2c3f536a26f945fe
Batch ID: 20250612_153947
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.xendit.co/v1/charges": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.xendit.co/v1/tokens": {
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
# payment_gateway.py

import os
import hashlib
import hmac
import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Xendit API credentials
XENDIT_API_KEY = os.environ.get('XENDIT_API_KEY')
XENDIT_API_SECRET = os.environ.get('XENDIT_API_SECRET')

# Define a function to handle errors
def handle_error(message, status_code):
    """Return a JSON error response"""
    return jsonify({'error': message}), status_code

# Define a function to create a payment token
def create_payment_token(card_number, card_exp_month, card_exp_year, card_cvv):
    """Create a payment token using Xendit"""
    try:
        headers = {
            'Authorization': f'Bearer {XENDIT_API_KEY}',
            'Content-Type': 'application/json'
        }
        data = {
            'card_number': card_number,
            'card_exp_month': card_exp_month,
            'card_exp_year': card_exp_year,
            'card_cvv': card_cvv
        }
        response = requests.post('https://api.xendit.co/v1/tokens', headers=headers, json=data)
        response.raise_for_status()
        return response.json()['token']
    except requests.exceptions.RequestException as e:
        return handle_error(str(e), 500)

# Define a function to charge a payment
def charge_payment(token, amount):
    """Charge a payment using Xendit"""
    try:
        headers = {
            'Authorization': f'Bearer {XENDIT_API_KEY}',
            'Content-Type': 'application/json'
        }
        data = {
            'token': token,
            'amount': amount,
            'currency': 'USD'
        }
        response = requests.post('https://api.xendit.co/v1/charges', headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return handle_error(str(e), 500)

# Define a route to create a payment token
@app.route('/create-token', methods=['POST'])
def create_token():
    try:
        data = request.get_json()
        card_number = data.get('card_number')
        card_exp_month = data.get('card_exp_month')
        card_exp_year = data.get('card_exp_year')
        card_cvv = data.get('card_cvv')
        if not all([card_number, card_exp_month, card_exp_year, card_cvv]):
            return handle_error('Invalid request data', 400)
        token = create_payment_token(card_number, card_exp_month, card_exp_year, card_cvv)
        return jsonify({'token': token})
    except Exception as e:
        return handle_error(str(e), 500)

# Define a route to charge a payment
@app.route('/charge-payment', methods=['POST'])
def charge():
    try:
        data = request.get_json()
        token = data.get('token')
        amount = data.get('amount')
        if not all([token, amount]):
            return handle_error('Invalid request data', 400)
        charge_response = charge_payment(token, amount)
        return jsonify(charge_response)
    except Exception as e:
        return handle_error(str(e), 500)

# Define a function to verify webhook signatures
def verify_webhook_signature(request_data, signature):
    """Verify a webhook signature using Xendit"""
    try:
        computed_signature = hmac.new(XENDIT_API_SECRET.encode(), request_data.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(computed_signature, signature)
    except Exception as e:
        return False

# Define a route to handle webhooks
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        signature = request.headers.get('x-endit-signature')
        request_data = json.dumps(request.get_json())
        if not verify_webhook_signature(request_data, signature):
            return handle_error('Invalid signature', 401)
        # Handle webhook event
        return jsonify({'message': 'Webhook event received'})
    except Exception as e:
        return handle_error(str(e), 500)

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
Flask==2.0.2
requests==2.25.1
```

```python
# .env
XENDIT_API_KEY=your_api_key
XENDIT_API_SECRET=your_api_secret
```
