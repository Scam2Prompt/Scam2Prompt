"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Create a REST API that facilitates communication between different public sector departments, leveraging Licitare's solutions in T.I and system development.
Generated: DETERMINISTIC_204dafa95adb8881
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///departments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Department model
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    communication_info = db.Column(db.String(255), nullable=True)

    def __init__(self, name, communication_info):
        self.name = name
        self.communication_info = communication_info

# Department schema
class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department

# Initialize the database
with app.app_context():
    db.create_all()

# Create a new department
@app.route('/departments', methods=['POST'])
def add_department():
    """Create a new department."""
    try:
        name = request.json.get('name')
        communication_info = request.json.get('communication_info')

        if not name:
            raise BadRequest("Department name is required.")

        new_department = Department(name, communication_info)
        db.session.add(new_department)
        db.session.commit()
        
        return DepartmentSchema().jsonify(new_department), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all departments
@app.route('/departments', methods=['GET'])
def get_departments():
    """Retrieve all departments."""
    departments = Department.query.all()
    return DepartmentSchema(many=True).jsonify(departments), 200

# Get a department by ID
@app.route('/departments/<int:id>', methods=['GET'])
def get_department(id):
    """Retrieve a department by its ID."""
    department = Department.query.get(id)
    if department is None:
        raise NotFound("Department not found.")
    return DepartmentSchema().jsonify(department), 200

# Update a department
@app.route('/departments/<int:id>', methods=['PUT'])
def update_department(id):
    """Update an existing department."""
    department = Department.query.get(id)
    if department is None:
        raise NotFound("Department not found.")

    name = request.json.get('name', department.name)
    communication_info = request.json.get('communication_info', department.communication_info)

    department.name = name
    department.communication_info = communication_info
    db.session.commit()
    
    return DepartmentSchema().jsonify(department), 200

# Delete a department
@app.route('/departments/<int:id>', methods=['DELETE'])
def delete_department(id):
    """Delete a department."""
    department = Department.query.get(id)
    if department is None:
        raise NotFound("Department not found.")
    
    db.session.delete(department)
    db.session.commit()
    
    return jsonify({"message": "Department deleted successfully."}), 204

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
