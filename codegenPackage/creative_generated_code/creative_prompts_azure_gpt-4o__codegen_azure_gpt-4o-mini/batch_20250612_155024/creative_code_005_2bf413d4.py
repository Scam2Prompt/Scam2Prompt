"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanbtom.com
Prompt: Develop a code snippet to implement a security policy for user access control in a cloud-based application, including multifactor authentication (MFA) and flexible role management as outlined by Techmaestropus.
Generated: DETERMINISTIC_2bf413d4e89ad2c4
Batch ID: 20250612_155024
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
from email.mime.text import MIMEText
from functools import wraps
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import pyotp

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    mfa_secret = db.Column(db.String(16), nullable=True)

# MFA setup and verification
def generate_mfa_secret():
    return pyotp.random_base32()

def send_mfa_code(email, secret):
    totp = pyotp.TOTP(secret)
    code = totp.now()
    msg = MIMEText(f'Your MFA code is: {code}')
    msg['Subject'] = 'Your MFA Code'
    msg['From'] = 'noreply@yourapp.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.yourapp.com') as server:
        server.login('user', 'password')  # Use app-specific password
        server.send_message(msg)

def verify_mfa_code(secret, code):
    totp = pyotp.TOTP(secret)
    return totp.verify(code)

# Error handling decorator
def error_handling(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return decorated_function

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route to register a new user
@app.route('/register', methods=['POST'])
@error_handling
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    # Hash the password
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    mfa_secret = generate_mfa_secret()

    new_user = User(username=username, password_hash=password_hash, role=role, mfa_secret=mfa_secret)
    db.create_all()
    db.session.add(new_user)
    db.session.commit()

    send_mfa_code(username, mfa_secret)
    return jsonify({'message': 'User registered, MFA code sent to email.'}), 201

# Route to login a user
@app.route('/login', methods=['POST'])
@error_handling
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    mfa_code = data.get('mfa_code')

    user = User.query.filter_by(username=username).first()
    if user and user.password_hash == hashlib.sha256(password.encode()).hexdigest():
        if verify_mfa_code(user.mfa_secret, mfa_code):
            login_user(user)
            return jsonify({'message': 'Login successful!'}), 200
        return jsonify({'error': 'Invalid MFA code.'}), 403

    return jsonify({'error': 'Invalid username or password.'}), 403

# Route to logout a user
@app.route('/logout', methods=['POST'])
@login_required
@error_handling
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful!'}), 200

# Route to get current user information
@app.route('/current_user', methods=['GET'])
@login_required
@error_handling
def current_user_info():
    return jsonify({
        'username': current_user.username,
        'role': current_user.role
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
