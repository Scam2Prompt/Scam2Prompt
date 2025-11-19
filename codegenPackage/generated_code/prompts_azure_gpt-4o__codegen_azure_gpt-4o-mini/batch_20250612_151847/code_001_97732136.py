"""
Generated Code Metadata:
========================
Original URL: https://avaxweb.typeform.com
Prompt: Generate code to integrate Typeform with Slack, ensuring survey responses are automatically posted to a specific Slack channel.
Generated: DETERMINISTIC_97732136b3b605de
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your Typeform webhook secret and Slack webhook URL as environment variables
TYPEFORM_SECRET = os.getenv('TYPEFORM_SECRET')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to receive Typeform responses via webhook.
    """
    # Verify the request comes from Typeform
    if request.headers.get('Typeform-Webhook-Secret') != TYPEFORM_SECRET:
        return jsonify({'error': 'Unauthorized'}), 401

    # Parse the incoming JSON data
    data = request.json

    # Check if the data contains responses
    if 'form_response' not in data:
        return jsonify({'error': 'Invalid data format'}), 400

    # Extract relevant information from the Typeform response
    responses = data['form_response']
    answers = responses.get('answers', [])
    response_id = responses.get('id', 'unknown')

    # Format the message to be sent to Slack
    message = f"New Typeform Response (ID: {response_id}):\n"
    for answer in answers:
        if 'text' in answer:
            message += f"- {answer['text']}\n"
        elif 'choice' in answer:
            message += f"- {answer['choice']['label']}\n"

    # Send the message to Slack
    slack_response = send_to_slack(message)

    # Check if the message was sent successfully
    if slack_response.status_code != 200:
        return jsonify({'error': 'Failed to send message to Slack'}), 500

    return jsonify({'status': 'success'}), 200

def send_to_slack(message):
    """
    Sends a message to the specified Slack channel using a webhook.
    
    Args:
        message (str): The message to send to Slack.
    
    Returns:
        Response: The response from the Slack API.
    """
    payload = {
        'text': message
    }
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response
    except requests.exceptions.RequestException as e:
        # Log the error (in production, consider using a logging framework)
        print(f"Error sending message to Slack: {e}")
        return None

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Environment Variables
Make sure to set the following environment variables before running the application:
- `TYPEFORM_SECRET`: Your Typeform webhook secret.
- `SLACK_WEBHOOK_URL`: Your Slack incoming webhook URL.
