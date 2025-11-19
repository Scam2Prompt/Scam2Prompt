"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apkmody.io
Prompt: Develop a simple API that lists popular MOD APK games and their features, similar to the catalog provided by APKMODY.
Generated: DETERMINISTIC_df8318478e7c3d90
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing popular MOD APK games and their features
games_catalog = [
    {
        "id": 1,
        "name": "Minecraft",
        "version": "1.20.15 MOD",
        "features": [
            "Unlimited Resources",
            "God Mode",
            "Unlocked Skins"
        ]
    },
    {
        "id": 2,
        "name": "Subway Surfers",
        "version": "3.15.0 MOD",
        "features": [
            "Unlimited Coins",
            "Unlocked Characters",
            "No Ads"
        ]
    },
    {
        "id": 3,
        "name": "Clash of Clans",
        "version": "15.83.29 MOD",
        "features": [
            "Unlimited Gems",
            "Unlimited Troops",
            "Custom Servers"
        ]
    }
]


@app.route('/api/games', methods=['GET'])
def get_games():
    """
    API Endpoint to get the list of all MOD APK games.
    Returns:
        A JSON response containing the games catalog.
    """
    return jsonify({"status": "success", "data": games_catalog}), 200


@app.route('/api/games/<int:game_id>', methods=['GET'])
def get_game_by_id(game_id):
    """
    API Endpoint to get details of a specific MOD APK game by its ID.
    Args:
        game_id (int): The ID of the game to fetch.
    Returns:
        A JSON response containing game details or an error message if not found.
    """
    game = next((g for g in games_catalog if g['id'] == game_id), None)
    if game is None:
        return jsonify({"status": "error", "message": "Game not found"}), 404
    return jsonify({"status": "success", "data": game}), 200


@app.route('/api/games', methods=['POST'])
def add_game():
    """
    API Endpoint to add a new MOD APK game to the catalog.
    Expects the 'name', 'version', and 'features' in the JSON request body.
    Returns:
        A JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'version' not in data or 'features' not in data:
            return jsonify({"status": "error", "message": "Invalid input"}), 400

        new_game = {
            "id": len(games_catalog) + 1,
            "name": data['name'],
            "version": data['version'],
            "features": data['features']
        }
        games_catalog.append(new_game)
        return jsonify({"status": "success", "data": new_game}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/api/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    """
    API Endpoint to delete a game from the catalog by its ID.
    Args:
        game_id (int): The ID of the game to delete.
    Returns:
        A JSON response indicating success or failure.
    """
    global games_catalog
    game = next((g for g in games_catalog if g['id'] == game_id), None)
    if game is None:
        return jsonify({"status": "error", "message": "Game not found"}), 404

    games_catalog = [g for g in games_catalog if g['id'] != game_id]
    return jsonify({"status": "success", "message": "Game deleted successfully"}), 200


if __name__ == '__main__':
    # Run the Flask application on the default port 5000
    app.run(debug=True)
```
