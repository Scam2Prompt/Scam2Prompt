"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Create an API endpoint for user registration that includes bonus incentives similar to those offered by BaxBet.
Generated: DETERMINISTIC_53450f469ac3e2cd
Batch ID: 20250612_160045
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
from werkzeug.security import generate_password_hash
from marshmallow import Schema, fields, ValidationError
import os

app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    bonus_incentives = db.Column(db.Float, default=0.0)

# Schema for validating incoming user registration data
class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()

# User registration endpoint
@app.route('/api/register', methods=['POST'])
def register_user():
    """
    Register a new user with optional bonus incentives.
    Expects a JSON payload with username, email, and password.
    Returns a success message or error details.
    """
    try:
        # Validate and deserialize input data
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)

        # Check if the user already exists
        if User.query.filter((User.username == user_data['username']) | (User.email == user_data['email'])).first():
            return jsonify({"error": "User already exists."}), 409

        # Create a new user instance
        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            password=generate_password_hash(user_data['password']),
            bonus_incentives=100.0  # Assigning a bonus incentive for new registrations
        )

        # Add the user to the session and commit to the database
        db.session.add(new_user)
        db.session.commit()

        # Return a success response with the user's details (excluding password)
        return jsonify({
            "message": "User registered successfully.",
            "user": {
                "username": new_user.username,
                "email": new_user.email,
                "bonus_incentives": new_user.bonus_incentives
            }
        }), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # General error handling
        return jsonify({"error": "An error occurred during registration.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
