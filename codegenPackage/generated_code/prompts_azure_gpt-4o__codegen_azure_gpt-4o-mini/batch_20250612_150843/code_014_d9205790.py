"""
Generated Code Metadata:
========================
Original URL: https://tradegpt360-evix.com
Prompt: Write code to implement a secure login system for a cryptocurrency trading platform, incorporating SSL encryption as described in the TradeGPT 360 Evix application.
Generated: DETERMINISTIC_d92057908482687f
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sslify import SSLify
import os

# Initialize the Flask application
app = Flask(__name__)

# Enable SSL for secure connections
sslify = SSLify(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a secure database in production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Use a strong secret key

# Initialize the database
db = SQLAlchemy(app)

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

# Create the database tables
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
    """Log in an existing user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({'message': 'Logout successful.'}), 200

@app.route('/secure-data', methods=['GET'])
def secure_data():
    """Access secure data (requires login)."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access.'}), 403

    return jsonify({'data': 'This is secure data.'}), 200

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))  # Use your SSL certificate and key
```

**Note:** Ensure you have the necessary SSL certificate (`cert.pem`) and key (`key.pem`) for the application to run securely.
