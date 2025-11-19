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
import time
from flask import Flask, request, jsonify
from functools import wraps
from collections import defaultdict

app = Flask(__name__)

# Configuration for rate limiting
RATE_LIMIT_WINDOW = 60  # seconds
RATE_LIMIT_REQUESTS = 100  # max requests allowed in the window

# Dictionary to track request counts
request_counts = defaultdict(list)

def rate_limiter(f):
    """
    Rate limiter decorator to limit the number of requests from a single IP address.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        current_time = time.time()

        # Clean up old request timestamps
        request_counts[client_ip] = [timestamp for timestamp in request_counts[client_ip] if timestamp > current_time - RATE_LIMIT_WINDOW]

        if len(request_counts[client_ip]) >= RATE_LIMIT_REQUESTS:
            # If the request count exceeds the limit, return an error response
            return jsonify({"error": "Too many requests, please try again later."}), 429

        # Log the current request
        request_counts[client_ip].append(current_time)
        return f(*args, **kwargs)

    return decorated_function

@app.route('/api/resource', methods=['GET'])
@rate_limiter
def get_resource():
    """
    Endpoint to retrieve a resource.
    Applies rate limiting to protect against DDoS attacks.
    """
    return jsonify({"message": "Resource accessed successfully!"}), 200

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the server: {e}")
```
