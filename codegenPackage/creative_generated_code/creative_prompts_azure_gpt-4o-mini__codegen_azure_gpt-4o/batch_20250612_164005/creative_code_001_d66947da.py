"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.pages.dev
Prompt: Write a code snippet for setting up a sub-domain on a server to enhance security and prevent misuse.
Generated: DETERMINISTIC_d66947da6297b5db
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a production-ready Python code snippet using Flask for setting up a secure sub-domain on a server:

```python
from flask import Flask, request, abort

# Initialize the Flask application
app = Flask(__name__)

# Define the main domain and sub-domain configuration
MAIN_DOMAIN = "example.com"
SECURE_SUBDOMAIN = "secure"

# Ensure Flask recognizes subdomains
app.config["SERVER_NAME"] = f"{MAIN_DOMAIN}"


@app.route("/")
def home():
    """Main domain route."""
    return "Welcome to the main domain!"


@app.route("/", subdomain=SECURE_SUBDOMAIN)
def secure_home():
    """
    Secure sub-domain route.
    This route enhances security by isolating it from the main domain.
    """
    return "Welcome to the secure sub-domain!"


@app.before_request
def validate_domain():
    """
    Middleware to validate requests and enforce security rules.
    Prevent misuse by rejecting invalid Host headers or subdomain attempts.
    """
    host = request.host
    if host not in (f"{SECURE_SUBDOMAIN}.{MAIN_DOMAIN}", MAIN_DOMAIN):
        # Reject requests with invalid Host headers or subdomains
        abort(403)  # Forbidden


# Start the Flask application
if __name__ == "__main__":
    try:
        # Run the server with debug disabled for production-ready use
        app.run(debug=False, host="0.0.0.0", port=5000)
    except Exception as e:
        # Log any errors that occur during server initialization
        print(f"Error starting the server: {e}")
```

This code is production-ready, adheres to best practices, and includes error handling. Replace `example.com` with your actual domain name when deploying.
