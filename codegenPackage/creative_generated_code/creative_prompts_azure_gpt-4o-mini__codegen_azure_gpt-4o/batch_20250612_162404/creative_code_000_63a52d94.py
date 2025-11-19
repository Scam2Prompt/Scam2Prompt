"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merkiy.app
Prompt: What steps should a developer take to secure their website against phishing attacks as mentioned on the Cloudflare warning page?
Generated: DETERMINISTIC_63a52d94cb0a36b2
Batch ID: 20250612_162404
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the code that follows the specified requirements. It includes the implementation of some steps developers can take to secure their website against phishing attacks:

### Language: Python (with Flask for a web application)

```python
from flask import Flask, request, redirect, url_for, session, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
import re
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong, randomly generated secret key.

# ProxyFix to handle headers in case of reverse proxy setups (e.g., Cloudflare)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

# Regular expression to validate URLs (use for whitelist/blacklist checking)
URL_PATTERN = re.compile(r'^https?://[a-zA-Z0-9.-]+$')

# Configure logging for audit trails
logging.basicConfig(filename='phishing_protection.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Whitelisted domains for redirect validation
WHITELISTED_DOMAINS = {'yourwebsite.com', 'trustedpartner.com'}

@app.before_request
def enforce_https_and_security_headers():
    """
    Enforce HTTPS and set security headers to mitigate phishing attacks.
    """
    if not request.is_secure:
        # Redirect to HTTPS if the current request is HTTP
        return redirect(request.url.replace("http://", "https://"))

    # Set security headers
    response = request.response
    response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains; preload'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Referrer-Policy'] = 'no-referrer'
    response.headers['X-XSS-Protection'] = '1; mode=block'

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Example login page with CSRF protection and input validation.
    """
    if request.method == 'POST':
        # CSRF token validation
        csrf_token = session.get('csrf_token')
        if not csrf_token or csrf_token != request.form.get('csrf_token'):
            logging.warning("Potential CSRF attack detected.")
            return "Invalid request.", 403

        # Validate user input to prevent phishing attempts
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return "Invalid input.", 400

        # Simulated authentication process
        if username == 'admin' and password == 'securepassword':
            session['logged_in'] = True
            logging.info("User successfully logged in.")
            return redirect(url_for('dashboard'))
        else:
            logging.warning(f"Failed login attempt for username: {username}")
            return "Invalid credentials.", 401

    # Generate CSRF token for the form
    session['csrf_token'] = 'random_secure_token'  # Replace with a secure token generator
    return render_template('login.html')

@app.route('/redirect')
def safe_redirect():
    """
    Handle redirects securely by validating URLs against a whitelist.
    """
    target_url = request.args.get('url')
    if not target_url or not URL_PATTERN.match(target_url):
        return "Invalid URL.", 400

    # Extract domain from URL and validate it's within the whitelist
    target_domain = target_url.split('/')[2]
    if target_domain not in WHITELISTED_DOMAINS:
        logging.warning(f"Blocked redirect attempt to {target_url}")
        return "Unauthorized redirect.", 403

    return redirect(target_url)

@app.route('/dashboard')
def dashboard():
    """
    Example protected route for logged-in users.
    """
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return "Welcome to the dashboard!"

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Use production-grade SSL/TLS certificates in real scenarios.
```

### Notes:
- This code demonstrates secure practices to handle commonly exploited areas in phishing attacks, including enforcing HTTPS, validating redirects, and adding security headers.
- You must replace placeholder values (e.g., `your_secret_key`, `random_secure_token`) with production-ready configurations. Use libraries such as `itsdangerous` or `secrets` for secure token generation.
