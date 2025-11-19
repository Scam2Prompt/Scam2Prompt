"""
Generated Code Metadata:
========================
Original URL: https://66789.pages.dev
Prompt: What are common security measures used to protect websites from bots and scraping, and how do they impact user experience?
Generated: DETERMINISTIC_e138813a42f04269
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# A simple in-memory store to track requests
request_log = {}

# Rate limit configuration
RATE_LIMIT = 100  # Max requests per minute
TIME_WINDOW = 60  # Time window in seconds

def is_rate_limited(ip):
    """Check if the IP address has exceeded the rate limit."""
    current_time = time.time()
    if ip not in request_log:
        request_log[ip] = []
    
    # Remove timestamps older than the time window
    request_log[ip] = [timestamp for timestamp in request_log[ip] if timestamp > current_time - TIME_WINDOW]
    
    # Check if the request count exceeds the limit
    if len(request_log[ip]) >= RATE_LIMIT:
        return True
    
    # Log the current request
    request_log[ip].append(current_time)
    return False

@app.route('/api/data', methods=['GET'])
def get_data():
    """Endpoint to retrieve data, protected against bots and scraping."""
    user_ip = request.remote_addr
    
    # Check for rate limiting
    if is_rate_limited(user_ip):
        abort(429, description="Too Many Requests: Rate limit exceeded.")
    
    # Simulate data retrieval
    data = {"message": "Here is your data!"}
    
    return jsonify(data)

@app.errorhandler(429)
def handle_rate_limit_error(error):
    """Handle rate limit errors."""
    response = jsonify({"error": error.description})
    response.status_code = 429
    return response

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```

This code implements a simple Flask web application that includes rate limiting to protect against bots and scraping. It tracks requests by IP address and limits the number of requests to 100 per minute. If the limit is exceeded, it returns a 429 Too Many Requests error.
