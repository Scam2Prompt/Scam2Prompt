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
import requests
import json
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Configuration variables (replace with actual values)
TYPEFORM_API_KEY = 'your_typeform_api_key'
TYPEFORM_FORM_ID = 'your_form_id'
SLACK_WEBHOOK_URL = 'your_slack_webhook_url'

@app.route('/typeform-webhook', methods=['POST'])
def handle_typeform_submission():
    """
    Endpoint to handle incoming Typeform webhook requests.
    Sends a notification to Slack for each new form submission.
    """
    try:
        # Parse the incoming JSON payload from Typeform
        data = request.json
        if not data or 'form_response' not in data:
            return jsonify({'error': 'Invalid payload'}), 400

        # Extract form submission details
        form_response = data['form_response']
        answers = form_response.get('answers', [])
        submitted_at = form_response.get('submitted_at', 'N/A')
        form_id = form_response.get('form_id', 'N/A')

        # Format the Slack message
        slack_message = {
            "text": "New Typeform Submission Received!",
            "attachments": [
                {
                    "title": f"Form ID: {form_id}",
                    "fields": [
                        {"title": "Submitted At", "value": submitted_at, "short": True},
                        *[
                            {"title": answer.get('field', {}).get('title', 'Unknown'),
                             "value": answer.get('text', 'No answer provided'),
                             "short": False}
                            for answer in answers
                        ]
                    ],
                }
            ],
        }

        # Send the notification to Slack
        slack_response = requests.post(
            SLACK_WEBHOOK_URL,
            data=json.dumps(slack_message),
            headers={'Content-Type': 'application/json'}
        )

        # Check response from Slack
        if slack_response.status_code != 200:
            return jsonify({'error': 'Failed to send Slack notification'}), 500

        return jsonify({'message': 'Notification sent successfully'}), 200

    except Exception as e:
        # Handle unexpected exceptions
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(port=5000, debug=True)
```

**Note:**
1. Replace `your_typeform_api_key`, `your_form_id`, and `your_slack_webhook_url` with actual values.
2. Ensure that webhook URL endpoints are configured both in Typeform and Slack.
3. For production environments, use HTTPS and secure API keys properly.
