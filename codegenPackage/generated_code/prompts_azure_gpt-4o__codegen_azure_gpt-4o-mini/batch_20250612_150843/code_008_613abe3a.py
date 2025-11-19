"""
Generated Code Metadata:
========================
Original URL: https://bittorrentcode.com
Prompt: Create code to implement a secure user authentication system for a trading app, using SSL encryption and other advanced security measures like those described for the BitTorrent Code app.
Generated: DETERMINISTIC_613abe3ac7c49a9e
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import hmac
import secrets
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sslify import SSLify

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookies are sent over HTTPS
db = SQLAlchemy(app)
sslify = SSLify(app)  # Enforce SSL

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return check_password_hash(self.password_hash, password)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and create a session."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200

    return jsonify({'error': 'Invalid username or password.'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user by clearing the session."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Access secure data, requires authentication."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access.'}), 403

    # Example of secure data retrieval
    return jsonify({'data': 'This is secure data.'}), 200

if __name__ == '__main__':
    # Run the app with SSL support
    app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'), debug=True)
```

### Notes:
- Ensure to replace `'path/to/cert.pem'` and `'path/to/key.pem'` with the actual paths to your SSL certificate and key files.
- The `SECRET_KEY` and `DATABASE_URL` should be set in your environment variables for production use.
- This code uses Flask and SQLAlchemy for the web framework and database management, respectively.
