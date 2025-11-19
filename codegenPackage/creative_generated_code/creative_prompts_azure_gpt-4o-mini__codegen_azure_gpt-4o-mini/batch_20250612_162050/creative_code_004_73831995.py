"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Illustrate how to implement a customer support chat feature for a car rental service, inspired by the 24/7 assistance provided by Rental Car Elena.
Generated: DETERMINISTIC_738319959bd9a116
Batch ID: 20250612_162050
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
import logging

# Initialize the Flask application and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for chat messages
chat_history = []

@app.route('/')
def index():
    """Render the main chat interface."""
    return 'Welcome to the Car Rental Support Chat!'

@socketio.on('send_message')
def handle_message(data):
    """
    Handle incoming chat messages.

    Args:
        data (dict): Dictionary containing 'username' and 'message'.
    """
    try:
        username = data['username']
        message = data['message']
        # Log the incoming message
        logging.info(f"Message from {username}: {message}")

        # Store the message in chat history
        chat_history.append({'username': username, 'message': message})

        # Emit the message to all connected clients
        emit('receive_message', {'username': username, 'message': message}, broadcast=True)

    except KeyError as e:
        logging.error(f"Missing key in incoming data: {e}")
        emit('error', {'error': 'Invalid message format'}, broadcast=False)

@app.route('/chat_history', methods=['GET'])
def get_chat_history():
    """Retrieve the chat history."""
    return jsonify(chat_history)

if __name__ == '__main__':
    # Start the SocketIO server
    try:
        socketio.run(app, host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"Server failed to start: {e}")
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SocketIO
``` 

This code snippet provides a basic implementation of a customer support chat feature using Flask and SocketIO, including error handling and logging for better traceability in a production environment.
