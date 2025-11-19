"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://us.mercari-vip5.vip
Prompt: Create a tutorial on implementing a mobile-focused user authentication system, referencing the strategic and creative aspects seen in Mercari's approach.
Generated: DETERMINISTIC_526f466f4231c47d
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# mobile_auth.py

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, jwt_refresh_token_required
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Setup database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# User schema for input validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

# Initialize the database (for development/testing purposes)
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """
    User registration endpoint. Accepts a JSON payload with username and password.
    Hashes the password and stores the user in the database.
    """
    user_schema = UserSchema()

    # Validate request data
    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)

    # Save the new user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    User login endpoint. Authenticates a user and returns a JWT token.
    """
    user_schema = UserSchema()

    # Validate request data
    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Find the user
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        # Create JWT token
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Protected endpoint that requires a valid JWT token.
    """
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, you will need to install the following packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Bcrypt Flask-JWT-Extended marshmallow
```

### Environment Variables
Make sure to set the `DATABASE_URL` and `JWT_SECRET_KEY` environment variables before running the application.
