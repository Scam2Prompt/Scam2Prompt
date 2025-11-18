"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wizfairllc.com
Prompt: Suggest a method to implement real-time customer support chat functionality for Wizfair LLC's travel booking platform.
Generated: DETERMINISTIC_4599f4e4eae27206
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Real-time customer support chat implementation using Flask and Socket.IO
# This is the backend code for the chat functionality on Wizfair LLC's travel booking platform

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Enable CORS if needed for frontend integration
from flask_cors import CORS
CORS(app)

# Configure Socket.IO
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key
socketio = SocketIO(app, cors_allowed_origins="*")

# A dictionary to store active chat rooms and their participants
active_rooms = {}

# Route to test server health
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "Server is running"}), 200

# Event listener for a new client connection
@socketio.on('connect')
def handle_connect():
    print(f"Client connected: {request.sid}")

# Event listener for client disconnection
@socketio.on('disconnect')
def handle_disconnect():
    print(f"Client disconnected: {request.sid}")
    # Remove user from active_rooms if they were in a room
    for room, users in active_rooms.items():
        if request.sid in users:
            users.remove(request.sid)
            if not users:  # Clean up empty rooms
                del active_rooms[room]

# Event listener for joining a chat room
@socketio.on('join_room')
def on_join(data):
    try:
        username = data.get('username')
        room = data.get('room')
        if not username or not room:
            emit('error', {'message': 'Username and room are required'})
            return

        join_room(room)
        if room not in active_rooms:
            active_rooms[room] = []

        active_rooms[room].append(request.sid)
        emit('message', {'username': 'System', 'message': f'{username} has joined the room'}, room=room)
    except Exception as e:
        emit('error', {'message': f'Error occurred: {str(e)}'})

# Event listener for leaving a chat room
@socketio.on('leave_room')
def on_leave(data):
    try:
        username = data.get('username')
        room = data.get('room')
        if not username or not room:
            emit('error', {'message': 'Username and room are required'})
            return

        leave_room(room)
        if room in active_rooms and request.sid in active_rooms[room]:
            active_rooms[room].remove(request.sid)
            if not active_rooms[room]:  # Clean up empty rooms
                del active_rooms[room]

        emit('message', {'username': 'System', 'message': f'{username} has left the room'}, room=room)
    except Exception as e:
        emit('error', {'message': f'Error occurred: {str(e)}'})

# Event listener for handling chat messages
@socketio.on('send_message')
def handle_message(data):
    try:
        username = data.get('username')
        room = data.get('room')
        message = data.get('message')
        if not username or not room or not message:
            emit('error', {'message': 'Username, room, and message are required'})
            return

        # Broadcast the message to everyone in the room
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        emit('message', {'username': username, 'message': message, 'timestamp': timestamp}, room=room)
    except Exception as e:
        emit('error', {'message': f'Error occurred: {str(e)}'})

# Run the Flask app and Socket.IO server
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
```
