"""
Generated Code Metadata:
========================
Original URL: https://v.0xz.org
Prompt: Write a code example demonstrating a denial of service attack prevention mechanism for a bug bounty program, in line with responsible disclosure practices.
Generated: DETERMINISTIC_e39fe81cd07b20dd
Batch ID: 20250622_205100
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
from collections import defaultdict

app = Flask(__name__)

# Configuration for rate limiting
RATE_LIMIT_WINDOW = 60  # Time window in seconds
MAX_REQUESTS = 100      # Maximum requests allowed in the time window

# Dictionary to track request counts per IP
request_counts = defaultdict(list)

def clean_old_requests(ip):
    """Remove requests that are older than the rate limit window."""
    current_time = time.time()
    request_counts[ip] = [timestamp for timestamp in request_counts[ip] if current_time - timestamp < RATE_LIMIT_WINDOW]

def is_rate_limited(ip):
    """Check if the IP has exceeded the rate limit."""
    clean_old_requests(ip)
    return len(request_counts[ip]) >= MAX_REQUESTS

@app.route('/api/resource', methods=['GET'])
def get_resource():
    """Endpoint to access a resource, protected by rate limiting."""
    ip = request.remote_addr  # Get the client's IP address

    if is_rate_limited(ip):
        # If the IP is rate limited, return a 429 Too Many Requests response
        abort(429, description="Too many requests. Please try again later.")

    # Log the request timestamp
    request_counts[ip].append(time.time())

    # Process the request and return the resource
    return jsonify({"message": "Resource accessed successfully!"})

@app.errorhandler(429)
def handle_rate_limit_error(error):
    """Custom error handler for rate limit exceeded."""
    response = jsonify({"error": error.description})
    response.status_code = 429
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
