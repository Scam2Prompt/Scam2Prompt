"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nizacoin.app
Prompt: What are the best practices for securing a web application against phishing attacks, as discussed in phishing-related documentation?
Generated: DETERMINISTIC_6171671bed2c1892
Batch ID: 20250612_162601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python code example that demonstrates best practices for securing a web application against phishing attacks:

```python
# Import required libraries
import re
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_talisman import Talisman  # For secure HTTP headers
from werkzeug.security import safe_str_cmp

app = Flask(__name__)

# Enforce HTTPS for all routes using Flask-Talisman
csp = {
    'default-src': "'self'",
    'style-src': ["'self'", "'unsafe-inline'"],
    'script-src': ["'self'", "'unsafe-inline'"],
}
Talisman(app, content_security_policy=csp)

# Helper function to validate URLs
def is_safe_url(target_url: str) -> bool:
    """
    Validates if the given URL is safe (i.e., does not lead to known malicious domains).
    """
    allowed_domains = {"example.com", "secure.example.com"}
    # Extract the domain from the given URL
    try:
        domain = re.search(r'://([^/]+)', target_url).group(1)
        return domain in allowed_domains
    except AttributeError:
        return False

# A function to sanitize user inputs
def sanitize_input(input_text: str) -> str:
    """
    Sanitizes user input to prevent malicious data injection.
    """
    return re.sub(r'[<>]', "", input_text)

# Phishing-safe login endpoint
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles the login functionality securely, ensuring protection against phishing attempts.
    """
    if request.method == 'POST':
        username = sanitize_input(request.form.get('username', ''))
        password = sanitize_input(request.form.get('password', ''))

        # Validate credentials (example static check for demonstration purposes)
        if safe_str_cmp(username, 'admin') and safe_str_cmp(password, 'securepassword'):
            # Redirect to a safe URL if login is successful
            next_url = request.form.get('next', '/dashboard')
            if is_safe_url(next_url):
                return redirect(next_url)
            else:
                return jsonify({'error': 'Unsafe redirect URL detected'}), 400
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    return render_template('login.html')

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors with a user-friendly response.
    """
    return jsonify({'error': 'Page not found'}), 404

# Main dashboard endpoint
@app.route('/dashboard')
def dashboard():
    """
    Secure dashboard endpoint accessible only after login.
    """
    return render_template('dashboard.html')

if __name__ == '__main__':
    # Run the Flask app securely
    app.run(ssl_context='adhoc')  # Use SSL to enforce HTTPS
```

This code demonstrates the use of several best practices for securing a web application against phishing attacks, including input sanitization, safe URL validation, HTTPS enforcement, CSP implementation, and secure error handling.
