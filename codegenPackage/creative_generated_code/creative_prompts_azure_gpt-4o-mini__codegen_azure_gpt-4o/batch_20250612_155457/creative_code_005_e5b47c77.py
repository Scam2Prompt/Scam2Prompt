"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipmbway.pages.dev
Prompt: How can I develop an API endpoint to retrieve the latest proof of reserves for IPMB's gold-backed tokens?
Generated: DETERMINISTIC_e5b47c779e38fc11
Batch ID: 20250612_155457
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
import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Mock data for IPMB's gold-backed tokens proof of reserves
PROOF_OF_RESERVES = {
    "gold_backed_tokens": [
        {
            "token_name": "GoldTokenA",
            "reserve_amount": 1000,  # Measured in ounces
            "last_verified": "2023-10-01T10:00:00Z"
        },
        {
            "token_name": "GoldTokenB",
            "reserve_amount": 1500,  # Measured in ounces
            "last_verified": "2023-10-02T15:30:00Z"
        }
    ]
}

@app.route('/api/proof-of-reserves/latest', methods=['GET'])
def get_latest_proof_of_reserves():
    """
    API endpoint to retrieve the latest proof of reserves for IPMB's gold-backed tokens.
    Returns proof of reserves data in JSON format.
    """
    try:
        # Fetch the latest proof of reserves data
        latest_proof = PROOF_OF_RESERVES
        
        # Log the request (for monitoring purposes)
        logging.info(f"Proof of reserves data requested at {datetime.datetime.utcnow()} UTC.")
        
        # Return the data as JSON response
        return jsonify({
            "status": "success",
            "data": latest_proof
        }), 200
    except Exception as e:
        # Log the error
        logging.error(f"An error occurred: {str(e)}")
        
        # Return an error response
        return jsonify({
            "status": "error",
            "message": "Failed to fetch proof of reserves data."
        }), 500


# Error handler for handling 404 errors
@app.errorhandler(404)
def resource_not_found(e):
    """
    Error handler for 404 Not Found.
    """
    return jsonify({
        "status": "error",
        "message": "Resource not found."
    }), 404


# Error handler for handling 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    """
    Error handler for 500 Internal Server Error.
    """
    return jsonify({
        "status": "error",
        "message": "Internal server error."
    }), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
