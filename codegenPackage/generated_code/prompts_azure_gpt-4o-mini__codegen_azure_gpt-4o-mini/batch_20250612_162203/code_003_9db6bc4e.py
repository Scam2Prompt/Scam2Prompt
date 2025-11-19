"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Create a RESTful API design for a church community platform that supports features like member engagement and ministry updates, reflecting the mission of Word of Life Northwest.
Generated: DETERMINISTIC_9db6bc4eb9a44303
Batch ID: 20250612_162203
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///church_community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    ministry = db.Column(db.String(100), nullable=True)

# Define the schema for serialization
class MemberSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    ministry = fields.Str()

# Initialize the schema
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Route to create a new member
@app.route('/members', methods=['POST'])
def add_member():
    """Add a new member to the community."""
    json_data = request.get_json()
    try:
        member = member_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_member = Member(**member)
    db.session.add(new_member)
    db.session.commit()
    return member_schema.jsonify(new_member), 201

# Route to get all members
@app.route('/members', methods=['GET'])
def get_members():
    """Retrieve all members in the community."""
    members = Member.query.all()
    return members_schema.jsonify(members), 200

# Route to get a specific member by ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    """Retrieve a member by their ID."""
    member = Member.query.get(member_id)
    if member is None:
        abort(404, description="Member not found")
    return member_schema.jsonify(member), 200

# Route to update a member's information
@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    """Update a member's information."""
    member = Member.query.get(member_id)
    if member is None:
        abort(404, description="Member not found")

    json_data = request.get_json()
    try:
        updated_member = member_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    for key, value in updated_member.items():
        setattr(member, key, value)
    
    db.session.commit()
    return member_schema.jsonify(member), 200

# Route to delete a member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """Delete a member from the community."""
    member = Member.query.get(member_id)
    if member is None:
        abort(404, description="Member not found")

    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
