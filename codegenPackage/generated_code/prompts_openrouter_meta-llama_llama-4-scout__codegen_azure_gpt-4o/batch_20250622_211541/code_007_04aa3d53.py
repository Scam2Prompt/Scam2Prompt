"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Develop an API endpoint to retrieve information about a specific slot game on Coin Rush, including game details, demo mode, and provider information.
Generated: DETERMINISTIC_04aa3d5342d9e312
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Mock database for slot games
slot_games = {
    "game1": {
        "id": "game1",
        "name": "Treasure Hunt",
        "provider": "Provider A",
        "demo_mode": True,
        "details": {
            "reels": 5,
            "paylines": 20,
            "theme": "Pirates"
        }
    },
    "game2": {
        "id": "game2",
        "name": "Wild Safari",
        "provider": "Provider B",
        "demo_mode": False,
        "details": {
            "reels": 4,
            "paylines": 10,
            "theme": "Animals"
        }
    }
}

@app.route('/api/slot-game/<string:game_id>', methods=['GET'])
def get_slot_game(game_id):
    """
    API endpoint to retrieve information about a specific slot game.
    :param game_id: The ID of the slot game to retrieve.
    :return: JSON response containing game details or an error message.
    """
    try:
        # Check if the game exists in the mock database
        game = slot_games.get(game_id)
        if not game:
            # Return a 404 error if the game is not found
            abort(404, description=f"Slot game with ID '{game_id}' not found.")
        
        # Return the game details as a JSON response
        return jsonify({
            "success": True,
            "data": game
        }), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "success": False,
            "error": "An unexpected error occurred.",
            "message": str(e)
        }), 500

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 Not Found.
    :param error: The error object.
    :return: JSON response with error details.
    """
    return jsonify({
        "success": False,
        "error": "Not Found",
        "message": error.description
    }), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    """
    Custom error handler for 400 Bad Request.
    :param error: The error object.
    :return: JSON response with error details.
    """
    return jsonify({
        "success": False,
        "error": "Bad Request",
        "message": error.description
    }), 400

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
