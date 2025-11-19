"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: How can I implement a 24/7 support chat feature for a casino website similar to the one described on BaxBet?
Generated: DETERMINISTIC_eacfac6ae465c264
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime
import logging

# Initialize Flask app and Socket.IO
app = Flask(__name__)
socketio = SocketIO(app)

# Configure logging for production
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# In-memory storage for active chat rooms and messages (use a database for production)
CHAT_ROOMS = {}

# Error messages
ERROR_MESSAGES = {
    "room_not_found": "Chat room not found.",
    "invalid_request": "Invalid request.",
}

@app.route('/')
def index():
    """
    Health check route to verify the service is running.
    """
    return jsonify({"status": "running", "message": "Support chat is active!"}), 200

@socketio.on('connect')
def handle_connect():
    """
    Handle new client connection to the Socket.IO server.
    """
    logging.info("Client connected")
    emit('status', {'message': 'Connected to support chat.'})

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handle client disconnection from the Socket.IO server.
    """
    logging.info("Client disconnected")

@socketio.on('join')
def handle_join(data):
    """
    Handle a user joining a chat room.
    """
    try:
        room = data.get('room')
        username = data.get('username')

        # Validate input
        if not room or not username:
            emit('error', {'message': ERROR_MESSAGES["invalid_request"]})
            return
        
        join_room(room)

        # Initialize chat room if it does not exist
        if room not in CHAT_ROOMS:
            CHAT_ROOMS[room] = []

        logging.info(f"User {username} joined room {room}")
        emit('status', {'message': f'{username} joined the room.'}, room=room)
    except Exception as e:
        logging.error(f"Error joining room: {str(e)}")
        emit('error', {'message': 'An error occurred while joining the room.'})

@socketio.on('leave')
def handle_leave(data):
    """
    Handle a user leaving a chat room.
    """
    try:
        room = data.get('room')
        username = data.get('username')

        # Validate input
        if not room or not username:
            emit('error', {'message': ERROR_MESSAGES["invalid_request"]})
            return

        leave_room(room)
        logging.info(f"User {username} left room {room}")
        emit('status', {'message': f'{username} left the room.'}, room=room)
    except Exception as e:
        logging.error(f"Error leaving room: {str(e)}")
        emit('error', {'message': 'An error occurred while leaving the room.'})

@socketio.on('message')
def handle_message(data):
    """
    Handle a user sending a message to a chat room.
    """
    try:
        room = data.get('room')
        username = data.get('username')
        message = data.get('message')

        # Validate input
        if not room or not username or not message:
            emit('error', {'message': ERROR_MESSAGES["invalid_request"]})
            return

        # Save the message in the chat room (use a database for production)
        timestamp = datetime.now().isoformat()
        CHAT_ROOMS[room].append({'username': username, 'message': message, 'timestamp': timestamp})

        logging.info(f"Message from {username} in room {room}: {message}")
        emit('message', {'username': username, 'message': message, 'timestamp': timestamp}, room=room)
    except Exception as e:
        logging.error(f"Error sending message: {str(e)}")
        emit('error', {'message': 'An error occurred while sending the message.'})

@socketio.on('fetch_messages')
def fetch_messages(data):
    """
    Handle fetching all messages for a given chat room.
    """
    try:
        room = data.get('room')

        # Validate input
        if not room:
            emit('error', {'message': ERROR_MESSAGES["invalid_request"]})
            return

        # Fetch messages from the chat room
        messages = CHAT_ROOMS.get(room, [])
        emit('messages', {'messages': messages})
    except Exception as e:
        logging.error(f"Error fetching messages: {str(e)}")
        emit('error', {'message': 'An error occurred while fetching messages.'})

# Run the application
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
```
