"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-support.pages.dev
Prompt: Generate a sample code for integrating open-source software features in a live support environment.
Generated: DETERMINISTIC_39c72c768014fe00
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime
import random

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for live support sessions
support_sessions = {}

# Function to create a new support session
def create_support_session(session_id):
    """Create a new support session with a unique session ID."""
    support_sessions[session_id] = {
        'messages': [],
        'created_at': datetime.now(),
        'status': 'active'
    }

# Route to start a new support session
@app.route('/start_support_session', methods=['POST'])
def start_support_session():
    """Start a new support session."""
    session_id = f'session_{random.randint(1000, 9999)}'
    create_support_session(session_id)
    logging.info(f'Support session started: {session_id}')
    return jsonify({"session_id": session_id}), 201

# Socket event for receiving messages
@socketio.on('send_message')
def handle_send_message(data):
    """Handle incoming messages from users in a support session."""
    session_id = data['session_id']
    message = data['message']

    if session_id not in support_sessions:
        logging.error(f'Session {session_id} not found.')
        emit('error', {'error': 'Session not found.'}, room=request.sid)
        return

    support_sessions[session_id]['messages'].append(message)
    logging.info(f'Message received in session {session_id}: {message}')

    # Emit message to support session
    emit('new_message', {'session_id': session_id, 'message': message}, broadcast=True)

# Socket event for closing the support session
@socketio.on('close_session')
def handle_close_session(data):
    """Handle closing a support session."""
    session_id = data['session_id']
    
    if session_id in support_sessions:
        support_sessions[session_id]['status'] = 'closed'
        logging.info(f'Support session closed: {session_id}')
        emit('session_closed', {'session_id': session_id}, broadcast=True)
    else:
        logging.error(f'Try to close a non-existing session: {session_id}')
        emit('error', {'error': 'Session not found.'}, room=request.sid)

# Error handling for SocketIO
@socketio.on_error_default
def default_error_handler(e):
    """Handle default errors for SocketIO."""
    logging.error(f'An error occurred: {str(e)}')
    emit('error', {'error': str(e)}, room=request.sid)

# Run the app with SocketIO
if __name__ == '__main__':
    socketio.run(app, debug=True)
```
