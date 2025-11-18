"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wa.gl
Prompt: How can I integrate han.gl's API with Slack or Zapier to receive notifications whenever a short URL is clicked?
Generated: DETERMINISTIC_cdf1210a6ed1bb9a
Batch ID: 20250612_154432
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.han.gl/v1/short-urls": {
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
# han.gl and Slack/Zapier integration script
# This script listens for click events on han.gl short URLs using their API 
# and sends notifications to Slack or Zapier webhook endpoints.

import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration settings
HANGL_API_KEY = "your_hangl_api_key"  # Replace with your han.gl API key
SLACK_WEBHOOK_URL = "your_slack_webhook_url"  # Replace with your Slack webhook URL
ZAPIER_WEBHOOK_URL = "your_zapier_webhook_url"  # Replace with your Zapier webhook URL

# URL for han.gl API endpoint
HANGL_API_ENDPOINT = "https://api.han.gl/v1/short-urls"

# Function to fetch click events from han.gl API
def fetch_click_events():
    try:
        response = requests.get(
            f"{HANGL_API_ENDPOINT}/click-events",
            headers={"Authorization": f"Bearer {HANGL_API_KEY}"}
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4XX, 5XX)
        return response.json()  # Return JSON response containing click events
    except requests.exceptions.RequestException as e:
        # Log and handle request errors
        print(f"Error fetching click events from han.gl API: {e}")
        return None

# Function to send notifications to Slack or Zapier
def send_notification(event, webhook_url):
    try:
        payload = {
            "text": f"Short URL clicked!\nURL: {event['url']}\nTimestamp: {event['timestamp']}\nIP Address: {event['ip_address']}"
        }
        response = requests.post(
            webhook_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(f"Notification sent successfully to {webhook_url}")
    except requests.exceptions.RequestException as e:
        # Log and handle request errors
        print(f"Error sending notification to webhook: {e}")

# Flask route to process han.gl click events and send notifications
@app.route("/process-click-events", methods=["POST"])
def process_click_events():
    try:
        # Fetch click events from han.gl API
        events = fetch_click_events()
        if events:
            for event in events:
                # Send notification to Slack webhook
                send_notification(event, SLACK_WEBHOOK_URL)
                # Send notification to Zapier webhook
                send_notification(event, ZAPIER_WEBHOOK_URL)
            return jsonify({"status": "success", "message": "Notifications processed"}), 200
        else:
            return jsonify({"status": "error", "message": "Failed to fetch click events"}), 500
    except Exception as e:
        # Handle generic exceptions
        print(f"Error processing click events: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**Note:** Replace placeholders like `your_hangl_api_key`, `your_slack_webhook_url`, and `your_zapier_webhook_url` with actual values. This script uses Flask as a web server to trigger the integration. Ensure the han.gl API is properly set up to allow access to click event data. Also, secure the webhooks and API keys in production environments.
