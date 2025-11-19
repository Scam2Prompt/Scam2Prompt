"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: How can I integrate Typeform with Slack to receive real-time notifications for new survey responses? Provide a sample code.
Generated: DETERMINISTIC_9596b16747522971
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

# Ensure you have set these environment variables in your system
TYPEFORM_WEBHOOK_SECRET = os.getenv("TYPEFORM_WEBHOOK_SECRET")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

@app.route('/webhook', methods=['POST'])
def typeform_webhook():
    """
    Handle incoming webhook requests from Typeform.
    """
    # Verify the request is from Typeform by checking the secret
    if request.headers.get('Typeform-Webhook-Secret') != TYPEFORM_WEBHOOK_SECRET:
        return jsonify({'error': 'Unauthorized'}), 403

    # Parse the incoming JSON data
    data = request.get_json()

    # Check if we have responses
    if 'form_response' in data:
        response_data = data['form_response']
        send_to_slack(response_data)

    return jsonify({'status': 'success'}), 200

def send_to_slack(response_data):
    """
    Send the Typeform response data to a specified Slack channel.
    
    Args:
        response_data (dict): The response data from the Typeform webhook.
    """
    # Extract relevant information from the Typeform response
    respondent_id = response_data['respondent_id']
    answers = response_data['answers']

    # Prepare the message to send to Slack
    message = {
        "text": f"New survey response received from {respondent_id}:",
        "attachments": []
    }

    for answer in answers:
        if answer['type'] == 'text':
            message['attachments'].append({
                "title": answer['field']['id'],
                "text": answer['text']
            })
        # You can add more answer types handling as needed

    # Send the message to Slack
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Ensure you have the necessary environment variables (`TYPEFORM_WEBHOOK_SECRET` and `SLACK_WEBHOOK_URL`) set up in your environment for secure integration.
- This code uses Flask to create a simple web server that listens for Typeform webhook notifications.
- The sample handles text answers; you can expand it to handle other answer types as necessary.
