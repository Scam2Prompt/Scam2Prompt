"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Create a RESTful API design for a construction management system that includes features for tracking civil engineering projects and equipment maintenance, inspired by the operations of Ntalo Investments.
Generated: DETERMINISTIC_a759157b6fbe7b1f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Project(db.Model):
    """Model for civil engineering projects."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), nullable=False)

class Equipment(db.Model):
    """Model for equipment maintenance records."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    maintenance_due_date = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Schemas for validation
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str(required=True)

class EquipmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    maintenance_due_date = fields.Str(required=True)
    status = fields.Str(required=True)

# Initialize schemas
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# RESTful API endpoints

@app.route('/projects', methods=['POST'])
def add_project():
    """Add a new project."""
    try:
        data = request.get_json()
        project = project_schema.load(data)
        new_project = Project(**project)
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    projects = Project.query.all()
    return projects_schema.dump(projects), 200

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Retrieve a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    return project_schema.dump(project), 200

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    try:
        data = request.get_json()
        updated_project = project_schema.load(data)
        for key, value in updated_project.items():
            setattr(project, key, value)
        db.session.commit()
        return project_schema.dump(project), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a specific project by ID."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message": "Project deleted successfully."}), 204

@app.route('/equipment', methods=['POST'])
def add_equipment():
    """Add a new equipment record."""
    try:
        data = request.get_json()
        equipment = equipment_schema.load(data)
        new_equipment = Equipment(**equipment)
        db.session.add(new_equipment)
        db.session.commit()
        return equipment_schema.dump(new_equipment), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/equipment', methods=['GET'])
def get_equipment():
    """Retrieve all equipment records."""
    equipment = Equipment.query.all()
    return equipments_schema.dump(equipment), 200

@app.route('/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment_by_id(equipment_id):
    """Retrieve a specific equipment record by ID."""
    equipment = Equipment.query.get_or_404(equipment_id)
    return equipment_schema.dump(equipment), 200

@app.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    """Update a specific equipment record by ID."""
    equipment = Equipment.query.get_or_404(equipment_id)
    try:
        data = request.get_json()
        updated_equipment = equipment_schema.load(data)
        for key, value in updated_equipment.items():
            setattr(equipment, key, value)
        db.session.commit()
        return equipment_schema.dump(equipment), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    """Delete a specific equipment record by ID."""
    equipment = Equipment.query.get_or_404(equipment_id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({"message": "Equipment deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
