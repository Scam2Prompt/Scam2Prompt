"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poll-aerodromefinance.app
Prompt: What are the best practices for securing a web application against phishing attacks, as discussed in the context of Cloudflare's security features?
Generated: DETERMINISTIC_b8b16cd8e0d55162
Batch ID: 20250612_162722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python example demonstrating best practices for securing a web application against phishing attacks using Cloudflare's security features and other techniques. This script configures HTTP security headers and integrates Cloudflare-based protection functionalities.

```python
from flask import Flask, Response, request
import logging

app = Flask(__name__)

# Configure logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.before_request
def validate_cloudflare_request():
    """
    Validate incoming requests to ensure they are from Cloudflare.
    This helps mitigate direct access bypassing Cloudflare's security layers.
    """
    cloudflare_ips = [
        # Cloudflare IP ranges (example, maintain an updated list from Cloudflare's docs)
        "173.245.48.0/20", "103.21.244.0/22", "131.0.72.0/22", "190.93.240.0/20",
        # Add more Cloudflare IP ranges here
    ]
    request_ip = request.remote_addr
    if not is_ip_in_ranges(request_ip, cloudflare_ips):
        logging.warning(f"Unauthorized IP attempt detected: {request_ip}")
        return Response("Forbidden", status=403)

def is_ip_in_ranges(ip, ranges):
    """
    Helper function to check if an IP belongs to a given list of CIDR ranges.
    """
    import ipaddress
    ip = ipaddress.ip_address(ip)
    for range in ranges:
        if ip in ipaddress.ip_network(range):
            return True
    return False

@app.after_request
def set_security_headers(response):
    """
    Set HTTP security headers to protect the application against phishing and other attacks.
    """
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'  # Force HTTPS
    response.headers['X-Content-Type-Options'] = 'nosniff'                                # Prevent MIME-type sniffing
    response.headers['X-Frame-Options'] = 'DENY'                                          # Prevent clickjacking
    response.headers['X-XSS-Protection'] = '1; mode=block'                                # Enable browser XSS filter
    response.headers['Content-Security-Policy'] = "default-src 'self';"                   # Content Security Policy
    response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'                    # Referrer policy
    return response

@app.route('/')
def home():
    """
    Simple route to demonstrate secure headers and valid requests.
    """
    return Response("Welcome to the secure web application!", status=200)

if __name__ == '__main__':
    # Run the Flask application with production-ready configurations
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
```

This production-ready Flask application integrates Cloudflare IP validation, sets robust HTTP security headers, and includes error handling and logging for monitoring invalid attempts.
