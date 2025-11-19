"""
Generated Code Metadata:
========================
Original URL: https://cancellationflights.com
Prompt: How can I create an API endpoint to handle account suspension requests in a RESTful service?
Generated: DETERMINISTIC_fe8281118e2876cc
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database for demonstration purposes
accounts_db = {
    1: {"username": "user1", "suspended": False},
    2: {"username": "user2", "suspended": False},
    3: {"username": "user3", "suspended": False},
}

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and return JSON responses."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.route('/api/suspend_account', methods=['POST'])
def suspend_account():
    """
    API endpoint to suspend an account.
    Expects a JSON payload with 'account_id'.
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data or 'account_id' not in data:
            return jsonify({"error": "Bad Request", "message": "Missing 'account_id' in request body"}), 400

        account_id = data['account_id']

        # Validate account ID
        if account_id not in accounts_db:
            return jsonify({"error": "Not Found", "message": f"Account with ID {account_id} not found"}), 404

        # Suspend the account
        account = accounts_db[account_id]
        if account['suspended']:
            return jsonify({"error": "Conflict", "message": f"Account with ID {account_id} is already suspended"}), 409

        account['suspended'] = True

        # Return success response
        return jsonify({"message": f"Account with ID {account_id} has been suspended successfully"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
