"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aphatradespro.com
Prompt: Develop a secure login system for a trading platform that uses encryption and server security measures, inspired by Aphatradespro's emphasis on safety.
Generated: DETERMINISTIC_4ec323b1ab01817f
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app and set up configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize database and session
db = SQLAlchemy(app)
Session(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Generate a key for encryption and store it securely
def generate_key():
    key = Fernet.generate_key()
    return key

# Encrypt sensitive data (e.g., JWT secret)
def encrypt_data(data):
    fernet = Fernet(os.getenv('FERNET_KEY'))
    encrypted = fernet.encrypt(data.encode())
    return encrypted

# Decrypt sensitive data
def decrypt_data(encrypted_data):
    fernet = Fernet(os.getenv('FERNET_KEY'))
    decrypted = fernet.decrypt(encrypted_data).decode()
    return decrypted

# Create a new user with secure password hashing
def create_user(username, password):
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    try:
        create_user(username, password)
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        session['user_id'] = user.id  # Store user session
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# User logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Clear the user session
    return jsonify({'message': 'Logout successful'}), 200

# Run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```

### Required Packages
Ensure to install the required packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Session bcrypt python-dotenv cryptography
```

### Environment Variables
Create a `.env` file in your project root with the following variables:

```env
DATABASE_URI=sqlite:///trading_platform.db
SECRET_KEY=your_secret_key
FERNET_KEY=your_fernet_key
``` 

### Important Security Notes
1. Always use a strong secret key and Fernet key.
2. Use HTTPS for network communications to secure data in transit.
3. Consider implementing additional security measures such as rate limiting and account lockout for failed login attempts.
