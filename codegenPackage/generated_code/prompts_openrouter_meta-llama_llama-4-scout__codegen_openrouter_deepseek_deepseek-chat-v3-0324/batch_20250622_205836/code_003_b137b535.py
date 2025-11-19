"""
Generated Code Metadata:
========================
Original URL: https://web3-protection.com
Prompt: "Write a code snippet to handle rate limiting and IP blocking for a Web3 service."
Generated: DETERMINISTIC_b137b53513e09ba8
Batch ID: 20250622_205836
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
from collections import defaultdict
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Rate limiting configuration
RATE_LIMIT = 10  # Requests per minute
BLOCK_TIME = 300  # 5 minutes in seconds
IP_BLOCKLIST = set()

# Store request counts and timestamps per IP
request_logs = defaultdict(list)

def rate_limited(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ip = request.remote_addr
        
        # Check if IP is blocked
        if ip in IP_BLOCKLIST:
            abort(429, description="IP temporarily blocked due to excessive requests.")
        
        # Clean up old requests
        current_time = time.time()
        request_logs[ip] = [t for t in request_logs[ip] if current_time - t < 60]
        
        # Check rate limit
        if len(request_logs[ip]) >= RATE_LIMIT:
            IP_BLOCKLIST.add(ip)
            # Schedule unblock after BLOCK_TIME
            app.logger.warning(f"IP {ip} blocked due to rate limiting.")
            abort(429, description="Too many requests. IP temporarily blocked.")
        
        # Log the request
        request_logs[ip].append(current_time)
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/web3', methods=['GET'])
@rate_limited
def web3_service():
    # Your Web3 service logic here
    return jsonify({"status": "success", "data": "Web3 service response"})

@app.errorhandler(429)
def handle_rate_limit(e):
    return jsonify({"status": "error", "message": str(e.description)}), 429

def cleanup_blocklist():
    """Periodically clean up expired IP blocks"""
    while True:
        time.sleep(BLOCK_TIME)
        current_time = time.time()
        expired_ips = [ip for ip in IP_BLOCKLIST if current_time - ip_block_time[ip] > BLOCK_TIME]
        for ip in expired_ips:
            IP_BLOCKLIST.remove(ip)
            request_logs.pop(ip, None)
            app.logger.info(f"IP {ip} unblocked after timeout.")

if __name__ == '__main__':
    # In a production environment, run cleanup in a separate thread/process
    import threading
    cleanup_thread = threading.Thread(target=cleanup_blocklist, daemon=True)
    cleanup_thread.start()
    
    app.run(host='0.0.0.0', port=5000)
```
