"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Develop a RESTful API to manage PSHP membership applications and approvals.
Generated: DETERMINISTIC_dabae7dd297fe441
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Membership model
class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    approved = db.Column(db.Boolean, default=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Define the Membership schema
class MembershipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Membership

# Initialize the schema
membership_schema = MembershipSchema()
memberships_schema = MembershipSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new membership application
@app.route('/memberships', methods=['POST'])
def add_membership():
    try:
        name = request.json['name']
        email = request.json['email']
        if not name or not email:
            raise BadRequest("Name and email are required.")

        new_membership = Membership(name, email)
        db.session.add(new_membership)
        db.session.commit()

        return membership_schema.jsonify(new_membership), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all membership applications
@app.route('/memberships', methods=['GET'])
def get_memberships():
    memberships = Membership.query.all()
    return memberships_schema.jsonify(memberships), 200

# Get a specific membership application by ID
@app.route('/memberships/<int:id>', methods=['GET'])
def get_membership(id):
    membership = Membership.query.get(id)
    if not membership:
        raise NotFound("Membership not found.")
    return membership_schema.jsonify(membership), 200

# Approve a membership application
@app.route('/memberships/<int:id>/approve', methods=['PUT'])
def approve_membership(id):
    membership = Membership.query.get(id)
    if not membership:
        raise NotFound("Membership not found.")
    
    membership.approved = True
    db.session.commit()
    return membership_schema.jsonify(membership), 200

# Delete a membership application
@app.route('/memberships/<int:id>', methods=['DELETE'])
def delete_membership(id):
    membership = Membership.query.get(id)
    if not membership:
        raise NotFound("Membership not found.")
    
    db.session.delete(membership)
    db.session.commit()
    return jsonify({"message": "Membership deleted."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
