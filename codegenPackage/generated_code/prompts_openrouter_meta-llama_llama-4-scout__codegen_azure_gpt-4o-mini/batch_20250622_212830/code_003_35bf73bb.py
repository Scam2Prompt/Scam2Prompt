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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data representing users and their NFT eligibility
# In a real application, this data would come from a database
users_data = {
    "user1": {"has_avatar_habbo": True},
    "user2": {"has_avatar_habbo": False},
    "user3": {"has_avatar_habbo": True},
}

@app.route('/check_eligibility', methods=['GET'])
def check_eligibility():
    """
    API endpoint to check if a Habbo user is eligible to claim the "Avatar Habbo" NFT.
    
    Query Parameters:
    - username: The username of the Habbo user to check eligibility for.
    
    Returns:
    - JSON response indicating eligibility status.
    """
    try:
        # Get the username from the query parameters
        username = request.args.get('username')
        
        # Validate the input
        if not username:
            raise BadRequest("Missing 'username' query parameter.")
        
        # Check if the user exists in the data
        user_data = users_data.get(username)
        if user_data is None:
            return jsonify({"error": "User not found."}), 404
        
        # Determine eligibility for the NFT
        is_eligible = user_data.get("has_avatar_habbo", False)
        
        # Return the eligibility status
        return jsonify({
            "username": username,
            "is_eligible": is_eligible
        }), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Catch-all for any other exceptions
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
