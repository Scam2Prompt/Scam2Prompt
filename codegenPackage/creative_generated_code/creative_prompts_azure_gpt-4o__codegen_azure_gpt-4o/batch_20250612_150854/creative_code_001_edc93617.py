"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-unity-profit.com
Prompt: Create a REST API for a platform like Juros Xyro that allows users to register, input their preferences, and receive matched investment education firms.
Generated: DETERMINISTIC_edc93617bfa4fdac
Batch ID: 20250612_150854
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
import uuid

app = Flask(__name__)

# In-memory data storage (for simplicity)
users = {}
investment_education_firms = [
    {"id": "1", "name": "Firm A", "specialization": ["stocks", "bonds"]},
    {"id": "2", "name": "Firm B", "specialization": ["real estate", "commodities"]},
    {"id": "3", "name": "Firm C", "specialization": ["crypto", "stocks"]},
]

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    """
    try:
        # Validate input
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({"error": "Missing required fields: name, email"}), 400

        # Generate a unique user ID
        user_id = str(uuid.uuid4())
        user_data = {
            "id": user_id,
            "name": data["name"],
            "email": data["email"],
            "preferences": data.get("preferences", [])
        }

        # Save user to in-memory storage
        users[user_id] = user_data

        return jsonify({"message": "User registered successfully", "user": user_data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/update_preferences/<user_id>', methods=['PUT'])
def update_preferences(user_id):
    """
    Endpoint to update user preferences.
    """
    try:
        # Validate if user exists
        user = users.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Validate input
        data = request.json
        if not data or 'preferences' not in data:
            return jsonify({"error": "Missing required field: preferences"}), 400

        # Update preferences
        user["preferences"] = data["preferences"]

        return jsonify({"message": "Preferences updated successfully", "user": user}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_matches/<user_id>', methods=['GET'])
def get_matches(user_id):
    """
    Endpoint to get matching investment education firms based on user preferences.
    """
    try:
        # Validate if user exists
        user = users.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Match firms based on preferences
        preferences = set(user.get("preferences", []))
        matched_firms = [
            firm for firm in investment_education_firms
            if preferences.intersection(set(firm["specialization"]))
        ]

        return jsonify({"message": "Matches found", "matches": matched_firms}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    """
    return jsonify({"error": str(e)}), e.code


@app.errorhandler(Exception)
def handle_general_exception(e):
    """
    Global error handler for uncaught exceptions.
    """
    return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
