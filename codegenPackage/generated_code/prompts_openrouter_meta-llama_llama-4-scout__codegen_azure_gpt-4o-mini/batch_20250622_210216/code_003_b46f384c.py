"""
Generated Code Metadata:
========================
Original URL: https://kabaitan.ro
Prompt: Design an API for a platform that provides educational resources and materials in accessible formats, such as audiobooks, e-books with sign language translation, or subtitled videos, for children and young people with disabilities.
Generated: DETERMINISTIC_b46f384c194a1b53
Batch ID: 20250622_210216
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///resources.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for educational resources
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    format_type = db.Column(db.String(50), nullable=False)  # e.g., 'audiobook', 'e-book', 'video'
    accessibility_features = db.Column(db.String(200), nullable=True)  # e.g., 'sign language, subtitles'
    description = db.Column(db.Text, nullable=True)

# Schema for validating resource input
class ResourceSchema(Schema):
    title = fields.Str(required=True)
    format_type = fields.Str(required=True)
    accessibility_features = fields.Str(required=False)
    description = fields.Str(required=False)

resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a new resource
@app.route('/resources', methods=['POST'])
def add_resource():
    try:
        # Validate and deserialize input data
        resource_data = resource_schema.load(request.json)
        new_resource = Resource(**resource_data)
        db.session.add(new_resource)
        db.session.commit()
        return resource_schema.dump(new_resource), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve all resources
@app.route('/resources', methods=['GET'])
def get_resources():
    try:
        resources = Resource.query.all()
        return resources_schema.dump(resources), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a specific resource by ID
@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    try:
        resource = Resource.query.get_or_404(resource_id)
        return resource_schema.dump(resource), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update a resource
@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    try:
        resource = Resource.query.get_or_404(resource_id)
        resource_data = resource_schema.load(request.json)
        for key, value in resource_data.items():
            setattr(resource, key, value)
        db.session.commit()
        return resource_schema.dump(resource), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a resource
@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    try:
        resource = Resource.query.get_or_404(resource_id)
        db.session.delete(resource)
        db.session.commit()
        return jsonify({"message": "Resource deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
