"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfree.website
Prompt: Write code to securely integrate AKANWD with a healthcare analytics system, ensuring compliance with its top-tier security protocols for data encryption and access controls.
Generated: DETERMINISTIC_61e1525d097f286a
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

# Initialize Flask application
app = Flask(__name__)

# Configure the application to connect to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_analytics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a strong key

# Initialize the database
db = SQLAlchemy(app)

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Use Fernet for symmetric encryption
class Encryptor:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt(self, data):
        """Encrypt the data."""
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        """Decrypt the data."""
        return self.cipher.decrypt(encrypted_data).decode()

# User model for database representation
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.LargeBinary, nullable=False)

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Error handling for invalid user access
def access_control(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.headers.get('Authorization'):
            logging.warning('Unauthorized access attempt')
            return jsonify({'message': 'Unauthorized access'}), 403
        return func(*args, **kwargs)
    return wrapper

# Endpoint for user registration with encryption
@app.route('/register', methods=['POST'])
def register():
    """Register a new user with encrypted password."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    key = generate_key()  # Generate a key for encryption
    encryptor = Encryptor(key)
    encrypted_password = encryptor.encrypt(password)

    new_user = User(username=username, password_hash=encrypted_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# Endpoint for user login with decryption
@app.route('/login', methods=['POST'])
@access_control
def login():
    """Login an existing user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    encryptor = Encryptor(user.password_hash)
    try:
        decryptor_password = encryptor.decrypt(user.password_hash)
    except Exception as e:
        logging.error(f'Decryption error: {e}')
        return jsonify({'message': 'Invalid credentials'}), 403

    if decryptor_password == password.encode():
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 403

# Main function to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the app in production mode
```

Make sure to replace `'your_secret_key'` with a strong, secure key for your application. Additionally, configure the SQLAlchemy database URI to match your actual database setup.
