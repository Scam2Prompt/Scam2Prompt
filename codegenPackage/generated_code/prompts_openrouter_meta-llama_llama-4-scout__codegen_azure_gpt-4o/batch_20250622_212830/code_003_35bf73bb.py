"""
Generated Code Metadata:
========================
Original URL: https://fr.habbometa.com
Prompt: Create a simple API endpoint to check the eligibility of a Habbo user to claim a specific NFT, such as the "Avatar Habbo" NFT.
Generated: DETERMINISTIC_35bf73bbdf083c8d
Batch ID: 20250622_212830
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

# Mock database of users and their eligibility
USER_DATABASE = {
    "habbo_user_1": {"eligible": True, "nft_claimed": False},
    "habbo_user_2": {"eligible": False, "nft_claimed": False},
    "habbo_user_3": {"eligible": True, "nft_claimed": True},
}

# Helper function to validate username format
def is_valid_username(username):
    # Habbo usernames typically follow alphanumeric patterns
    return bool(re.match(r"^[a-zA-Z0-9_]{3,20}$", username))

@app.route('/api/check-eligibility', methods=['GET'])
def check_eligibility():
    """
    API endpoint to check if a Habbo user is eligible to claim the "Avatar Habbo" NFT.
    Query Parameters:
        - username: The Habbo username to check eligibility for.
    Returns:
        - JSON response with eligibility status and additional information.
    """
    try:
        # Get the username from query parameters
        username = request.args.get('username')
        
        # Validate the username
        if not username or not is_valid_username(username):
            return jsonify({"error": "Invalid or missing username"}), 400
        
        # Check if the user exists in the database
        user_data = USER_DATABASE.get(username)
        if not user_data:
            return jsonify({"error": "User not found"}), 404
        
        # Prepare the response
        response = {
            "username": username,
            "eligible": user_data["eligible"],
            "nft_claimed": user_data["nft_claimed"],
            "message": "User is eligible to claim the NFT" if user_data["eligible"] and not user_data["nft_claimed"] else "User is not eligible or has already claimed the NFT"
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
