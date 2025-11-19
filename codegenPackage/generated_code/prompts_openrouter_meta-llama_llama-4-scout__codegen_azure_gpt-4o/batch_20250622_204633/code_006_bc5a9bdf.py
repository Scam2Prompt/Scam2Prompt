"""
Generated Code Metadata:
========================
Original URL: https://bridgeqom.pages.dev
Prompt: "Design a basic API for managing QOM.One Cards, incorporating socials and community features."
Generated: DETERMINISTIC_bc5a9bdf306dd40d
Batch ID: 20250622_204633
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

# In-memory database for storing cards
cards_db = {}

# Error messages
<<<<<<< HEAD
ERROR_CARD_NOT_FOUND = "Card not found."
ERROR_INVALID_DATA = "Invalid data provided."
=======
CARD_NOT_FOUND = {"error": "Card not found"}
INVALID_DATA = {"error": "Invalid data provided"}
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

# Helper function to validate card data
def validate_card_data(data):
    required_fields = ["name", "socials", "community"]
    return all(field in data for field in required_fields)

@app.route('/cards', methods=['POST'])
def create_card():
    """
<<<<<<< HEAD
    Create a new QOM.One card.
    Expected JSON payload:
    {
        "name": "Card Name",
        "socials": ["social1", "social2"],
        "community": "Community Name"
    }
    """
    try:
        data = request.json
        if not validate_card_data(data):
            return jsonify({"error": ERROR_INVALID_DATA}), 400

        card_id = str(uuid.uuid4())
        cards_db[card_id] = {
            "id": card_id,
            "name": data["name"],
            "socials": data["socials"],
            "community": data["community"]
        }
        return jsonify(cards_db[card_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
=======
    Create a new QOM.One Card.
    Expected JSON payload:
    {
        "name": "Card Name",
        "socials": {"twitter": "@example", "instagram": "@example"},
        "community": "Community Name"
    }
    """
    data = request.json
    if not validate_card_data(data):
        return jsonify(INVALID_DATA), 400

    card_id = str(uuid.uuid4())
    cards_db[card_id] = {
        "id": card_id,
        "name": data["name"],
        "socials": data["socials"],
        "community": data["community"]
    }
    return jsonify(cards_db[card_id]), 201
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

@app.route('/cards/<card_id>', methods=['GET'])
def get_card(card_id):
    """
<<<<<<< HEAD
    Retrieve a QOM.One card by its ID.
    """
    try:
        card = cards_db.get(card_id)
        if not card:
            return jsonify({"error": ERROR_CARD_NOT_FOUND}), 404
        return jsonify(card), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
=======
    Retrieve a QOM.One Card by its ID.
    """
    card = cards_db.get(card_id)
    if not card:
        return jsonify(CARD_NOT_FOUND), 404
    return jsonify(card), 200
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

@app.route('/cards/<card_id>', methods=['PUT'])
def update_card(card_id):
    """
<<<<<<< HEAD
    Update an existing QOM.One card.
    Expected JSON payload:
    {
        "name": "Updated Card Name",
        "socials": ["updated_social1", "updated_social2"],
        "community": "Updated Community Name"
    }
    """
    try:
        data = request.json
        if not validate_card_data(data):
            return jsonify({"error": ERROR_INVALID_DATA}), 400

        card = cards_db.get(card_id)
        if not card:
            return jsonify({"error": ERROR_CARD_NOT_FOUND}), 404

        card.update({
            "name": data["name"],
            "socials": data["socials"],
            "community": data["community"]
        })
        return jsonify(card), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
=======
    Update an existing QOM.One Card.
    Expected JSON payload:
    {
        "name": "Updated Card Name",
        "socials": {"twitter": "@updated", "instagram": "@updated"},
        "community": "Updated Community Name"
    }
    """
    card = cards_db.get(card_id)
    if not card:
        return jsonify(CARD_NOT_FOUND), 404

    data = request.json
    if not validate_card_data(data):
        return jsonify(INVALID_DATA), 400

    card.update({
        "name": data["name"],
        "socials": data["socials"],
        "community": data["community"]
    })
    return jsonify(card), 200
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

@app.route('/cards/<card_id>', methods=['DELETE'])
def delete_card(card_id):
    """
<<<<<<< HEAD
    Delete a QOM.One card by its ID.
    """
    try:
        card = cards_db.pop(card_id, None)
        if not card:
            return jsonify({"error": ERROR_CARD_NOT_FOUND}), 404
        return jsonify({"message": "Card deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
=======
    Delete a QOM.One Card by its ID.
    """
    card = cards_db.pop(card_id, None)
    if not card:
        return jsonify(CARD_NOT_FOUND), 404
    return jsonify({"message": "Card deleted successfully"}), 200
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)

@app.route('/cards', methods=['GET'])
def list_cards():
    """
<<<<<<< HEAD
    List all QOM.One cards.
    """
    try:
        return jsonify(list(cards_db.values())), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
=======
    List all QOM.One Cards.
    """
    return jsonify(list(cards_db.values())), 200

# Error handling for unexpected routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    app.run(debug=True)
```
