"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://24397033.4d1df63187c716fb9bc6ff22.workers.dev
Prompt: Generate a code example that demonstrates how to implement performance and security checks in a web application.
Generated: DETERMINISTIC_2cf393a90bae23e5
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: web_app_security_performance.py

from flask import Flask, request, jsonify
import time
import logging
import re

app = Flask(__name__)

# Setting up logging for security and performance monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Regular expression for validating input (e.g., user input sanitation)
INPUT_SANITIZATION_REGEX = re.compile(r'^[a-zA-Z0-9_]+$')

# Endpoint performance metrics
endpoint_metrics = {}

@app.before_request
def start_timer():
    """
    Middleware to start a timer for measuring request performance.
    """
    request.start_time = time.time()

@app.after_request
def log_request(response):
    """
    Middleware to log the request details and performance metrics.
    """
    # Calculate time taken for the request
    duration = time.time() - request.start_time
    endpoint = request.path
    method = request.method

    # Update performance metrics for the endpoint
    if endpoint not in endpoint_metrics:
        endpoint_metrics[endpoint] = []
    endpoint_metrics[endpoint].append(duration)

    # Log request details
    logging.info(f"Endpoint: {endpoint}, Method: {method}, Duration: {duration:.2f}s, Status: {response.status_code}")

    return response

@app.route('/submit', methods=['POST'])
def submit_data():
    """
    Example endpoint that performs security checks and handles data submission.
    """
    try:
        # Get data from the request
        data = request.json

        if not data or 'username' not in data:
            logging.warning("Invalid request: Missing 'username' field.")
            return jsonify({"error": "Invalid input"}), 400

        username = data['username']

        # Validate input using regex (security check)
        if not INPUT_SANITIZATION_REGEX.match(username):
            logging.warning(f"Security alert: Malicious input detected - {username}")
            return jsonify({"error": "Invalid characters in input"}), 400

        # Process data (dummy processing for demonstration)
        logging.info(f"Processing data for user: {username}")
        return jsonify({"message": f"Data successfully processed for {username}."}), 200

    except Exception as e:
        # General error handling
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """
    Endpoint to retrieve performance metrics for each endpoint.
    """
    try:
        metrics = {
            endpoint: {
                "request_count": len(durations),
                "average_duration": sum(durations) / len(durations) if durations else 0,
                "max_duration": max(durations) if durations else 0
            }
            for endpoint, durations in endpoint_metrics.items()
        }

        return jsonify(metrics), 200

    except Exception as e:
        # General error handling
        logging.error(f"An error occurred while fetching metrics: {str(e)}")
        return jsonify({"error": "Unable to fetch metrics at this time."}), 500

if __name__ == '__main__':
    # Run the application securely
    app.run(host='127.0.0.1', port=5000, debug=False)
```
