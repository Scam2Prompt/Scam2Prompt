"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.faretrolley.com
Prompt: Suggest a method to integrate 24/7 customer support chat functionality into a travel booking website, referencing the support features highlighted on Faretrolley.com.
Generated: DETERMINISTIC_801a71bbe7390e00
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create Flask app and SocketIO instance
app = Flask(__name__)
socketio = SocketIO(app)

# In-memory storage for active chat sessions
active_chats = {}

@app.route('/')
def index():
    """Render the home page of the travel booking website."""
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """Handle new client connections."""
    logging.info(f"User connected: {request.sid}")
    emit('response', {'message': 'Welcome to 24/7 Customer Support!'})

@socketio.on('start_chat')
def handle_start_chat(data):
    """Start a new chat session."""
    user_id = data.get('user_id')
    chat_id = f"chat_{user_id}_{datetime.now().timestamp()}"
    active_chats[chat_id] = {'user_id': user_id, 'messages': []}
    
    logging.info(f"Started chat session: {chat_id} for user: {user_id}")
    emit('chat_started', {'chat_id': chat_id})

@socketio.on('send_message')
def handle_send_message(data):
    """Handle sending messages in a chat session."""
    chat_id = data.get('chat_id')
    message = data.get('message')

    if chat_id not in active_chats:
        logging.error(f"Attempt to send message to non-existent chat ID: {chat_id}")
        emit('error', {'message': 'Chat session not found.'})
        return

    active_chats[chat_id]['messages'].append(message)
    logging.info(f"Message sent in chat {chat_id}: {message}")
    
    # Emit the received message back to the user
    emit('receive_message', {'chat_id': chat_id, 'message': message}, broadcast=True)

@socketio.on('end_chat')
def handle_end_chat(data):
    """End a chat session."""
    chat_id = data.get('chat_id')

    if chat_id in active_chats:
        del active_chats[chat_id]
        logging.info(f"Ended chat session: {chat_id}")
        emit('chat_ended', {'chat_id': chat_id}, broadcast=True)
    else:
        logging.error(f"Attempt to end non-existent chat ID: {chat_id}")
        emit('error', {'message': 'Chat session not found.'})

if __name__ == '__main__':
    try:
        # Run the app with SocketIO
        socketio.run(app, debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"An error occurred while running the app: {e}")
```

### Installation Requirements
To run this code, ensure you have the necessary packages installed:

```bash
pip install flask flask-socketio
```

### Note
This code sets up a simple web server with Flask and SocketIO to handle customer support chat functionality. It includes error handling, logging, and maintains chat session information in memory. For production use, consider implementing persistent storage and authentication.
