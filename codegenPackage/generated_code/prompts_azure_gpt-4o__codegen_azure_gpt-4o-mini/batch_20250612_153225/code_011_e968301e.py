"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Create a web application prototype for managing the roles and responsibilities of "Weavers" and "Keepers" in a Kallimos pocket neighborhood.
Generated: DETERMINISTIC_e968301e73f5459f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kallimos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Role model
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    responsibilities = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Role {self.name}>'

# Define the Role Schema for serialization
class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    responsibilities = fields.Str(required=True)

# Initialize the schema
role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new role
@app.route('/roles', methods=['POST'])
def create_role():
    """Create a new role with responsibilities."""
    try:
        # Validate and deserialize input
        role_data = role_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if the role already exists
    if Role.query.filter_by(name=role_data['name']).first():
        return jsonify({"error": "Role already exists."}), 400

    # Create a new role
    new_role = Role(name=role_data['name'], responsibilities=role_data['responsibilities'])
    db.session.add(new_role)
    db.session.commit()

    return role_schema.jsonify(new_role), 201

# Route to get all roles
@app.route('/roles', methods=['GET'])
def get_roles():
    """Retrieve all roles."""
    roles = Role.query.all()
    return roles_schema.jsonify(roles), 200

# Route to update a role
@app.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    """Update an existing role."""
    role = Role.query.get(role_id)
    if not role:
        return jsonify({"error": "Role not found."}), 404

    try:
        # Validate and deserialize input
        role_data = role_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update role attributes
    role.name = role_data['name']
    role.responsibilities = role_data['responsibilities']
    db.session.commit()

    return role_schema.jsonify(role), 200

# Route to delete a role
@app.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    """Delete a role."""
    role = Role.query.get(role_id)
    if not role:
        return jsonify({"error": "Role not found."}), 404

    db.session.delete(role)
    db.session.commit()

    return jsonify({"message": "Role deleted successfully."}), 204

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found."}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
