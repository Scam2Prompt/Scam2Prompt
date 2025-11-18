"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goldfeathers-thentwrk.pages.dev
Prompt: Suggest tools or APIs for managing user reactions (e.g., LFGOOO, 👀🔥) on a live collectible drop page, as seen on NTWRK's Pudgy Penguins section.
Generated: DETERMINISTIC_a4acbcd83a923f77
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# In-memory storage for user reactions
user_reactions = {}

@app.route('/reactions', methods=['POST'])
def post_reaction():
    """
    Endpoint to post a user reaction for a collectible.
    Expected JSON payload: {"user_id": "string", "reaction": "string"}
    """
    try:
        data = request.get_json()

        # Validate input
        if 'user_id' not in data or 'reaction' not in data:
            return jsonify({"error": "user_id and reaction are required"}), 400

        user_id = data['user_id']
        reaction = data['reaction']

        # Store the reaction
        user_reactions.setdefault(user_id, []).append(reaction)
        
        # Emit the reaction to all connected clients
        socketio.emit('new_reaction', {'user_id': user_id, 'reaction': reaction})

        return jsonify({"message": "Reaction recorded"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/reactions/<user_id>', methods=['GET'])
def get_reactions(user_id):
    """
    Endpoint to retrieve all reactions for a specific user.
    """
    try:
        reactions = user_reactions.get(user_id, [])
        return jsonify({"user_id": user_id, "reactions": reactions}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@socketio.on('connect')
def handle_connect():
    """
    Handle a new client connection.
    """
    print("Client connected:", request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    """
    Handle a client disconnection.
    """
    print("Client disconnected:", request.sid)


if __name__ == '__main__':
    # Run the application
    socketio.run(app, debug=False, host='0.0.0.0', port=5000)
```
