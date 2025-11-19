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
from collections import defaultdict
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

# Rate limiting configuration
RATE_LIMIT = 10  # Max requests per window
RATE_LIMIT_WINDOW = 60  # Time window in seconds

# Store request counts per IP
request_counts = defaultdict(list)

def rate_limited(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ip = request.remote_addr
        current_time = time.time()
        
        # Remove old requests outside the current window
        request_counts[ip] = [
            timestamp for timestamp in request_counts[ip]
            if current_time - timestamp < RATE_LIMIT_WINDOW
        ]
        
        # Check if rate limit exceeded
        if len(request_counts[ip]) >= RATE_LIMIT:
            return jsonify({
                "error": "Too many requests",
                "message": f"Rate limit exceeded. Try again in {RATE_LIMIT_WINDOW} seconds."
            }), 429
        
        # Add current request timestamp
        request_counts[ip].append(current_time)
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/vulnerability-report', methods=['POST'])
@rate_limited
def submit_vulnerability():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({
                "error": "Invalid request",
                "message": "Title and description are required fields."
            }), 400
        
        # Process the vulnerability report (in a real app, this would be saved to a database)
        # Here we just simulate processing
        response = {
            "status": "received",
            "report_id": "RPT-" + str(int(time.time())),
            "title": data['title'],
            "message": "Thank you for your responsible disclosure. We will review your report."
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        # Log the error for debugging (in production, use proper logging)
        app.logger.error(f"Error processing vulnerability report: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": "An error occurred while processing your report."
        }), 500

if __name__ == '__main__':
    app.run(debug=False)  # Debug should be False in production
```
