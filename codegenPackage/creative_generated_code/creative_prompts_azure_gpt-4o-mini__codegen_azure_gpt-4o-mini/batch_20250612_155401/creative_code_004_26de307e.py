"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetagreatamerican.com
Prompt: Illustrate how to implement a user registration system for the Meet A Great American community, focusing on capturing user details and their professional achievements.
Generated: DETERMINISTIC_26de307e3e685b60
Batch ID: 20250612_155401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    achievements = db.Column(db.Text, nullable=True)

# Create a schema for user registration validation
class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, validate=lambda p: len(p) >= 6)
    achievements = fields.Str(required=False)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        # Validate the input data
        user_schema = UserSchema()
        user_data = user_schema.load(request.json)

        # Check if the username or email already exists
        if User.query.filter((User.username == user_data['username']) | 
                              (User.email == user_data['email'])).first():
            return jsonify({"message": "Username or email already exists."}), 400

        # Hash the password before storing it
        hashed_password = generate_password_hash(user_data['password'], method='sha256')
        
        # Create a new user instance
        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            password=hashed_password,
            achievements=user_data.get('achievements', None)
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    except ValidationError as ve:
        return jsonify({"errors": ve.messages}), 422
    except Exception as e:
        return jsonify({"message": "An error occurred during registration.", "error": str(e)}), 500

# Endpoint to create the database (for demonstration purposes, should be run once)
@app.cli.command('create_db')
def create_db():
    """Create the database."""
    db.create_all()
    print("Database created successfully.")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
