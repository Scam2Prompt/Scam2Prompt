"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-vow.pages.dev
Prompt: How can I implement a feature to check user eligibility for claiming $VOW on a web application?
Generated: DETERMINISTIC_9641144c381ff899
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database of users for demonstration purposes
users_db = {
    "user1": {"id": 1, "name": "John Doe", "age": 25, "country": "US", "is_registered": True},
    "user2": {"id": 2, "name": "Jane Smith", "age": 17, "country": "US", "is_registered": True},
    "user3": {"id": 3, "name": "Alice Brown", "age": 30, "country": "UK", "is_registered": False},
}

# Eligibility criteria
def is_eligible(user):
    """
    Check if a user is eligible to claim $VOW based on the following criteria:
    - User must be registered
    - User must be 18 years or older
    - User must be from an eligible country (e.g., US or UK)
    """
    eligible_countries = {"US", "UK"}

    try:
        # Check registration status
        if not user.get("is_registered"):
            return False, "User is not registered."

        # Check age
        if user.get("age") < 18:
            return False, "User must be 18 years or older to claim $VOW."

        # Check country eligibility
        if user.get("country") not in eligible_countries:
            return False, "User is not from an eligible country."

        # User is eligible
        return True, "User is eligible to claim $VOW."
    
    except KeyError as e:
        return False, f"Missing required user information: {e}"

@app.route('/check-eligibility', methods=['POST'])
def check_eligibility():
    """
    API endpoint to check user eligibility for claiming $VOW.
    Expects a JSON payload with `username`.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()

        if not data or "username" not in data:
            return jsonify({"success": False, "message": "Invalid request. 'username' is required."}), 400

        username = data["username"]

        # Lookup user in the database
        user = users_db.get(username)

        if not user:
            return jsonify({"success": False, "message": "User not found."}), 404

        # Check eligibility
        eligible, message = is_eligible(user)

        return jsonify({"success": eligible, "message": message}), 200 if eligible else 403

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
