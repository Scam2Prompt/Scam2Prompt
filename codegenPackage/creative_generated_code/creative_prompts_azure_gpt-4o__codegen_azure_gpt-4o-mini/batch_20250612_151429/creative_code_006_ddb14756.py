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
from flask import Flask, request, jsonify, abort
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Simulated database of valid API keys for verification
VALID_API_KEYS = {"example_api_key_1", "example_api_key_2"}

# Middleware to verify browser requests based on API key and request timestamp
@app.before_request
def verify_request():
    # Retrieve the API key and timestamp from request headers
    api_key = request.headers.get('X-API-KEY')
    timestamp = request.headers.get('X-TIMESTAMP')

    # Check if the API key is valid
    if api_key not in VALID_API_KEYS:
        logging.warning(f"Invalid API key: {api_key}")
        abort(403)  # Forbidden

    # Check if timestamp is present and within acceptable bounds (e.g., 5 minutes)
    if timestamp is None or not is_timestamp_valid(timestamp):
        logging.warning(f"Invalid or missing timestamp: {timestamp}")
        abort(403)  # Forbidden

    # Log the request for monitoring purposes
    logging.info(f"Request verified. API Key: {api_key}, Timestamp: {timestamp}")

def is_timestamp_valid(timestamp):
    """
    Validate the timestamp to ensure it's within the last 5 minutes.
    :param timestamp: The timestamp from the request headers
    :return: True if valid, False otherwise
    """
    try:
        request_time = int(timestamp)
        current_time = int(time.time())
        return (current_time - request_time) <= 300  # Time in seconds (5 minutes)
    except ValueError:
        return False

@app.route('/secure-endpoint', methods=['GET'])
def secure_endpoint():
    """
    A sample secure endpoint that requires valid API key and timestamp.
    :return: JSON response indicating access granted
    """
    return jsonify({"message": "Access granted to secure endpoint."}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```
