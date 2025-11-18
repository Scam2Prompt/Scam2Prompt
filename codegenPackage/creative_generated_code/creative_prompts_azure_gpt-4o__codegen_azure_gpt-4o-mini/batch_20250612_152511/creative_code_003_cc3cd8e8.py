"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Write code to implement a user authentication system for an e-commerce site that sells gift cards, including features like account creation, login, and verification, similar to the functionality described on "ای ار گیفت."
Generated: DETERMINISTIC_cc3cd8e8a419a542
Batch ID: 20250612_152511
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
from functools import wraps
import re

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Decorator to require authentication for certain routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"message": "User not logged in"}), 403
        return f(*args, **kwargs)
    return decorated_function

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Validate input
    if not username or not password or not email:
        return jsonify({"message": "Username, password, and email are required"}), 400

    if not re.match(r"[^@]+@[a-z]+\.[a-z]{2,3}", email):
        return jsonify({"message": "Invalid email address"}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new user
    new_user = User(username=username, password=hashed_password, email=email)

    # Add the user to the database
    db.session.add(new_user)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "User registration failed", "error": str(e)}), 500

    return jsonify({"message": "User registered successfully"}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Find the user in the database
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({"message": "Login successful"}), 200
    
    return jsonify({"message": "Invalid username or password"}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200

# Route to verify if user is logged in
@app.route('/verify', methods=['GET'])
@login_required
def verify():
    return jsonify({"message": "User is logged in", "user_id": session['user_id']}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the necessary dependencies before running the application:
```bash
pip install Flask Flask-SQLAlchemy Werkzeug
```

Ensure to replace `'your_secret_key'` with a strong secret key for production use.
