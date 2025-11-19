"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mary.finance
Prompt: How does MARY AI facilitate real-time collaboration among team members during project development?
Generated: DETERMINISTIC_8e8c0eb32a7b1555
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import logging

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize SocketIO for real-time communication
socketio = SocketIO(app, cors_allowed_origins="*")

# Set up logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dictionary to store project rooms and members
project_rooms = {}

@app.route('/')
def home():
    """
    Root route to confirm that the server is running.
    """
    return "MARY AI Collaboration Server is running."

@socketio.on('join_project')
def handle_join_project(data):
    """
    Handles a user joining a project collaboration room.
    :param data: JSON containing 'username' and 'project_id'
    """
    try:
        username = data['username']
        project_id = data['project_id']
        
        # Create the room if it doesn't exist
        if project_id not in project_rooms:
            project_rooms[project_id] = []

        # Add user to the room
        if username not in project_rooms[project_id]:
            project_rooms[project_id].append(username)
            join_room(project_id)
            emit('user_joined', {
                'message': f"{username} has joined the project.",
                'project_id': project_id,
                'members': project_rooms[project_id]
            }, room=project_id)

            logging.info(f"User {username} joined project {project_id}.")
        else:
            emit('error', {'message': f"User {username} is already in the project."}, room=request.sid)
    except KeyError as e:
        logging.error(f"Missing data for 'join_project': {str(e)}")
        emit('error', {'message': f"Invalid request data: {str(e)}"}, room=request.sid)
    except Exception as e:
        logging.error(f"Error handling join_project: {str(e)}")
        emit('error', {'message': "An unexpected error occurred."}, room=request.sid)

@socketio.on('leave_project')
def handle_leave_project(data):
    """
    Handles a user leaving a project collaboration room.
    :param data: JSON containing 'username' and 'project_id'
    """
    try:
        username = data['username']
        project_id = data['project_id']
        
        # Remove user from the room
        if project_id in project_rooms and username in project_rooms[project_id]:
            project_rooms[project_id].remove(username)
            leave_room(project_id)
            emit('user_left', {
                'message': f"{username} has left the project.",
                'project_id': project_id,
                'members': project_rooms[project_id]
            }, room=project_id)

            logging.info(f"User {username} left project {project_id}.")
        else:
            emit('error', {'message': f"User {username} is not in the project."}, room=request.sid)
    except KeyError as e:
        logging.error(f"Missing data for 'leave_project': {str(e)}")
        emit('error', {'message': f"Invalid request data: {str(e)}"}, room=request.sid)
    except Exception as e:
        logging.error(f"Error handling leave_project: {str(e)}")
        emit('error', {'message': "An unexpected error occurred."}, room=request.sid)

@socketio.on('send_message')
def handle_send_message(data):
    """
    Handles sending messages in real-time within a project room.
    :param data: JSON containing 'username', 'project_id', and 'message'
    """
    try:
        username = data['username']
        project_id = data['project_id']
        message = data['message']

        # Relay the message to all participants in the room
        emit('new_message', {
            'username': username,
            'message': message
        }, room=project_id)

        logging.info(f"Message from {username} in project {project_id}: {message}")
    except KeyError as e:
        logging.error(f"Missing data for 'send_message': {str(e)}")
        emit('error', {'message': f"Invalid request data: {str(e)}"}, room=request.sid)
    except Exception as e:
        logging.error(f"Error handling send_message: {str(e)}")
        emit('error', {'message': "An unexpected error occurred."}, room=request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handles a user disconnecting from the server.
    """
    logging.info(f"User {request.sid} disconnected.")

# Start the server
if __name__ == '__main__':
    logging.info("Starting MARY AI Collaboration Server...")
    socketio.run(app, host='0.0.0.0', port=5000)
```
