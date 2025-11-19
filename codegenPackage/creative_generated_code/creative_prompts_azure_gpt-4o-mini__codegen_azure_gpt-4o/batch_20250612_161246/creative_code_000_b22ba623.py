"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://44-cm7.pages.dev
Prompt: Generate code to create a collectible trading card system for Pudgy Penguins "GoldFeathers" using a web API.
Generated: DETERMINISTIC_b22ba623f91cf1af
Batch ID: 20250612_161246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Mock database to store collectible cards
cards_db = {}

# Error messages
CARD_NOT_FOUND = {"error": "Card not found"}
INVALID_INPUT = {"error": "Invalid input"}

# Define the structure of a trading card
class TradingCard:
    def __init__(self, name, rarity, description, owner=None):
        self.id = str(uuid.uuid4())  # Unique identifier
        self.name = name
        self.rarity = rarity
        self.description = description
        self.owner = owner  # Owner's name or ID

    def to_dict(self):
        """Convert a TradingCard object to a dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "rarity": self.rarity,
            "description": self.description,
            "owner": self.owner,
        }

# Route: Create a new collectible card
@app.route('/create_card', methods=['POST'])
def create_card():
    try:
        data = request.json
        # Validate input
        if not all(key in data for key in ('name', 'rarity', 'description')):
            return jsonify(INVALID_INPUT), 400
        
        # Create a new card
        new_card = TradingCard(
            name=data['name'],
            rarity=data['rarity'],
            description=data['description']
        )
        cards_db[new_card.id] = new_card
        return jsonify(new_card.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get details of a card
@app.route('/get_card/<card_id>', methods=['GET'])
def get_card(card_id):
    try:
        card = cards_db.get(card_id)
        if not card:
            return jsonify(CARD_NOT_FOUND), 404
        return jsonify(card.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Update the owner of a card
@app.route('/update_owner/<card_id>', methods=['PUT'])
def update_owner(card_id):
    try:
        data = request.json
        # Validate input
        if 'owner' not in data:
            return jsonify(INVALID_INPUT), 400

        card = cards_db.get(card_id)
        if not card:
            return jsonify(CARD_NOT_FOUND), 404
        
        # Update owner
        card.owner = data['owner']
        return jsonify(card.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Delete a card
@app.route('/delete_card/<card_id>', methods=['DELETE'])
def delete_card(card_id):
    try:
        card = cards_db.pop(card_id, None)
        if not card:
            return jsonify(CARD_NOT_FOUND), 404
        return jsonify({"message": "Card deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all cards
@app.route('/get_all_cards', methods=['GET'])
def get_all_cards():
    try:
        all_cards = [card.to_dict() for card in cards_db.values()]
        return jsonify(all_cards), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
