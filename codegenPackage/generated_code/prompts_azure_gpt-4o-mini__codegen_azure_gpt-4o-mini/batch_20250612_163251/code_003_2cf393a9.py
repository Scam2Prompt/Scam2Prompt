"""
Generated Code Metadata:
========================
Original URL: https://24397033.4d1df63187c716fb9bc6ff22.workers.dev
Prompt: Generate a code example that demonstrates how to implement performance and security checks in a web application.
Generated: DETERMINISTIC_2cf393a90bae23e5
Batch ID: 20250612_163251
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
import time
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Middleware for performance monitoring
@app.before_request
def start_timer():
    """Start a timer before processing the request."""
    request.start_time = time.time()

@app.after_request
def log_performance(response):
    """Log the performance of the request after processing."""
    duration = time.time() - request.start_time
    logging.info(f"Request to {request.path} took {duration:.2f} seconds")
    return response

# Middleware for security checks
@app.before_request
def security_checks():
    """Perform security checks on incoming requests."""
    # Example: Check for a specific header
    if 'X-API-KEY' not in request.headers:
        logging.warning("Missing API key")
        return jsonify({"error": "Unauthorized"}), 401

    # Example: Rate limiting (simple implementation)
    if request.remote_addr in app.config['BLOCKED_IPS']:
        logging.warning(f"Blocked IP: {request.remote_addr}")
        return jsonify({"error": "Forbidden"}), 403

# Example of a simple in-memory rate limiting
app.config['BLOCKED_IPS'] = set()

@app.route('/data', methods=['GET'])
def get_data():
    """Endpoint to retrieve data."""
    return jsonify({"data": "Here is your data!"})

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions and return a JSON response."""
    response = e.get_response()
    response.data = jsonify({"error": e.name, "description": e.description}).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    """Handle general exceptions and return a JSON response."""
    logging.error(f"An error occurred: {str(e)}")
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Set the environment variable for production
    app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
    app.run(host='0.0.0.0', port=5000)
```
