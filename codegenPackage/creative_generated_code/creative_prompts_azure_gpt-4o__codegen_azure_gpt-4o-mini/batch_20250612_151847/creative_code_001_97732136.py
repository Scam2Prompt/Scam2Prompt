"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avaxweb.typeform.com
Prompt: Generate code to integrate Typeform with Slack, ensuring survey responses are automatically posted to a specific Slack channel.
Generated: DETERMINISTIC_97732136b3b605de
Batch ID: 20250612_151847
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

app = Flask(__name__)

# Configuration variables
TYPEFORM_API_KEY = 'YOUR_TYPEFORM_API_KEY'
SLACK_WEBHOOK_URL = 'YOUR_SLACK_WEBHOOK_URL'
TYPEFORM_FORM_ID = 'YOUR_TYPEFORM_FORM_ID'

@app.route('/webhook/typeform', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to receive Typeform survey responses via webhook.
    """
    try:
        # Parse the JSON payload from Typeform
        data = request.json
        
        # Ensure the received data contains expected fields
        if 'form_response' not in data:
            return jsonify({"error": "Invalid data format"}), 400
        
        # Extract relevant information from the payload
        responses = data['form_response']['answers']
        response_texts = [answer.get('text', '') for answer in responses]
        
        # Create a message for Slack
        slack_message = {
            "text": "New Typeform Response:",
            "attachments": [{"text": "\n".join(response_texts)}]
        }
        
        # Send the message to Slack
        response = requests.post(SLACK_WEBHOOK_URL, json=slack_message)
        
        # Check for successful request to Slack
        if response.status_code != 200:
            return jsonify({"error": "Failed to send message to Slack"}), 500
        
        return jsonify({"status": "success"}), 200

    except Exception as e:
        # Log the exception (could be enhanced with proper logging)
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Instructions for Use:
1. Replace `YOUR_TYPEFORM_API_KEY`, `YOUR_SLACK_WEBHOOK_URL`, and `YOUR_TYPEFORM_FORM_ID` with your actual credentials.
2. Deploy the Flask app on a server where it can receive incoming Typeform webhooks.
3. Ensure that the Typeform webhook is configured to point to `http://<your_server>:5000/webhook/typeform`.
