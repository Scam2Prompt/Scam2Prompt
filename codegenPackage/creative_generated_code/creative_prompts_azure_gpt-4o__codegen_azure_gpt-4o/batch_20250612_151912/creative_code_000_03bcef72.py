"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Write code to integrate Typeform with Slack using Typeform's API, ensuring form responses are automatically sent to a designated Slack channel.
Generated: DETERMINISTIC_03bcef72c55e4bdc
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX": {
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
from flask import Flask, request, jsonify

# Flask app to handle incoming Typeform webhooks
app = Flask(__name__)

# Slack webhook URL (replace with your actual Slack webhook URL)
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX"

# Typeform webhook secret (replace with your secret for validation)
TYPEFORM_WEBHOOK_SECRET = "your_typeform_webhook_secret"

# Helper function to send a message to Slack
def send_to_slack(message):
    try:
        payload = {
            "text": message
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

        if response.status_code != 200:
            print(f"Error sending message to Slack: {response.status_code}, {response.text}")
            return False
        return True
    except Exception as e:
        print(f"Exception occurred while sending to Slack: {str(e)}")
        return False

# Endpoint to handle Typeform webhook
@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    try:
        # Verify the request signature for security
        if TYPEFORM_WEBHOOK_SECRET:
            signature = request.headers.get('Typeform-Signature')
            if not signature:
                return jsonify({"error": "Missing Typeform-Signature header"}), 403
            # Add signature verification logic here if needed

        # Parse the incoming webhook data
        webhook_data = request.get_json()
        if not webhook_data:
            return jsonify({"error": "Invalid or missing request payload"}), 400

        # Extract relevant details from Typeform response
        form_id = webhook_data.get('form_response', {}).get('form_id', 'Unknown Form ID')
        answers = webhook_data.get('form_response', {}).get('answers', [])

        # Format the message for Slack
        slack_message = f"New Typeform Response:\nForm ID: {form_id}\n"
        for answer in answers:
            question = answer.get('field', {}).get('title', 'Unknown Question')
            response = answer.get('text', answer.get('choice', {}).get('label', 'No Response'))
            slack_message += f"{question}: {response}\n"

        # Send the formatted message to Slack
        if send_to_slack(slack_message):
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"error": "Failed to send message to Slack"}), 500

    except Exception as e:
        print(f"Error processing Typeform webhook: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Main entry point for running the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

This code sets up a simple Flask application to process Typeform webhook requests and send the parsed form responses to a Slack channel using Slack's webhook API. Ensure you replace placeholders like `SLACK_WEBHOOK_URL` and `TYPEFORM_WEBHOOK_SECRET` with actual values.
