"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airpot-02.vercel.app
Prompt: Provide code snippets for creating a user authentication system that includes sign-in and sign-up functionalities.
Generated: DETERMINISTIC_54bda44a9c74a52e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_auth.py

import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a strong secret key
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Initialize the database (create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Sign-up endpoint
@app.route('/signup', methods=['POST'])
def signup():
    """Sign up a new user."""
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        # Check if the user already exists
        if User.query.filter_by(username=username).first() is not None:
            return jsonify({"message": "User already exists"}), 400

        # Create a new user
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Sign-in endpoint
@app.route('/signin', methods=['POST'])
def signin():
    """Sign in an existing user."""
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        # Fetch user from DB
        user = User.query.filter_by(username=username).first()

        # Validate user credentials
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            session['user_id'] = user.id  # Manage session
            return jsonify({"message": "Sign-in successful", "user_id": user.id}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401

    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    try:
        session.pop('user_id', None)
        return jsonify({"message": "Logged out successfully"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
To run the above code, you'll need to install the following packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow bcrypt
```

Make sure to replace `'your_secret_key_here'` with a strong, random secret key before deploying in production.
