"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-dop.app
Prompt: Can you provide code examples for implementing security measures to prevent phishing on a web application?
Generated: DETERMINISTIC_9b79dec098fe0042
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
import re
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong secret key in production!

# Configure logging
logging.basicConfig(level=logging.INFO)

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Dummy user database for demonstration
users_db = {
    'user@example.com': generate_password_hash('securepassword')
}

def is_valid_email(email):
    """Check if the provided email matches the regex pattern."""
    return re.match(EMAIL_REGEX, email) is not None

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login with basic phishing prevention measures."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate email format
        if not is_valid_email(email):
            return "Invalid email format", 400

        # Check user credentials
        if email in users_db and check_password_hash(users_db[email], password):
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            logging.warning(f'Failed login attempt for email: {email}')
            return "Invalid credentials", 401

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """User dashboard, accessible only when logged in."""
    if 'user' not in session:
        return redirect(url_for('login'))
    return f"Welcome {session['user']}!"

@app.route('/logout')
def logout():
    """Log the user out and clear the session."""
    session.pop('user', None)
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors by returning a custom message."""
    return "Page not found", 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors by logging and returning a custom message."""
    logging.error(f'Internal server error: {error}')
    return "Internal server error", 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production!
```

**Notes:**
- Ensure to replace `'your_secret_key'` with a strong, random secret key in a production environment.
- Update the user database with secure user management practices.
- Use HTTPS to further enhance security.
- Implement rate limiting and CAPTCHA mechanisms to mitigate brute force attacks.
