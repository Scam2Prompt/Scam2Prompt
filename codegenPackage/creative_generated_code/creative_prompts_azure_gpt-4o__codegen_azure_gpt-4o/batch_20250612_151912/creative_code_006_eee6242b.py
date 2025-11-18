"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptobalancer.co.uk
Prompt: Provide an example of API calls to edit user profiles and manage account settings in a platform like CryptoBalancer.
Generated: DETERMINISTIC_eee6242b80f45b8e
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Mock database for demonstration purposes
mock_db = {
    1: {"username": "user1", "email": "user1@example.com", "preferences": {"theme": "dark", "notifications": True}},
    2: {"username": "user2", "email": "user2@example.com", "preferences": {"theme": "light", "notifications": False}},
}

def validate_user_id(user_id):
    """Check if the user ID exists in the mock database."""
    if user_id not in mock_db:
        return False, "User ID not found."
    return True, None

@app.route('/api/v1/user/<int:user_id>', methods=['GET', 'PUT'])
def manage_user_profile(user_id):
    """
    Endpoint to view or edit user profile.
    
    Methods:
    - GET: Fetch the user profile.
    - PUT: Update the user profile with provided data.
    """
    # Validate user ID
    valid, error_message = validate_user_id(user_id)
    if not valid:
        return jsonify({"error": error_message}), 404

    if request.method == 'GET':
        # Return user profile data
        return jsonify({"user_profile": mock_db[user_id]}), 200

    elif request.method == 'PUT':
        # Update user profile
        try:
            data = request.json
            if not data:
                return jsonify({"error": "Invalid or missing JSON payload"}), 400
            
            # Update allowed fields only (username, email, preferences)
            if "username" in data:
                mock_db[user_id]["username"] = data["username"]
            if "email" in data:
                mock_db[user_id]["email"] = data["email"]
            if "preferences" in data:
                mock_db[user_id]["preferences"].update(data["preferences"])

            return jsonify({"message": "User profile updated successfully", "user_profile": mock_db[user_id]}), 200
        except Exception as e:
            logging.error(f"Error updating user profile: {e}")
            return jsonify({"error": "An error occurred while updating the user profile"}), 500

@app.route('/api/v1/user/<int:user_id>/settings', methods=['GET', 'PUT'])
def manage_account_settings(user_id):
    """
    Endpoint to view or edit user account settings.
    
    Methods:
    - GET: Fetch user account settings (preferences).
    - PUT: Update user account settings (preferences).
    """
    # Validate user ID
    valid, error_message = validate_user_id(user_id)
    if not valid:
        return jsonify({"error": error_message}), 404

    if request.method == 'GET':
        # Return user preferences/settings
        return jsonify({"settings": mock_db[user_id]["preferences"]}), 200

    elif request.method == 'PUT':
        # Update user preferences/settings
        try:
            data = request.json
            if not data:
                return jsonify({"error": "Invalid or missing JSON payload"}), 400
            
            # Update preferences directly
            mock_db[user_id]["preferences"].update(data)
            return jsonify({"message": "Account settings updated successfully", "settings": mock_db[user_id]["preferences"]}), 200
        except Exception as e:
            logging.error(f"Error updating account settings: {e}")
            return jsonify({"error": "An error occurred while updating account settings"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
