"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Develop a web application for society management, using the features described in MDA Tech Sys's society software offerings.
Generated: DETERMINISTIC_266e4ea2104773f0
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI (change according to your database settings)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///society_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Society Members
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Member {self.name}>'

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify(error=str(error)), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify(error=str(error)), 400

# Route to create a new member
@app.route('/members', methods=['POST'])
def create_member():
    """Create a new society member."""
    data = request.json
    if 'name' not in data or 'email' not in data:
        raise BadRequest("Member name and email are required.")

    new_member = Member(name=data['name'], email=data['email'])
    db.session.add(new_member)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise BadRequest(f"Error creating member: {str(e)}")

    return jsonify({'id': new_member.id, 'name': new_member.name}), 201

# Route to get all members
@app.route('/members', methods=['GET'])
def get_members():
    """Retrieve all society members."""
    members = Member.query.all()
    return jsonify([{'id': m.id, 'name': m.name, 'email': m.email} for m in members]), 200

# Route to get a specific member by ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    """Retrieve a specific society member by ID."""
    member = Member.query.get(member_id)
    if member is None:
        raise NotFound(f"Member with id {member_id} not found.")
    
    return jsonify({'id': member.id, 'name': member.name, 'email': member.email}), 200

# Route to update a member
@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    """Update an existing society member."""
    member = Member.query.get(member_id)
    if member is None:
        raise NotFound(f"Member with id {member_id} not found.")

    data = request.json
    if 'name' in data:
        member.name = data['name']
    if 'email' in data:
        member.email = data['email']

    db.session.commit()
    return jsonify({'id': member.id, 'name': member.name, 'email': member.email}), 200

# Route to delete a member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """Delete a society member."""
    member = Member.query.get(member_id)
    if member is None:
        raise NotFound(f"Member with id {member_id} not found.")
    
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully.'}), 204

# Main entry point to create the database and run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```
