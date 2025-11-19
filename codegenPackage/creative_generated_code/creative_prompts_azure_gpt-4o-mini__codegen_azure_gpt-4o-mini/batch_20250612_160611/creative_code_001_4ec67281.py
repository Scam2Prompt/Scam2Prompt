"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ens.gifts
Prompt: How can I implement a user authentication system for a gift-giving platform similar to ens.gifts?
Generated: DETERMINISTIC_4ec672814eb8cb73
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Input validation
    if not username or not email or not password:
        return jsonify({'message': 'Missing fields'}), 400

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'message': 'User already exists'}), 400

    # Create a new user
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate an existing user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Input validation
    if not username or not password:
        return jsonify({'message': 'Missing fields'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful', 'username': user.username}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/profile', methods=['GET'])
def profile():
    """Get the current user's profile."""
    user_id = session.get('user_id')
    if user_id is None:
        return jsonify({'message': 'Not logged in'}), 401

    user = User.query.get(user_id)
    if user:
        return jsonify({'username': user.username, 'email': user.email}), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Make sure to set the `SECRET_KEY` as an environment variable or replace it with a secure value before running the application.
- This implementation uses Flask and SQLite for simplicity. For production, consider using a more robust database and implementing additional security measures.
