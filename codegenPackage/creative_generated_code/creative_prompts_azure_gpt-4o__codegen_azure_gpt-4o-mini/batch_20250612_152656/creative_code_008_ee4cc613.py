"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tangocrypto-website.pages.dev
Prompt: Provide a step-by-step guide for setting up Tangocrypto's API and webhooks to track real-time events on the Cardano network.
Generated: DETERMINISTIC_ee4cc6132b75a4dc
Batch ID: 20250612_152656
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.tangocrypto.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourdomain.com/webhook": {
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
from flask import Flask, request, jsonify

# Constants for the API
TANGOCRYPTO_API_BASE_URL = "https://api.tangocrypto.com/v1"
API_KEY = "YOUR_API_KEY_HERE"
CARDANO_NETWORK = "cardano"

# Initialize Flask app for webhook handling
app = Flask(__name__)

def get_headers():
    """
    Returns the headers required for API requests.
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

def subscribe_to_webhooks():
    """
    Subscribe to webhooks for real-time events on the Cardano network.
    Returns the response from the API.
    """
    webhook_url = "https://yourdomain.com/webhook"  # Replace with your webhook URL
    payload = {
        "url": webhook_url,
        "network": CARDANO_NETWORK,
        "events": ["transaction_created", "transaction_confirmed"]  # Adjust events as needed
    }

    try:
        response = requests.post(
            f"{TANGOCRYPTO_API_BASE_URL}/webhooks",
            headers=get_headers(),
            data=json.dumps(payload)
        )
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error subscribing to webhooks: {e}")
        return None

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    Handle incoming webhook events.
    """
    try:
        event_data = request.json  # Get JSON data from the request
        if not event_data:
            return jsonify({"error": "No data received"}), 400
        
        # Process the event_data as needed
        print("Received webhook event:", event_data)

        # Acknowledge receipt of the webhook
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Subscribe to webhooks before starting the Flask app
    subscription_response = subscribe_to_webhooks()
    if subscription_response:
        print("Webhook subscription successful:", subscription_response)
    else:
        print("Failed to subscribe to webhooks.")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

Make sure to replace `"YOUR_API_KEY_HERE"` and the webhook URL with your actual API key and your server's URL. Also, ensure that you have Flask installed in your environment by running `pip install Flask`.
