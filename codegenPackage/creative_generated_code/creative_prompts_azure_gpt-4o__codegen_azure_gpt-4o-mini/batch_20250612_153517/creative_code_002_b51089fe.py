"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openweb-3ua.pages.dev
Prompt: Recommend a library or API for managing cryptographic tokens and demonstrate how it can be integrated into a platform like Opepen for tracking submissions and votes.
Generated: DETERMINISTIC_b51089feb9808e89
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import json
import hashlib
import hmac
import time
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

# Create a Flask application
app = Flask(__name__)

# Configuration for HMAC and token expiration
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
TOKEN_EXPIRATION = 3600  # Token valid for 1 hour

# Function to generate a cryptographic token
def generate_token(user_id):
    """
    Generates a secure token for a given user_id.
    
    Args:
        user_id (str): The user's unique identifier.

    Returns:
        str: A hashed token that can be used to authenticate the user.
    """
    timestamp = int(time.time())
    message = f"{user_id}:{timestamp}"
    token = hmac.new(SECRET_KEY.encode(), message.encode(), hashlib.sha256).hexdigest()
    return json.dumps({"token": token, "timestamp": timestamp})

# Function to validate the token
def validate_token(token, user_id):
    """
    Validates the provided token for a given user_id.
    
    Args:
        token (str): The token to validate.
        user_id (str): The user's unique identifier.

    Returns:
        bool: True if the token is valid, False otherwise.
    """
    try:
        token_data = json.loads(token)
        expected_token = hmac.new(
            SECRET_KEY.encode(),
            f"{user_id}:{token_data['timestamp']}".encode(),
            hashlib.sha256
        ).hexdigest()

        # Check if the timestamp is valid
        if int(time.time()) - token_data['timestamp'] > TOKEN_EXPIRATION:
            return False

        return hmac.compare_digest(expected_token, token_data['token'])
    except (KeyError, ValueError, TypeError):
        return False

@app.route('/submit', methods=['POST'])
def submit_submission():
    """
    Endpoint to submit a new submission.
    
    Request:
        - JSON containing user_id and submission_data
        - Header: Authorization containing user token

    Returns:
        JSON response containing success/failure message.
    """
    try:
        # Get user token from request headers
        user_token = request.headers.get('Authorization')
        if user_token is None:
            raise BadRequest("Authorization header is missing.")

        # Get submission data from request body
        submission_data = request.json
        user_id = submission_data.get('user_id')
        if not user_id or 'submission_data' not in submission_data:
            raise BadRequest("user_id and submission_data are required.")
        
        # Validate the user token
        if not validate_token(user_token, user_id):
            raise BadRequest("Invalid or expired token.")

        # Here, you can process the submission data (e.g., save to a database)
        return jsonify({"message": "Submission successful!"}), 200
    
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/get_token/<user_id>', methods=['GET'])
def get_token(user_id):
    """
    Endpoint to retrieve a cryptographic token for a given user_id.
    
    Args:
        user_id (str): The user's unique identifier.

    Returns:
        JSON containing the generated token.
    """
    try:
        token = generate_token(user_id)
        return jsonify(json.loads(token)), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Make sure to set the `SECRET_KEY` environment variable before running the application. This code provides endpoints to generate tokens and submit data securely while handling errors appropriately.
