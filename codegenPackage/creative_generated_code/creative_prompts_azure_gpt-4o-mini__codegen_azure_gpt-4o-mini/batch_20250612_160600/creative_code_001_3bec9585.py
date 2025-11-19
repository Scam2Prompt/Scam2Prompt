"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Write code to integrate Typeform with Slack for real-time notifications of new survey responses.
Generated: DETERMINISTIC_3bec95857ac7d83c
Batch ID: 20250612_160600
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

app = Flask(__name__)

# Set up environment variables for Typeform and Slack tokens
TYPEFORM_TOKEN = os.getenv('TYPEFORM_TOKEN')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Handle incoming webhook notifications from Typeform.
    This function is triggered when a new survey response is received.
    """

    # Validate the request
    if request.method != 'POST':
        return jsonify({'error': 'Invalid request method'}), 405

    # Parse the JSON payload
    payload = request.get_json()
    if not payload:
        return jsonify({'error': 'Invalid JSON payload'}), 400

    # Extract necessary information from the payload
    try:
        form_id = payload['form_response']['form_id']
        answers = payload['form_response']['answers']
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

    # Format the message to send to Slack
    message = f"New response received for form ID: {form_id}\n"
    for answer in answers:
        # Handle different answer types
        if answer['type'] == 'text':
            answer_text = answer['text']
        elif answer['type'] == 'multiple_choice':
            answer_text = ', '.join(choice['text'] for choice in answer['choices'])
        else:
            answer_text = '[Unsupported answer type]'

        message += f"{answer['field']['id']}: {answer_text}\n"

    # Send the message to Slack
    response = send_to_slack(message)
    if not response:
        return jsonify({'error': 'Failed to send message to Slack'}), 500

    return jsonify({'status': 'success'}), 200

def send_to_slack(message):
    """
    Send a message to a Slack channel using a webhook URL.
    
    Args:
        message (str): The message to send to Slack.
    
    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    try:
        slack_data = {'text': message}
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'})

        # Check for a successful response
        if response.status_code != 200:
            print(f"Error sending message to Slack: {response.status_code}, {response.text}")
            return False

        return True
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {str(e)}")
        return False

if __name__ == '__main__':
    # Run the Flask app on the defined host and port
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

Make sure to set up the environment variables `TYPEFORM_TOKEN` and `SLACK_WEBHOOK_URL` with the respective tokens before running this Flask application.
