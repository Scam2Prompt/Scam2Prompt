"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://keyfundairdrop.typeform.com
Prompt: "How can I integrate Typeform with Slack to receive real-time notifications for new survey responses? Provide an example."
Generated: DETERMINISTIC_aa297ff04e096fd0
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

# Slack webhook URL for sending notifications
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')

# Typeform webhook endpoint to receive responses
@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """Endpoint to receive Typeform responses and send notifications to Slack."""
    # Check if the request is valid
    if request.method == 'POST':
        data = request.json
        
        # Validate incoming data
        if not data or 'form_response' not in data:
            return jsonify({'error': 'Invalid data received'}), 400

        # Extract relevant information from Typeform response
        response_data = data['form_response']
        answers = response_data.get('answers', [])
        respondent_id = response_data.get('respondent', {}).get('id', 'Unknown')
        
        # Format the message for Slack
        message = format_slack_message(respondent_id, answers)
        
        # Send message to Slack
        if send_to_slack(message):
            return jsonify({'status': 'Notification sent'}), 200
        else:
            return jsonify({'error': 'Failed to send notification to Slack'}), 500
    return jsonify({'error': 'Invalid request method'}), 405

def format_slack_message(respondent_id, answers):
    """Format the response data into a Slack-friendly message."""
    answer_details = "\n".join([f"{ans['field']['id']}: {ans['text']}" for ans in answers if 'text' in ans])
    
    message = (
        f"*New Typeform Response*\n"
        f"Respondent ID: {respondent_id}\n"
        f"Answers:\n{answer_details}"
    )
    return message

def send_to_slack(message):
    """Send a message to the Slack channel via the webhook URL."""
    payload = {
        'text': message
    }
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return True
    except requests.exceptions.RequestException as e:
        # Log the exception (in production, use a proper logging mechanism)
        print(f"Error sending to Slack: {e}")
        return False

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)  # Adjust the port as necessary
```

**Note:** Be sure to set the `SLACK_WEBHOOK_URL` environment variable with your Slack webhook URL before running the application.
