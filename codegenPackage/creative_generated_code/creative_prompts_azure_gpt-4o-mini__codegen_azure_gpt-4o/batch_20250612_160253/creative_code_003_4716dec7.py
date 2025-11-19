"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-sonic-lab.xyz
Prompt: Suggest an API for integrating multiplayer tournament features in a mobile game, similar to the tournaments mentioned in the Holders App.
Generated: DETERMINISTIC_4716dec7b4f275fa
Batch ID: 20250612_160253
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: tournament_api.py

from flask import Flask, request, jsonify
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory database for demonstration purposes
tournaments = {}
players = {}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Utility function to validate tournament structure
def validate_tournament(tournament):
    required_fields = ["name", "game", "start_time", "end_time", "max_players"]
    for field in required_fields:
        if field not in tournament:
            return False, f"Missing required field: {field}"
    return True, None

# API endpoint: Create a new tournament
@app.route('/api/tournaments', methods=['POST'])
def create_tournament():
    try:
        data = request.json
        is_valid, error = validate_tournament(data)
        if not is_valid:
            return jsonify({"error": error}), 400

        tournament_id = generate_id()
        tournaments[tournament_id] = {
            "id": tournament_id,
            "name": data["name"],
            "game": data["game"],
            "start_time": datetime.fromisoformat(data["start_time"]),
            "end_time": datetime.fromisoformat(data["end_time"]),
            "max_players": data["max_players"],
            "players": []
        }
        return jsonify({"tournament_id": tournament_id, "message": "Tournament created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint: Register a player into a tournament
@app.route('/api/tournaments/<tournament_id>/register', methods=['POST'])
def register_player(tournament_id):
    try:
        if tournament_id not in tournaments:
            return jsonify({"error": "Tournament not found"}), 404

        tournament = tournaments[tournament_id]

        # Validate player data
        data = request.json
        player_name = data.get("name")
        if not player_name:
            return jsonify({"error": "Player name is required"}), 400

        if len(tournament["players"]) >= tournament["max_players"]:
            return jsonify({"error": "Tournament is full"}), 403

        # Register player
        player_id = generate_id()
        player = {"id": player_id, "name": player_name}
        tournament["players"].append(player)
        players[player_id] = player

        return jsonify({"player_id": player_id, "message": "Player registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint: List all tournaments
@app.route('/api/tournaments', methods=['GET'])
def list_tournaments():
    try:
        result = []
        for tournament in tournaments.values():
            result.append({
                "id": tournament["id"],
                "name": tournament["name"],
                "game": tournament["game"],
                "start_time": tournament["start_time"].isoformat(),
                "end_time": tournament["end_time"].isoformat(),
                "max_players": tournament["max_players"],
                "current_players": len(tournament["players"])
            })
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint: Get details of a specific tournament
@app.route('/api/tournaments/<tournament_id>', methods=['GET'])
def get_tournament_details(tournament_id):
    try:
        if tournament_id not in tournaments:
            return jsonify({"error": "Tournament not found"}), 404

        tournament = tournaments[tournament_id]
        details = {
            "id": tournament["id"],
            "name": tournament["name"],
            "game": tournament["game"],
            "start_time": tournament["start_time"].isoformat(),
            "end_time": tournament["end_time"].isoformat(),
            "max_players": tournament["max_players"],
            "players": tournament["players"]
        }
        return jsonify(details), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint: Delete a tournament
@app.route('/api/tournaments/<tournament_id>', methods=['DELETE'])
def delete_tournament(tournament_id):
    try:
        if tournament_id not in tournaments:
            return jsonify({"error": "Tournament not found"}), 404

        del tournaments[tournament_id]
        return jsonify({"message": "Tournament deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint: List all players in a tournament
@app.route('/api/tournaments/<tournament_id>/players', methods=['GET'])
def list_tournament_players(tournament_id):
    try:
        if tournament_id not in tournaments:
            return jsonify({"error": "Tournament not found"}), 404

        tournament = tournaments[tournament_id]
        return jsonify(tournament["players"]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
