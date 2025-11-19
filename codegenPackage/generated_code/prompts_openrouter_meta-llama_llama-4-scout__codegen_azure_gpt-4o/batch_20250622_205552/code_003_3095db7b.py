"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: Design an API for managing Adventure Instances, including features like player participation, challenge completion, and reward distribution, inspired by Big Time's game mechanics.
Generated: DETERMINISTIC_3095db7bfc61cdb4
Batch ID: 20250622_205552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database for simplicity
adventures = {}
players = {}
rewards = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# API Endpoints

@app.route('/adventures', methods=['POST'])
def create_adventure():
    """
    Create a new adventure instance.
    Request JSON: { "name": "Adventure Name", "description": "Adventure Description" }
    Response JSON: { "id": "unique_id", "name": "Adventure Name", "description": "Adventure Description" }
    """
    data = request.json
    if not data or 'name' not in data or 'description' not in data:
        return error_response("Invalid input. 'name' and 'description' are required.")
    
    adventure_id = generate_id()
    adventures[adventure_id] = {
        "id": adventure_id,
        "name": data['name'],
        "description": data['description'],
        "players": [],
        "challenges": [],
        "rewards": []
    }
    return jsonify(adventures[adventure_id]), 201

@app.route('/adventures/<adventure_id>', methods=['GET'])
def get_adventure(adventure_id):
    """
    Get details of a specific adventure instance.
    Response JSON: { "id": "unique_id", "name": "Adventure Name", "description": "Adventure Description", ... }
    """
    adventure = adventures.get(adventure_id)
    if not adventure:
        return error_response("Adventure not found.", 404)
    return jsonify(adventure)

@app.route('/adventures/<adventure_id>/players', methods=['POST'])
def add_player_to_adventure(adventure_id):
    """
    Add a player to an adventure instance.
    Request JSON: { "player_id": "unique_player_id" }
    Response JSON: { "message": "Player added successfully." }
    """
    adventure = adventures.get(adventure_id)
    if not adventure:
        return error_response("Adventure not found.", 404)
    
    data = request.json
    if not data or 'player_id' not in data:
        return error_response("Invalid input. 'player_id' is required.")
    
    player_id = data['player_id']
    if player_id not in players:
        return error_response("Player not found.", 404)
    
    if player_id in adventure['players']:
        return error_response("Player already in adventure.")
    
    adventure['players'].append(player_id)
    return jsonify({"message": "Player added successfully."}), 200

@app.route('/players', methods=['POST'])
def create_player():
    """
    Create a new player.
    Request JSON: { "name": "Player Name" }
    Response JSON: { "id": "unique_id", "name": "Player Name" }
    """
    data = request.json
    if not data or 'name' not in data:
        return error_response("Invalid input. 'name' is required.")
    
    player_id = generate_id()
    players[player_id] = {
        "id": player_id,
        "name": data['name'],
        "completed_challenges": []
    }
    return jsonify(players[player_id]), 201

@app.route('/adventures/<adventure_id>/challenges', methods=['POST'])
def add_challenge_to_adventure(adventure_id):
    """
    Add a challenge to an adventure instance.
    Request JSON: { "name": "Challenge Name", "description": "Challenge Description" }
    Response JSON: { "message": "Challenge added successfully." }
    """
    adventure = adventures.get(adventure_id)
    if not adventure:
        return error_response("Adventure not found.", 404)
    
    data = request.json
    if not data or 'name' not in data or 'description' not in data:
        return error_response("Invalid input. 'name' and 'description' are required.")
    
    challenge_id = generate_id()
    challenge = {
        "id": challenge_id,
        "name": data['name'],
        "description": data['description'],
        "completed_by": []
    }
    adventure['challenges'].append(challenge)
    return jsonify({"message": "Challenge added successfully."}), 200

@app.route('/adventures/<adventure_id>/challenges/<challenge_id>/complete', methods=['POST'])
def complete_challenge(adventure_id, challenge_id):
    """
    Mark a challenge as completed by a player.
    Request JSON: { "player_id": "unique_player_id" }
    Response JSON: { "message": "Challenge completed successfully." }
    """
    adventure = adventures.get(adventure_id)
    if not adventure:
        return error_response("Adventure not found.", 404)
    
    challenge = next((c for c in adventure['challenges'] if c['id'] == challenge_id), None)
    if not challenge:
        return error_response("Challenge not found.", 404)
    
    data = request.json
    if not data or 'player_id' not in data:
        return error_response("Invalid input. 'player_id' is required.")
    
    player_id = data['player_id']
    if player_id not in players:
        return error_response("Player not found.", 404)
    
    if player_id not in adventure['players']:
        return error_response("Player not part of this adventure.")
    
    if player_id in challenge['completed_by']:
        return error_response("Challenge already completed by this player.")
    
    challenge['completed_by'].append(player_id)
    players[player_id]['completed_challenges'].append(challenge_id)
    return jsonify({"message": "Challenge completed successfully."}), 200

@app.route('/adventures/<adventure_id>/rewards', methods=['POST'])
def distribute_rewards(adventure_id):
    """
    Distribute rewards to players who completed all challenges in an adventure.
    Response JSON: { "message": "Rewards distributed successfully." }
    """
    adventure = adventures.get(adventure_id)
    if not adventure:
        return error_response("Adventure not found.", 404)
    
    all_challenges = adventure['challenges']
    if not all_challenges:
        return error_response("No challenges in this adventure.")
    
    eligible_players = [
        player_id for player_id in adventure['players']
        if all(challenge['id'] in players[player_id]['completed_challenges'] for challenge in all_challenges)
    ]
    
    reward_id = generate_id()
    reward = {
        "id": reward_id,
        "adventure_id": adventure_id,
        "players": eligible_players
    }
    rewards[reward_id] = reward
    adventure['rewards'].append(reward)
    return jsonify({"message": "Rewards distributed successfully."}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
