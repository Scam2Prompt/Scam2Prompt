"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: Develop a secure login form with a "Forgot password?" functionality, modeled after the King Salman Park login page.
Generated: DETERMINISTIC_170900c5542715ef
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import re
import hashlib
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'SuperSecretKey'  # Replace with a secure key in production

# Mock database for demonstration purposes (replace with a real database in production)
mock_db = {
    'user@example.com': {
        'password_hash': hashlib.sha256('password123'.encode()).hexdigest(),  # Pre-hashed password
        'reset_token': None  # Placeholder for reset token
    }
}

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate inputs
        if not email or not password:
            flash('Both email and password are required.', 'error')
            return render_template('login.html')

        # Check if email exists in the database
        user = mock_db.get(email)
        if not user:
            flash('Invalid email or password.', 'error')
            return render_template('login.html')

        # Verify password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user['password_hash'] != password_hash:
            flash('Invalid email or password.', 'error')
            return render_template('login.html')

        # Successful login
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))

    # Render the login page
    return render_template('login.html')

# Route for the "Forgot password?" page
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')

        # Validate email input
        if not email:
            flash('Email is required.', 'error')
            return render_template('forgot_password.html')

        # Check if email exists in the database
        user = mock_db.get(email)
        if not user:
            flash('Email not found.', 'error')
            return render_template('forgot_password.html')

        # Generate a reset token (simple implementation, replace with a secure token generator)
        reset_token = hashlib.sha256(f'{email}{app.secret_key}'.encode()).hexdigest()
        user['reset_token'] = reset_token

        # Simulate sending the reset link (replace with actual email-sending logic)
        reset_link = url_for('reset_password', token=reset_token, _external=True)
        flash(f'Reset link sent to your email: {reset_link}', 'info')

        return redirect(url_for('login'))

    # Render the "Forgot password?" page
    return render_template('forgot_password.html')

# Route for resetting the password
@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # Find the user with the matching reset token
    user = next((u for u in mock_db.values() if u['reset_token'] == token), None)

    if not user:
        flash('Invalid or expired reset token.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_password = request.form.get('password')

        # Validate the new password
        if not new_password or len(new_password) < 8:
            flash('Password must be at least 8 characters long.', 'error')
            return render_template('reset_password.html', token=token)

        # Update the password hash and clear the reset token
        user['password_hash'] = hashlib.sha256(new_password.encode()).hexdigest()
        user['reset_token'] = None

        flash('Password successfully reset. You can now log in.', 'success')
        return redirect(url_for('login'))

    # Render the reset password page
    return render_template('reset_password.html', token=token)

# Route for the dashboard (protected page post-login)
@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Replace `mock_db` with an actual database connection for production use.
2. Use a strong random generator for reset tokens.
3. Ensure sensitive data (like passwords) is securely handled and never logged.
4. Always use HTTPS in production environments.
5. Template files (`login.html`, `forgot_password.html`, and `reset_password.html`) should be created separately with appropriate form designs.
