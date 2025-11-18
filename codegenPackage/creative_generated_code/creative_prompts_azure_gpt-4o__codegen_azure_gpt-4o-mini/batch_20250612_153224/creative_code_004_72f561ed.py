"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Suggest an API for managing green infrastructure projects, including plant selection and maintenance, as mentioned in the Ilmam Construction zelenih površin services.
Generated: DETERMINISTIC_72f561ed096dbe2c
Batch ID: 20250612_153224
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
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///green_infrastructure.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for GreenProject
class GreenProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    plant_selection = db.Column(db.String(300), nullable=False)
    maintenance_schedule = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<GreenProject {self.name}>'

# Schema for validating input data
class GreenProjectSchema(Schema):
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    plant_selection = fields.Str(required=True)
    maintenance_schedule = fields.Str(required=True)

# Initialize schema
green_project_schema = GreenProjectSchema()
green_projects_schema = GreenProjectSchema(many=True)

# Create a new green infrastructure project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        project_data = green_project_schema.load(data)

        # Create a new project instance
        new_project = GreenProject(**project_data)
        db.session.add(new_project)
        db.session.commit()

        return jsonify(green_project_schema.dump(new_project)), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Retrieve all green infrastructure projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = GreenProject.query.all()
        return jsonify(green_projects_schema.dump(projects)), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Retrieve a single green project by ID
@app.route('/projects/<int:id>', methods=['GET'])
def get_project(id):
    try:
        project = GreenProject.query.get_or_404(id)
        return jsonify(green_project_schema.dump(project)), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Update a green infrastructure project
@app.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    try:
        project = GreenProject.query.get_or_404(id)
        data = request.get_json()
        updated_data = green_project_schema.load(data)

        for key, value in updated_data.items():
            setattr(project, key, value)

        db.session.commit()
        return jsonify(green_project_schema.dump(project)), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete a green infrastructure project
@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    try:
        project = GreenProject.query.get_or_404(id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully."}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Create the database tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
