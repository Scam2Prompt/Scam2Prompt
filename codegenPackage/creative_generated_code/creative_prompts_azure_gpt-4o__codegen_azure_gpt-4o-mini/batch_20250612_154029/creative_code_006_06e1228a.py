"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://us.mercari-vip5.vip
Prompt: Create a Python Flask API for user registration and login, including functionality for "Sign Up" and "Sign In" features.
Generated: DETERMINISTIC_06e1228a46c246a8
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration features
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    """User model for storing user data."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route for user registration (Sign Up)
@app.route('/signup', methods=['POST'])
def signup():
    """Handles user registration."""

    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400

    username = data['username']
    password = data['password']

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 409

    # Hash the password and create a new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error occurred during registration', 'error': str(e)}), 500

# Route for user login (Sign In)
@app.route('/signin', methods=['POST'])
def signin():
    """Handles user login."""

    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Username and password required'}), 400

    username = data['username']
    password = data['password']

    # Fetch the user from the database
    user = User.query.filter_by(username=username).first()

    # Verify the user and password
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Additional Notes for Production:
- Ensure to set the `DATABASE_URL` environment variable to your production database.
- Consider enabling HTTPS and configuring proper logging for production.
- Implement rate limiting and account lockout mechanisms for enhanced security.
