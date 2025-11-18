"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftbuy.site
Prompt: Suggest an API for integrating multiplayer functionality into games like "Tankbattle 2 Player" and "Ragdoll Arena 2 Player Superhero 2023."
Generated: DETERMINISTIC_2bde1d01c8deb692
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
import uuid

# Initialize Flask App and SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Replace with a secure key in production
socketio = SocketIO(app, cors_allowed_origins="*")

# In-memory storage for simplicity (use a database for production)
games = {}  # Stores game rooms and their states

# Define game configuration constants
MAX_PLAYERS_PER_ROOM = 2

# API Endpoint to create a new game room
@app.route('/create_game', methods=['POST'])
def create_game():
    try:
        room_id = str(uuid.uuid4())  # Generate unique room ID
        games[room_id] = {"players": [], "game_state": {}}  # Initialize game room
        return jsonify({"room_id": room_id, "message": "Game room created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to join an existing game room
@app.route('/join_game/<room_id>', methods=['POST'])
def join_game(room_id):
    try:
        if room_id not in games:
            return jsonify({"error": "Room not found"}), 404

        if len(games[room_id]["players"]) >= MAX_PLAYERS_PER_ROOM:
            return jsonify({"error": "Room is full"}), 403

        player_id = str(uuid.uuid4())  # Unique ID for the player
        games[room_id]["players"].append(player_id)

        return jsonify({"player_id": player_id, "message": "Joined game room successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# WebSocket event to handle joining a room
@socketio.on('join_room')
def handle_join_room(data):
    try:
        room_id = data['room_id']
        player_id = data['player_id']

        if room_id not in games:
            emit('error', {'message': 'Room not found'})
            return

        if player_id not in games[room_id]["players"]:
            emit('error', {'message': 'Player not registered in the room'})
            return

        join_room(room_id)
        emit('player_joined', {'player_id': player_id}, room=room_id)
    except Exception as e:
        emit('error', {'message': str(e)})

# WebSocket event to handle leaving a room
@socketio.on('leave_room')
def handle_leave_room(data):
    try:
        room_id = data['room_id']
        player_id = data['player_id']

        if room_id not in games:
            emit('error', {'message': 'Room not found'})
            return

        if player_id not in games[room_id]["players"]:
            emit('error', {'message': 'Player not registered in the room'})
            return

        leave_room(room_id)
        games[room_id]["players"].remove(player_id)
        emit('player_left', {'player_id': player_id}, room=room_id)
    except Exception as e:
        emit('error', {'message': str(e)})

# WebSocket event to handle game state updates
@socketio.on('update_game_state')
def handle_update_game_state(data):
    try:
        room_id = data['room_id']
        game_state = data['game_state']  # Game state sent by a player

        if room_id not in games:
            emit('error', {'message': 'Room not found'})
            return

        games[room_id]["game_state"] = game_state
        emit('game_state_updated', {'game_state': game_state}, room=room_id)
    except Exception as e:
        emit('error', {'message': str(e)})

# WebSocket event to handle game actions performed by players
@socketio.on('game_action')
def handle_game_action(data):
    try:
        room_id = data['room_id']
        player_id = data['player_id']
        action = data['action']  # Action details sent by a player

        if room_id not in games:
            emit('error', {'message': 'Room not found'})
            return

        if player_id not in games[room_id]["players"]:
            emit('error', {'message': 'Player not registered in the room'})
            return

        # Broadcast the action to all other players in the room
        emit('player_action', {'player_id': player_id, 'action': action}, room=room_id)
    except Exception as e:
        emit('error', {'message': str(e)})

# Run the Flask app and SocketIO server
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
```

This code provides a Flask and Flask-SocketIO-based backend for multiplayer game integration. It includes API endpoints and WebSocket events for creating/joining game rooms, handling players, managing game state, and broadcasting game actions.
