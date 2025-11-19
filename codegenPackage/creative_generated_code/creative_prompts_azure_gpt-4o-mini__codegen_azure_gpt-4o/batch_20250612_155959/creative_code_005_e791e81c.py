"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Create a sample API endpoint for sending notifications to users on a platform that allows private chats and tips, based on Lovr's functionalities.
Generated: DETERMINISTIC_e791e81c5ad9a2d3
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock database storage for users and notifications
users = {
    1: {"username": "Alice"},
    2: {"username": "Bob"}
}

notifications = []

# Function to send notification
def send_notification(user_id, message):
    """
    Sends a notification to a user if the user exists.

    Args:
        user_id (int): The ID of the user to send the notification to.
        message (str): The notification message.

    Returns:
        dict: A success or error response.
    """
    if user_id in users:
        notification = {
            "user_id": user_id,
            "username": users[user_id]["username"],
            "message": message
        }
        notifications.append(notification)
        return {"success": True, "notification": notification}
    else:
        return {"success": False, "error": f"User with ID {user_id} not found."}

@app.route('/send-notification', methods=['POST'])
def send_notification_endpoint():
    """
    API endpoint to send a notification to a user.
    
    Expects a JSON payload with:
    - 'user_id' (int): The ID of the user to send the notification to.
    - 'message' (str): The notification message.
    
    Returns:
        JSON response indicating success or failure.
    """
    try:
        # Parse and validate request data
        data = request.get_json()
        if not data or 'user_id' not in data or 'message' not in data:
            return jsonify({"success": False, "error": "Invalid request payload."}), 400
        
        user_id = data['user_id']
        message = data['message']

        # Send notification
        result = send_notification(user_id, message)
        if result["success"]:
            return jsonify(result), 200
        else:
            return jsonify(result), 404
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Error while sending notification: {e}")
        return jsonify({"success": False, "error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
```
