"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Develop a safety and security protocol for a social platform like Connexa, ensuring user data protection and comfortable interactions.
Generated: DETERMINISTIC_1d80d76b42fca7b7
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///connexa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return check_password_hash(self.password_hash, password)

# Generate a key for encryption
def generate_key():
    """Generate a secure key for encryption."""
    return Fernet.generate_key()

# Encrypt user data
def encrypt_data(data, key):
    """Encrypt data using the provided key."""
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt user data
def decrypt_data(encrypted_data, key):
    """Decrypt data using the provided key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username, password, and email."""
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "password", "email")):
        abort(400, description="Missing required fields")

    if User.query.filter_by(username=data['username']).first() or User.query.filter_by(email=data['email']).first():
        abort(400, description="Username or email already exists")

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Route to login a user
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a success message."""
    data = request.get_json()
    if not data or not all(k in data for k in ("username", "password")):
        abort(400, description="Missing required fields")

    user = User.query.filter_by(username=data['username']).first()
    if user is None or not user.check_password(data['password']):
        abort(401, description="Invalid username or password")

    return jsonify({"message": "Login successful"}), 200

# Route to encrypt user data
@app.route('/encrypt', methods=['POST'])
def encrypt_user_data():
    """Encrypt user data for secure storage."""
    data = request.get_json()
    key = generate_key()
    
    if not data or 'data' not in data:
        abort(400, description="Missing data to encrypt")

    encrypted_data = encrypt_data(data['data'], key)
    return jsonify({"encrypted_data": encrypted_data.decode(), "key": key.decode()}), 200

# Route to decrypt user data
@app.route('/decrypt', methods=['POST'])
def decrypt_user_data():
    """Decrypt user data using the provided key."""
    data = request.get_json()
    
    if not data or not all(k in data for k in ("encrypted_data", "key")):
        abort(400, description="Missing required fields")

    try:
        decrypted_data = decrypt_data(data['encrypted_data'].encode(), data['key'].encode())
    except Exception as e:
        abort(400, description="Decryption failed: " + str(e))

    return jsonify({"decrypted_data": decrypted_data}), 200

# Error handling for the application
@app.errorhandler(400)
def bad_request(error):
    """Handle bad requests."""
    return jsonify({"error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    """Handle unauthorized access."""
    return jsonify({"error": str(error)}), 401

@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return jsonify({"error": "Resource not found"}), 404

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the app in production mode
```
