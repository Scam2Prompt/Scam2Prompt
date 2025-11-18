"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Generate code to implement a secure user login system for Sabka Future, including password reset functionality as described on the site.
Generated: DETERMINISTIC_7d36c238923bac9e
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from datetime import timedelta
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
app.permanent_session_lifetime = timedelta(days=7)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
mail = Mail(app)

# Serializer for generating secure tokens
serializer = URLSafeTimedSerializer(app.secret_key)

# Simulating a database with a dictionary for demo purposes
users_db = {
    # Example: 'user@example.com': {'password': hashed_password}
}

# Route: User Registration
@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user with email and password.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    if email in users_db:
        return jsonify({'error': 'User already exists'}), 400

    # Store hashed password
    hashed_password = generate_password_hash(password)
    users_db[email] = {'password': hashed_password}
    return jsonify({'message': 'Registration successful'}), 201

# Route: User Login
@app.route('/login', methods=['POST'])
def login():
    """
    Authenticates a user by checking the email and password.
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = users_db.get(email)
    if user and check_password_hash(user['password'], password):
        session.permanent = True
        session['user'] = email
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Route: Password Reset Request
@app.route('/password-reset-request', methods=['POST'])
def password_reset_request():
    """
    Sends a password reset email with a secure token.
    """
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    if email not in users_db:
        return jsonify({'error': 'Email not found'}), 404

    # Generate reset token
    token = serializer.dumps(email, salt='password-reset')
    reset_link = f"{request.url_root}password-reset/{token}"

    # Send email with reset link
    try:
        msg = Message('Password Reset Request', sender='your-email@example.com', recipients=[email])
        msg.body = f"Click the link to reset your password: {reset_link}"
        mail.send(msg)
        return jsonify({'message': 'Password reset email sent'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to send email', 'details': str(e)}), 500

# Route: Password Reset
@app.route('/password-reset/<token>', methods=['POST'])
def password_reset(token):
    """
    Resets the user's password using the token.
    """
    data = request.json
    new_password = data.get('password')

    if not new_password:
        return jsonify({'error': 'Password is required'}), 400

    try:
        # Validate token and extract email
        email = serializer.loads(token, salt='password-reset', max_age=3600)
        if email in users_db:
            # Update the password
            hashed_password = generate_password_hash(new_password)
            users_db[email]['password'] = hashed_password
            return jsonify({'message': 'Password reset successful'}), 200
        else:
            return jsonify({'error': 'Invalid token'}), 400
    except Exception as e:
        return jsonify({'error': 'Invalid or expired token', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
