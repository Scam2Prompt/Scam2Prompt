"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: Create an API that connects small business owners with resources for capacity building and skills training, reflecting the mission of جمعية علشانك يا بلدي.
Generated: DETERMINISTIC_32b7694abd1ae347
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///resources.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False)

# Create a schema for serializing Resource objects
class ResourceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    category = fields.Str(required=True)

# Initialize the schema
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

# Error handling for resource creation
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Endpoint to create a new resource
@app.route('/resources', methods=['POST'])
def create_resource():
    """Create a new resource for capacity building and skills training."""
    json_data = request.get_json()
    try:
        resource = resource_schema.load(json_data)
        new_resource = Resource(**resource)
        db.session.add(new_resource)
        db.session.commit()
        return resource_schema.dump(new_resource), 201
    except ValidationError as err:
        return handle_validation_error(err)

# Endpoint to get all resources
@app.route('/resources', methods=['GET'])
def get_resources():
    """Retrieve all resources."""
    resources = Resource.query.all()
    return resources_schema.dump(resources), 200

# Endpoint to get a specific resource by ID
@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """Retrieve a specific resource by its ID."""
    resource = Resource.query.get_or_404(resource_id)
    return resource_schema.dump(resource), 200

# Endpoint to update a resource
@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """Update an existing resource."""
    json_data = request.get_json()
    resource = Resource.query.get_or_404(resource_id)
    try:
        updated_resource = resource_schema.load(json_data)
        for key, value in updated_resource.items():
            setattr(resource, key, value)
        db.session.commit()
        return resource_schema.dump(resource), 200
    except ValidationError as err:
        return handle_validation_error(err)

# Endpoint to delete a resource
@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """Delete a resource by its ID."""
    resource = Resource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify({'message': 'Resource deleted successfully'}), 204

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
