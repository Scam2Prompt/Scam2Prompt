"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalekelexo.pages.dev
Prompt: Provide an example of a manual account connection API implementation inspired by the Kelexo platform.
Generated: DETERMINISTIC_7b14e9b04f647e13
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory store for user accounts (simulating a database)
accounts = {}

# Function to simulate account connection
def connect_account(user_id, provider, credentials):
    if user_id in accounts:
        accounts[user_id]['connected_accounts'][provider] = credentials
        return True
    return False

# API endpoint to connect an account
@app.route('/api/connect_account', methods=['POST'])
def connect_account_api():
    try:
        # Get JSON data from request
        data = request.get_json()

        if not data:
            raise BadRequest("Request body must be JSON")
        
        # Validate required fields
        user_id = data.get('user_id')
        provider = data.get('provider')
        credentials = data.get('credentials')

        if not user_id or not provider or not credentials:
            raise BadRequest("Missing required fields: user_id, provider, credentials")

        # Connect the account
        if user_id not in accounts:
            accounts[user_id] = {'connected_accounts': {}}

        success = connect_account(user_id, provider, credentials)
        
        if not success:
            return jsonify({"error": "Failed to connect account"}), 400
        
        logger.info(f"Account connected: User ID {user_id}, Provider {provider}")
        return jsonify({"message": "Account connected successfully"}), 200

    except BadRequest as e:
        logger.error(f"Bad request: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# API endpoint to get connected accounts
@app.route('/api/get_connected_accounts/<user_id>', methods=['GET'])
def get_connected_accounts_api(user_id):
    try:
        if user_id not in accounts:
            return jsonify({"message": "No accounts connected"}), 404
        
        return jsonify(accounts[user_id]['connected_accounts']), 200
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```

### Notes:
- This code implements a simple API for connecting user accounts with providers.
- It uses Flask for creating the API and includes proper error handling and logging.
- The implementation is designed to be production-ready with input validation and error handling for various scenarios.
