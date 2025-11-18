"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Suggest a framework or library for building a customer support system with 24/7 live service, similar to Apex Capital Investment's offering.
Generated: DETERMINISTIC_845ee1ddfb4ff8b9
Batch ID: 20250612_150135
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
from datetime import datetime
import logging

# Set up logging for error handling and tracking
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app)

# Store active support sessions in a dictionary
active_sessions = {}

@app.route('/start_session', methods=['POST'])
def start_session():
    """
    API endpoint to start a new customer support session.
    Expects JSON data with 'customer_id' and 'issue_description'.
    Returns session ID or error message.
    """
    try:
        data = request.get_json()
        customer_id = data['customer_id']
        issue_description = data['issue_description']
        
        # Generate a session ID based on the current timestamp
        session_id = f"session_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # Store the session details
        active_sessions[session_id] = {
            'customer_id': customer_id,
            'issue_description': issue_description,
            'status': 'active'
        }
        logging.info(f"Started session: {session_id} for customer: {customer_id}")

        return jsonify({'session_id': session_id}), 201
    except Exception as e:
        logging.error(f"Error starting session: {e}")
        return jsonify({'error': 'Failed to start session'}), 500

@socketio.on('join_support')
def join_support(session_id):
    """
    WebSocket event to allow support agents to join a specific support session.
    """
    if session_id in active_sessions:
        emit('joined', {'message': f"You have joined session: {session_id}"}, broadcast=True)
        logging.info(f"A support agent has joined session: {session_id}")
    else:
        emit('error', {'message': 'Session not found.'})

@socketio.on('send_message')
def send_message(data):
    """
    WebSocket event to send messages between customer and support agent.
    Expects a session ID and message content.
    """
    session_id = data['session_id']
    message = data['message']
    
    if session_id in active_sessions:
        emit('receive_message', {'message': message}, room=session_id)
        logging.info(f"Message sent in session {session_id}: {message}")
    else:
        emit('error', {'message': 'Session not found.'})

if __name__ == '__main__':
    # Run the application with SocketIO
    try:
        socketio.run(app, host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"Error running the application: {e}")
```
