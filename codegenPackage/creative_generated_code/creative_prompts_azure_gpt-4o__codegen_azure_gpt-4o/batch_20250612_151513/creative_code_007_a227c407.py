"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Design a REST API for MetaLeagues' guild verification tool, enabling games to find top players and guilds to identify enthusiastic gamers.
Generated: DETERMINISTIC_a227c40757375a87
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulation
players = [
    {"id": 1, "username": "player1", "game": "gameA", "rating": 1200},
    {"id": 2, "username": "player2", "game": "gameB", "rating": 1500},
    {"id": 3, "username": "player3", "game": "gameA", "rating": 1700},
]

guilds = [
    {"id": 1, "name": "GuildAlpha", "game": "gameA", "members": [1, 3]},
    {"id": 2, "name": "GuildBeta", "game": "gameB", "members": [2]},
]


@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the API.
    Returns JSON response for all exceptions.
    """
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({"error": e.description}).data
        response.content_type = "application/json"
        return response
    return jsonify({"error": "Internal server error"}), 500


@app.route('/players', methods=['GET'])
def get_players():
    """
    Retrieve a list of players.
    Optional query parameter: `game` (filter by game).
    """
    game = request.args.get('game')
    if game:
        filtered_players = [player for player in players if player['game'] == game]
        return jsonify(filtered_players)
    return jsonify(players)


@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    """
    Retrieve information about a specific player by ID.
    """
    player = next((p for p in players if p['id'] == player_id), None)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    return jsonify(player)


@app.route('/guilds', methods=['GET'])
def get_guilds():
    """
    Retrieve a list of guilds.
    Optional query parameter: `game` (filter by game).
    """
    game = request.args.get('game')
    if game:
        filtered_guilds = [guild for guild in guilds if guild['game'] == game]
        return jsonify(filtered_guilds)
    return jsonify(guilds)


@app.route('/guilds/<int:guild_id>', methods=['GET'])
def get_guild(guild_id):
    """
    Retrieve information about a specific guild by ID.
    Includes details about its members.
    """
    guild = next((g for g in guilds if g['id'] == guild_id), None)
    if not guild:
        return jsonify({"error": "Guild not found"}), 404

    guild_data = {
        **guild,
        "members_details": [p for p in players if p['id'] in guild['members']]
    }
    return jsonify(guild_data)


@app.route('/top-players', methods=['GET'])
def get_top_players():
    """
    Retrieve a list of top players across all games or a specific game.
    Optional query parameter: `game` (filter by game).
    """
    game = request.args.get('game')
    if game:
        filtered_players = [player for player in players if player['game'] == game]
    else:
        filtered_players = players

    # Sort players by rating in descending order and return top 10
    top_players = sorted(filtered_players, key=lambda p: p['rating'], reverse=True)[:10]
    return jsonify(top_players)


@app.route('/verify-gamer', methods=['POST'])
def verify_gamer():
    """
    Verify gamer association with a guild.
    Expects JSON payload: {"guild_id": int, "player_id": int}.
    """
    data = request.get_json()
    guild_id = data.get('guild_id')
    player_id = data.get('player_id')

    if not guild_id or not player_id:
        return jsonify({"error": "guild_id and player_id are required"}), 400

    guild = next((g for g in guilds if g['id'] == guild_id), None)
    if not guild:
        return jsonify({"error": "Guild not found"}), 404

    if player_id in guild['members']:
        return jsonify({"message": "Player is a member of the guild"}), 200
    else:
        return jsonify({"message": "Player is not a member of the guild"}), 404


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
