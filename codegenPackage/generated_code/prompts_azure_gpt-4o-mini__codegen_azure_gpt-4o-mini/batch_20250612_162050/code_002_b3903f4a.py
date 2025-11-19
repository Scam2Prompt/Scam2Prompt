"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: Generate a sample API that provides resources and exercises for DBT skills training, targeting adolescents and adults with emotional regulation issues.
Generated: DETERMINISTIC_b3903f4a197d8ae9
Batch ID: 20250612_162050
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbt_resources.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50), nullable=False)

# Define the Resource schema for serialization
class ResourceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    type = fields.Str(required=True)

# Initialize the schema
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new resource
@app.route('/resources', methods=['POST'])
def add_resource():
    """Add a new resource for DBT skills training."""
    try:
        # Validate and deserialize input
        resource_data = resource_schema.load(request.json)
        new_resource = Resource(**resource_data)
        db.session.add(new_resource)
        db.session.commit()
        return resource_schema.jsonify(new_resource), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all resources
@app.route('/resources', methods=['GET'])
def get_resources():
    """Retrieve all resources for DBT skills training."""
    try:
        resources = Resource.query.all()
        return resources_schema.jsonify(resources), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get a specific resource by ID
@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """Retrieve a specific resource by its ID."""
    try:
        resource = Resource.query.get_or_404(resource_id)
        return resource_schema.jsonify(resource), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a resource
@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """Update an existing resource."""
    try:
        resource = Resource.query.get_or_404(resource_id)
        resource_data = resource_schema.load(request.json)
        for key, value in resource_data.items():
            setattr(resource, key, value)
        db.session.commit()
        return resource_schema.jsonify(resource), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a resource
@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """Delete a specific resource."""
    try:
        resource = Resource.query.get_or_404(resource_id)
        db.session.delete(resource)
        db.session.commit()
        return jsonify({"message": "Resource deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
