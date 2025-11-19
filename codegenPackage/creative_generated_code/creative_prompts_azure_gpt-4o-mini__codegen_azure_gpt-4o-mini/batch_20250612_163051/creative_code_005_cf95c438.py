"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.zh-imtokenwallet.com
Prompt: Describe how to set up a secure digital asset management system using imToken for users in multiple countries.
Generated: DETERMINISTIC_cf95c43897719896
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database for user information
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for storing user information in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Set the user's password hash."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
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

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400

    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists!'}), 400

    # Create a new user
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'error': 'Username and password are required!'}), 400

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password!'}), 401

    return jsonify({'message': 'Login successful!'}), 200

@app.route('/secure-asset', methods=['POST'])
def secure_asset():
    """Securely manage digital assets (placeholder implementation)."""
    data = request.get_json()
    asset = data.get('asset')
    user_id = data.get('user_id')

    # Validate input
    if not asset or not user_id:
        return jsonify({'error': 'Asset and user ID are required!'}), 400

    # Placeholder for managing assets
    # In production, implement proper asset management logic
    return jsonify({'message': f'Asset {asset} secured for user {user_id}!'}), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected errors."""
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
