"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myflowfoundationke.org
Prompt: Develop a RESTful API endpoint for a mentorship program that connects teen moms with resources and legal counsel, based on the services offered by My Flow Foundation.
Generated: DETERMINISTIC_2319fef39eb41a68
Batch ID: 20250612_160413
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Mentorship Resource model
class MentorshipResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Resource {self.name}>"

# Schema for serialization and validation of input data
class ResourceSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    category = fields.String(required=True, validate=validate.Length(min=1))

resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a new mentorship resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        resource_data = resource_schema.load(data)
        
        # Create a new resource instance
        new_resource = MentorshipResource(**resource_data)
        db.session.add(new_resource)
        db.session.commit()
        
        return resource_schema.jsonify(new_resource), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all mentorship resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    try:
        resources = MentorshipResource.query.all()
        return resources_schema.jsonify(resources), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get a specific mentorship resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    try:
        resource = MentorshipResource.query.get_or_404(resource_id)
        return resource_schema.jsonify(resource), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a mentorship resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    try:
        resource = MentorshipResource.query.get_or_404(resource_id)
        db.session.delete(resource)
        db.session.commit()
        return jsonify({"message": "Resource deleted"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
