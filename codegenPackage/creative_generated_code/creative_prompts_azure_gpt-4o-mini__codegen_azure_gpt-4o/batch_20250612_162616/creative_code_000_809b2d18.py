"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paramgaminglabs.app
Prompt: What are the best practices for securing a web application against phishing attacks, as discussed in the context of website safety?
Generated: DETERMINISTIC_809b2d187e6708df
Batch ID: 20250612_162616
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

```python
"""
Secure Web Application Against Phishing Attacks
This Python code demonstrates best practices to secure a web application against phishing attacks.
It includes features such as HTTPS enforcement, email validation, anti-CSRF mechanisms, and content security policies.
"""

from flask import Flask, request, render_template, abort, make_response
from flask_wtf.csrf import CSRFProtect

# Initialize Flask application
app = Flask(__name__)

# Enable CSRF protection for forms
csrf = CSRFProtect(app)

# Best practice 1: Use HTTPS
# Force HTTPS usage by redirecting HTTP requests to HTTPS
@app.before_request
def enforce_https():
    if not request.is_secure and app.env == "production":
        return redirect(request.url.replace("http://", "https://"), code=301)

# Best practice 2: Validate user input (e.g., email addresses)
def is_valid_email(email):
    """
    Validates an email address format.
    """
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Example form submission endpoint.
    Validates the provided email address and protects against malicious input.
    """
    email = request.form.get('email')
    
    if not email or not is_valid_email(email):
        abort(400, description="Invalid email address.")

    # Pretend to process the email
    return "Email submitted successfully."

# Best practice 3: Set Content Security Policy (CSP) header
@app.after_request
def set_security_headers(response):
    """
    Adds security headers to the response to protect against phishing and other attacks.
    """
    # Content Security Policy
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; script-src 'self'; style-src 'self';"
        "frame-ancestors 'none'; form-action 'self';"
    )
    # Prevent browsers from guessing the content type
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Prevent clickjacking
    response.headers['X-Frame-Options'] = 'DENY'
    # Enable strict HTTPS transport security
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    return response

# Best practice 4: Anti-phishing measures in email links
@app.route('/reset-password/<token>', methods=['GET'])
def reset_password(token):
    """
    Handles password reset requests securely using tokens.
    """
    # Validate token (example implementation)
    if not validate_token(token):
        abort(400, description="Invalid or expired token.")
    
    # Render a secure password reset page
    return render_template('reset_password.html')

def validate_token(token):
    """
    Validates the reset token (placeholder logic).
    """
    # Replace with actual validation logic (e.g., check against a database)
    return token == "valid_token"

# Run the application
if __name__ == '__main__':
    # Best practice: Use a secure secret key for session management
    app.secret_key = 'your_secure_secret_key'
    
    # Run the app with debugging disabled in production
    app.run(debug=False)
```

This code demonstrates key principles to secure a web application against phishing attacks, including HTTPS enforcement, CSP headers, CSRF protection, and careful handling of user inputs like email addresses.
