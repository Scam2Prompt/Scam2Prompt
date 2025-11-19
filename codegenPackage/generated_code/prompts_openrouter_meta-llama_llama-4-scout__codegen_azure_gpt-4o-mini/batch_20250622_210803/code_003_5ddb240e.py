"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: What are some best practices for organizing a local civil protection group, similar to the one in Torre d'Isola, and how can they be implemented using existing libraries and frameworks?
Generated: DETERMINISTIC_5ddb240e6794d730
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civil_protection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Group model
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    members = db.relationship('Member', backref='group', lazy=True)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)

# Define schemas for validation
class GroupSchema(Schema):
    name = fields.Str(required=True)

class MemberSchema(Schema):
    name = fields.Str(required=True)
    contact_info = fields.Str(required=True)
    group_id = fields.Int(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new group
@app.route('/groups', methods=['POST'])
def create_group():
    try:
        # Validate and deserialize input
        group_schema = GroupSchema()
        group_data = group_schema.load(request.json)
        
        # Create a new group
        new_group = Group(name=group_data['name'])
        db.session.add(new_group)
        db.session.commit()
        
        return jsonify({"message": "Group created", "id": new_group.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating group: {e}")
        return jsonify({"error": "An error occurred while creating the group."}), 500

# Route to add a member to a group
@app.route('/members', methods=['POST'])
def add_member():
    try:
        # Validate and deserialize input
        member_schema = MemberSchema()
        member_data = member_schema.load(request.json)
        
        # Create a new member
        new_member = Member(
            name=member_data['name'],
            contact_info=member_data['contact_info'],
            group_id=member_data['group_id']
        )
        db.session.add(new_member)
        db.session.commit()
        
        return jsonify({"message": "Member added", "id": new_member.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error adding member: {e}")
        return jsonify({"error": "An error occurred while adding the member."}), 500

# Route to get all groups
@app.route('/groups', methods=['GET'])
def get_groups():
    try:
        groups = Group.query.all()
        return jsonify([{"id": group.id, "name": group.name} for group in groups]), 200
    except Exception as e:
        logging.error(f"Error retrieving groups: {e}")
        return jsonify({"error": "An error occurred while retrieving groups."}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
