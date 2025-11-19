"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypton-exchange.com
Prompt: Develop a user registration process in a web application that mimics the Crypton exchange's alpha testing registration system.
Generated: DETERMINISTIC_2ae9aa22a43ce1d8
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import re

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model to store user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate password strength
def is_strong_password(password):
    return (len(password) >= 8 and 
            re.search(r'\d', password) and 
            re.search(r'[A-Z]', password) and 
            re.search(r'[a-z]', password) and 
            re.search(r'[!@#$%^&*()_+]', password))

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input data
    try:
        username = data['username']
        email = data['email']
        password = data['password']
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400

    # Check for username and email validity
    if not username or not email or not password:
        return jsonify({'error': 'Username, email, and password are required.'}), 400

    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format.'}), 400

    if not is_strong_password(password):
        return jsonify({'error': 'Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'}), 400

    # Check for existing user
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists.'}), 400

    # Create new user
    new_user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password)
    )

    # Add user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
