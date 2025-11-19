"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-kombatgame.com
Prompt: Describe how to implement a scoring system for a hamster-themed combat game using APIs.
Generated: DETERMINISTIC_62da0fdcb0bd7086
Batch ID: 20250612_163646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store player scores
player_scores = {}

# API endpoint to get a player's score
@app.route('/api/score/<player_id>', methods=['GET'])
def get_score(player_id):
    """
    Get the current score of a player.
    :param player_id: The ID of the player
    :return: JSON response containing the player's score or an error message
    """
    if player_id in player_scores:
        return jsonify({"player_id": player_id, "score": player_scores[player_id]}), 200
    else:
        return jsonify({"error": "Player not found"}), 404


# API endpoint to update a player's score
@app.route('/api/score/<player_id>', methods=['POST'])
def update_score(player_id):
    """
    Update the score of a player.
    :param player_id: The ID of the player
    :return: JSON response indicating success or error
    """
    try:
        data = request.get_json()
        increment = data.get('increment', 0)  # Default increment value is 0

        if not isinstance(increment, int):
            return jsonify({"error": "Invalid increment value. Must be an integer."}), 400

        if player_id not in player_scores:
            # If player does not exist, initialize with a score of 0 before incrementing
            player_scores[player_id] = 0

        player_scores[player_id] += increment

        return jsonify({"player_id": player_id, "new_score": player_scores[player_id]}), 200
    except Exception as e:
        # Handle any unexpected server error
        return jsonify({"error": str(e)}), 500


# API endpoint to reset a player's score
@app.route('/api/score/<player_id>', methods=['DELETE'])
def reset_score(player_id):
    """
    Reset the score of a player to 0.
    :param player_id: The ID of the player
    :return: JSON response indicating success or error
    """
    if player_id in player_scores:
        player_scores[player_id] = 0
        return jsonify({"player_id": player_id, "score_reset": True}), 200
    else:
        return jsonify({"error": "Player not found"}), 404


# API endpoint to list all player scores
@app.route('/api/scores', methods=['GET'])
def list_scores():
    """
    List all scores for players in the game.
    :return: JSON response containing all player scores
    """
    return jsonify(player_scores), 200


# Main entry point for the Flask application
if __name__ == '__main__':
    # Start the Flask server
    app.run(host='0.0.0.0', port=5000)
```
