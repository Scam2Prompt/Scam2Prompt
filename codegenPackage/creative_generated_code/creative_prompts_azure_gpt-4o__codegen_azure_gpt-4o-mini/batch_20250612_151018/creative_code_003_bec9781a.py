"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Create a registration system for new users, ensuring it includes validation for required fields, as seen on the Diverbox website.
Generated: DETERMINISTIC_bec9781a25e9ab04
Batch ID: 20250612_151018
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
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the SQLAlchemy ORM
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Schema for validating user input using Marshmallow
class UserSchema(Schema):
    username = fields.Str(required=True, validate=lambda s: len(s) > 2)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=lambda s: len(s) >= 6)

# Initialize the database
with app.app_context():
    db.create_all()

# Function to validate password complexity
def validate_password(password):
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError("Password must contain at least one special character.")

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    # Parse and validate the request data
    schema = UserSchema()
    try:
        # Validate and deserialize the input data
        user_data = schema.load(request.json)

        # Validate password complexity
        validate_password(user_data['password'])

        # Hash the password for security
        hashed_password = generate_password_hash(user_data['password'])

        # Create a new User instance
        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            password=hashed_password
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully."}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
