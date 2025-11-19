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
from flask import Flask, request, jsonify
import time
import logging
import functools
import os
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Set up logging for performance monitoring and error handling
logging.basicConfig(level=logging.INFO)

# Performance check decorator
def performance_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            duration = end_time - start_time
            logging.info(f"Performance: {func.__name__} took {duration:.4f} seconds")
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper

# Security check middleware
@app.before_request
def security_check():
    # Simple security check: Validate API key
    api_key = request.headers.get('x-api-key')
    expected_api_key = os.getenv('EXPECTED_API_KEY')

    if api_key != expected_api_key:
        logging.warning("Invalid API Key")
        return jsonify({"error": "Unauthorized access"}), 401

@app.route('/process_data', methods=['POST'])
@performance_check
def process_data():
    """Endpoint to process data."""
    try:
        data = request.json
        if not data:
            raise ValueError("No data provided")

        # Simulate data processing
        # (e.g., save to database, perform calculations, etc.)
        # This is just a placeholder for actual processing logic.
        logging.info("Data processed successfully.")
        
        return jsonify({"message": "Data processed successfully"}), 200
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions and format the response."""
    logging.error(f"HTTPException: {str(e)}")
    return jsonify({"error": e.description}), e.code

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
