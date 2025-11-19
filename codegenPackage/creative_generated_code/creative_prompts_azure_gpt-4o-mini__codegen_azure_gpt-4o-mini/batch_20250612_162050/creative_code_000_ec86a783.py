"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfivetechnologies.com
Prompt: Generate a code snippet for a web application that utilizes best practices in application design and quality assurance as described by DFIVE Technologies.
Generated: DETERMINISTIC_ec86a783549d6629
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the database model
class User(db.Model):
    """User model to store user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for input validation using Marshmallow
class UserSchema(Schema):
    """Schema for validating user input data."""
    username = fields.String(required=True)
    email = fields.String(required=True)

user_schema = UserSchema()

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    try:
        # Validate request data
        data = request.get_json()
        validated_data = user_schema.load(data)

        # Create a new User instance
        new_user = User(username=validated_data['username'], email=validated_data['email'])
        db.session.add(new_user)
        db.session.commit()

        # Return success response
        return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email}), 201

    except ValidationError as ve:
        # Handle validation errors
        return jsonify({'error': ve.messages}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by their ID."""
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by their ID."""
    user = User.query.get(user_id)
    if user is None:
        abort(404, description="User not found")
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully'}), 204

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)
```
