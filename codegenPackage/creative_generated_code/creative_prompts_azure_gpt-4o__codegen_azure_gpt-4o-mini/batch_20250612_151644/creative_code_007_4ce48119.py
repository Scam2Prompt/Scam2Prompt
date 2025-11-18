"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerlab.org
Prompt: Suggest a library or framework to implement MinerLab's "24/7 Support" system for real-time customer queries using chatbots or live chat.
Generated: DETERMINISTIC_4ce48119b6c38ba1
Batch ID: 20250612_151644
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
from werkzeug.exceptions import BadRequest

# Initialize Flask application and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Store active support agents in a list
active_agents = []

@app.route('/api/start_chat', methods=['POST'])
def start_chat():
    """
    Endpoint to start a chat session.
    Expects a JSON payload with 'customer_id'.
    Returns a chat session ID.
    """
    try:
        data = request.get_json()
        customer_id = data.get('customer_id')

        if not customer_id:
            raise BadRequest("Missing 'customer_id' in request.")

        # Create a unique chat session ID (for simplicity using customer_id)
        chat_session_id = f"chat_{customer_id}"
        
        # Notify that a new customer has joined the chat
        socketio.emit('new_customer', {'session_id': chat_session_id, 'customer_id': customer_id})
        
        return jsonify({'session_id': chat_session_id}), 200

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

@socketio.on('join_chat')
def handle_join_chat(data):
    """
    Handle an agent joining a chat session.
    Expects 'session_id' and 'agent_id'.
    """
    agent_id = request.sid
    session_id = data.get('session_id')

    if session_id not in active_agents:
        active_agents.append(session_id)

    # Notify all participants in the session about the new agent
    emit('agent_joined', {'agent_id': agent_id}, room=session_id)

@socketio.on('send_message')
def handle_send_message(data):
    """
    Handle incoming messages from customers or agents.
    Expects 'session_id', 'sender_id', and 'message'.
    """
    session_id = data.get('session_id')
    sender_id = data.get('sender_id')
    message = data.get('message')

    if not session_id or not sender_id or not message:
        emit('error', {'error': 'Missing required fields.'}, room=request.sid)
        return

    # Broadcast the message to all participants in the session
    emit('new_message', {'sender_id': sender_id, 'message': message}, room=session_id)

@socketio.on('disconnect')
def handle_disconnect():
    """
    Handle disconnection of a customer or agent from the chat.
    """
    agent_id = request.sid
    # Remove the agent from active agents list if they disconnect
    if agent_id in active_agents:
        active_agents.remove(agent_id)
        emit('agent_left', {'agent_id': agent_id}, broadcast=True)

if __name__ == '__main__':
    # Start the SocketIO server
    socketio.run(app, debug=True)
```
