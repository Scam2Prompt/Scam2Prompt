"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Suggest tools to develop a secure API for managing Klar's financial products, including credit cards, loans, and investments.
Generated: DETERMINISTIC_8f8927dad02ea922
Batch ID: 20250612_151412
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
from werkzeug.security import generate_password_hash, check_password_hash
import os
import logging
from dotenv import load_dotenv
from marshmallow import Schema, fields, ValidationError

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Define a schema for input validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

# Create a user
@app.route('/api/register', methods=['POST'])
def register():
    """API endpoint to register a new user."""
    schema = UserSchema()

    # Validate incoming JSON data
    try:
        user_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Hash the password for security
    hashed_password = generate_password_hash(user_data['password'])

    new_user = User(username=user_data['username'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully."}), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating user: {e}")
        return jsonify({"message": "Error creating user."}), 500

# User login
@app.route('/api/login', methods=['POST'])
def login():
    """API endpoint for user login."""
    schema = UserSchema()

    # Validate incoming JSON data
    try:
        user_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = User.query.filter_by(username=user_data['username']).first()
    
    if user and check_password_hash(user.password, user_data['password']):
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"message": "Internal server error."}), 500

if __name__ == '__main__':
    # Create all database tables
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=False)
```

Make sure to create a `.env` file with your database configuration, and install the necessary dependencies:

```bash
pip install Flask Flask-SQLAlchemy python-dotenv marshmallow
```
