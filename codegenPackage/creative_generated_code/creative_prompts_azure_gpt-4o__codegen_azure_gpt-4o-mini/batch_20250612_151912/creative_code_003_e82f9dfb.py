"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenforms.typeform.com
Prompt: Write a script to connect Typeform with Slack to send notifications whenever a new form response is submitted.
Generated: DETERMINISTIC_e82f9dfb6283fe62
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

# Set your Typeform and Slack API tokens as environment variables
TYPEFORM_API_KEY = os.getenv('TYPEFORM_API_KEY')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
TYPEFORM_FORM_ID = os.getenv('TYPEFORM_FORM_ID')

@app.route('/webhook/typeform', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to receive Typeform webhook notifications.
    """
    try:
        # Get the JSON data sent by Typeform
        data = request.json
        
        # Verify that the form ID matches
        if data['form_response']['form_id'] != TYPEFORM_FORM_ID:
            return jsonify({'status': 'ignored', 'message': 'Form ID does not match'}), 200

        # Prepare a message for Slack
        responses = data['form_response']['answers']
        message = "New Typeform Response:\n"
        
        for idx, response in enumerate(responses):
            message += f"Q{idx + 1}: {response.get('text', response.get('boolean', response.get('number', '')))}\n"

        # Send the message to Slack
        response = requests.post(SLACK_WEBHOOK_URL, json={'text': message})

        # Check for successful Slack response
        if response.status_code != 200:
            return jsonify({'status': 'error', 'message': 'Failed to send message to Slack'}), 500
        
        return jsonify({'status': 'success', 'message': 'Notification sent to Slack'}), 200

    except Exception as e:
        # Log the error for debugging
        print(f"Error: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(port=5000)
```

### Environment Variable Setup
Make sure to set the following environment variables before running the script:
- `TYPEFORM_API_KEY`: Your Typeform API key.
- `SLACK_WEBHOOK_URL`: Your Slack incoming webhook URL.
- `TYPEFORM_FORM_ID`: The ID of the Typeform you want to receive responses from.
