"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quarkchain.typeform.com
Prompt: Write code to integrate Typeform with Slack for real-time notifications when a user submits a form.
Generated: DETERMINISTIC_f39346c4b0fb0cf9
Batch ID: 20250612_151912
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

# Configuration
TYPEFORM_API_KEY = "your_typeform_api_key"  # Replace with your Typeform API key
SLACK_WEBHOOK_URL = "your_slack_webhook_url"  # Replace with your Slack webhook URL

# Function to send notification to Slack
def send_to_slack(form_response):
    try:
        # Extract relevant data from the form response
        form_id = form_response.get('form_id', 'Unknown Form')
        answers = form_response.get('answers', [])
        
        # Format the message for Slack
        message = f"New Typeform submission from form ID: {form_id}\n"
        for answer in answers:
            question = answer.get('field', {}).get('title', 'Unknown Question')
            response = answer.get('text', 'No Answer')
            message += f"- {question}: {response}\n"

        # Prepare the payload for Slack
        slack_payload = {"text": message}

        # Send the request to Slack webhook
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(slack_payload), headers={'Content-Type': 'application/json'})

        if response.status_code != 200:
            raise Exception(f"Slack Webhook Error: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"Error sending to Slack: {e}")

# Webhook endpoint to handle Typeform submissions
@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    try:
        # Parse the incoming JSON request
        data = request.json
        if not data or 'event_id' not in data or 'form_response' not in data:
            return jsonify({"error": "Invalid payload"}), 400

        form_response = data['form_response']

        # Send the form response to Slack
        send_to_slack(form_response)

        # Return success response
        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Error processing Typeform webhook: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask server
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Replace `your_typeform_api_key` and `your_slack_webhook_url` with actual values.
- This code assumes Typeform sends POST requests to the `/typeform-webhook` endpoint with form responses.
- Flask is used for the webhook implementation, and requests library is used for sending Slack notifications.
