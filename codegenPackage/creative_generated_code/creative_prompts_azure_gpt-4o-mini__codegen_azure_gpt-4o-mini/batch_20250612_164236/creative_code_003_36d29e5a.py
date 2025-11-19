"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-website.vercel.app
Prompt: Explain how to set up a custom bridge server for WalletConnect and the benefits of doing so.
Generated: DETERMINISTIC_36d29e5ac61854c1
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Custom Bridge Server for WalletConnect

This code demonstrates how to set up a simple custom bridge server for WalletConnect using Flask.
The server will handle connection requests and subscribe to events.

Requirements:
- Flask
- Flask-SocketIO
- Eventlet

Install required packages:
pip install Flask Flask-SocketIO eventlet

Run the server:
python custom_bridge_server.py
"""

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import eventlet

# Create a Flask application
app = Flask(__name__)
# Initialize SocketIO with the Flask app
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage for connected clients
clients = {}

@app.route('/session/request', methods=['POST'])
def session_request():
    """Handle session requests from clients."""
    # Get the request data
    data = request.json
    if not data or 'peerId' not in data:
        return jsonify({"error": "Invalid session request"}), 400

    peer_id = data['peerId']
    # Register the client
    clients[peer_id] = request.sid
    return jsonify({"message": "Session request accepted", "peerId": peer_id}), 200

@app.route('/session/approve', methods=['POST'])
def session_approve():
    """Approve a session request."""
    data = request.json
    if not data or 'peerId' not in data or 'response' not in data:
        return jsonify({"error": "Invalid approval request"}), 400

    peer_id = data['peerId']
    response = data['response']
    if peer_id not in clients:
        return jsonify({"error": "Client not found"}), 404

    # Emit event to the client for session approval
    socketio.emit('session_approved', response, room=clients[peer_id])
    return jsonify({"message": "Session approved", "peerId": peer_id}), 200

@socketio.on('connect')
def handle_connect():
    """Handle new client connections."""
    print("Client connected:", request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnections."""
    # Remove the client from the list
    for peer_id, sid in clients.items():
        if sid == request.sid:
            del clients[peer_id]
            print("Client disconnected:", peer_id)
            break

if __name__ == '__main__':
    # Start the SocketIO server
    try:
        socketio.run(app, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting server: {e}")
```
