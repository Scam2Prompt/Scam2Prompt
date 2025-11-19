"""
Generated Code Metadata:
========================
Original URL: https://tangocrypto-website.pages.dev
Prompt: What are the steps to set up webhooks with Tangocrypto to receive updates on minted blocks and payments?
Generated: DETERMINISTIC_8b30e161230f3012
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hmac
import hashlib
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your Tangocrypto webhook secret key
WEBHOOK_SECRET = "your_webhook_secret_key"

# Endpoint to handle webhook events
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        # Verify the webhook signature
        signature = request.headers.get('X-Tangocrypto-Signature')
        if not signature:
            return jsonify({"error": "Missing signature"}), 400

        # Compute the HMAC SHA256 hash of the request body using the secret key
        computed_signature = hmac.new(
            WEBHOOK_SECRET.encode(),
            request.data,
            hashlib.sha256
        ).hexdigest()

        # Compare the computed signature with the one sent in the header
        if not hmac.compare_digest(computed_signature, signature):
            return jsonify({"error": "Invalid signature"}), 400

        # Parse the JSON payload
        payload = request.get_json()
        if not payload:
            return jsonify({"error": "Invalid payload"}), 400

        # Handle the webhook event based on its type
        event_type = payload.get('event_type')
        if event_type == 'block.minted':
            # Handle minted block event
            block_data = payload.get('data', {})
            print(f"New block minted: {block_data}")
        elif event_type == 'payment.received':
            # Handle payment received event
            payment_data = payload.get('data', {})
            print(f"Payment received: {payment_data}")
        else:
            # Unknown event type
            print(f"Unhandled event type: {event_type}")

        # Respond with a 200 OK to acknowledge receipt of the event
        return jsonify({"status": "success"}), 200

    except Exception as e:
        # Log the error and respond with a 500 Internal Server Error
        print(f"Error handling webhook: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
```

This code sets up a Flask application to handle webhooks from Tangocrypto. It verifies the webhook signature, processes the event payload, and handles specific event types (`block.minted` and `payment.received`). Make sure to replace `your_webhook_secret_key` with your actual Tangocrypto webhook secret key.
