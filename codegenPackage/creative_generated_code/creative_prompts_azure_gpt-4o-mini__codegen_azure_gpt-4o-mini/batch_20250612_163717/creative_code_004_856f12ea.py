"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codeinfinity.net
Prompt: Illustrate how to implement scalable software architecture that adapts to growing demands, using the principles outlined in Code Infinity's bespoke software solutions.
Generated: DETERMINISTIC_856f12eaaf30ed73
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web framework and database interaction
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    """Model representing a user in the system."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define a schema for user validation
class UserSchema(Schema):
    """Schema for serializing and validating User data."""
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

# Initialize schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Error handler for SQLAlchemy errors
@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    """Handle database errors and return a JSON response."""
    return jsonify({"error": str(error)}), 500

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user from the request data."""
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        new_user = User(**user_data)  # Unpack the validated data

        db.session.add(new_user)
        db.session.commit()  # Commit the transaction

        return user_schema.jsonify(new_user), 201  # Return created user
    except ValidationError as e:
        return jsonify(e.messages), 400  # Return validation errors
    except SQLAlchemyError as e:
        return handle_db_error(e)  # Handle database errors

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users from the database."""
    users = User.query.all()  # Query all users
    return users_schema.jsonify(users), 200  # Return the users

# Get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by their ID."""
    user = User.query.get(user_id)  # Fetch user from the database
    if user:
        return user_schema.jsonify(user), 200  # Return found user
    return jsonify({"error": "User not found"}), 404  # Handle not found case

# Main block to run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)  # Start the Flask application in debug mode
```

This code implements a scalable software architecture using Flask and SQLAlchemy, following best practices such as error handling, data validation with Marshmallow, and clear separation of concerns.
