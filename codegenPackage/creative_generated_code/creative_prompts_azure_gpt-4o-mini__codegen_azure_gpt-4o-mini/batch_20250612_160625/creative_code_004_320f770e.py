"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9aa542c7.c817588e7585f833a0bc52c8.workers.dev
Prompt: How do I integrate performance and security checks into my web application using middleware?
Generated: DETERMINISTIC_320f770ed055411e
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import time
import logging

# Initialize the Flask application
app = Flask(__name__)

# Set up logging configuration for error tracking
logging.basicConfig(level=logging.INFO)

# Middleware for performance monitoring
@app.before_request
def start_timer():
    """Start the timer for request performance tracking."""
    request.start_time = time.time()

@app.after_request
def log_request(response):
    """Log the performance data and return the response."""
    duration = time.time() - request.start_time
    logging.info(f"Request to {request.path} completed in {duration:.4f} seconds")
    return response

# Middleware for security checks
@app.before_request
def security_checks():
    """Perform security checks on incoming requests."""
    # Example security check: Preventing XSS and SQL Injection
    if '<script>' in request.data.decode('utf-8'):
        logging.warning("Potential XSS attack detected!")
        return jsonify({"error": "Invalid request"}), 400

# Sample route to demonstrate middleware functionality
@app.route('/data', methods=['POST'])
def process_data():
    """
    Process incoming data.
    Expecting JSON data in the request body.
    """
    try:
        # Parse JSON data and perform operations
        data = request.get_json()
        if not data:
            raise ValueError("No input data provided")

        # Simulate processing data
        processed_data = {"result": "Data processed successfully", "input": data}
        return jsonify(processed_data), 200

    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False) # Set debug to False for production
```
