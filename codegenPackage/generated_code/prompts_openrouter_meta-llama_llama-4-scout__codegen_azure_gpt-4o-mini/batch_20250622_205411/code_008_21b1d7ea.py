"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Design a RESTful API for a zero-resistance living system, as described in Matt Furey's The Zero Resistance Living System course.
Generated: DETERMINISTIC_21b1d7ead19cd700
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zero_resistance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Create a schema for serializing User data
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)

# Initialize the schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    users = User.query.all()
    return users_schema.jsonify(users), 200

# Get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by ID."""
    user = User.query.get_or_404(user_id)
    return user_schema.jsonify(user), 200

# Update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user by ID."""
    user = User.query.get_or_404(user_id)
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        for key, value in user_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user_schema.jsonify(user), 200
    except Exception as e:
        db.session.rollback()
        abort(400, str(e))

# Delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
