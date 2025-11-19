"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Generate code for a simple app that allows users to redeem points for gift cards, inspired by the Cosmic Rewards platform.
Generated: DETERMINISTIC_69f35ee1c2e38b94
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for users and gift cards
users = {
    "user1": {"points": 500},
    "user2": {"points": 300},
}

gift_cards = [
    {"id": 1, "name": "Amazon $10 Gift Card", "points_required": 200},
    {"id": 2, "name": "Starbucks $5 Gift Card", "points_required": 150},
    {"id": 3, "name": "Netflix 1-Month Subscription", "points_required": 500},
]

# Endpoint to retrieve available gift cards
@app.route('/gift-cards', methods=['GET'])
def get_gift_cards():
    """
    Returns the list of available gift cards.
    """
    return jsonify(gift_cards), 200

# Endpoint to redeem points for a gift card
@app.route('/redeem', methods=['POST'])
def redeem_points():
    """
    Allows users to redeem points for a gift card.
    Expects JSON payload with 'username' and 'gift_card_id'.
    """
    try:
        # Parse the request JSON
        data = request.get_json()

        # Validate request data
        if not data or "username" not in data or "gift_card_id" not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        username = data["username"]
        gift_card_id = data["gift_card_id"]

        # Check if the user exists
        if username not in users:
            return jsonify({"error": "User not found"}), 404

        user = users[username]

        # Find the requested gift card
        gift_card = next((gc for gc in gift_cards if gc["id"] == gift_card_id), None)
        if not gift_card:
            return jsonify({"error": "Gift card not found"}), 404

        # Check if the user has enough points
        if user["points"] < gift_card["points_required"]:
            return jsonify({"error": "Insufficient points"}), 400

        # Deduct points and redeem the gift card
        user["points"] -= gift_card["points_required"]
        return jsonify({"message": f"Successfully redeemed {gift_card['name']}", "remaining_points": user["points"]}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to ensure the service is running.
    """
    return jsonify({"status": "healthy"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
