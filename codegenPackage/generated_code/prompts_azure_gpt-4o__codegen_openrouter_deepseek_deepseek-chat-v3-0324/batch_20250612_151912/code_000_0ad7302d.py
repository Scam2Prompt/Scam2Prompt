"""
Generated Code Metadata:
========================
Original URL: https://jenniferaustin.typeform.com
Prompt: Write code to integrate Typeform with Slack using Typeform's API to send form responses directly to a Slack channel in real time.
Generated: DETERMINISTIC_0ad7302deae557b2
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from flask import Flask, request, jsonify
from typing import Dict, Any

app = Flask(__name__)

# Configuration - Load from environment variables
TYPEFORM_API_KEY = os.getenv('TYPEFORM_API_KEY')
SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
TYPEFORM_FORM_ID = os.getenv('TYPEFORM_FORM_ID')

# Headers for Typeform API
TYPEFORM_HEADERS = {
    'Authorization': f'Bearer {TYPEFORM_API_KEY}',
    'Content-Type': 'application/json'
}

def validate_config() -> None:
    """Validate required configuration variables."""
    required_vars = {
        'TYPEFORM_API_KEY': TYPEFORM_API_KEY,
        'SLACK_WEBHOOK_URL': SLACK_WEBHOOK_URL,
        'TYPEFORM_FORM_ID': TYPEFORM_FORM_ID
    }
    
    for var_name, var_value in required_vars.items():
        if not var_value:
            raise ValueError(f"Missing required environment variable: {var_name}")

def format_slack_message(response_data: Dict[str, Any]) -> Dict[str, Any]:
    """Format Typeform response into a Slack message."""
    answers = response_data.get('form_response', {}).get('answers', [])
    
    message_blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*New Typeform Submission*"
            }
        },
        {
            "type": "divider"
        }
    ]
    
    for answer in answers:
        field_name = answer.get('field', {}).get('title', 'Unknown Field')
        field_value = answer.get('text', answer.get('choice', {}).get('label', 'No answer provided'))
        
        message_blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{field_name}*: {field_value}"
            }
        })
    
    return {
        "blocks": message_blocks
    }

def send_to_slack(message: Dict[str, Any]) -> bool:
    """Send formatted message to Slack via webhook."""
    try:
        response = requests.post(
            SLACK_WEBHOOK_URL,
            json=message,
            timeout=10
        )
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Failed to send message to Slack: {e}")
        return False

@app.route('/webhook', methods=['POST'])
def handle_webhook() -> jsonify:
    """Handle incoming Typeform webhook."""
    try:
        data = request.json
        
        # Verify the form ID matches our expected form
        if data.get('form_response', {}).get('form_id') != TYPEFORM_FORM_ID:
            return jsonify({"status": "error", "message": "Invalid form ID"}), 400
        
        slack_message = format_slack_message(data)
        success = send_to_slack(slack_message)
        
        if success:
            return jsonify({"status": "success"})
        return jsonify({"status": "error", "message": "Failed to send to Slack"}), 500
        
    except Exception as e:
        app.logger.error(f"Error processing webhook: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    try:
        validate_config()
        app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
    except ValueError as e:
        print(f"Configuration error: {e}")
        exit(1)
```
