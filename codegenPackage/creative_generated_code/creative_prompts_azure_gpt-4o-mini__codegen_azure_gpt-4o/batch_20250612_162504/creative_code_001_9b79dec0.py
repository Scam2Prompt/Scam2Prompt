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

Below is a production-ready implementation of security measures to prevent phishing for a web application, written in Python using the Flask framework:

```python
from flask import Flask, request, redirect, url_for, render_template, session, flash
from flask_wtf.csrf import CSRFProtect
import re
import secrets

app = Flask(__name__)

# Secure configs
app.secret_key = secrets.token_hex(32)  # Generate a strong secret key
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevent client-side JavaScript from accessing session cookies
app.config['SESSION_COOKIE_SECURE'] = True  # Use HTTPS for cookies
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'  # Prevent cookies from being sent with cross-site requests

# Enable CSRF protection
csrf = CSRFProtect(app)

# Whitelist for allowed URLs (to prevent open redirect attacks)
ALLOWED_REDIRECT_DOMAINS = ['yourdomain.com', 'trustedpartner.com']

def is_safe_url(target):
    """
    Validate if the target URL is safe and belongs to a whitelisted domain.
    """
    if not target:
        return False
    domain = re.search(r'^(?:https?://)?([^/]+)', target).group(1)
    return domain in ALLOWED_REDIRECT_DOMAINS

@app.route('/')
def home():
    """
    Render the homepage.
    """
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login securely.
    """
    if request.method == 'POST':
        # Simulated login logic (replace with actual authentication)
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate inputs
        if not username or not password:
            flash("Invalid input. Please try again.", "error")
            return redirect(url_for('login'))

        if username == 'admin' and password == 'password123':  # Example dummy credentials
            session['user'] = username
            flash("Logged in successfully!", "success")

            # Check for safe redirect
            next_url = request.args.get('next')
            if is_safe_url(next_url):
                return redirect(next_url)
            return redirect(url_for('dashboard'))

        flash("Invalid username or password.", "error")
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    Render the user dashboard after login.
    """
    if 'user' not in session:
        flash("You must be logged in to access the dashboard.", "error")
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.errorhandler(403)
def forbidden_error(error):
    """
    Handle 403 Forbidden errors.
    """
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 Not Found errors.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 Internal Server errors.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Force HTTPS in production
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    app.run(ssl_context=('cert.pem', 'key.pem'))  # Replace cert.pem/key.pem with your SSL certificate files
```

### Key Features of the Code:
1. **CSRF Protection:** Enabled using Flask-WTF's CSRF module to prevent cross-site request forgery attacks.
2. **Session Security:** Configured secure session cookie settings (`HttpOnly`, `Secure`, `SameSite`).
3. **Open Redirect Prevention:** Whitelist validation for redirect URLs.
4. **Error Handling:** Custom error handlers for 403, 404, and 500 response codes.
5. **HTTPS Enforcement:** Flask is configured to run over HTTPS in production.
