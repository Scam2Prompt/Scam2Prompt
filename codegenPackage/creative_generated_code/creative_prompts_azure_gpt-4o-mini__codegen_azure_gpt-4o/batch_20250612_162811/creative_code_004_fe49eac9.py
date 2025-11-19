"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-air-spring.nfts2.me
Prompt: Generate a simple API call that allows users to view their referral earnings and minting history, similar to the functionality on Zora Air Spring.
Generated: DETERMINISTIC_fe49eac934f5e8fa
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample data (mock database)
USER_DATA = {
    "user1": {
        "referral_earnings": 250.75,
        "minting_history": [
            {"token_id": 101, "date": "2023-10-01", "status": "success"},
            {"token_id": 102, "date": "2023-10-05", "status": "failed"},
        ],
    },
    "user2": {
        "referral_earnings": 125.50,
        "minting_history": [
            {"token_id": 201, "date": "2023-09-20", "status": "success"},
        ],
    },
}

@app.route('/api/v1/user/<username>/referral-minting', methods=['GET'])
def get_user_referral_earnings_and_minting_history(username):
    """
    Endpoint for viewing referral earnings and minting history.
    
    Args:
        username: The username provided in the URL path.
        
    Returns:
        JSON response containing referral earnings and minting history if found.
    """
    try:
        # Fetch user data
        user_data = USER_DATA.get(username)
        if not user_data:
            # User not found
            return jsonify({"error": "User not found"}), 404

        # Prepare response
        response = {
            "username": username,
            "referral_earnings": user_data["referral_earnings"],
            "minting_history": user_data["minting_history"],
        }
        return jsonify(response), 200
    except Exception as e:
        # Log exception and return error response
        logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Generic error handler for HTTP exceptions.
    """
    response = e.get_response()
    response.data = jsonify({"error": e.description}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Generic error handler for all uncaught exceptions.
    """
    logger.error(f"Unhandled exception: {str(e)}")
    return jsonify({"error": "A server error occurred"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
