"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinetictokenform.typeform.com
Prompt: Write code to integrate Typeform with Slack using Typeform's API to send form responses directly to a Slack channel.
Generated: DETERMINISTIC_b2998c5b1dadb708
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

app = Flask(__name__)

# Configuration for Typeform and Slack
TYPEFORM_SECRET = 'YOUR_TYPEFORM_SECRET'  # Replace with your Typeform secret
SLACK_WEBHOOK_URL = 'YOUR_SLACK_WEBHOOK_URL'  # Replace with your Slack webhook URL

def send_to_slack(form_response):
    """
    Sends the Typeform response to the specified Slack channel.

    :param form_response: The response data from the Typeform webhook
    :return: Response from the Slack API
    """
    # Construct the message payload to send to Slack
    message_payload = {
        "text": "New Typeform response received!",
        "attachments": [
            {
                "text": json.dumps(form_response, indent=2),
                "color": "#36a64f"
            }
        ]
    }

    # Send the message to Slack using a POST request
    response = requests.post(SLACK_WEBHOOK_URL, json=message_payload)

    # Raise an exception if the Slack API returns an error
    if response.status_code != 200:
        raise ValueError(f'Failed to send message to Slack: {response.status_code}, {response.text}')

@app.route('/webhook/typeform', methods=['POST'])
def typeform_webhook():
    """
    Endpoint to receive Typeform responses.

    :return: JSON response indicating success
    """
    # Check if the request is authorized by validating the Typeform secret
    if request.headers.get('Typeform-Webhook-Secret') != TYPEFORM_SECRET:
        return jsonify({"error": "Unauthorized"}), 403

    # Get the JSON data from the request
    form_response = request.json

    # Send the response to Slack
    try:
        send_to_slack(form_response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(port=5000)
```

### Instructions to Run the Code
1. Make sure you have `Flask` and `requests` installed. You can install them via pip:
   ```bash
   pip install Flask requests
   ```
2. Replace `YOUR_TYPEFORM_SECRET` and `YOUR_SLACK_WEBHOOK_URL` with your actual Typeform secret and Slack webhook URL.
3. Run the script:
   ```bash
   python your_script_name.py
   ```
4. Configure your Typeform to use the `/webhook/typeform` endpoint for sending responses.
