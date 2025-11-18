"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Suggest methods for integrating social collaboration and competition features into a game platform, similar to SCATTER HITAM's social aspects.
Generated: DETERMINISTIC_7882f67aafa8e4f0
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation to showcase social collaboration and competition features on a game platform. It uses a simulated Flask backend:

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Sample in-memory database for players and teams
players = {}
teams = {}
leaderboard = {}

# Helper function to create unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handler for invalid requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400


# --- Social Collaboration: Teams ---
@app.route('/create_team', methods=['POST'])
def create_team():
    """
    Endpoint to create a new team.
    Request JSON: {"team_name": "TeamName"}
    """
    data = request.get_json()
    if not data or 'team_name' not in data:
        return bad_request("Missing 'team_name'")
    
    team_id = generate_id()
    teams[team_id] = {
        "team_name": data['team_name'],
        "members": []
    }
    return jsonify({"message": "Team created successfully!", "team_id": team_id})


@app.route('/join_team', methods=['POST'])
def join_team():
    """
    Endpoint to join an existing team.
    Request JSON: {"player_id": "PlayerID", "team_id": "TeamID"}
    """
    data = request.get_json()
    if not data or 'player_id' not in data or 'team_id' not in data:
        return bad_request("Missing 'player_id' or 'team_id'")
    
    player_id = data['player_id']
    team_id = data['team_id']
    
    if team_id not in teams:
        return bad_request("Invalid team ID")
    if player_id not in players:
        return bad_request("Invalid player ID")
    
    teams[team_id]['members'].append(player_id)
    return jsonify({"message": f"Player {player_id} joined team {team_id} successfully!"})


# --- Social Competition: Leaderboard ---
@app.route('/submit_score', methods=['POST'])
def submit_score():
    """
    Endpoint to submit a score.
    Request JSON: {"player_id": "PlayerID", "score": Integer}
    """
    data = request.get_json()
    if not data or 'player_id' not in data or 'score' not in data:
        return bad_request("Missing 'player_id' or 'score'")
    
    player_id = data['player_id']
    score = data['score']
    
    if player_id not in players:
        return bad_request("Invalid player ID")
    if not isinstance(score, int) or score < 0:
        return bad_request("Invalid score")
    
    leaderboard[player_id] = leaderboard.get(player_id, 0) + score
    return jsonify({"message": f"Score submitted successfully for player {player_id}!", "total_score": leaderboard[player_id]})


@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    """
    Endpoint to retrieve the leaderboard.
    Returns a sorted list of players and their scores.
    """
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    return jsonify({"leaderboard": [{"player_id": k, "score": v} for k, v in sorted_leaderboard]})


# --- Player Management ---
@app.route('/create_player', methods=['POST'])
def create_player():
    """
    Endpoint to create a new player.
    Request JSON: {"username": "Username"}
    """
    data = request.get_json()
    if not data or 'username' not in data:
        return bad_request("Missing 'username'")
    
    player_id = generate_id()
    players[player_id] = {
        "username": data['username']
    }
    return jsonify({"message": "Player created successfully!", "player_id": player_id})


if __name__ == '__main__':
    app.run(debug=True)
```
