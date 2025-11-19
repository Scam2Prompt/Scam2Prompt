"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://essentialairdrop.typeform.com
Prompt: Write a code snippet to integrate Typeform with Slack for real-time notifications of new survey responses.
Generated: DETERMINISTIC_a41fb09484670c6f
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set Slack webhook URL and Typeform secret token from environment variables
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
TYPEFORM_SECRET_TOKEN = os.getenv('TYPEFORM_SECRET_TOKEN')

@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to receive webhook notifications from Typeform.
    Processes the incoming data and sends a message to Slack.
    """
    # Check for valid secret token to secure the webhook
    if request.headers.get('Authorization') != f'Bearer {TYPEFORM_SECRET_TOKEN}':
        return jsonify({'error': 'Unauthorized'}), 401

    # Parse the incoming JSON data from Typeform
    try:
        data = request.get_json()
        responses = data.get('form_response', {})
        if not responses:
            return jsonify({'error': 'No form response found'}), 400
        
        # Extract relevant information from the Typeform response
        respondent = responses.get('hidden', {}).get('respondent_name', 'Anonymous')
        answers = responses.get('answers', [])

        # Build the message to send to Slack
        message = f"New response from {respondent}:\n"
        for answer in answers:
            message += f"- {answer.get('field', {}).get('id', 'Unknown Field')}: {answer.get('text', 'No Answer')}\n"

        # Send the message to Slack
        send_to_slack(message)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'status': 'success'}), 200

def send_to_slack(message):
    """
    Sends a message to the Slack webhook URL.
    
    :param message: The message to send to Slack.
    """
    payload = {'text': message}
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Environment Variables
- `SLACK_WEBHOOK_URL`: The webhook URL for sending messages to Slack.
- `TYPEFORM_SECRET_TOKEN`: The secret token used to authenticate Typeform webhook requests.
    app.run(port=5000)
```

Make sure to set the environment variables `SLACK_WEBHOOK_URL` and `TYPEFORM_SECRET_TOKEN` before running this application. The application listens for incoming POST requests from Typeform and sends notifications to a specified Slack channel.
