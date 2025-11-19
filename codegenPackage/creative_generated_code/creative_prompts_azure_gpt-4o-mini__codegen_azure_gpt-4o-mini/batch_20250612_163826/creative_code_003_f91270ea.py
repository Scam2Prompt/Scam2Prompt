"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Develop an API endpoint for managing membership registrations and inquiries for a running club, similar to the features offered by Thompson Estate Athletics.
Generated: DETERMINISTIC_f91270ead353990f
Batch ID: 20250612_163826
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Membership model
class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    inquiry = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'inquiry': self.inquiry
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to register a new member
@app.route('/api/members', methods=['POST'])
def register_member():
    data = request.json

    # Validate the input data
    if 'name' not in data or 'email' not in data:
        raise BadRequest("Missing 'name' or 'email' in request data.")
    
    # Create a new membership record
    new_member = Membership(name=data['name'], email=data['email'], inquiry=data.get('inquiry'))
    db.session.add(new_member)
    db.session.commit()

    return jsonify(new_member.to_dict()), 201

# API endpoint to get all members
@app.route('/api/members', methods=['GET'])
def get_members():
    members = Membership.query.all()
    return jsonify([member.to_dict() for member in members]), 200

# API endpoint to get a member by ID
@app.route('/api/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = Membership.query.get(member_id)
    if member is None:
        raise NotFound("Member not found.")
    return jsonify(member.to_dict()), 200

# API endpoint to update a member's inquiry
@app.route('/api/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.json
    member = Membership.query.get(member_id)

    if member is None:
        raise NotFound("Member not found.")

    if 'inquiry' in data:
        member.inquiry = data['inquiry']
    
    db.session.commit()
    return jsonify(member.to_dict()), 200

# API endpoint to delete a member
@app.route('/api/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = Membership.query.get(member_id)
    
    if member is None:
        raise NotFound("Member not found.")
    
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully."}), 204

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400

# Error handler for not found
@app.errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({"error": str(e)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
