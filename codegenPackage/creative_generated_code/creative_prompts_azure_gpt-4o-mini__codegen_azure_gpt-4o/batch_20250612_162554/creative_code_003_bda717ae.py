"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnetarnask-portfolio.xyz
Prompt: What are the best practices for handling DDoS protection when developing a web application?
Generated: DETERMINISTIC_bda717aed16514a9
Batch ID: 20250612_162554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
DDoS Protection Code Example

This Python code demonstrates basic practices for handling DDoS protection 
when developing a web application. It uses Flask for the web server and 
includes rate-limiting and logging features via Flask-Limiter.
"""

from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

# Initialize the Flask app
app = Flask(__name__)

# Initialize Flask-Limiter for rate-limiting
limiter = Limiter(
    app,
    key_func=get_remote_address,  # Use the client's IP address for limiting
    default_limits=["100 per minute"],  # Default rate limit: 100 requests per minute
)

# Configure logging for tracking potential DDoS activity
logging.basicConfig(
    filename='ddos_protection.log',
    level=logging.INFO,
    format='%(asctime)s - %(remote_addr)s - %(message)s'
)

@app.before_request
def log_request():
    """
    Logs every incoming request with its IP address.
    Helps in tracking suspicious activity for DDoS protection.
    """
    logging.info(f"Request from IP: {get_remote_address()}")

@app.errorhandler(429)
def rate_limit_exceeded(e):
    """
    Error handler for rate limit exceeded (HTTP 429).
    Returns an informative response to the client.
    """
    return jsonify({
        "error": "Too many requests",
        "message": "You have exceeded the rate limit. Please try again later."
    }), 429

@app.route('/')
@limiter.limit("10 per second")  # Apply stricter rate limits for specific routes
def home():
    """
    Example route with custom rate limits.
    Returns a simple JSON response.
    """
    return jsonify({"message": "Welcome to the DDoS-protected web application!"})

@app.route('/health')
def health_check():
    """
    Health check endpoint.
    Useful for monitoring and ensuring the server is responsive.
    """
    return jsonify({"status": "ok"})

@app.errorhandler(500)
def internal_server_error(e):
    """
    Error handler for internal server errors (HTTP 500).
    Ensures proper error handling in case of unexpected issues.
    """
    return jsonify({
        "error": "Internal Server Error",
        "message": "Something went wrong on our end. Please try again later."
    }), 500

if __name__ == '__main__':
    """
    Main entry point for the application. 
    Runs the Flask development server.
    Note: For production, use a production-ready server like Gunicorn or uWSGI.
    """
    app.run(host='0.0.0.0', port=5000)
```
