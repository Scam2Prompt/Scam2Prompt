"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rembytservis02.ru
Prompt: Illustrate how to implement a notification system in a mobile app that alerts users when a technician is on their way to evaluate their used electronics, based on the service model described.
Generated: DETERMINISTIC_7fb06e131ca1f9b4
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation of the notification system in Python using Flask and Firebase Cloud Messaging (FCM) for sending push notifications. This assumes the mobile app integrates with Firebase SDK for receiving notifications.

```python
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import messaging, credentials

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
# Replace 'path/to/serviceAccountKey.json' with your Firebase service account key file
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Endpoint to send notification
@app.route('/send_notification', methods=['POST'])
def send_notification():
    """
    Send a notification to the user when a technician is on their way.
    Expecting a JSON body with 'user_token', 'technician_name', and 'eta'.
    """
    try:
        # Parse request data
        data = request.get_json()
        user_token = data.get('user_token')  # Firebase device token of the user
        technician_name = data.get('technician_name')  # Name of the technician
        eta = data.get('eta')  # Estimated time of arrival (e.g., "15 minutes")

        # Validate required fields
        if not user_token or not technician_name or not eta:
            return jsonify({'error': 'Missing required fields'}), 400

        # Create notification message
        notification = messaging.Notification(
            title="Technician is on the way!",
            body=f"{technician_name} will arrive in {eta}.",
        )

        # Send message via FCM
        message = messaging.Message(
            notification=notification,
            token=user_token,
        )
        response = messaging.send(message)

        # Return success response
        return jsonify({'message': 'Notification sent successfully!', 'response_id': response}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500


# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint to verify server status.
    """
    return jsonify({'status': 'OK'}), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Notes:
- Replace `path/to/serviceAccountKey.json` with the path to your Firebase service account JSON file.
- Ensure the Firebase project is correctly linked to your mobile app and the FCM SDK is integrated.
- For a production-ready deployment, disable `debug` mode and consider using a WSGI server like Gunicorn or uWSGI to serve the Flask app.
