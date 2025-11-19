"""
Generated Code Metadata:
========================
Original URL: https://squid.wtf
Prompt: Develop a webhook in Flask that triggers an alert when SQUID.WTF updates its server status or Deezer functionality information.
Generated: DETERMINISTIC_f8edf8385267f42d
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
import logging
import os
import requests

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define constants
SQUID_WTF_WEBHOOK_SECRET = os.environ.get('SQUID_WTF_WEBHOOK_SECRET')
DEEZER_FUNCTIONALITY_URL = os.environ.get('DEEZER_FUNCTIONALITY_URL')
ALERT_WEBHOOK_URL = os.environ.get('ALERT_WEBHOOK_URL')

# Define a function to send alerts
def send_alert(message):
    try:
        response = requests.post(ALERT_WEBHOOK_URL, json={'message': message})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to send alert: {e}')

# Define a function to verify webhook signature
def verify_webhook_signature(request_data, request_headers):
    signature = request_headers.get('X-Webhook-Signature')
    computed_signature = hmac.new(SQUID_WTF_WEBHOOK_SECRET.encode(), request_data, hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, computed_signature)

# Define the webhook endpoint
@app.route('/squid_wtf_webhook', methods=['POST'])
def squid_wtf_webhook():
    try:
        # Verify webhook signature
        request_data = request.get_data()
        if not verify_webhook_signature(request_data, request.headers):
            logger.error('Invalid webhook signature')
            return jsonify({'error': 'Invalid webhook signature'}), 401

        # Parse JSON payload
        payload = json.loads(request_data.decode())

        # Check for server status updates
        if payload.get('type') == 'server_status_update':
            send_alert(f'SQUID.WTF server status updated: {payload.get("status")}')
            logger.info(f'Received server status update: {payload.get("status")}')

        # Check for Deezer functionality updates
        elif payload.get('type') == 'deezer_functionality_update':
            send_alert(f'Deezer functionality updated: {payload.get("functionality")} at {DEEZER_FUNCTIONALITY_URL}')
            logger.info(f'Received Deezer functionality update: {payload.get("functionality")}')

        return jsonify({'message': 'Webhook received successfully'}), 200

    except Exception as e:
        logger.error(f'Error processing webhook: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    import hmac
    import hashlib
    import json
    app.run(debug=True)
```
