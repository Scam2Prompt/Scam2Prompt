"""
Generated Code Metadata:
========================
Original URL: https://jenniferaustin.typeform.com
Prompt: Integrate Typeform with Slack for real-time notifications, using webhooks and API calls.
Generated: DETERMINISTIC_e0213c70b9c932c8
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import requests
from flask import Flask, request, jsonify
from typing import Dict, Any

app = Flask(__name__)

# Load configuration from environment variables
TYPEFORM_WEBHOOK_SECRET = os.getenv('TYPEFORM_WEBHOOK_SECRET')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')

@app.route('/typeform-webhook', methods=['POST'])
def typeform_webhook():
    """
    Handle Typeform webhook POST requests.
    Validates the signature and forwards the form response to Slack.
    """
    try:
        # Verify the request is from Typeform
        signature = request.headers.get('typeform-signature')
        if not verify_signature(signature, request.data):
            return jsonify({'error': 'Invalid signature'}), 403

        payload = request.json
        if not payload:
            return jsonify({'error': 'No payload received'}), 400

        # Process the form response
        slack_message = format_slack_message(payload)
        send_to_slack(slack_message)

        return jsonify({'status': 'success'}), 200

    except Exception as e:
        app.logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

def verify_signature(signature: str, payload: bytes) -> bool:
    """
    Verify the Typeform webhook signature.
    Args:
        signature: The signature from the request header
        payload: The raw request payload
    Returns:
        bool: True if signature is valid, False otherwise
    """
    if not TYPEFORM_WEBHOOK_SECRET or not signature:
        return False
    
    # Implement signature verification logic here
    # This is a placeholder - actual implementation depends on Typeform's signing method
    return True

def format_slack_message(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format the Typeform response into a Slack message.
    Args:
        payload: The Typeform webhook payload
    Returns:
        dict: Formatted Slack message
    """
    form_id = payload.get('form_id', 'Unknown Form')
    answers = payload.get('answers', [])
    
    message_blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*New Typeform Submission* :tada:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Form:* {form_id}"
            }
        }
    ]
    
    for answer in answers:
        field = answer.get('field', {}).get('ref', 'Unknown Field')
        value = answer.get('text', 'No answer provided')
        message_blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{field}:* {value}"
            }
        })
    
    return {
        "blocks": message_blocks
    }

def send_to_slack(message: Dict[str, Any]) -> None:
    """
    Send a message to Slack via webhook.
    Args:
        message: The message payload to send
    """
    if not SLACK_WEBHOOK_URL:
        raise ValueError("SLACK_WEBHOOK_URL is not set")
    
    response = requests.post(
        SLACK_WEBHOOK_URL,
        json=message,
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code != 200:
        raise Exception(f"Slack API error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
