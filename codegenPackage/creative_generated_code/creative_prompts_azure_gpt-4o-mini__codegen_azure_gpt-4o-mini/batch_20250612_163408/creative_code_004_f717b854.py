"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Create a simple API endpoint in Python for user registration that includes input validation, similar to the registration process on diverbox.com.pe.
Generated: DETERMINISTIC_f717b854662519fe
Batch ID: 20250612_163408
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# User registration schema for input validation
class UserRegistrationSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=lambda s: len(s) >= 6)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register_user():
    # Parse and validate input data
    try:
        data = request.json
        validated_data = UserRegistrationSchema().load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Check if the user already exists
    if User.query.filter_by(username=validated_data['username']).first() or \
       User.query.filter_by(email=validated_data['email']).first():
        return jsonify({"error": "Username or email already exists."}), 400

    # Create new user
    new_user = User(
        username=validated_data['username'],
        email=validated_data['email'],
        password=generate_password_hash(validated_data['password'])
    )

    # Add user to the database and commit
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User registered successfully."}), 201

# Create database before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
