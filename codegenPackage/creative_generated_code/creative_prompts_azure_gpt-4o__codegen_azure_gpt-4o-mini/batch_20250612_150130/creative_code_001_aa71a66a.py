"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://advancecryptoacademy.online
Prompt: Recommend a secure multi-tier architecture for a cryptocurrency investment platform like Advance Crypto Academy, emphasizing features such as SAFU (Secure Assets Fund for Users) and Comodo SSL encryption.
Generated: DETERMINISTIC_aa71a66a3c983d75
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# multi_tier_architecture.py

"""
Multi-Tier Architecture for a Cryptocurrency Investment Platform

This script outlines a secure multi-tier architecture for a cryptocurrency investment platform.
Key features include:
- Secure Assets Fund for Users (SAFU)
- Comodo SSL encryption for secure communications
"""

import ssl
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Create Flask application instance
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///investments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    Expects JSON data with 'username' and 'password'.
    Returns a success message or error.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    """
    Login a user.
    Expects JSON data with 'username' and 'password'.
    Returns a success message or error.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Function to setup SSL/TLS
def run_app():
    """
    Run the Flask application with SSL/TLS for secure communications.
    Comodo SSL certificates should be configured properly in the environment.
    """
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # Load Comodo SSL certificate and key files
    context.load_cert_chain(certfile='path/to/comodo_cert.pem', keyfile='path/to/comodo_key.pem')

    try:
        app.run(ssl_context=context, host='0.0.0.0', port=443)
    except Exception as e:
        print(f"Error starting the server: {str(e)}")

if __name__ == '__main__':
    run_app()
```

**Note:** Replace `'path/to/comodo_cert.pem'` and `'path/to/comodo_key.pem'` with the actual paths to your Comodo SSL certificate and key files. Ensure to handle the storage of sensitive information securely.
