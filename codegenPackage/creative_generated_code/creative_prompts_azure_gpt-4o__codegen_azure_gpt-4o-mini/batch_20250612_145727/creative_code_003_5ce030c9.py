"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Write an API for a live chat and notification system that supports private messaging and real-time updates, mimicking the Lovr platform's features.
Generated: DETERMINISTIC_5ce030c951040792
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from threading import Lock
import logging

# Initialize Flask app and SocketIO
app = Flask(__name__)
CORS(app)  # Enable CORS for all domains
socketio = SocketIO(app, cors_allowed_origins="*")

# Set up logging
logging.basicConfig(level=logging.INFO)

# Store connected users and messages in memory for simplicity
connected_users = {}
message_history = []
lock = Lock()

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with a unique username."""
    username = request.json.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    with lock:
        if username in connected_users:
            return jsonify({"error": "Username already taken"}), 400
        connected_users[username] = request.sid
    
    logging.info(f"User registered: {username}")
    return jsonify({"message": "User registered successfully"}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    """Retrieve the message history."""
    return jsonify(message_history), 200

@socketio.on('message')
def handle_message(data):
    """Handle incoming messages from users."""
    username = data.get('username')
    message = data.get('message')

    if not username or not message:
        emit('error', {'error': 'Username and message are required'})
        return

    # Store the message in history
    with lock:
        message_history.append({'username': username, 'message': message})

    # Emit the message to all connected clients
    socketio.emit('message', {'username': username, 'message': message})

@app.route('/private_message', methods=['POST'])
def send_private_message():
    """Send a private message to a specific user."""
    sender = request.json.get('sender')
    recipient = request.json.get('recipient')
    message = request.json.get('message')

    if not all([sender, recipient, message]):
        return jsonify({"error": "Sender, recipient and message are required"}), 400

    if recipient not in connected_users:
        return jsonify({"error": "Recipient not found"}), 404

    # Emit the private message to the recipient
    socketio.emit('private_message', {'sender': sender, 'message': message}, room=connected_users[recipient])
    return jsonify({"message": "Private message sent successfully"}), 200

@socketio.on('connect')
def handle_connect():
    """Handle new user connections."""
    logging.info(f"User connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    """Handle user disconnections."""
    username_to_remove = None
    for username, sid in connected_users.items():
        if sid == request.sid:
            username_to_remove = username
            break

    if username_to_remove:
        with lock:
            connected_users.pop(username_to_remove)
        logging.info(f"User disconnected: {username_to_remove}")

if __name__ == '__main__':
    # Start the Flask application with SocketIO
    socketio.run(app, debug=True)
```
