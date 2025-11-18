"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sundusartjrny.pages.dev
Prompt: Recommend best practices for designing a secure and private user registration system for a digital art gallery platform, referencing JRNY Gallery's encryption approach.
Generated: DETERMINISTIC_cc6d9653149905c8
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Create the database
with app.app_context():
    db.create_all()

# Function to hash passwords
def hash_password(password):
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check password validity
def check_password(password, password_hash):
    """Validates a password against its hash."""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

# User registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user."""
    data = request.get_json()

    # Validate input
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Email and password are required"}), 400

    email = data['email']
    password = data['password']

    # Hash the password
    password_hash = hash_password(password)

    # Create a new user
    new_user = User(email=email, password_hash=password_hash)

    # Attempt to add the user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
        return UserSchema().jsonify(new_user), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        # Log error (to be implemented)
        return jsonify({"error": "An unexpected error occurred: {}".format(str(e))}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application with debug mode off for production
    app.run(debug=False)
```
