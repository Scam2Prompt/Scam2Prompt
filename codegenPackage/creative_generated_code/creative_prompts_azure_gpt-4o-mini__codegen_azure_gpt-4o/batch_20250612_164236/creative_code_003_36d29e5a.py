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
# WalletConnect Custom Bridge Server Setup
# This example demonstrates how to set up a custom bridge server for WalletConnect using Python and Flask.

from flask import Flask, request, jsonify
import logging
import uuid

# Initialize Flask app
app = Flask(__name__)

# Configure detailed logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

# In-memory data store for active connections (for demonstration purposes)
connections = {}

# Route: Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    A simple endpoint to check the health of the server.
    """
    return jsonify({"status": "ok", "message": "WalletConnect Bridge is running"}), 200

# Route: Establish a connection (example logic for pairing)
@app.route('/connect', methods=['POST'])
def connect():
    """
    Establishes a connection between two WalletConnect clients.
    """
    try:
        # Generate a unique session ID for the connection
        session_id = str(uuid.uuid4())

        # Parse request JSON data
        data = request.json
        peer_id = data.get('peer_id')

        if not peer_id:
            return jsonify({"error": "peer_id is required"}), 400

        # Store the session data in the connection dictionary
        connections[session_id] = {
            "peer_id": peer_id,
            "status": "connected"
        }

        logging.info(f"New connection established: {session_id} with peer_id: {peer_id}")

        # Respond with session details
        return jsonify({"session_id": session_id, "peer_id": peer_id, "status": "connected"}), 201

    except Exception as e:
        logging.error(f"Error while establishing connection: {e}")
        return jsonify({"error": "Failed to establish connection"}), 500

# Route: Disconnect a session
@app.route('/disconnect/<session_id>', methods=['DELETE'])
def disconnect(session_id):
    """
    Disconnects an active WalletConnect session.
    """
    try:
        if session_id in connections:
            # Remove connection from the store
            del connections[session_id]

            logging.info(f"Connection disconnected: {session_id}")
            return jsonify({"message": f"Session {session_id} disconnected"}), 200
        else:
            return jsonify({"error": "Session ID not found"}), 404

    except Exception as e:
        logging.error(f"Error while disconnecting session: {e}")
        return jsonify({"error": "Failed to disconnect session"}), 500

# Route: List active connections
@app.route('/connections', methods=['GET'])
def list_connections():
    """
    Lists all active WalletConnect sessions.
    """
    try:
        return jsonify({"connections": connections}), 200
    except Exception as e:
        logging.error(f"Error while listing connections: {e}")
        return jsonify({"error": "Failed to retrieve connections"}), 500

# Main entry point: Run the Flask app
if __name__ == '__main__':
    """
    Starts the Flask server. Uses default HTTP port 5000.
    """
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### **Key Notes (Comments in the Code):**
- This example sets up a simple bridge server for WalletConnect using Python's Flask framework.
- The `/connect` endpoint demonstrates basic pairing logic between peers.
- Error handling is added to provide informative responses for invalid requests or unexpected failures.
- Logging is configured for monitoring the server activity.
- For production use, consider replacing the in-memory data store with a persistent database.
- Deploy the app on a secure server and use HTTPS to ensure secure communication.
