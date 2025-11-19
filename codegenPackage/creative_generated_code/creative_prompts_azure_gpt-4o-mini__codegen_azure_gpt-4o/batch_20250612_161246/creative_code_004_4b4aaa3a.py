"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://44-cm7.pages.dev
Prompt: Suggest an API for managing user notifications for collectible drops like Pudgy Penguins "GoldFeathers".
Generated: DETERMINISTIC_4b4aaa3a8f2ee09f
Batch ID: 20250612_161246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory data storage for notifications (for demo purposes, replace with a database in production)
notifications = {}

# Error handler for generic errors
@app.errorhandler(Exception)
def handle_exception(e):
    response = {"error": str(e)}
    return jsonify(response), 500

# Helper function to create a unique identifier for notifications
def generate_notification_id():
    return str(uuid.uuid4())

# API endpoint to create a new notification
@app.route('/notifications', methods=['POST'])
def create_notification():
    """
    Create a new user notification for collectible drops.
    Expected JSON body:
    {
        "user_id": "string",  # ID of the user to notify
        "collectible_name": "string",  # Name of the collectible (e.g., "GoldFeathers")
        "drop_time": "ISO 8601 string",  # Scheduled drop time
        "message": "string"  # Notification message
    }
    """
    try:
        data = request.get_json()
        user_id = data['user_id']
        collectible_name = data['collectible_name']
        drop_time = data['drop_time']
        message = data['message']

        # Validate drop_time format
        try:
            scheduled_time = datetime.fromisoformat(drop_time)
        except ValueError:
            return jsonify({"error": "Invalid date format for 'drop_time'. Use ISO 8601 format."}), 400

        # Create notification
        notification_id = generate_notification_id()
        notification = {
            "id": notification_id,
            "user_id": user_id,
            "collectible_name": collectible_name,
            "drop_time": scheduled_time.isoformat(),
            "message": message,
        }
        notifications[notification_id] = notification

        return jsonify({"notification": notification}), 201
    except KeyError as ke:
        return jsonify({"error": f"Missing required field: {str(ke)}"}), 400

# API endpoint to get all notifications
@app.route('/notifications', methods=['GET'])
def get_notifications():
    """
    Get all notifications.
    Optional query parameters:
    - user_id: Filter notifications by user ID.
    """
    user_id = request.args.get('user_id')
    if user_id:
        user_notifications = [
            notification for notification in notifications.values() if notification['user_id'] == user_id
        ]
        return jsonify({"notifications": user_notifications}), 200
    return jsonify({"notifications": list(notifications.values())}), 200

# API endpoint to get a specific notification by ID
@app.route('/notifications/<notification_id>', methods=['GET'])
def get_notification(notification_id):
    """
    Get notification details by ID.
    """
    notification = notifications.get(notification_id)
    if not notification:
        return jsonify({"error": "Notification not found"}), 404
    return jsonify({"notification": notification}), 200

# API endpoint to delete a notification by ID
@app.route('/notifications/<notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    """
    Delete a notification by ID.
    """
    if notification_id in notifications:
        del notifications[notification_id]
        return jsonify({"message": "Notification deleted successfully"}), 200
    return jsonify({"error": "Notification not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
