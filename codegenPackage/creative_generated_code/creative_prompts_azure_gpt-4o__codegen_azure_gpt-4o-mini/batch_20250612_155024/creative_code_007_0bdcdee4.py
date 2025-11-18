"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Develop an API that allows users to interact with Avatars in a growing colony simulation, inspired by the "Parallel Colony" concept on the website.
Generated: DETERMINISTIC_0bdcdee47fc1a906
Batch ID: 20250612_155024
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

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avatars.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Avatar model
class Avatar(db.Model):
    """Model representing an Avatar in the colony."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    species = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Avatar {self.name}, Age: {self.age}, Species: {self.species}>'

# Schema for validating Avatar data
class AvatarSchema(Schema):
    """Schema for serializing and validating Avatar data."""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    age = fields.Int(required=True)
    species = fields.Str(required=True)

avatar_schema = AvatarSchema()
avatars_schema = AvatarSchema(many=True)

# Create the database and tables
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# API endpoint to create a new Avatar
@app.route('/avatars', methods=['POST'])
def add_avatar():
    """Create a new Avatar."""
    try:
        # Validate input data
        avatar_data = avatar_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_avatar = Avatar(**avatar_data)
    db.session.add(new_avatar)
    db.session.commit()
    return avatar_schema.jsonify(new_avatar), 201

# API endpoint to retrieve all Avatars
@app.route('/avatars', methods=['GET'])
def get_avatars():
    """Retrieve all Avatars."""
    avatars = Avatar.query.all()
    return avatars_schema.jsonify(avatars), 200

# API endpoint to retrieve a specific Avatar by ID
@app.route('/avatars/<int:id>', methods=['GET'])
def get_avatar(id):
    """Retrieve a specific Avatar by ID."""
    avatar = Avatar.query.get_or_404(id)
    return avatar_schema.jsonify(avatar), 200

# API endpoint to update an Avatar
@app.route('/avatars/<int:id>', methods=['PUT'])
def update_avatar(id):
    """Update an existing Avatar."""
    avatar = Avatar.query.get_or_404(id)
    try:
        # Validate input data
        avatar_data = avatar_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    avatar.name = avatar_data['name']
    avatar.age = avatar_data['age']
    avatar.species = avatar_data['species']
    db.session.commit()
    return avatar_schema.jsonify(avatar), 200

# API endpoint to delete an Avatar
@app.route('/avatars/<int:id>', methods=['DELETE'])
def delete_avatar(id):
    """Delete an Avatar."""
    avatar = Avatar.query.get_or_404(id)
    db.session.delete(avatar)
    db.session.commit()
    return jsonify({'message': 'Avatar deleted successfully'}), 204

# Error handling for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unhandled exceptions."""
    return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```
