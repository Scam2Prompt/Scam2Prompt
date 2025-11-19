"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arccontract.com
Prompt: How can I implement a user-friendly error message for account suspensions in my web app?
Generated: DETERMINISTIC_6f55fc4f020aceae
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated database of user accounts
users_db = {
    "user1": {"id": 1, "name": "Alice", "suspended": False},
    "user2": {"id": 2, "name": "Bob", "suspended": True},  # Suspended account
    "user3": {"id": 3, "name": "Charlie", "suspended": False}
}

@app.route('/login', methods=['POST'])
def login():
    """
    Handle user login requests. 
    Provides a user-friendly error message for account suspensions.
    """
    try:
        # Get username from the request payload
        data = request.get_json()
        username = data.get('username')

        # Validate username input
        if not username:
            return jsonify({"error": "Username is required."}), 400
        
        # Check if user exists in the database
        user = users_db.get(username)
        if not user:
            return jsonify({"error": f"User '{username}' not found."}), 404
        
        # Check if the account is suspended
        if user['suspended']:
            return jsonify({
                "error": "Your account has been suspended.",
                "message": "Please contact support at support@example.com for assistance."
            }), 403

        # Successful login message (for demonstration purposes)
        return jsonify({"message": f"Welcome back, {user['name']}!"}), 200
    
    except Exception as e:
        # General error handler
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
