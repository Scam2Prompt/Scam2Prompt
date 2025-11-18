"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Write code to implement a leaderboard system for ranking players based on their activity and achievements, as described in Genopets Phase 1 roadmap.
Generated: DETERMINISTIC_5314a3376bf202aa
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from collections import defaultdict
import heapq

# Initialize Flask app
app = Flask(__name__)

# In-memory data store
players = {}  # Stores player information
leaderboard = []  # Min-heap to track top players
MAX_LEADERBOARD_SIZE = 10  # Maximum number of players to display on the leaderboard


class Player:
    """Class to represent a Player."""
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.score = 0  # Player's initial score

    def update_score(self, activity_points, achievements_points):
        """
        Update the player's score based on activity and achievements.
        """
        self.score += activity_points + achievements_points


def update_leaderboard(player):
    """
    Update the leaderboard with the given player's new score.
    Uses a min-heap to maintain the top players efficiently.
    """
    for i, item in enumerate(leaderboard):
        if item[1] == player.player_id:
            # Remove old score entry
            leaderboard.pop(i)
            heapq.heapify(leaderboard)
            break

    # Push the new score onto the heap
    heapq.heappush(leaderboard, (player.score, player.player_id))

    # If the leaderboard exceeds the max size, remove the lowest score
    if len(leaderboard) > MAX_LEADERBOARD_SIZE:
        heapq.heappop(leaderboard)


@app.route('/player', methods=['POST'])
def create_player():
    """
    API endpoint to create a new player.
    Expected JSON payload: {"player_id": "unique_id", "name": "player_name"}
    """
    try:
        data = request.get_json()
        player_id = data["player_id"]
        name = data["name"]

        if player_id in players:
            return jsonify({"error": "Player ID already exists"}), 400

        # Add new player to the data store
        players[player_id] = Player(player_id, name)
        return jsonify({"message": "Player created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/player/<player_id>/score', methods=['POST'])
def update_player_score(player_id):
    """
    API endpoint to update a player's score.
    Expected JSON payload: {"activity_points": 10, "achievements_points": 20}
    """
    try:
        if player_id not in players:
            return jsonify({"error": "Player not found"}), 404

        data = request.get_json()
        activity_points = data.get("activity_points", 0)
        achievements_points = data.get("achievements_points", 0)

        # Update player's score
        player = players[player_id]
        player.update_score(activity_points, achievements_points)

        # Update leaderboard
        update_leaderboard(player)

        return jsonify({"message": "Player score updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    """
    API endpoint to retrieve the current leaderboard.
    Returns data in descending order of scores.
    """
    try:
        # Sort leaderboard from highest to lowest score
        sorted_leaderboard = sorted(leaderboard, key=lambda x: -x[0])

        result = [
            {
                "player_id": player_id,
                "name": players[player_id].name,
                "score": score
            } for score, player_id in sorted_leaderboard
        ]

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True)
```
