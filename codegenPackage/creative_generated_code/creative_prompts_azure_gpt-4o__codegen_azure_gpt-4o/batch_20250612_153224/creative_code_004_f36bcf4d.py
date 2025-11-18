"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: Develop a solution for hosting live and semi-live plenary sessions with simultaneous mini-sessions, including a virtual backstage feature for director communication, as described on Virtual Media Events.
Generated: DETERMINISTIC_f36bcf4d6104c561
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example solution for hosting live and semi-live plenary sessions with simultaneous mini-sessions and a virtual backstage feature for director communication. This is a simplified implementation in Python using Flask and WebSockets.

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
from threading import Lock

# Initialize Flask application
app = Flask(__name__)

# Configurations for Flask-SocketIO
app.config['SECRET_KEY'] = 'secret_key_for_sessions'
socketio = SocketIO(app, cors_allowed_origins="*")

# Thread-safe rooms lock
rooms_lock = Lock()

# Dictionary to manage active rooms
rooms = {
    "plenary_sessions": [],
    "mini_sessions": [],
    "backstage": []
}

@app.route('/')
def index():
    """
    Root endpoint to serve the main application interface.
    """
    return render_template('index.html')

@app.route('/create_room', methods=['POST'])
def create_room():
    """
    Endpoint to create a new session room (plenary, mini, or backstage).
    """
    try:
        room_type = request.json.get('type')
        room_name = request.json.get('name')
        
        if room_type not in rooms:
            return jsonify({"error": "Invalid room type."}), 400
        
        with rooms_lock:
            if room_name in rooms[room_type]:
                return jsonify({"error": "Room already exists."}), 400
            rooms[room_type].append(room_name)
        
        return jsonify({"message": "Room created successfully.", "room_name": room_name}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@socketio.on('join_room')
def join_room_event(data):
    """
    WebSocket handler for users joining a room.
    """
    try:
        room_name = data.get('room_name')
        room_type = data.get('room_type')
        
        if room_type not in rooms or room_name not in rooms[room_type]:
            emit('error', {'message': 'Room does not exist.'})
            return
        
        join_room(room_name)
        emit('message', {'message': f'User joined {room_name}.'}, to=room_name)
    except Exception as e:
        emit('error', {'message': str(e)})

@socketio.on('leave_room')
def leave_room_event(data):
    """
    WebSocket handler for users leaving a room.
    """
    try:
        room_name = data.get('room_name')
        leave_room(room_name)
        emit('message', {'message': f'User left {room_name}.'}, to=room_name)
    except Exception as e:
        emit('error', {'message': str(e)})

@socketio.on('send_message')
def send_message_event(data):
    """
    WebSocket handler for sending messages to a room.
    """
    try:
        room_name = data.get('room_name')
        message = data.get('message')
        emit('message', {'message': message}, to=room_name)
    except Exception as e:
        emit('error', {'message': str(e)})

@socketio.on('director_message')
def director_message_event(data):
    """
    WebSocket handler for director communication in the backstage.
    """
    try:
        room_name = data.get('room_name')
        message = data.get('message')
        
        # Ensure this room is a backstage room
        if room_name not in rooms['backstage']:
            emit('error', {'message': 'Room is not a backstage room.'})
            return
        
        emit('director_message', {'message': message}, to=room_name)
    except Exception as e:
        emit('error', {'message': str(e)})

@app.route('/rooms', methods=['GET'])
def get_rooms():
    """
    Endpoint to fetch all available rooms and their respective types.
    """
    return jsonify(rooms), 200

if __name__ == '__main__':
    # Run the Flask app and SocketIO server
    socketio.run(app, host='0.0.0.0', port=5000)
```

### Notes:
- The Flask-SocketIO library is used to handle WebSocket-based real-time communication.
- This code provides endpoints for creating rooms, joining and leaving rooms, and sending messages.
- The "backstage" functionality is implemented as a room type where directors can communicate with messages tagged as `director_message`.
- Error handling ensures invalid room types or non-existent rooms are managed gracefully.
- A simple locking mechanism (`rooms_lock`) ensures thread-safe management of room lists.
