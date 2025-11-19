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
from flask import Flask, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO)

# A simple route to verify the webhook
@app.route('/webhook', methods=['GET'])
def verify_webhook():
    # This endpoint can be used to verify the webhook URL with the Musdt XYZ platform
    # Typically, you would expect a challenge or token for verification
    token = request.args.get('token')
    if token == 'your_verification_token':  # Replace with your actual verification token
        logging.info("Webhook verification successful.")
        return jsonify({'status': 'success', 'message': 'Webhook verified'}), 200
    else:
        logging.warning("Webhook verification failed.")
        return jsonify({'status': 'error', 'message': 'Invalid token'}), 403

# Endpoint to receive updates from the Musdt XYZ platform
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Log the incoming data for debugging
        logging.info("Received webhook data: %s", data)

        # Process the exchange rate update
        if 'exchange_rate' in data:
            exchange_rate = data['exchange_rate']
            logging.info(f"Updated exchange rate received: {exchange_rate}")
            # Here you would typically update your database or perform other actions

            return jsonify({'status': 'success', 'message': 'Exchange rate processed'}), 200
        else:
            logging.warning("Invalid data received: %s", data)
            return jsonify({'status': 'error', 'message': 'Invalid data format'}), 400
            
    except Exception as e:
        logging.error("Error processing webhook: %s", str(e))
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```

**Note**: 
- Replace `'your_verification_token'` with the actual verification token provided by the Musdt XYZ platform.
- Ensure that you configure your server to expose the webhook endpoint and handle HTTPS for production environments to secure your data.
