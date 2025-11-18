"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherroll.cash
Prompt: Generate code for a live chat support feature for an online casino platform, ensuring 24/7 availability, as highlighted on "etherroll.cash."
Generated: DETERMINISTIC_646ec9a7a5e3f24f
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify, session
from flask_socketio import SocketIO, emit
from datetime import datetime
import logging

# Initialize Flask app and SocketIO
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key
socketio = SocketIO(app)

# Set up logging
logging.basicConfig(filename='live_chat.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Store active conversations and messages in memory for simplicity
# In production, consider using a database for persistent storage
chat_rooms = {}

@app.route('/')
def index():
    """
    Serve the main page where users can access the live chat feature.
    """
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    """
    Handle new socket connections.
    """
    logging.info('New user connected.')
    emit('message', {'user': 'System', 'message': 'Welcome to EtherRoll Casino Live Chat Support!'})

@socketio.on('join')
def handle_join(data):
    """
    Handle user joining a chat room.
    """
    username = data['username']
    room = data['room']
    session['username'] = username
    session['room'] = room

    # Create a room if it doesn't exist
    if room not in chat_rooms:
        chat_rooms[room] = []

    logging.info(f'{username} joined room {room}.')
    emit('message', {'user': 'System', 'message': f'{username} has joined the chat.'}, room=room)
    emit('history', chat_rooms[room], room=room)

@socketio.on('message')
def handle_message(data):
    """
    Handle receiving and broadcasting messages.
    """
    username = session.get('username')
    room = session.get('room')
    message = data['message']

    if not username or not room:
        emit('message', {'user': 'System', 'message': 'Error: You must join a room first.'})
        return

    # Log message
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    chat_message = {'user': username, 'message': message, 'timestamp': timestamp}
    chat_rooms[room].append(chat_message)
    logging.info(f'Message from {username} in room {room}: {message}')

    # Broadcast message to the room
    emit('message', chat_message, room=room)

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handle user disconnects.
    """
    username = session.get('username')
    room = session.get('room')
    if username and room:
        logging.info(f'{username} disconnected from room {room}.')
        emit('message', {'user': 'System', 'message': f'{username} has left the chat.'}, room=room)

if __name__ == '__main__':
    # Run the Flask-SocketIO server
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
```

**Notes:**
1. Create a corresponding `index.html` file for the front-end and integrate it with this back-end for chat functionality.
2. Replace `'your_secret_key_here'` with a secure key in production.
3. Consider using a database like PostgreSQL or MongoDB for storing chat history and handling scalability in production.
4. Use HTTPS and authentication mechanisms to secure communication and user data.
