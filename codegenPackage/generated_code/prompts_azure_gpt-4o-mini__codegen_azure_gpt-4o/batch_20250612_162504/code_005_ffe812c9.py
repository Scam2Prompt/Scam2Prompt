"""
Generated Code Metadata:
========================
Original URL: https://register-stormwarfarecom.pages.dev
Prompt: Create an API endpoint for managing player hands and card collections in a game like Storm Warfare, focusing on true ownership of assets.
Generated: DETERMINISTIC_ffe812c986bc8af4
Batch ID: 20250612_162504
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

# In-memory storage for players and their card collections
players = {}

# Error messages
PLAYER_NOT_FOUND = "Player not found."
INVALID_REQUEST = "Invalid request data."

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# API endpoint to create a new player
@app.route('/players', methods=['POST'])
def create_player():
    try:
        data = request.json
        if not data or 'name' not in data:
            return jsonify({"error": INVALID_REQUEST}), 400
        
        player_id = generate_id()
        players[player_id] = {
            "name": data['name'],
            "hand": [],
            "collection": []
        }
        return jsonify({"player_id": player_id, "name": data['name']}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to add a card to a player's collection
@app.route('/players/<player_id>/collection', methods=['POST'])
def add_card_to_collection(player_id):
    try:
        if player_id not in players:
            return jsonify({"error": PLAYER_NOT_FOUND}), 404
        
        data = request.json
        if not data or 'card' not in data:
            return jsonify({"error": INVALID_REQUEST}), 400
        
        card = data['card']
        players[player_id]['collection'].append(card)
        return jsonify({"message": f"Card '{card}' added to collection."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to move a card from collection to hand
@app.route('/players/<player_id>/hand', methods=['POST'])
def move_card_to_hand(player_id):
    try:
        if player_id not in players:
            return jsonify({"error": PLAYER_NOT_FOUND}), 404
        
        data = request.json
        if not data or 'card' not in data:
            return jsonify({"error": INVALID_REQUEST}), 400
        
        card = data['card']
        if card not in players[player_id]['collection']:
            return jsonify({"error": f"Card '{card}' not found in collection."}), 404
        
        players[player_id]['collection'].remove(card)
        players[player_id]['hand'].append(card)
        return jsonify({"message": f"Card '{card}' moved to hand."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to view a player's hand and collection
@app.route('/players/<player_id>', methods=['GET'])
def view_player(player_id):
    try:
        if player_id not in players:
            return jsonify({"error": PLAYER_NOT_FOUND}), 404
        
        player_data = players[player_id]
        return jsonify({
            "name": player_data['name'],
            "hand": player_data['hand'],
            "collection": player_data['collection']
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to remove a card from a player's hand
@app.route('/players/<player_id>/hand', methods=['DELETE'])
def remove_card_from_hand(player_id):
    try:
        if player_id not in players:
            return jsonify({"error": PLAYER_NOT_FOUND}), 404
        
        data = request.json
        if not data or 'card' not in data:
            return jsonify({"error": INVALID_REQUEST}), 400
        
        card = data['card']
        if card not in players[player_id]['hand']:
            return jsonify({"error": f"Card '{card}' not found in hand."}), 404
        
        players[player_id]['hand'].remove(card)
        return jsonify({"message": f"Card '{card}' removed from hand."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
