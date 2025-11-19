"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonicolab.com
Prompt: Illustrate how to implement a 24/7 support chat feature for a travel website, taking cues from the dedicated support team at Soniclabs.
Generated: DETERMINISTIC_87785358d6f799de
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from threading import Lock

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
thread_lock = Lock()

# Store active users and messages
active_users = {}
messages = []

# Function to broadcast messages to all connected clients
def send_message_to_all(message):
    with thread_lock:
        socketio.emit('chat_message', message)

# Endpoint for user connection
@app.route('/connect', methods=['POST'])
def connect_user():
    try:
        user_id = request.json.get('user_id')
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
        
        active_users[user_id] = True
        return jsonify({'status': 'connected'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Socket event for receiving messages
@socketio.on('send_message')
def handle_send_message(data):
    try:
        user_id = data.get('user_id')
        message = data.get('message')

        if not user_id or not message:
            emit('error', {'error': 'User ID and message are required'})
            return

        # Save the message
        messages.append({'user_id': user_id, 'message': message})
        send_message_to_all({'user_id': user_id, 'message': message})
    except Exception as e:
        emit('error', {'error': str(e)})

# Socket event for user disconnect
@socketio.on('disconnect')
def handle_disconnect(data):
    try:
        user_id = data.get('user_id')
        if user_id in active_users:
            del active_users[user_id]
            emit('user_disconnected', {'user_id': user_id}, broadcast=True)
    except Exception as e:
        print(f"Error on disconnect: {str(e)}")

# Endpoint for retrieving chat history
@app.route('/chat_history', methods=['GET'])
def get_chat_history():
    try:
        return jsonify(messages), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    socketio.run(app, debug=False)
```

This code implements a simple 24/7 support chat feature using Flask and Flask-SocketIO. It includes endpoints for connecting users, handling message sending and receiving, disconnecting users, and retrieving chat history. Proper error handling and basic user management are integrated as well.
