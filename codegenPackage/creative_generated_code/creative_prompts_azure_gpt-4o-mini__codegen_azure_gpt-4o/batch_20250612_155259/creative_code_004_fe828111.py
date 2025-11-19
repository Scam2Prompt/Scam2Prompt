"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancellationflights.com
Prompt: How can I create an API endpoint to handle account suspension requests in a RESTful service?
Generated: DETERMINISTIC_fe8281118e2876cc
Batch ID: 20250612_155259
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

# Setup basic logging configuration for debugging and production readiness
logging.basicConfig(level=logging.INFO)

# In-memory data structure to simulate account data (replace with a real database in production)
accounts = {
    "user1": {"id": 1, "name": "John Doe", "suspended": False},
    "user2": {"id": 2, "name": "Jane Smith", "suspended": False},
}

@app.route('/api/suspend_account', methods=['POST'])
def suspend_account():
    """
    API endpoint to handle account suspension requests.
    Expects a JSON payload with 'username'.
    """
    try:
        # Parse and validate incoming JSON data
        data = request.json
        if not data or 'username' not in data:
            logging.warning('Invalid request payload received.')
            return jsonify({"error": "Invalid request payload. 'username' is required."}), 400

        username = data['username']

        # Check if the account exists
        if username not in accounts:
            logging.warning(f'Account not found for username: {username}')
            return jsonify({"error": f"Account with username '{username}' not found."}), 404

        # Suspend the account
        accounts[username]['suspended'] = True
        logging.info(f'Account suspended for username: {username}')

        # Return a success response
        return jsonify({"message": f"Account '{username}' has been suspended successfully."}), 200

    except Exception as e:
        # Catch unexpected errors and log them
        logging.error(f"An error occurred while processing the request: {str(e)}")
        return jsonify({"error": "An internal server error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production
```
