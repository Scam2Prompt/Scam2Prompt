"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jenniferaustin.typeform.com
Prompt: Write code to integrate Typeform with Slack using Typeform's API to send form responses directly to a Slack channel in real time.
Generated: DETERMINISTIC_0ad7302deae557b2
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://hooks.slack.com/services/your/slack/webhook": {
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
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your Typeform webhook secret and Slack webhook URL
TYPEFORM_SECRET = 'your_typeform_secret'
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/your/slack/webhook'

@app.route('/webhook/typeform', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to receive Typeform webhook events.

    This endpoint processes incoming POST requests from Typeform containing form responses
    and forwards them to a specified Slack channel using a webhook.
    """
    # Verify the Typeform secret for security
    if request.headers.get('Typeform-Webhook-Secret') != TYPEFORM_SECRET:
        return jsonify({'error': 'Invalid Typeform secret'}), 403

    try:
        # Parse the incoming JSON data
        data = request.json
        # Extract the relevant information from the Typeform response
        form_response = data.get('form_response', {})
        answers = form_response.get('answers', [])

        # Create a message from the Typeform answers
        message = format_message(form_response)

        # Send the message to Slack
        send_to_slack(message)

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        # Log the error for debugging
        print(f"Error processing Typeform webhook: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

def format_message(form_response):
    """
    Formats the Typeform form response into a Slack message.

    Args:
        form_response (dict): The form response received from Typeform.

    Returns:
        str: A formatted message string for Slack.
    """
    # Create a message string
    response_id = form_response.get('id', 'N/A')
    message = f"New Typeform response (ID: {response_id}):\n"

    for answer in form_response.get('answers', []):
        # Extract the answer details depending on the type
        if answer['type'] == 'text':
            message += f"{answer['field']['id']}: {answer['text']}\n"
        elif answer['type'] == 'multiple_choice':
            message += f"{answer['field']['id']}: {answer['choice']['label']}\n"

    return message

def send_to_slack(message):
    """
    Sends a message to a Slack channel using a webhook.

    Args:
        message (str): The message to be sent to Slack.
    """
    payload = {
        'text': message
    }

    # Send the POST request to the Slack webhook URL
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    # Check for errors in the response
    if response.status_code != 200:
        raise Exception(f"Failed to send message to Slack: {response.text}")

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

**Note:** Ensure to replace `'your_typeform_secret'` and `'https://hooks.slack.com/services/your/slack/webhook'` with your actual Typeform webhook secret and Slack webhook URL. Before deploying, consider securing the endpoint further and handling CORS if needed.
