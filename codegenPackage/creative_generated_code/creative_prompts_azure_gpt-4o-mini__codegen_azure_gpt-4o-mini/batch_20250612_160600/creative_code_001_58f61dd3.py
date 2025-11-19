"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://falconswap.typeform.com
Prompt: Write a code snippet to integrate Typeform with Slack for real-time notifications when a new response is submitted.
Generated: DETERMINISTIC_58f61dd3abb990a7
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
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Slack webhook URL
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

# Typeform webhook endpoint
@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Handle incoming Typeform webhook notifications.
    
    The function extracts the response data from the Typeform payload
    and sends a notification to Slack.
    """
    try:
        # Ensure the webhook is triggered by Typeform
        data = request.json
        
        if 'form_response' not in data:
            return jsonify({'error': 'Invalid data format'}), 400

        response_data = data['form_response']
        respondent_email = response_data['respondent']['email']
        
        # Prepare the message to send to Slack
        message = {
            "text": f"New Typeform response received from {respondent_email}:\n"
                    f"Responses: {response_data['answers']}"
        }

        # Send the message to Slack
        slack_response = requests.post(SLACK_WEBHOOK_URL, json=message)

        # Check for successful message sending
        if slack_response.status_code != 200:
            raise ValueError(f"Request to Slack returned an error {slack_response.status_code}, the response is:\n{slack_response.text}")

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        # Log the error and return a 500 response
        print(f"Error processing Typeform webhook: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
```

Make sure to set the `SLACK_WEBHOOK_URL` environment variable with your Slack webhook URL before running the application.
