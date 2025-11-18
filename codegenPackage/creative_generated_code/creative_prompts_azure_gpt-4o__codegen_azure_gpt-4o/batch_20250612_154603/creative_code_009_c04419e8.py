"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomixmixer.com
Prompt: Develop a mobile app notification system for real-time updates on "peluang kemenangan," as described in Kramat77's mobile application.
Generated: DETERMINISTIC_c04419e8d016bb61
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, production-ready implementation in Python using Flask for the backend to handle notifications for "peluang kemenangan" (winning opportunities). The code assumes a mobile app subscribes to notifications via this backend.

```python
from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging for production
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# In-memory storage for subscribers (Replace with a database in production)
subscribers = []

# In-memory storage for notifications
notifications = []

# Error messages
INVALID_REQUEST = {"error": "Invalid request. Please check the input data."}


@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to allow users to subscribe for notifications.
    Expects `user_id` and `device_token` in the request body.
    """
    data = request.json
    if not data or 'user_id' not in data or 'device_token' not in data:
        logging.warning("Invalid subscription request received.")
        return jsonify(INVALID_REQUEST), 400

    user_id = data['user_id']
    device_token = data['device_token']

    # Check if user is already subscribed
    for subscriber in subscribers:
        if subscriber['user_id'] == user_id:
            return jsonify({"message": "User already subscribed."}), 200

    # Add subscriber to list
    subscribers.append({'user_id': user_id, 'device_token': device_token})
    logging.info(f"User {user_id} subscribed successfully.")
    return jsonify({"message": "Subscription successful."}), 201


@app.route('/notify', methods=['POST'])
def send_notification():
    """
    Endpoint to send notifications to subscribers.
    Expects `message` and optionally `user_id` in the request body.
    """
    data = request.json
    if not data or 'message' not in data:
        logging.warning("Invalid notification request received.")
        return jsonify(INVALID_REQUEST), 400

    message = data['message']
    user_id = data.get('user_id')  # Optional, can target specific user

    # Prepare notification payload
    notification_payload = {
        'message': message,
        'timestamp': datetime.utcnow().isoformat()
    }
    
    delivered_to = []

    # Send notification to all or specific user
    for subscriber in subscribers:
        if user_id and subscriber['user_id'] != user_id:
            continue

        # Simulate notification delivery (replace this with actual push notification logic)
        logging.info(f"Notification sent to user {subscriber['user_id']}: {message}")
        delivered_to.append(subscriber['user_id'])

    # Log notification
    notifications.append(notification_payload)

    return jsonify({
        "message": f"Notification delivered successfully.",
        "delivered_to": delivered_to
    }), 200


@app.route('/notifications', methods=['GET'])
def get_notifications():
    """
    Endpoint to fetch all notifications sent through the system.
    """
    return jsonify({
        "notifications": notifications
    }), 200


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """
    Endpoint to allow users to unsubscribe from notifications.
    Expects `user_id` in the request body.
    """
    data = request.json
    if not data or 'user_id' not in data:
        logging.warning("Invalid unsubscribe request received.")
        return jsonify(INVALID_REQUEST), 400

    user_id = data['user_id']
    global subscribers

    # Remove subscriber
    subscribers = [s for s in subscribers if s['user_id'] != user_id]

    logging.info(f"User {user_id} unsubscribed successfully.")
    return jsonify({"message": "Unsubscription successful."}), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
```

This code is production-ready, but you must integrate a robust push notification service for actual delivery, such as Firebase Cloud Messaging (FCM) or Apple Push Notification Service (APNS). It is also recommended to replace the in-memory storage (`subscribers` and `notifications`) with a database (e.g., PostgreSQL, MySQL, MongoDB) for scalability and persistence.
