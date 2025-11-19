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
import time
from functools import wraps
from flask import Flask, request, jsonify
import re
import logging
from werkzeug.middleware.proxy_fix import ProxyFix

# Initialize Flask application
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security headers middleware
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

# Performance monitoring decorator
def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"Performance: {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Input validation decorator
def validate_input(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in expected_args:
                if arg not in request.json:
                    return jsonify({"error": f"Missing required parameter: {arg}"}), 400
                
                # Basic XSS protection
                if isinstance(request.json[arg], str):
                    if re.search(r'<script.*?>.*?</script>', request.json[arg], re.IGNORECASE):
                        return jsonify({"error": "Invalid input detected"}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example secure and performant endpoint
@app.route('/api/data', methods=['POST'])
@measure_performance
@validate_input('username', 'email')
def process_data():
    try:
        data = request.json
        # Simulate processing
        time.sleep(0.1)
        
        # Validate email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', data['email']):
            return jsonify({"error": "Invalid email format"}), 400
        
        # Return processed data
        return jsonify({
            "status": "success",
            "username": data['username'],
            "email": data['email']
        }), 200
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Rate limiting middleware (simplified example)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
