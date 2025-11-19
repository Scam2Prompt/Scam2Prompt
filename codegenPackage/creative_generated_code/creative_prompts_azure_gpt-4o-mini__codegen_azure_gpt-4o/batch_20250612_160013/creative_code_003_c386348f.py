"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piaht.lol
Prompt: Can you provide an example of an API that handles card activation and user ID management?
Generated: DETERMINISTIC_c386348fc2cf3a24
Batch ID: 20250612_160013
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

# Simulated database for storing user and card information
database = {
    "users": {},  # Format: {user_id: {name: str, cards: list}}
    "cards": {},  # Format: {card_id: {user_id: str, activated: bool}}
}

@app.route('/create_user', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    Expects 'name' in the request JSON body.
    """
    try:
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({"error": "Name is required"}), 400

        # Generate a unique user ID
        user_id = str(uuid.uuid4())
        database["users"][user_id] = {"name": name, "cards": []}

        return jsonify({"message": "User created successfully", "user_id": user_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add_card', methods=['POST'])
def add_card():
    """
    Endpoint to add a card to a user.
    Expects 'user_id' in the request JSON body.
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')

        if not user_id or user_id not in database["users"]:
            return jsonify({"error": "Valid user_id is required"}), 400

        # Generate unique card ID
        card_id = str(uuid.uuid4())
        database["cards"][card_id] = {"user_id": user_id, "activated": False}
        database["users"][user_id]["cards"].append(card_id)

        return jsonify({"message": "Card added successfully", "card_id": card_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/activate_card', methods=['POST'])
def activate_card():
    """
    Endpoint to activate a card.
    Expects 'card_id' in the request JSON body.
    """
    try:
        data = request.get_json()
        card_id = data.get('card_id')

        if not card_id or card_id not in database["cards"]:
            return jsonify({"error": "Valid card_id is required"}), 400

        if database["cards"][card_id]["activated"]:
            return jsonify({"message": "Card is already activated"}), 200

        # Activate the card
        database["cards"][card_id]["activated"] = True

        return jsonify({"message": "Card activated successfully", "card_id": card_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user_cards/<user_id>', methods=['GET'])
def get_user_cards(user_id):
    """
    Endpoint to retrieve all cards associated with a user.
    :param user_id: User ID from the URL route.
    """
    try:
        if user_id not in database["users"]:
            return jsonify({"error": "User not found"}), 404

        user_data = database["users"][user_id]
        cards = user_data["cards"]
        card_details = [{"card_id": card, **database["cards"][card]} for card in cards]

        return jsonify({"user_id": user_id, "cards": card_details}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/card_info/<card_id>', methods=['GET'])
def get_card_info(card_id):
    """
    Endpoint to retrieve card information.
    :param card_id: Card ID from the URL route.
    """
    try:
        if card_id not in database["cards"]:
            return jsonify({"error": "Card not found"}), 404

        card_info = database["cards"][card_id]

        return jsonify({"card_id": card_id, **card_info}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
