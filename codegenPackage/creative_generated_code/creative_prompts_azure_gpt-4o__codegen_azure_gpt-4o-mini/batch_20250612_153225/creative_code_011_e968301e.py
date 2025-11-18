"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Create a web application prototype for managing the roles and responsibilities of "Weavers" and "Keepers" in a Kallimos pocket neighborhood.
Generated: DETERMINISTIC_e968301e73f5459f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kallimos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Role model
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    responsibilities = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Role instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'responsibilities': self.responsibilities,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/roles', methods=['GET'])
def get_roles():
    """Retrieve all roles in the Kallimos neighborhood."""
    roles = Role.query.all()
    return jsonify([role.to_dict() for role in roles]), 200

@app.route('/roles', methods=['POST'])
def create_role():
    """Create a new role in the Kallimos neighborhood."""
    if not request.json or not 'name' in request.json or not 'responsibilities' in request.json:
        abort(400, description="Request must include 'name' and 'responsibilities'.")

    new_role = Role(
        name=request.json['name'],
        responsibilities=request.json['responsibilities']
    )
    db.session.add(new_role)
    db.session.commit()
    
    return jsonify(new_role.to_dict()), 201

@app.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    """Retrieve a specific role by ID."""
    role = Role.query.get_or_404(role_id)
    return jsonify(role.to_dict()), 200

@app.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    """Update an existing role by ID."""
    role = Role.query.get_or_404(role_id)

    if not request.json:
        abort(400, description="Request must be JSON.")

    # Update fields if provided
    if 'name' in request.json:
        role.name = request.json['name']
    if 'responsibilities' in request.json:
        role.responsibilities = request.json['responsibilities']

    db.session.commit()
    return jsonify(role.to_dict()), 200

@app.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    """Delete a specific role by ID."""
    role = Role.query.get_or_404(role_id)
    db.session.delete(role)
    db.session.commit()
    return jsonify({'result': True}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
