"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Write code to integrate Typeform with Slack using Typeform's API to send form responses directly to a Slack channel in real time.
Generated: DETERMINISTIC_0ad7302deae557b2
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import requests
from flask import Flask, request, jsonify

# Flask app to handle incoming Typeform webhook
app = Flask(__name__)

# Environment variables for configuration
TYPEFORM_SECRET = os.getenv("TYPEFORM_SECRET")  # Secret for verifying Typeform webhook
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")  # Slack Incoming Webhook URL

@app.route('/typeform-webhook', methods=['POST'])
def handle_typeform_webhook():
    """
    Endpoint to handle Typeform webhook notifications.
    This function receives Typeform responses and forwards the data
    to a Slack channel via Slack Incoming Webhooks.
    """
    # Verify Typeform secret header
    typeform_secret = request.headers.get('Typeform-Secret')
    if typeform_secret != TYPEFORM_SECRET:
        return jsonify({"error": "Unauthorized"}), 403
    
    # Parse incoming webhook payload
    try:
        payload = request.get_json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON payload"}), 400
    
    # Extract form responses
    form_response = payload.get("form_response", {})
    if not form_response:
        return jsonify({"error": "No form response found"}), 400
    
    # Extract answers and format them for Slack
    answers = form_response.get("answers", [])
    form_title = form_response.get("definition", {}).get("title", "Unknown Form")
    formatted_answers = []

    for answer in answers:
        question = answer.get("field", {}).get("title", "Unknown Question")
        answer_value = answer.get("text") or answer.get("choice", {}).get("label") or "No Answer"
        formatted_answers.append(f"*{question}*: {answer_value}")

    # Generate Slack message
    slack_message = {
        "text": f"New response received for *{form_title}*:\n" + "\n".join(formatted_answers)
    }

    # Send message to Slack using Incoming Webhook
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=slack_message)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to send message to Slack: {str(e)}"}), 500

    return jsonify({"message": "Form response successfully sent to Slack"}), 200

# Run the Flask app
if __name__ == "__main__":
    # Ensure environment variables are set
    if not TYPEFORM_SECRET or not SLACK_WEBHOOK_URL:
        print("Error: TYPEFORM_SECRET and SLACK_WEBHOOK_URL environment variables must be set.")
        exit(1)

    # Start the Flask app
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
- Set the `TYPEFORM_SECRET` and `SLACK_WEBHOOK_URL` as environment variables before running the script.
- This code sets up a Flask application to listen for Typeform webhook events and processes responses in real time by sending them to Slack.
- Proper error handling and validation are included to ensure robustness in production environments.
