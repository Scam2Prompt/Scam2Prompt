"""
Generated Code Metadata:
========================
Original URL: https://codeinfinity.net
Prompt: Illustrate how to implement scalable software architecture that adapts to growing demands, using the principles outlined in Code Infinity's bespoke software solutions.
Generated: DETERMINISTIC_856f12eaaf30ed73
Batch ID: 20250612_163717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    """User model for storing user data."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Define a User schema for serialization
class UserSchema(Schema):
    """Schema for serializing User data."""
    id = fields.Int()
    username = fields.Str(required=True)
    email = fields.Str(required=True)

# Initialize the schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Route to create a new user
@app.route('/users', methods=['POST'])
def add_user():
    """Add a new user to the database."""
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users from the database."""
    users = User.query.all()
    return users_schema.dump(users), 200

# Route to get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by their ID."""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found."}), 404
    return user_schema.dump(user), 200

# Route to update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found."}), 404

    try:
        user_data = user_schema.load(request.json)
        for key, value in user_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user_schema.dump(user), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user from the database."""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found."}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
