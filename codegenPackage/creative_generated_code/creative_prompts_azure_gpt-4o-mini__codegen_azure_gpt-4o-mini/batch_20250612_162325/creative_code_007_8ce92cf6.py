"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Describe how to set up a notification system for users to receive updates on the TG.Casino presale and token launch using a webhook.
Generated: DETERMINISTIC_8ce92cf6459be922
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for user subscriptions (for demonstration purposes)
subscriptions = {}

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to subscribe a user to notifications.
    Expects JSON data with 'user_id' and 'webhook_url'.
    """
    try:
        data = request.json
        user_id = data['user_id']
        webhook_url = data['webhook_url']

        if user_id in subscriptions:
            return jsonify({'message': 'User already subscribed'}), 400

        # Save subscription
        subscriptions[user_id] = webhook_url
        logging.info(f"User {user_id} subscribed successfully.")
        return jsonify({'message': 'Subscription successful'}), 201

    except KeyError as e:
        logging.error(f"Key error: {e}")
        return jsonify({'error': 'Missing required field'}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An error occurred during subscription'}), 500

@app.route('/notify', methods=['POST'])
def notify():
    """
    Endpoint to send notifications to subscribed users.
    Expects JSON data with 'message'.
    """
    try:
        data = request.json
        message = data['message']

        if not message:
            return jsonify({'error': 'Message cannot be empty'}), 400

        for user_id, webhook_url in subscriptions.items():
            response = send_notification(webhook_url, message)
            logging.info(f"Notification sent to {user_id} with response: {response.status_code}")

        return jsonify({'message': 'Notifications sent successfully'}), 200

    except KeyError as e:
        logging.error(f"Key error: {e}")
        return jsonify({'error': 'Missing required field'}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An error occurred during notification'}), 500

def send_notification(webhook_url, message):
    """
    Helper function to send a notification to a user's webhook.
    Uses a POST request to the specified webhook URL.
    """
    import requests

    payload = {'message': message}
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response
    except requests.RequestException as e:
        logging.error(f"Failed to send notification to {webhook_url}: {e}")
        return None

if __name__ == '__main__':
    app.run(port=5000)
```

Make sure to install Flask and Requests libraries if you haven't:

```bash
pip install Flask requests
``` 

This code sets up a simple notification system using Flask, allowing users to subscribe to updates and receive notifications via webhooks.
