"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-100maxair.com
Prompt: Develop a secure registration system for a cryptocurrency trading platform that includes account activation and personalized investment education firm connections, inspired by Bitcoin +100 Maxair's process.
Generated: DETERMINISTIC_67d20121f7cfe2d7
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import smtplib
import sqlite3
from flask import Flask, request, jsonify, render_template, redirect, url_for
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management
app.config['SECURITY_PASSWORD_SALT'] = os.urandom(24)  # Salt for password hashing
app.config['DATABASE'] = 'users.db'  # SQLite database file
app.config['MAIL_SERVER'] = 'smtp.example.com'  # SMTP server
app.config['MAIL_PORT'] = 587  # SMTP port
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # SMTP username
app.config['MAIL_PASSWORD'] = 'your_password'  # SMTP password
app.config['MAIL_USE_TLS'] = True  # Use TLS
app.config['MAIL_USE_SSL'] = False  # Do not use SSL
s = URLSafeTimedSerializer(app.secret_key)  # Serializer for token generation

def init_db():
    """Initialize the SQLite database."""
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                activated BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def send_activation_email(user_email, token):
    """Send an account activation email to the user."""
    link = url_for('activate_account', token=token, _external=True)
    message = f'Click the link to activate your account: {link}'
    try:
        with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
            server.starttls()
            server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            server.sendmail(app.config['MAIL_USERNAME'], user_email, message)
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    email = request.form['email']
    password = request.form['password']

    hashed_password = hash_password(password)

    try:
        with sqlite3.connect(app.config['DATABASE']) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))
            conn.commit()

            # Generate activation token
            token = s.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])
            send_activation_email(email, token)

        return jsonify({'message': 'Registration successful! Please check your email to activate your account.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already registered.'}), 400

@app.route('/activate/<token>')
def activate_account(token):
    """Activate user account using the token."""
    try:
        email = s.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=3600)
        with sqlite3.connect(app.config['DATABASE']) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET activated = 1 WHERE email = ?', (email,))
            conn.commit()
        return jsonify({'message': 'Account activated successfully!'}), 200
    except (BadSignature, SignatureExpired):
        return jsonify({'error': 'Invalid or expired activation token.'}), 400

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users (for administrative purposes)."""
    try:
        with sqlite3.connect(app.config['DATABASE']) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT email, activated FROM users')
            users = cursor.fetchall()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask application
```

**Note**: Make sure to replace SMTP configuration with your actual email service provider settings. The SQLite database file `users.db` will be created in the same directory as this script.
