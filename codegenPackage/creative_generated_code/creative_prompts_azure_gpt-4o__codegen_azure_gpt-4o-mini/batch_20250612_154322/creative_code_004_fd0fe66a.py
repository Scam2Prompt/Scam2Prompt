"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Suggest tools or libraries for real-time communication and coordination between service centers in multiple locations, such as Dysnix's centers in Lviv and Vinnytsia.
Generated: DETERMINISTIC_fd0fe66a74686dc3
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Real-time Communication and Coordination Tool for Service Centers

This script provides a basic framework for establishing real-time communication
between service centers located in different locations, such as Lviv and Vinnytsia.
It utilizes WebSocket for real-time messaging and a simple REST API for coordination.

Requirements:
- Flask
- Flask-SocketIO

Run the Flask application to start the server.
"""

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
socketio = SocketIO(app)

# In-memory storage for service center messages
messages = []

@app.route('/api/message', methods=['POST'])
def send_message():
    """
    API endpoint to send a message between service centers.

    Request body should contain:
    - 'sender': The name of the service center sending the message
    - 'receiver': The name of the service center receiving the message
    - 'content': The content of the message
    """
    try:
        data = request.json
        sender = data['sender']
        receiver = data['receiver']
        content = data['content']
        
        # Save the message to the in-memory storage
        messages.append({'sender': sender, 'receiver': receiver, 'content': content})
        
        # Emit message to the specified receiver
        socketio.emit('new_message', {'sender': sender, 'content': content}, room=receiver)
        
        return jsonify({'status': 'success', 'message': 'Message sent successfully'}), 200
    except KeyError as e:
        logging.error(f'Missing key in request data: {e}')
        return jsonify({'status': 'error', 'message': 'Missing key in request data'}), 400
    except Exception as e:
        logging.error(f'Error sending message: {e}')
        return jsonify({'status': 'error', 'message': 'An error occurred while sending the message'}), 500

@socketio.on('connect')
def handle_connect():
    """
    Handle new socket connection.
    """
    logging.info('A service center has connected.')

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handle socket disconnection.
    """
    logging.info('A service center has disconnected.')

@socketio.on('register')
def handle_register(data):
    """
    Handle registration of service centers for real-time communication.

    Request data should contain:
    - 'center_name': The name of the service center registering for messages.
    """
    try:
        center_name = data['center_name']
        join_room(center_name)  # Join a room named after the center
        logging.info(f'Service center {center_name} has registered for messages.')
    except KeyError as e:
        logging.error(f'Missing key in registration data: {e}')
    except Exception as e:
        logging.error(f'Error during registration: {e}')

if __name__ == '__main__':
    # Run the application with SocketIO
    socketio.run(app, host='0.0.0.0', port=5000)
```
