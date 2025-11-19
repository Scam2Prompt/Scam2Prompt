"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Develop a code example for integrating multifactor authentication with an existing web application, using a library or API that supports various authentication methods."
Generated: DETERMINISTIC_bfe2bd8f07845019
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based example for integrating multifactor authentication (MFA) using PyOTP (Time-based One-Time Passwords)
# This code assumes you have an existing web application and user authentication system.

from flask import Flask, request, session, redirect, url_for, render_template, flash
import pyotp
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Mock user database
users = {
    "test_user": {
        "password": "password123",  # Replace with hashed passwords in production
        "mfa_secret": None,  # MFA secret will be generated during setup
    }
}

# Route: Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate user credentials
        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            # Check if MFA is enabled for the user
            if user['mfa_secret']:
                return redirect(url_for('mfa_verify'))
            else:
                flash("Login successful (MFA not enabled).")
                return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password.")
    return render_template('login.html')

# Route: MFA setup (for users who want to enable MFA)
@app.route('/mfa_setup', methods=['GET', 'POST'])
def mfa_setup():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    user = users[username]
    if request.method == 'POST':
        # Generate a new MFA secret for the user
        mfa_secret = pyotp.random_base32()
        user['mfa_secret'] = mfa_secret

        # Generate a QR code URL for the user to scan with an authenticator app
        totp = pyotp.TOTP(mfa_secret)
        qr_code_url = totp.provisioning_uri(username, issuer_name="MyWebApp")

        flash("MFA setup complete. Scan the QR code with your authenticator app.")
        return render_template('mfa_qr.html', qr_code_url=qr_code_url)
    return render_template('mfa_setup.html')

# Route: MFA verification during login
@app.route('/mfa_verify', methods=['GET', 'POST'])
def mfa_verify():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    user = users[username]
    if request.method == 'POST':
        mfa_code = request.form.get('mfa_code')
        totp = pyotp.TOTP(user['mfa_secret'])

        # Verify the MFA code
        if totp.verify(mfa_code):
            flash("Login successful (MFA verified).")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid MFA code. Please try again.")
    return render_template('mfa_verify.html')

# Route: Dashboard (protected resource)
@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    return f"Welcome to your dashboard, {username}!"

# Route: Logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found.", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "Internal server error.", 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Replace the mock user database with a real database in production.
- Use hashed passwords (e.g., bcrypt) instead of plain text for security.
- Ensure HTTPS is enabled for secure communication.
- Templates (`login.html`, `mfa_setup.html`, `mfa_qr.html`, `mfa_verify.html`) should be created to render the respective pages.
