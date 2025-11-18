"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://me2.kr
Prompt: Use Me2.kr's API to set up Slack notifications whenever a user clicks on a shortened link or scans a QR code.
Generated: DETERMINISTIC_4b6c3d48ddb40153
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration for Me2.kr API and Slack webhook
ME2KR_API_KEY = "your_me2kr_api_key"
SLACK_WEBHOOK_URL = "your_slack_webhook_url"

# Error handling function for Slack notifications
def send_slack_notification(message):
    try:
        payload = {"text": message}
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an error for non-2xx responses
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Slack notification: {e}")

# Endpoint to handle the webhook from Me2.kr
@app.route("/webhook/me2kr", methods=["POST"])
def me2kr_webhook():
    try:
        # Validate the incoming request
        if not request.is_json:
            return jsonify({"error": "Invalid request format"}), 400

        # Parse the incoming JSON payload
        data = request.get_json()

        # Extract relevant information from the payload
        event_type = data.get("event_type")  # e.g., "link_click" or "qr_code_scan"
        link_url = data.get("link_url")     # The shortened link or QR code URL
        user_agent = data.get("user_agent") # User agent information of the requester

        if not event_type or not link_url:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate a Slack message
        slack_message = (
            f"Event detected: {event_type}\n"
            f"URL: {link_url}\n"
            f"User Agent: {user_agent or 'N/A'}"
        )

        # Send the notification to Slack
        send_slack_notification(slack_message)

        # Respond to Me2.kr with success
        return jsonify({"status": "success"}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error handling webhook: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Start the Flask app
if __name__ == "__main__":
    # Run the Flask development server (use a production server like Gunicorn for production use)
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
- Replace `your_me2kr_api_key` and `your_slack_webhook_url` with appropriate values.
- Ensure that the Me2.kr API sends webhook data to the `/webhook/me2kr` endpoint. Configure this in your Me2.kr account settings.
- For production, consider deploying this app using a WSGI server like Gunicorn or uWSGI and secure the endpoint with authentication mechanisms.
