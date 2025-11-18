"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Create a leaderboard system for a multiplayer FPS game, similar to the one on ev.io, that tracks player performance, XP, and rankings in real-time.
Generated: DETERMINISTIC_cd3ebe699b2dca0c
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
from flask import Flask, request, jsonify
from collections import defaultdict

# Flask app for the leaderboard system
app = Flask(__name__)

# In-memory data storage for leaderboard
leaderboard = defaultdict(lambda: {"score": 0, "xp": 0, "rank": None})

# Lock for thread safety
lock = threading.Lock()

@app.route('/update_score', methods=['POST'])
def update_score():
    """
    Endpoint to update a player's score and XP.
    Expects JSON payload: {"player_id": str, "score": int, "xp": int}
    """
    data = request.json

    if not data or "player_id" not in data or "score" not in data or "xp" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    player_id = data['player_id']
    score = data['score']
    xp = data['xp']

    try:
        with lock:
            # Update player data
            leaderboard[player_id]['score'] += score
            leaderboard[player_id]['xp'] += xp
            update_rankings()
        
        return jsonify({"message": "Score updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    """
    Endpoint to retrieve the leaderboard.
    Returns a sorted list of players based on their rankings.
    """
    try:
        with lock:
            # Sort players by score (highest first)
            sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1]['score'], reverse=True)
            result = [
                {"player_id": player_id, "score": data['score'], "xp": data['xp'], "rank": data['rank']}
                for rank, (player_id, data) in enumerate(sorted_leaderboard, start=1)
            ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/player_stats/<player_id>', methods=['GET'])
def player_stats(player_id):
    """
    Endpoint to retrieve a specific player's statistics.
    """
    try:
        with lock:
            if player_id not in leaderboard:
                return jsonify({"error": "Player not found"}), 404

            player_data = leaderboard[player_id]
            return jsonify({
                "player_id": player_id,
                "score": player_data['score'],
                "xp": player_data['xp'],
                "rank": player_data['rank']
            }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_rankings():
    """
    Updates the rank of all players based on their scores.
    """
    sorted_players = sorted(leaderboard.items(), key=lambda x: x[1]['score'], reverse=True)
    for rank, (player_id, _) in enumerate(sorted_players, start=1):
        leaderboard[player_id]['rank'] = rank

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```
