"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancellationflights.com
Prompt: Write a code snippet for a web service that checks the status of user accounts and returns if they are active or suspended.
Generated: DETERMINISTIC_f4e19ff84eb93070
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Mock database of user accounts
USER_ACCOUNTS = {
    "user1": {"status": "active"},
    "user2": {"status": "suspended"},
    "user3": {"status": "active"},
    "user4": {"status": "suspended"},
}

@app.route('/check_status', methods=['GET'])
def check_status():
    """
    Endpoint to check the status of a user account.
    Query parameter: 'username' (string) - The username of the account to check.
    Returns:
        JSON response with the account status or an error message.
    """
    # Get the username from the query parameters
    username = request.args.get('username')

    # Validate the username parameter
    if not username:
        return jsonify({"error": "Missing 'username' query parameter"}), 400

    # Check if the user exists in the mock database
    user_account = USER_ACCOUNTS.get(username)
    if not user_account:
        return jsonify({"error": f"User '{username}' not found"}), 404

    # Return the user's account status
    return jsonify({"username": username, "status": user_account["status"]}), 200

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """
    Catch-all error handler for unexpected server errors.
    Returns:
        JSON response with an error message and status code 500.
    """
    return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for local testing; disable for production
    app.run(debug=True)
```
