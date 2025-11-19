"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Create an API endpoint for a community management system that allows users to manage shared resources in Kallimos Commons, focusing on inclusivity and multi-ability access.
Generated: DETERMINISTIC_c527fa5ce62c40b6
Batch ID: 20250612_162050
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
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kallimos_commons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Resource model for shared resources
class SharedResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    available = db.Column(db.Boolean, default=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Shared Resource Schema for input and output serialization
class SharedResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SharedResource
        load_instance = True

# Initialize the schema
resource_schema = SharedResourceSchema()
resources_schema = SharedResourceSchema(many=True)

# Endpoint to create a new shared resource
@app.route('/api/resources', methods=['POST'])
def create_resource():
    """Create a new shared resource."""
    try:
        # Validate and deserialize the input data
        data = request.get_json()
        resource = resource_schema.load(data)
        db.session.add(resource)
        db.session.commit()
        return resource_schema.jsonify(resource), 201  # Created
    except ValidationError as err:
        return jsonify(err.messages), 400  # Bad Request
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error

# Endpoint to get all shared resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """Retrieve all shared resources."""
    try:
        resources = SharedResource.query.all()
        return resources_schema.jsonify(resources), 200  # OK
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error

# Endpoint to update a shared resource
@app.route('/api/resources/<int:id>', methods=['PUT'])
def update_resource(id):
    """Update an existing shared resource."""
    try:
        resource = SharedResource.query.get_or_404(id)
        data = request.get_json()
        resource.name = data.get('name', resource.name)
        resource.description = data.get('description', resource.description)
        resource.available = data.get('available', resource.available)
        
        db.session.commit()
        return resource_schema.jsonify(resource), 200  # OK
    except ValidationError as err:
        return jsonify(err.messages), 400  # Bad Request
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error

# Endpoint to delete a shared resource
@app.route('/api/resources/<int:id>', methods=['DELETE'])
def delete_resource(id):
    """Delete a shared resource."""
    try:
        resource = SharedResource.query.get_or_404(id)
        db.session.delete(resource)
        db.session.commit()
        return jsonify({'message': 'Resource deleted successfully.'}), 204  # No Content
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error

# Create the database tables
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
