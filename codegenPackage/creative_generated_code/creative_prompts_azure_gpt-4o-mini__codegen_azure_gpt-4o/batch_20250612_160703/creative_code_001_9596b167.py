"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avaxweb.typeform.com
Prompt: How can I integrate Typeform with Slack to receive real-time notifications for new survey responses? Provide a sample code.
Generated: DETERMINISTIC_9596b16747522971
Batch ID: 20250612_160703
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
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Slack webhook URL (replace with your actual Slack webhook URL)
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# Verify that Slack webhook URL is provided
if not SLACK_WEBHOOK_URL:
    raise ValueError("Slack webhook URL is not configured. Set SLACK_WEBHOOK_URL environment variable.")

@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to handle incoming webhook requests from Typeform.
    Parses the survey response and sends a notification to Slack.
    """
    try:
        # Parse the incoming JSON payload from Typeform
        payload = request.json
        
        # Ensure payload contains 'form_response' key
        if 'form_response' not in payload:
            return jsonify({"error": "Invalid Typeform payload"}), 400
        
        form_response = payload['form_response']
        answers = form_response.get('answers', [])
        form_id = form_response.get('form_id', 'Unknown Form ID')
        form_title = form_response.get('definition', {}).get('title', 'Untitled Form')
        
        # Extract answers and format them for Slack
        response_text = f"New response received for '{form_title}' (Form ID: {form_id}):\n"
        for idx, answer in enumerate(answers, start=1):
            question = answer.get('field', {}).get('title', 'Unknown Question')
            response = answer.get('text', answer.get('choice', {}).get('label', 'No Answer'))
            response_text += f"{idx}. {question}: {response}\n"
        
        # Send the response to Slack
        slack_payload = {
            "text": response_text
        }
        slack_response = requests.post(SLACK_WEBHOOK_URL, json=slack_payload)
        
        # Check if Slack request was successful
        if slack_response.status_code != 200:
            return jsonify({"error": "Failed to send notification to Slack"}), 500
        
        return jsonify({"message": "Notification sent to Slack successfully"}), 200
    except Exception as e:
        # Log and handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)), debug=False)
```

### Notes:
1. Replace `SLACK_WEBHOOK_URL` with your actual Slack Incoming Webhook URL. It's recommended to set this as an environment variable for security purposes.
2. Ensure the Typeform webhook is correctly configured to send data to this Flask endpoint.
3. Deploy this code to a production-ready environment (e.g., AWS, Heroku, Google Cloud) and secure the endpoint to prevent unauthorized access.
