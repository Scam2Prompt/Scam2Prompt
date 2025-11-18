"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitcoin-generator.com
Prompt: Write code to implement a feature for accessing a trading account from multiple devices, ensuring compatibility with web browsers, tablets, and mobile devices, as outlined in the bitcoin generator description.
Generated: DETERMINISTIC_4529430e9cea8e33
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for multiple device compatibility
app.secret_key = 'your_secret_key'  # Secret key for managing sessions

# In-memory database for demonstration (Replace with a proper database in production)
users = {
    "example_user": {
        "password_hash": generate_password_hash("example_password"),
        "account_balance": 0.0
    }
}

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login from multiple devices: web, tablet, mobile.
    Expects JSON input with 'username' and 'password'.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Check if user exists
        user = users.get(username)
        if not user:
            return jsonify({"error": "Invalid username or password"}), 401

        # Verify password
        if not check_password_hash(user['password_hash'], password):
            return jsonify({"error": "Invalid username or password"}), 401

        # Create session for the user
        session['username'] = username
        return jsonify({"message": "Login successful"}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred during login", "details": str(e)}), 500


# Endpoint for accessing account details
@app.route('/account', methods=['GET'])
def account():
    """
    Provides account details for authenticated users.
    """
    try:
        # Check session
        username = session.get('username')
        if not username:
            return jsonify({"error": "Unauthorized access"}), 401

        # Fetch user account details
        user = users.get(username)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Return account information
        return jsonify({
            "username": username,
            "account_balance": user['account_balance']
        }), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while accessing the account", "details": str(e)}), 500


# Endpoint for logout
@app.route('/logout', methods=['POST'])
def logout():
    """
    Logs out the current user by clearing the session.
    """
    try:
        session.pop('username', None)
        return jsonify({"message": "Logout successful"}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred during logout", "details": str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    # Use a production-ready server like Gunicorn for deployment
    app.run(debug=True)
```
