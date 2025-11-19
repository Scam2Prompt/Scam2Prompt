"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apello.gg
Prompt: How can I set up a webhook to receive notifications for new Gmail messages using Google Cloud Functions?
Generated: DETERMINISTIC_a0b4aac6a6d6e260
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import base64
import os
from flask import Flask, request, jsonify
from google.auth import jwt
from google.cloud import pubsub_v1

# Initialize Flask app
app = Flask(__name__)

# Google Cloud Pub/Sub configuration
PROJECT_ID = os.environ.get('GCP_PROJECT_ID')
SUBSCRIPTION_ID = os.environ.get('GCP_SUBSCRIPTION_ID')
PUBSUB_CLIENT = pubsub_v1.SubscriberClient()
SUBSCRIPTION_PATH = PUBSUB_CLIENT.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def process_gmail_message(data):
    """
    Process the incoming Gmail message data.
    """
    # Decode the message from base64
    try:
        message = json.loads(base64.b64decode(data['message']['data']).decode('utf-8'))
        print("Received message: ", message)
        
        # Add your logic to handle the Gmail message here
        # For example: save to database, trigger other workflows, etc.
        
    except Exception as e:
        print(f"Error processing message: {e}")

@app.route('/', methods=['POST'])
def webhook():
    """
    Handle incoming webhook notifications from Google.
    """
    try:
        # Verify the request is from Google
        if 'X-Goog-Resource-State' not in request.headers:
            return jsonify({"error": "Unauthorized request"}), 403
        
        # Parse the request data
        data = request.get_json()

        # Process the incoming message
        process_gmail_message(data)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Error in webhook handler: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

def main():
    """
    Main entry point for the Cloud Function.
    """
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == '__main__':
    main()
```

Make sure to set the environment variables `GCP_PROJECT_ID` and `GCP_SUBSCRIPTION_ID` in your Google Cloud Function environment. The function listens for incoming POST requests, verifies the request, processes the Gmail message, and handles any errors gracefully.
