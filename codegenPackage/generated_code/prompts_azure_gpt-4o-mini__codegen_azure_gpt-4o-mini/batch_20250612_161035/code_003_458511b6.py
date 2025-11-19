"""
Generated Code Metadata:
========================
Original URL: https://daddysolana.info
Prompt: Generate an example of a web application that includes performance and security features similar to those provided by Cloudflare.
Generated: DETERMINISTIC_458511b6eee50477
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
import logging
import os

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure logging
logging.basicConfig(level=logging.INFO)

# Middleware for security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

# Rate limiting decorator
def rate_limit(limit):
    def decorator(f):
        f.requests = 0
        f.limit = limit

        def wrapper(*args, **kwargs):
            if f.requests >= f.limit:
                return jsonify({"error": "Too many requests"}), 429
            f.requests += 1
            return f(*args, **kwargs)

        return wrapper
    return decorator

@app.route('/api/data', methods=['GET'])
@rate_limit(limit=100)  # Limit to 100 requests
def get_data():
    """
    Endpoint to retrieve data.
    Returns a JSON response with sample data.
    """
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Handle HTTP exceptions and return a JSON response.
    """
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    """
    Handle general exceptions and return a JSON response.
    """
    logging.error(f"An error occurred: {str(e)}")
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the application with production settings
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```

### Requirements
To run this code, ensure you have the following Python packages installed:
```bash
pip install Flask Flask-Cors
```

### Note
This code is a basic example of a Flask web application with security headers, rate limiting, and error handling. For production use, consider deploying it behind a WSGI server like Gunicorn and using HTTPS.
