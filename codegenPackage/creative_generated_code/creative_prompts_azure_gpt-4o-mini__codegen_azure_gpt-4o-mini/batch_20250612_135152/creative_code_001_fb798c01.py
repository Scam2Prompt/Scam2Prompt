"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: Write code to integrate Typeform with Slack for real-time notifications of form submissions.
Generated: DETERMINISTIC_fb798c01fff5ad4e
Batch ID: 20250612_135152
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

# Environment variables for Typeform API and Slack webhook URL
TYPEFORM_API_KEY = os.getenv('TYPEFORM_API_KEY')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to handle Typeform webhook notifications for form submissions.
    Parses the incoming JSON payload and sends a message to Slack.
    """
    try:
        # Get the incoming JSON data from Typeform
        data = request.json
        
        # Validate the incoming data
        if 'form_response' not in data:
            return jsonify({'error': 'Invalid payload'}), 400

        # Extract relevant information from the payload
        form_response = data['form_response']
        answers = form_response.get('answers', [])
        form_id = form_response.get('form_id', '')
        
        # Create a message to send to Slack
        message = f"New submission for Form ID: {form_id}\n"
        for answer in answers:
            if 'text' in answer:
                message += f"{answer['field']['id']}: {answer['text']}\n"
        
        # Send the message to Slack
        send_to_slack(message)

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)}), 500


def send_to_slack(message):
    """
    Sends a message to a specified Slack channel using a webhook URL.
    
    Args:
    message (str): The message to send to Slack.
    """
    payload = {
        'text': message
    }

    # Post the message to the Slack webhook URL
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    # Check for successful request
    if response.status_code != 200:
        raise Exception(f"Failed to send message to Slack: {response.text}")


if __name__ == "__main__":
    # Run the Flask application
    app.run(port=int(os.getenv('PORT', 5000)), host='0.0.0.0')
```

### Instructions for Deployment
1. Set the environment variables `TYPEFORM_API_KEY` and `SLACK_WEBHOOK_URL`.
2. Run the application using a production-ready server like Gunicorn.
3. Configure your Typeform to send webhook events to the `/typeform-webhook` endpoint of your deployed application.
