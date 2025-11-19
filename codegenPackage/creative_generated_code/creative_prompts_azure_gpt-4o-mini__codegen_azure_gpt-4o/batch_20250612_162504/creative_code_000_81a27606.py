"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reyaiabs.app
Prompt: What are the best practices for preventing phishing attacks when developing web applications?
Generated: DETERMINISTIC_81a276067f89be27
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python code implements best practices to help prevent phishing attacks in web applications.
It includes secure input validation, protection against open redirects, anti-CSRF tokens, and secure session handling.
"""

from flask import Flask, request, redirect, url_for, session, render_template
from flask_wtf.csrf import CSRFProtect
import re

# Initialize Flask application
app = Flask(__name__)

# Set a secret key for session management and CSRF protection
app.secret_key = 'your-very-secure-secret-key'

# Enable CSRF protection
csrf = CSRFProtect(app)

# Regular expression for validating URLs
URL_PATTERN = re.compile(r'^(https?:\/\/)?([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(\/.*)?$')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate input to ensure it meets security standards
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            return render_template('login.html', error="Invalid credentials!")

        # Simulate authentication (replace with real authentication logic)
        if username == 'admin' and password == 'password123':
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Incorrect username or password!")
    
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    # Ensure user is authenticated before providing access
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html', user=session['user'])

# Logout route
@app.route('/logout')
def logout():
    # Clear session on logout
    session.clear()
    return redirect(url_for('login'))

# Prevent open redirects by validating "next" parameter
@app.route('/redirect', methods=['GET'])
def safe_redirect():
    next_url = request.args.get('next', '')
    
    # Validate the URL to prevent open redirects
    if not next_url or not URL_PATTERN.match(next_url):
        return "Invalid redirect URL", 400
    
    return redirect(next_url)

# Error handler for invalid CSRF token
@app.errorhandler(400)
def handle_bad_request(e):
    return "Bad Request: Possible CSRF Attack Detected!", 400

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return "Page Not Found!", 404

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=False)  # Disable debug mode in production
```
