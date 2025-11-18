"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tronlink.at
Prompt: Suggest a library or framework to implement a live chat feature for customer support on an online gambling platform, referencing VSO777's use of WhatsApp, Telegram, and Facebook.
Generated: DETERMINISTIC_2ed1cbdcbebb3351
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import logging
import os

# Initialize Flask app and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your_secret_key'
socketio = SocketIO(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Dictionary to hold current active users
active_users = {}

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user for the chat.
    Expects JSON with 'username' field.
    """
    data = request.get_json()
    username = data.get('username')

    if not username:
        logging.error("Username is required.")
        return jsonify({'error': 'Username is required.'}), 400

    active_users[username] = request.sid
    logging.info(f"User {username} registered with ID {request.sid}.")
    return jsonify({'message': f'User {username} registered successfully.'}), 200

@socketio.on('send_message')
def handle_send_message(data):
    """
    Handle incoming messages from users.
    Expects data with 'username' and 'message' fields.
    """
    username = data.get('username')
    message = data.get('message')

    if not username or not message:
        logging.error("Username and message are required.")
        emit('message_response', {'error': 'Username and message are required.'})
        return

    logging.info(f"Message from {username}: {message}")
    emit('message_response', {'username': username, 'message': message}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handle user disconnection.
    """
    for username, sid in active_users.items():
        if sid == request.sid:
            logging.info(f"User {username} disconnected.")
            del active_users[username]
            break

@app.errorhandler(500)
def internal_error(error):
    """
    Handle internal server errors.
    """
    logging.error(f"Internal error: {error}")
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the application with SocketIO
    socketio.run(app, host='0.0.0.0', port=5000)
```
