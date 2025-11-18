"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-hex.com
Prompt: Generate a REST API design for managing Lenovo Pro tier benefits, including endpoints for tracking spending, upgrading tiers, and accessing exclusive discounts.
Generated: DETERMINISTIC_dc7c2c3802a852a0
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database
users = {
    "user1": {"spending": 0, "tier": "Silver", "discounts": ["5% off accessories"]},
    "user2": {"spending": 1200, "tier": "Gold", "discounts": ["10% off laptops", "Free shipping"]},
}

# Tier thresholds
tier_thresholds = {"Silver": 0, "Gold": 1000, "Platinum": 2000}

# Error handling for unknown exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="Internal Server Error"), 500


# Endpoint: Get user benefits
@app.route('/api/users/<username>/benefits', methods=['GET'])
def get_user_benefits(username):
    """
    Retrieve the benefits for a specific user.
    """
    user = users.get(username)
    if not user:
        return jsonify(error="User not found"), 404

    return jsonify({
        "username": username,
        "spending": user["spending"],
        "tier": user["tier"],
        "discounts": user["discounts"]
    }), 200


# Endpoint: Update spending
@app.route('/api/users/<username>/spending', methods=['PUT'])
def update_spending(username):
    """
    Update a user's spending and possibly upgrade their tier.
    """
    user = users.get(username)
    if not user:
        return jsonify(error="User not found"), 404

    data = request.get_json()
    if not data or "spending" not in data:
        return jsonify(error="Invalid request data"), 400

    try:
        new_spending = float(data["spending"])
    except ValueError:
        return jsonify(error="Spending must be a number"), 400

    user["spending"] += new_spending

    # Update user tier based on spending
    for tier, threshold in sorted(tier_thresholds.items(), key=lambda x: x[1], reverse=True):
        if user["spending"] >= threshold:
            user["tier"] = tier
            break

    return jsonify({
        "message": "Spending updated successfully",
        "username": username,
        "spending": user["spending"],
        "tier": user["tier"]
    }), 200


# Endpoint: Access exclusive discounts
@app.route('/api/users/<username>/discounts', methods=['GET'])
def get_discounts(username):
    """
    Retrieve exclusive discounts for the user's tier.
    """
    user = users.get(username)
    if not user:
        return jsonify(error="User not found"), 404

    return jsonify({
        "username": username,
        "tier": user["tier"],
        "discounts": user["discounts"]
    }), 200


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
