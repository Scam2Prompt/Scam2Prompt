"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://availlabs.net
Prompt: Develop a solution for live chat integration to improve communication and support for swag management, similar to the dedicated support feature mentioned on Avail Labs' website.
Generated: DETERMINISTIC_b773268a8d04883b
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import logging

# Initialize the Flask application and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure secret key
socketio = SocketIO(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory storage for active chat sessions
active_chats = {}

@app.route('/api/start_chat', methods=['POST'])
def start_chat():
    """
    API endpoint to start a new chat session.
    Expects JSON payload with 'user_id' and 'user_name'.
    Returns chat session ID.
    """
    try:
        data = request.json
        user_id = data.get('user_id')
        user_name = data.get('user_name')
        
        if not user_id or not user_name:
            return jsonify({"error": "user_id and user_name are required"}), 400
        
        chat_id = f"chat_{user_id}"  # Unique chat ID based on user_id
        active_chats[chat_id] = {'user_id': user_id, 'user_name': user_name, 'messages': []}
        
        logging.info(f"Started chat for user {user_name} with ID {chat_id}")
        return jsonify({"chat_id": chat_id}), 200

    except Exception as e:
        logging.error(f"Error starting chat: {str(e)}")
        return jsonify({"error": "Failed to start chat"}), 500

@socketio.on('send_message')
def handle_send_message(data):
    """
    Socket event to handle incoming messages.
    Expects message payload containing 'chat_id' and 'message'.
    Broadcasts the message to the chat session.
    """
    try:
        chat_id = data.get('chat_id')
        message = data.get('message')
        
        if not chat_id or not message:
            emit('error', {'error': 'chat_id and message are required'})
            return
        
        if chat_id not in active_chats:
            emit('error', {'error': 'Chat session not found'})
            return
        
        # Append message to chat history
        active_chats[chat_id]['messages'].append(message)
        
        # Broadcast message to all clients in the chat session
        socketio.emit('new_message', {'chat_id': chat_id, 'message': message}, room=chat_id)
        logging.info(f"Message sent in chat {chat_id}: {message}")

    except Exception as e:
        logging.error(f"Error handling message: {str(e)}")
        emit('error', {'error': 'Failed to send message'})

@socketio.on('join_chat')
def handle_join_chat(chat_id):
    """
    Socket event for users to join a chat session.
    Adds the user to the specified chat room.
    """
    try:
        if chat_id in active_chats:
            join_room(chat_id)
            logging.info(f"User joined chat {chat_id}")
        else:
            emit('error', {'error': 'Chat session not found'})
    except Exception as e:
        logging.error(f"Error joining chat: {str(e)}")
        emit('error', {'error': 'Failed to join chat'})

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handle user disconnection from a chat session.
    Can be used for cleanup if necessary.
    """
    logging.info("User disconnected from chat")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
```

**Notes:**
- Ensure you have Flask and Flask-SocketIO installed in your environment.
- Adjust the logging configuration and secret key for production use.
- This app uses in-memory storage for active chat sessions, which is suitable for development and testing but may need to be replaced with a persistent storage solution for production.
