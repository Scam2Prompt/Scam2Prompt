"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Create a user registration and login system for an online gaming platform, incorporating features like currency selection and account security as described on 1Win.
Generated: DETERMINISTIC_3c987e2b382af066
Batch ID: 20250612_145255
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
import uuid

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # For production, use a more robust database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    currency = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

# Create all tables
with app.app_context():
    db.create_all()

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    currency = data.get('currency')

    # Basic validation
    if not username or not password or not currency:
        return jsonify({'message': 'All fields are required!'}), 400

    # Check for existing user
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists!'}), 400

    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new user
    new_user = User(username=username, password=hashed_password, currency=currency)
    db.session.add(new_user)
    
    try:
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error occurred during registration.', 'error': str(e)}), 500

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Basic validation
    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    # Find the user
    user = User.query.filter_by(username=username).first()

    # Check if user exists and password matches
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials!'}), 401

    return jsonify({'message': 'Login successful!', 'currency': user.currency}), 200

# Error handler for invalid JSON
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'message': 'Bad request'}), 400

# Main driver function
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=True during development only
```
