"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Develop a simple login and registration system for an online poker platform, referencing the easy registration process described on DominoBet.
Generated: DETERMINISTIC_368dd6fc0edcd364
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poker_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    try:
        username = request.json['username']
        password = request.json['password']

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"message": "Username already exists"}), 409

        # Create a new user
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    try:
        username = request.json['username']
        password = request.json['password']

        # Fetch user from database
        user = User.query.filter_by(username=username).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    try:
        session.pop('user_id', None)
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
