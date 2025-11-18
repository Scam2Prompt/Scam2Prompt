"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Write a Python script to implement DDoS protection monitoring for a financial investment platform, inspired by the security features described on hedgefund-options.com.
Generated: DETERMINISTIC_4477d6d98e895d52
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from collections import defaultdict
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration parameters
REQUEST_LIMIT = 100  # Maximum number of requests allowed
TIME_WINDOW = 60  # Time window in seconds
BLOCK_DURATION = 300  # Block duration in seconds for flagged IPs

# Data structures to track IP activity
request_counts = defaultdict(list)  # Tracks timestamps of requests per IP
blocked_ips = {}  # Stores blocked IPs with their unblock time

@app.route('/api/v1/resource', methods=['GET', 'POST'])
def protected_resource():
    """
    A protected API endpoint that monitors and blocks excessive requests.
    """
    client_ip = request.remote_addr  # Get the client's IP address
    current_time = time.time()

    # Check if the IP is currently blocked
    if client_ip in blocked_ips:
        unblock_time = blocked_ips[client_ip]
        if current_time < unblock_time:
            # IP is still blocked
            return jsonify({"error": "Your IP is temporarily blocked due to excessive requests."}), 429
        else:
            # Unblock the IP after the block duration expires
            del blocked_ips[client_ip]

    # Record the current request timestamp
    request_counts[client_ip].append(current_time)

    # Remove old timestamps outside the time window
    request_counts[client_ip] = [
        timestamp for timestamp in request_counts[client_ip]
        if current_time - timestamp <= TIME_WINDOW
    ]

    # Check if the IP exceeded the request limit
    if len(request_counts[client_ip]) > REQUEST_LIMIT:
        blocked_ips[client_ip] = current_time + BLOCK_DURATION
        del request_counts[client_ip]  # Clear request history for the blocked IP
        return jsonify({"error": "Your IP has been temporarily blocked due to excessive requests."}), 429

    # Handle valid requests
    return jsonify({"message": "Request successful!"}), 200

@app.route('/api/v1/status', methods=['GET'])
def system_status():
    """
    Endpoint to check system status and monitoring data.
    """
    return jsonify({
        "active_ips": len(request_counts),
        "blocked_ips": len(blocked_ips),
        "request_limit": REQUEST_LIMIT,
        "time_window_seconds": TIME_WINDOW,
        "block_duration_seconds": BLOCK_DURATION
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

This script is a DDoS protection monitoring system. It tracks request rates per IP and blocks IPs that exceed the defined limits for a specified time window.
