"""
Generated Code Metadata:
========================
Original URL: https://piaht.lol
Prompt: Design a simple card activation system API with user ID and card key validation.
Generated: DETERMINISTIC_b5dd73f45e91642e
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Mock database for storing user cards
user_cards = {
    "user123": {"card_key": "ABC123", "activated": False},
    "user456": {"card_key": "XYZ789", "activated": False},
}

def is_valid_user_id(user_id):
    """
    Validate the user ID format.
    User ID must be alphanumeric and between 5-15 characters.
    """
    return bool(re.match(r"^[a-zA-Z0-9]{5,15}$", user_id))

def is_valid_card_key(card_key):
    """
    Validate the card key format.
    Card key must be alphanumeric and between 6-10 characters.
    """
    return bool(re.match(r"^[a-zA-Z0-9]{6,10}$", card_key))

@app.route('/activate_card', methods=['POST'])
def activate_card():
    """
    API endpoint to activate a card.
    Expects JSON payload with 'user_id' and 'card_key'.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        user_id = data.get('user_id')
        card_key = data.get('card_key')

        # Validate input
        if not user_id or not card_key:
            return jsonify({"error": "Missing user_id or card_key"}), 400
        if not is_valid_user_id(user_id):
            return jsonify({"error": "Invalid user_id format"}), 400
        if not is_valid_card_key(card_key):
            return jsonify({"error": "Invalid card_key format"}), 400

        # Check if user exists
        user_data = user_cards.get(user_id)
        if not user_data:
            return jsonify({"error": "User not found"}), 404

        # Validate card key
        if user_data['card_key'] != card_key:
            return jsonify({"error": "Invalid card_key"}), 403

        # Check if card is already activated
        if user_data['activated']:
            return jsonify({"message": "Card is already activated"}), 200

        # Activate the card
        user_data['activated'] = True
        return jsonify({"message": "Card activated successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
