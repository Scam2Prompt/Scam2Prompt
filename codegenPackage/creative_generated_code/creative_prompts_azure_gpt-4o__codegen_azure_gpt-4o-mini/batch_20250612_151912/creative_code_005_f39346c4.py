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
import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Environment Variables
TYPEFORM_SECRET = os.environ.get('TYPEFORM_SECRET')  # The secret from Typeform for validation
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')  # The webhook URL for Slack notifications

# Endpoint to handle Typeform webhook
@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    # Check for valid secret to ensure the request is from Typeform
    if request.headers.get('Authorization') != TYPEFORM_SECRET:
        return jsonify({'error': 'Unauthorized'}), 403

    # Parse the incoming JSON data from Typeform
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON payload'}), 400

    # Extract relevant information from the Typeform submission
    try:
        form_response = data['form_response']
        answers = form_response.get('answers', [])
        submitted_data = {answer['field']['id']: answer['text'] for answer in answers if 'text' in answer}

        # Prepare the message to send to Slack
        message = f"New Typeform Submission:\n" + json.dumps(submitted_data, indent=2)
    except KeyError as e:
        return jsonify({'error': f'Missing key in payload: {str(e)}'}), 400

    # Send notification to Slack
    response = send_slack_notification(message)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to send notification to Slack'}), 500

    return jsonify({'success': 'Notification sent to Slack'}), 200

def send_slack_notification(message):
    """Send a message to Slack using the incoming webhook URL."""
    payload = {
        "text": message
    }
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        return response
    except requests.exceptions.RequestException as e:
        # Log the error (in production, consider logging to a file or monitoring system)
        print(f"Error sending message to Slack: {e}")
        return None

if __name__ == '__main__':
    # Start the Flask web server
    app.run(port=int(os.environ.get('PORT', 5000)), debug=False)
```

### Notes
- Ensure that you set the environment variables `TYPEFORM_SECRET` and `SLACK_WEBHOOK_URL` before running the application.
- The Flask application listens for POST requests at the `/typeform-webhook` endpoint.
- This example includes error handling for various potential issues, such as unauthorized access and missing keys in the payload.
- The message sent to Slack is formatted as JSON for clarity.
