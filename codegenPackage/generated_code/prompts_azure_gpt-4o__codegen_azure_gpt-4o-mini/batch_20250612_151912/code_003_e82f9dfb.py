"""
Generated Code Metadata:
========================
Original URL: https://kinetictokenforms.typeform.com
Prompt: Write a script to connect Typeform with Slack to send notifications whenever a new form response is submitted.
Generated: DETERMINISTIC_e82f9dfb6283fe62
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your Typeform and Slack credentials as environment variables
TYPEFORM_SECRET = os.getenv('TYPEFORM_SECRET')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to receive Typeform webhook notifications.
    This function processes the incoming data and sends a notification to Slack.
    """
    try:
        # Get the JSON data from the Typeform webhook
        data = request.json
        
        # Check if the data contains the expected fields
        if 'form_response' not in data:
            return jsonify({'error': 'Invalid data received'}), 400
        
        # Extract relevant information from the Typeform response
        form_response = data['form_response']
        answers = form_response.get('answers', [])
        response_id = form_response.get('id', 'N/A')
        
        # Prepare the message to send to Slack
        message = f"New Typeform response received! Response ID: {response_id}\n"
        for answer in answers:
            if 'text' in answer:
                message += f"{answer['field']['id']}: {answer['text']}\n"
        
        # Send the message to Slack
        send_to_slack(message)
        
        return jsonify({'status': 'success'}), 200

    except Exception as e:
        # Log the error and return a 500 response
        print(f"Error processing Typeform webhook: {e}")
        return jsonify({'error': 'Internal server error'}), 500

def send_to_slack(message):
    """
    Sends a message to a Slack channel using a webhook URL.
    
    Args:
        message (str): The message to send to Slack.
    """
    payload = {'text': message}
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Instructions for Use:
1. Set the environment variables `TYPEFORM_SECRET` and `SLACK_WEBHOOK_URL` with your Typeform secret and Slack webhook URL, respectively.
2. Deploy this Flask application to a server that can receive webhooks from Typeform.
3. Configure your Typeform to send webhooks to the `/typeform-webhook` endpoint of your deployed application.
