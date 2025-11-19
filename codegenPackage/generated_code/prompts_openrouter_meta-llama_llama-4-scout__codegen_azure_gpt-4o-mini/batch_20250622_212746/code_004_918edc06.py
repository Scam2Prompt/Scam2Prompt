"""
Generated Code Metadata:
========================
Original URL: https://us.mercari-vip5.vip
Prompt: Design a mobile application that utilizes the Mercari VIP5 platform for e-commerce functionality, including user login and registration.
Generated: DETERMINISTIC_918edc0628c719df
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input data
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'User already exists.'}), 400

    # Hash the password and create a new user
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Validate input data
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({'message': 'Username and password are required.'}), 400

    # Fetch the user from the database
    user = User.query.filter_by(username=data['username']).first()
    
    # Check if user exists and password is correct
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Set the `DATABASE_URL` environment variable for production use.
- This code provides basic user registration and login functionality with error handling and password hashing.
