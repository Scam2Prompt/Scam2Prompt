"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroraindrop.typeform.com
Prompt: Write a script to connect Typeform with Slack using its integration capabilities, sending notifications for every new form submission.
Generated: DETERMINISTIC_901c29e891568b91
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
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Typeform Configuration
TYPEFORM_SECRET = os.getenv('TYPEFORM_SECRET')  # Typeform webhook secret
TYPEFORM_URL = os.getenv('TYPEFORM_URL')        # Typeform webhook URL

# Slack Configuration
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')  # Incoming webhook URL for Slack

@app.route('/webhook', methods=['POST'])
def typeform_webhook():
    """
    Handle incoming webhook notifications from Typeform.
    
    This endpoint listens for POST requests sent by Typeform when a new 
    form submission is detected. It processes the submission data and 
    sends a notification to Slack.
    """

    try:
        # Verify the request using the Typeform secret
        if request.headers.get('Typeform-Webhook-Secret') != TYPEFORM_SECRET:
            return jsonify({'error': 'Unauthorized access'}), 403
        
        data = request.json
        
        # Extract relevant data from the Typeform submission
        form_response = data.get('form_response', {})
        answers = form_response.get('answers', [])
        submitted_data = {answer['field']['id']: answer['text'] for answer in answers}

        # Create a message to send to Slack
        message = {
            "text": "New Typeform Submission Received!",
            "attachments": [
                {
                    "fields": [{"title": key, "value": value, "short": True} for key, value in submitted_data.items()]
                }
            ]
        }

        # Send the message to Slack
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        response.raise_for_status()  # Raise an error if the request failed

        return jsonify({'status': 'success'}), 200

    except requests.exceptions.RequestException as e:
        # Log and return an error if the Slack message fails to send
        print(f"Error sending message to Slack: {e}")
        return jsonify({'error': 'Failed to send message to Slack'}), 500

    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An internal error occurred'}), 500

if __name__ == '__main__':
    # Ensure the application runs only in production with debug turned off
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Notes:
- Ensure to set the environment variables `TYPEFORM_SECRET`, `TYPEFORM_URL`, and `SLACK_WEBHOOK_URL` before running the script.
- This script requires Flask and Requests libraries. Install them via pip if not installed:
  ```bash
  pip install Flask requests
  ```
