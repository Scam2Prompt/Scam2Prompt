"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5f8d9eb3.d10f05e59e81e2f9cfa61b7e.workers.dev
Prompt: How do I integrate performance monitoring with security checks in my web application?
Generated: DETERMINISTIC_9cc9c8f9faeaf11e
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import time
import logging
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)

# Set up logging for performance monitoring and security checks
logging.basicConfig(level=logging.INFO)

# Custom exception for unauthorized access
class UnauthorizedAccessException(Exception):
    pass

# Middleware for performance monitoring and security checks
def monitor_performance_and_security(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start performance tracking
        start_time = time.time()
        
        # Security check: Simple example of an API key check
        api_key = request.headers.get('X-API-KEY')
        if api_key != 'your_secure_api_key':
            logging.warning(f"Unauthorized access attempt from {request.remote_addr}")
            raise UnauthorizedAccessException("Unauthorized access. Invalid API key.")

        # Call the original function
        response = func(*args, **kwargs)

        # End performance tracking
        end_time = time.time()
        processing_time = end_time - start_time
        logging.info(f"Processed request in {processing_time:.4f} seconds")

        return response
    return wrapper

@app.route('/secure-data', methods=['GET'])
@monitor_performance_and_security
def get_secure_data():
    """Endpoint to retrieve secure data."""
    data = {
        "message": "This is secure data.",
        "data": [1, 2, 3, 4, 5]
    }
    return jsonify(data), 200

@app.errorhandler(UnauthorizedAccessException)
def handle_unauthorized_access(error):
    """Handle unauthorized access errors."""
    response = jsonify({"error": str(error)})
    return response, 403

@app.errorhandler(Exception)
def handle_generic_error(error):
    """Handle all other exceptions."""
    logging.error(f"Internal server error: {str(error)}")
    response = jsonify({"error": "Internal server error"})
    return response, 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```
