"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketdarkzone.uk
Prompt: Write a server-side script to verify browser requests before granting access, inspired by the Darkzone Security approach.
Generated: DETERMINISTIC_ddb1475685c44319
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
import hashlib
import time

app = Flask(__name__)

# Secret key for request verification (should be kept secure)
SECRET_KEY = "your_secret_key_here"

# Expiry time for request validation in seconds
REQUEST_EXPIRY_TIME = 300  # 5 minutes

def generate_request_hash(data, timestamp, secret_key):
    """
    Generate a hash for verifying the request.

    :param data: Data from the request to be hashed
    :param timestamp: Timestamp from the request
    :param secret_key: Secret key for hashing
    :return: Hexadecimal hash string
    """
    hash_string = f"{data}{timestamp}{secret_key}"
    return hashlib.sha256(hash_string.encode()).hexdigest()

@app.route('/protected-endpoint', methods=['POST'])
def protected_endpoint():
    """
    Protected endpoint to verify browser requests.

    Expected JSON payload:
    {
        "data": "<request data>",
        "timestamp": "<timestamp>",
        "hash": "<hash>"
    }

    :return: JSON response
    """
    try:
        # Extract data from the request
        request_data = request.json
        if not request_data:
            return jsonify({"error": "Invalid request format"}), 400

        # Validate required fields
        data = request_data.get("data")
        timestamp = request_data.get("timestamp")
        request_hash = request_data.get("hash")
        if not all([data, timestamp, request_hash]):
            return jsonify({"error": "Missing required fields"}), 400

        # Check if timestamp is within the allowed time frame
        current_time = int(time.time())
        if abs(current_time - int(timestamp)) > REQUEST_EXPIRY_TIME:
            return jsonify({"error": "Request timestamp expired"}), 403

        # Generate server-side hash for comparison
        server_hash = generate_request_hash(data, timestamp, SECRET_KEY)

        # Verify the request hash
        if server_hash != request_hash:
            return jsonify({"error": "Invalid request hash"}), 403

        # If verification passes, grant access
        return jsonify({"message": "Access granted"}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
