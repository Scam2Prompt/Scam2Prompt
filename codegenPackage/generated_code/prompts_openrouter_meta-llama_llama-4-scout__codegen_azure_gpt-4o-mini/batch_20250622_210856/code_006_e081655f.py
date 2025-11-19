"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Design a RESTful API for a child protection system, incorporating features for reporting and responding to child rights violations.
Generated: DETERMINISTIC_e081655f9a153dac
Batch ID: 20250622_210856
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///child_protection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database model for Child Rights Violations
class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    reported_by = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')

    def __init__(self, description, reported_by):
        self.description = description
        self.reported_by = reported_by

# Marshmallow schema for serialization
class ViolationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Violation

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to report a child rights violation
@app.route('/violations', methods=['POST'])
def report_violation():
    """Report a new child rights violation."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'description' not in data or 'reported_by' not in data:
        raise BadRequest("Missing required fields: 'description' and 'reported_by'.")

    # Create a new violation
    new_violation = Violation(description=data['description'], reported_by=data['reported_by'])
    
    # Add to the database
    db.session.add(new_violation)
    db.session.commit()

    return ViolationSchema().jsonify(new_violation), 201

# Endpoint to get all reported violations
@app.route('/violations', methods=['GET'])
def get_violations():
    """Retrieve all reported child rights violations."""
    violations = Violation.query.all()
    return ViolationSchema(many=True).jsonify(violations), 200

# Endpoint to get a specific violation by ID
@app.route('/violations/<int:id>', methods=['GET'])
def get_violation(id):
    """Retrieve a specific child rights violation by ID."""
    violation = Violation.query.get(id)
    if violation is None:
        raise NotFound("Violation not found.")
    return ViolationSchema().jsonify(violation), 200

# Endpoint to update the status of a violation
@app.route('/violations/<int:id>', methods=['PUT'])
def update_violation(id):
    """Update the status of a child rights violation."""
    violation = Violation.query.get(id)
    if violation is None:
        raise NotFound("Violation not found.")

    data = request.get_json()
    if 'status' in data:
        violation.status = data['status']
    
    db.session.commit()
    return ViolationSchema().jsonify(violation), 200

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
