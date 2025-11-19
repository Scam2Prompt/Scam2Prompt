"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marttrade.org
Prompt: Describe how to securely implement user authentication for an investment platform like Lucidbrokers Investment, considering their focus on security.
Generated: DETERMINISTIC_6372e0b41bd5ef9e
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of secure user authentication using Flask, SQLAlchemy, and bcrypt for password hashing. This focuses on security best practices.

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

app = Flask(__name__)

# Configuration for the app and database
app.config['SECRET_KEY'] = 'your_super_secret_key'  # Replace with a strong random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model for storing user credentials securely
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

# Error handling decorator
@app.errorhandler(404)
def handle_404_error(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def handle_500_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        # Check if username is already taken
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already taken'}), 400

        # Hash the password securely
        password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

        # Create and save the new user
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to authenticate a user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Retrieve the user from the database
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Store user session (example, for demonstration purposes)
        session['user_id'] = user.id

        return jsonify({'message': 'Login successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to logout a user
@app.route('/logout', methods=['POST'])
def logout():
    try:
        session.pop('user_id', None)
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Replace `your_super_secret_key` in `SECRET_KEY` with a strong, securely generated random key. You can use Python's `secrets` module for this.
2. Use HTTPS in production to encrypt communication between the client and the server.
3. Consider implementing additional security features like rate limiting, account lockout for repeated failed login attempts, and two-factor authentication (2FA).
