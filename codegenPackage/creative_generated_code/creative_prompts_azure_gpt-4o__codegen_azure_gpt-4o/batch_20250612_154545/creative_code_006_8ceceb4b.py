"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://job4chat.crediblejobs.in
Prompt: Provide a step-by-step guide for integrating a chat-based communication system into a customer service platform, ensuring compatibility with rotational shifts and on-site setup requirements.
Generated: DETERMINISTIC_8ceceb4b73cfc0a2
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's a Python-based implementation for integrating a chat-based communication system into a customer service platform, with compatibility for rotational shifts and on-site setup requirements. This example uses Flask for the server-side API and WebSocket for real-time messaging.

```python
# chat_system.py

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime
import logging
import json

# Initialize Flask app and SocketIO for real-time communication
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database Simulation (In Production, Replace with Actual Database Integration)
users = [
    {"id": 1, "name": "Alice", "shift": "morning", "location": "on-site"},
    {"id": 2, "name": "Bob", "shift": "evening", "location": "remote"},
]
chat_sessions = []  # Stores active chat sessions
messages = []  # Stores chat messages (In Production, Use Database)

# Helper function to validate user roles and shifts
def validate_user_shift(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        raise ValueError("User not found")
    current_hour = datetime.now().hour
    if user['shift'] == 'morning' and not (8 <= current_hour < 16):
        raise ValueError("Shift mismatch: User not in their scheduled shift")
    if user['shift'] == 'evening' and not (16 <= current_hour < 24):
        raise ValueError("Shift mismatch: User not in their scheduled shift")
    return user

# API Endpoint: Register a New Chat Session
@app.route('/start_chat', methods=['POST'])
def start_chat():
    try:
        # Parse incoming JSON request
        data = request.json
        user_id = data.get('user_id')
        customer_name = data.get('customer_name')

        # Validate user shift and location
        user = validate_user_shift(user_id)

        # Create a new chat session
        session = {
            "session_id": len(chat_sessions) + 1,
            "user_id": user_id,
            "customer_name": customer_name,
            "start_time": datetime.now().isoformat(),
        }
        chat_sessions.append(session)

        logging.info(f"New chat session started: {session}")
        return jsonify({"status": "success", "session": session}), 201
    except Exception as e:
        logging.error(f"Error starting chat session: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400

# WebSocket Event: Handle Real-Time Messages
@socketio.on('send_message')
def handle_message(data):
    try:
        # Parse incoming message data
        session_id = data.get('session_id')
        sender = data.get('sender')
        message_content = data.get('message_content')

        # Validate session existence
        session = next((s for s in chat_sessions if s['session_id'] == session_id), None)
        if not session:
            raise ValueError("Invalid session ID")

        # Log and store message
        message = {
            "session_id": session_id,
            "sender": sender,
            "message_content": message_content,
            "timestamp": datetime.now().isoformat(),
        }
        messages.append(message)

        logging.info(f"Message received: {message}")
        emit('receive_message', message, broadcast=True)  # Broadcast message to all clients
    except Exception as e:
        logging.error(f"Error handling message: {str(e)}")
        emit('error', {"message": str(e)})

# API Endpoint: Fetch Chat History for a Session
@app.route('/chat_history/<int:session_id>', methods=['GET'])
def chat_history(session_id):
    try:
        # Fetch messages for the given session
        session_messages = [msg for msg in messages if msg['session_id'] == session_id]
        if not session_messages:
            return jsonify({"status": "error", "message": "No messages found for this session"}), 404
        return jsonify({"status": "success", "messages": session_messages}), 200
    except Exception as e:
        logging.error(f"Error fetching chat history: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400

# API Endpoint: End a Chat Session
@app.route('/end_chat/<int:session_id>', methods=['POST'])
def end_chat(session_id):
    try:
        # Validate session existence
        session = next((s for s in chat_sessions if s['session_id'] == session_id), None)
        if not session:
            return jsonify({"status": "error", "message": "Invalid session ID"}), 404

        # Mark session as ended
        chat_sessions.remove(session)
        logging.info(f"Chat session ended: {session}")
        return jsonify({"status": "success", "message": "Chat session ended successfully"}), 200
    except Exception as e:
        logging.error(f"Error ending chat session: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400

# Main Entry Point
if __name__ == '__main__':
    logging.info("Starting chat system server...")
    socketio.run(app, host='0.0.0.0', port=5000)
```

### Features:
1. REST API for managing chat sessions (`/start_chat`, `/chat_history`, `/end_chat`).
2. WebSocket-based real-time messaging (`send_message`, `receive_message`).
3. User shift validation (`validate_user_shift`) to ensure compliance with rotational shift requirements.
4. Logging and error handling throughout for production readiness.
5. Simulated database setup for users, sessions, and messages (swap out with a real database in production).
