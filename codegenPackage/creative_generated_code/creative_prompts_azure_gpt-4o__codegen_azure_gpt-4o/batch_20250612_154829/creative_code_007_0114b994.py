"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0g.notifi.network
Prompt: Develop a webhook integration to receive notifications about governance proposals from the 0G Foundation.
Generated: DETERMINISTIC_0114b994fa9edc16
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurations
WEBHOOK_SECRET = "your_webhook_secret"  # Replace with your actual secret
EXPECTED_EVENT_TYPE = "proposal_notification"  # Example event type to validate notifications

# Route to handle webhook notifications
@app.route("/webhook", methods=["POST"])
def webhook_handler():
    try:
        # Parse the incoming JSON payload
        payload = request.get_json()
        
        if not payload:
            return jsonify({"error": "Invalid JSON payload"}), 400

        # Validate the secret if included in the headers
        incoming_secret = request.headers.get("X-Webhook-Secret")
        if incoming_secret != WEBHOOK_SECRET:
            return jsonify({"error": "Unauthorized request"}), 403

        # Validate event type
        event_type = payload.get("event_type")
        if event_type != EXPECTED_EVENT_TYPE:
            return jsonify({"error": f"Unexpected event type: {event_type}"}), 400

        # Extract proposal data
        proposal_data = payload.get("data")
        if not proposal_data:
            return jsonify({"error": "Missing proposal data"}), 400

        # Process the proposal notification (implement your logic here)
        # For example, log the details or trigger further processing
        print(f"Received proposal notification: {json.dumps(proposal_data, indent=2)}")

        # Respond with a success message
        return jsonify({"message": "Notification received successfully"}), 200

    except Exception as e:
        # Catch unexpected errors and respond with a server error
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Health check route to ensure service is running
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK"}), 200


if __name__ == "__main__":
    # Run the Flask application
    # Ensure the server is properly secured in a production environment
    app.run(host="0.0.0.0", port=5000)
```
