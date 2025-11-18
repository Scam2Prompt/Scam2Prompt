"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://private-gomble.pages.dev
Prompt: Recommend APIs or libraries for creating competitive multiplayer game features, such as tracking whose balloon flies higher, as described in GOMBLE's game concept.
Generated: DETERMINISTIC_f8d076e15fca90ef
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for player data
players = {}

# Error handling for player not found
class PlayerNotFoundError(Exception):
    pass

# Endpoint to register a new player
@app.route('/register', methods=['POST'])
def register_player():
    """Register a new player and assign a unique ID."""
    player_id = str(random.randint(1000, 9999))  # Generate a random ID
    player_name = request.json.get('name')
    if not player_name:
        return jsonify({"error": "Player name is required"}), 400
    players[player_id] = {'name': player_name, 'height': 0}
    return jsonify({"player_id": player_id, "message": "Player registered successfully"}), 201

# Endpoint to update balloon height for a player
@app.route('/update_height/<player_id>', methods=['POST'])
def update_height(player_id):
    """Update the balloon height for the specified player."""
    if player_id not in players:
        raise PlayerNotFoundError(f"Player with ID {player_id} not found.")
    
    height = request.json.get('height')
    if height is None or height < 0:
        return jsonify({"error": "Height must be a non-negative number"}), 400
        
    players[player_id]['height'] = height
    return jsonify({"message": "Height updated successfully"}), 200

# Endpoint to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    """Return the current leaderboard based on balloon heights."""
    sorted_players = sorted(players.items(), key=lambda item: item[1]['height'], reverse=True)
    leaderboard_data = [{"player_id": pid, "name": pdata['name'], "height": pdata['height']} for pid, pdata in sorted_players]
    return jsonify(leaderboard_data), 200

# Error handling for player-related errors
@app.errorhandler(PlayerNotFoundError)
def handle_player_not_found(error):
    """Return a not found error message for players."""
    return jsonify({"error": str(error)}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
