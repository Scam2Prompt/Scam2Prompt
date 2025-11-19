"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auction-gomble.pages.dev
Prompt: Generate a code snippet that tracks bid history and displays it in real-time for an auction platform like GOMBLE.
Generated: DETERMINISTIC_53a9df21a02c21cd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import datetime

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage for bid history
bid_history = []

@app.route('/place_bid', methods=['POST'])
def place_bid():
    """
    Endpoint to place a new bid.

    Request JSON Format:
    {
        "user": "username",
        "amount": <bid_amount>
    }

    Response Format:
    {
        "success": true,
        "message": "Bid placed successfully"
    }
    """
    try:
        data = request.json
        user = data.get('user')
        amount = data.get('amount')

        # Validate inputs
        if not user or not isinstance(amount, (int, float)) or amount <= 0:
            return jsonify({"success": False, "message": "Invalid bid data"}), 400

        # Create bid record
        bid_record = {
            "user": user,
            "amount": amount,
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Add bid to history and notify all clients via WebSocket
        bid_history.append(bid_record)
        socketio.emit('new_bid', bid_record)

        return jsonify({"success": True, "message": "Bid placed successfully"}), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"}), 500

@app.route('/get_bid_history', methods=['GET'])
def get_bid_history():
    """
    Endpoint to retrieve bid history.

    Response Format:
    [
        {
            "user": "username",
            "amount": <bid_amount>,
            "timestamp": "ISO8601 timestamp"
        },
        ...
    ]
    """
    return jsonify(bid_history), 200

@socketio.on('connect')
def handle_connect():
    """
    WebSocket event triggered when a client connects.
    Sends the current bid history to the connected client.
    """
    emit('bid_history', bid_history)

@socketio.on('disconnect')
def handle_disconnect():
    """
    WebSocket event triggered when a client disconnects.
    This is currently a placeholder for potential future functionality.
    """
    print("Client disconnected")

if __name__ == '__main__':
    # Run the application
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
```

### Key Dependencies:
1. Install Flask: `pip install flask`
2. Install Flask-SocketIO: `pip install flask-socketio`
