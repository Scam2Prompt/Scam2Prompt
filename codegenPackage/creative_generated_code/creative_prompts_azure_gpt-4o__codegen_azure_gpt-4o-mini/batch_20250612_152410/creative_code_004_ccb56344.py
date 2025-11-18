"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaafmall.com
Prompt: Suggest frameworks or tools for building a WhatsApp-like chat clone with features like timestamped messages and emoji reactions, as shown on kaafmall.com.
Generated: DETERMINISTIC_ccb563448fbdbebc
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for chat application
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import datetime
import json

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Store messages in-memory for demonstration purposes
messages = []

@app.route('/messages', methods=['GET'])
def get_messages():
    """
    Endpoint to retrieve all chat messages.
    Returns a JSON array of messages.
    """
    return jsonify(messages), 200

@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Endpoint to send a new chat message.
    Expects JSON with 'username', 'message', and optional 'emoji' fields.
    Broadcasts the message to all connected clients.
    """
    try:
        data = request.get_json()
        username = data['username']
        message = data['message']
        emoji = data.get('emoji', None)

        # Create a timestamp for the message
        timestamp = datetime.datetime.now().isoformat()

        # Format the message object
        message_object = {
            'username': username,
            'message': message,
            'emoji': emoji,
            'timestamp': timestamp
        }

        # Store the message
        messages.append(message_object)

        # Emit the new message to all clients
        socketio.emit('new_message', message_object)

        return jsonify(message_object), 201

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@socketio.on('connect')
def handle_connect():
    """
    Handle client connection event.
    Sends a welcome message to the newly connected client.
    """
    emit('message', {'msg': 'Welcome to the chat!'})

if __name__ == '__main__':
    # Run the application with debug mode
    socketio.run(app, debug=True)
```
