"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mikamiairdrop.art
Prompt: Create a secure login system for a Telegram bot admin panel using Python, with a focus on session expiration and password protection, similar to the mikamiairdrop.art implementation.
Generated: DETERMINISTIC_f5c55b6f5861d84b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import hmac
import time
from flask import Flask, request, session, redirect, url_for, render_template, jsonify

# Initialize Flask application
app = Flask(__name__)

# Secret key for session management (should be stored securely in production)
app.secret_key = os.urandom(24)

# Configuration constants
SESSION_EXPIRATION_SECONDS = 3600  # 1 hour
ADMIN_USERNAME = "admin"  # Replace with your admin username
ADMIN_PASSWORD_HASH = hashlib.sha256(b"your_secure_password").hexdigest()  # Replace with a strong password

# Utility function to hash passwords
def hash_password(password: str) -> str:
    """Hashes the given password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Utility function to verify passwords
def verify_password(provided_password: str, stored_hash: str) -> bool:
    """
    Verifies if the provided password matches the stored hash.
    Uses a constant-time comparison for security.
    """
    return hmac.compare_digest(hash_password(provided_password), stored_hash)

# Route: Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles admin login. Validates username and password and initiates a session.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == ADMIN_USERNAME and verify_password(password, ADMIN_PASSWORD_HASH):
            # Successful login: Create a session
            session['user'] = username
            session['login_time'] = time.time()
            return redirect(url_for('admin_panel'))
        else:
            return render_template('login.html', error="Invalid credentials. Please try again.")
    return render_template('login.html')

# Route: Admin panel (requires authentication)
@app.route('/admin', methods=['GET'])
def admin_panel():
    """
    Protected admin panel route. Checks for session validity and expiration.
    """
    if 'user' in session:
        # Check session expiration
        login_time = session.get('login_time', 0)
        if time.time() - login_time > SESSION_EXPIRATION_SECONDS:
            # Session expired
            session.clear()
            return redirect(url_for('login'))
        return render_template('admin_panel.html', user=session['user'])
    return redirect(url_for('login'))

# Route: Logout
@app.route('/logout', methods=['GET'])
def logout():
    """
    Clears the current session and redirects to the login page.
    """
    session.clear()
    return redirect(url_for('login'))

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors gracefully.
    """
    return jsonify({"error": "Page not found"}), 404

# Run the application
if __name__ == '__main__':
    # Ensure debug is disabled in production
    app.run(host="0.0.0.0", port=5000, debug=False)
```

**Additional Notes:**
- Replace `your_secure_password` with a strong, hard-to-guess password.
- Store sensitive data such as the admin password hash and Flask secret key securely (e.g., environment variables or a secure vault).
- Make sure to implement HTTPS for secure communication in production.
- Templates such as `login.html` and `admin_panel.html` need to be created separately.
