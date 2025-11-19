"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Create an API that provides resources and exercises for women looking to improve their emotional stability, as outlined in the "5 atitudes que destroem o seu emocional."
Generated: DETERMINISTIC_2f1bffdc22fd6a3b
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotional_stability.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

# Define the Resource schema for serialization
class ResourceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/resources', methods=['POST'])
def add_resource():
    """Add a new resource to the database."""
    json_data = request.get_json()
    
    # Validate the input data
    try:
        resource_data = resource_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors
    
    # Create a new Resource instance
    new_resource = Resource(**resource_data)
    
    # Add the resource to the session and commit
    db.session.add(new_resource)
    db.session.commit()

    return resource_schema.dump(new_resource), 201

@app.route('/resources', methods=['GET'])
def get_resources():
    """Get all resources from the database."""
    resources = Resource.query.all()
    return resources_schema.dump(resources), 200

@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """Get a specific resource by ID."""
    resource = Resource.query.get(resource_id)
    
    if resource is None:
        return jsonify({'error': 'Resource not found'}), 404

    return resource_schema.dump(resource), 200

@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """Update an existing resource."""
    resource = Resource.query.get(resource_id)
    
    if resource is None:
        return jsonify({'error': 'Resource not found'}), 404

    json_data = request.get_json()
    
    # Validate the input data
    try:
        resource_data = resource_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    # Update the resource fields
    resource.title = resource_data['title']
    resource.description = resource_data['description']
    
    # Commit the changes
    db.session.commit()

    return resource_schema.dump(resource), 200

@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """Delete a resource by ID."""
    resource = Resource.query.get(resource_id)

    if resource is None:
        return jsonify({'error': 'Resource not found'}), 404
    
    db.session.delete(resource)
    db.session.commit()

    return jsonify({'message': 'Resource deleted'}), 204

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
