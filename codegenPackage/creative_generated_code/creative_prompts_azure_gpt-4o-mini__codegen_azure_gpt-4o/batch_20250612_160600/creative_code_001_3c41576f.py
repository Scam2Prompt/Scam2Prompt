"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://electrocoin.typeform.com
Prompt: Write a script to integrate Typeform with Slack for real-time notifications of new survey responses.
Generated: DETERMINISTIC_3c41576f9f5b514c
Batch ID: 20250612_160600
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
TYPEFORM_ACCESS_TOKEN = "your_typeform_access_token"
SLACK_WEBHOOK_URL = "your_slack_webhook_url"

# Helper function to send a message to Slack
def send_to_slack(message):
    try:
        payload = {"text": message}
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise exception if request failed
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")

# Route to handle Typeform webhook events
@app.route("/typeform-webhook", methods=["POST"])
def typeform_webhook():
    try:
        # Extract the payload from the request
        data = request.json
        
        # Ensure the payload is valid
        if not data or "form_response" not in data:
            return jsonify({"error": "Invalid payload"}), 400
        
        # Get form response details
        form_response = data["form_response"]
        form_id = form_response.get("form_id", "Unknown Form ID")
        answers = form_response.get("answers", [])
        
        # Format answers for Slack message
        answer_texts = [
            f"{answer['field']['type']}: {answer['text']}" if "text" in answer else str(answer)
            for answer in answers
        ]
        message = f"New response received for Form ID: {form_id}\n" + "\n".join(answer_texts)
        
        # Send to Slack
        send_to_slack(message)
        
        return jsonify({"status": "Success"}), 200
    except Exception as e:
        print(f"Error processing Typeform webhook: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Run the Flask server
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
- Replace `your_typeform_access_token` and `your_slack_webhook_url` with your actual Typeform token and Slack webhook URL.
- Deploy this script to a server with public access for Typeform webhook integration.
- Ensure your server supports HTTPS, as Typeform requires secure URLs for webhook endpoints.
