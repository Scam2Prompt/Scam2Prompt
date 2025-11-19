"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musdt.xyz
Prompt: Illustrate how to implement a webhook in Python that listens for updates from the Musdt XYZ platform regarding exchange rate changes.
Generated: DETERMINISTIC_856a40bf59b5c310
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("webhook.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

# Secret token for verifying the webhook (replace with your actual secret)
WEBHOOK_SECRET = "your_webhook_secret"

@app.route('/webhook', methods=['POST'])
def webhook_listener():
    """
    Endpoint to listen for webhook updates from Musdt XYZ platform regarding exchange rate changes.
    """
    try:
        # Parse the JSON payload from the request
        payload = request.json
        if not payload:
            logging.warning("Received a request with no JSON payload.")
            return jsonify({"error": "Invalid payload"}), 400
        
        # Verify the secret token if provided in headers (optional)
        received_secret = request.headers.get('X-Webhook-Secret')
        if WEBHOOK_SECRET and received_secret != WEBHOOK_SECRET:
            logging.warning("Received a request with an invalid secret token.")
            return jsonify({"error": "Unauthorized"}), 401

        # Log the received payload for debugging purposes
        logging.info("Received valid webhook payload: %s", payload)

        # Example processing logic: handle exchange rate updates
        if payload.get('event') == 'exchange_rate_updated':
            exchange_rate_data = payload.get('data')
            if not exchange_rate_data:
                logging.error("Exchange rate update event received with missing data.")
                return jsonify({"error": "Missing exchange rate data"}), 400

            # Process the exchange rate update (replace with actual logic)
            currency = exchange_rate_data.get('currency')
            new_rate = exchange_rate_data.get('rate')
            logging.info(f"Exchange rate updated for {currency}: {new_rate}")
            # You can add additional processing here (e.g., updating a database)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        # Log unexpected errors for diagnostics
        logging.error("An error occurred during webhook processing: %s", str(e))
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app (ensure production deployment uses a proper WSGI server)
    app.run(host='0.0.0.0', port=5000)
```
