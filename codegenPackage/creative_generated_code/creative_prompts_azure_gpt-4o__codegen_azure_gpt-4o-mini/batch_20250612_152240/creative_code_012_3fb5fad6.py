"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Suggest methods or libraries for implementing a Voxer-like private coaching communication tool, enabling real-time interaction between users and coaches.
Generated: DETERMINISTIC_3fb5fad6dcbc60d2
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import logging

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure key
socketio = SocketIO(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Dictionary to store users and their associated sockets
connected_users = {}

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with a unique username."""
    try:
        username = request.json.get('username')
        if username in connected_users:
            return jsonify({'error': 'Username already taken'}), 400
        
        # Create a new entry for the user
        connected_users[username] = request.sid
        logging.info(f'User registered: {username}')
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        logging.error(f'Error during registration: {str(e)}')
        return jsonify({'error': 'Registration failed'}), 500

@socketio.on('message')
def handle_message(data):
    """Handle incoming messages from users and emit them to the intended recipient."""
    try:
        sender = data.get('sender')
        recipient = data.get('recipient')
        message = data.get('message')

        if recipient not in connected_users:
            emit('error', {'error': 'Recipient not found'}, room=request.sid)
            return

        # Emit the message to the intended recipient
        socketio.emit('message', {'sender': sender, 'message': message}, room=connected_users[recipient])
        logging.info(f'Message from {sender} to {recipient}: {message}')
    except Exception as e:
        logging.error(f'Error handling message: {str(e)}')

@socketio.on('disconnect')
def handle_disconnect():
    """Remove user from the connected users list on disconnect."""
    try:
        # Find the user by their socket ID and remove them
        username_to_remove = None
        for username, sid in connected_users.items():
            if sid == request.sid:
                username_to_remove = username
                break

        if username_to_remove:
            del connected_users[username_to_remove]
            logging.info(f'User disconnected: {username_to_remove}')
    except Exception as e:
        logging.error(f'Error during disconnect: {str(e)}')

if __name__ == '__main__':
    # Start the SocketIO server
    socketio.run(app, host='0.0.0.0', port=5000)
```
