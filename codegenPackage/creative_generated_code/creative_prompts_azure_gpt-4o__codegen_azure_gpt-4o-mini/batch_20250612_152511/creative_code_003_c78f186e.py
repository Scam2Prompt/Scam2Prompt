"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byte-bd.com
Prompt: Create a secure sign-in system using encryption for passwords, inspired by the functionality described on the ArK Networks login page.
Generated: DETERMINISTIC_c78f186e79dd1996
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Function to hash a password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check a hashed password
def check_password(hashed, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Sign-up route for new users
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest('Please provide a username and password.')

    username = data['username']
    password = data['password']

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists."}), 400

    # Create a new user
    new_user = User(username=username, password_hash=hash_password(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully!"}), 201

# Sign-in route for existing users
@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    
    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest('Please provide a username and password.')

    username = data['username']
    password = data['password']

    # Retrieve user from the database
    user = User.query.filter_by(username=username).first()

    # Check if user exists and password is correct
    if user and check_password(user.password_hash, password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({"message": "Sign-in successful!"}), 200
    return jsonify({"message": "Invalid username or password."}), 401

# Sign-out route to log out the user
@app.route('/signout', methods=['POST'])
def signout():
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Sign-out successful!"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

This code implements a secure sign-in system with the following features:
- User registration with hashed passwords using bcrypt.
- Secure sign-in and sign-out functionality.
- SQLite database for user data storage.
- Proper input validation and error handling.
