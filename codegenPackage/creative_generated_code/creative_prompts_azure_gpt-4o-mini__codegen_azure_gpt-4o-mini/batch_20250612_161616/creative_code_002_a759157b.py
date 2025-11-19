"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Create a RESTful API design for a construction management system that includes features for tracking civil engineering projects and equipment maintenance, inspired by the operations of Ntalo Investments.
Generated: DETERMINISTIC_a759157b6fbe7b1f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Civil Engineering Projects
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    status = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'status': self.status
        }

# Model for Equipment Maintenance
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    maintenance_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'maintenance_date': self.maintenance_date.isoformat(),
            'status': self.status
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to get all projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.serialize() for project in projects]), 200

# API endpoint to create a new project
@app.route('/api/projects', methods=['POST'])
def create_project():
    if not request.json or 'name' not in request.json or 'status' not in request.json:
        abort(400, description="Bad Request: Missing required fields")
    
    new_project = Project(
        name=request.json['name'],
        start_date=request.json.get('start_date'),
        end_date=request.json.get('end_date'),
        status=request.json['status']
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.serialize()), 201

# API endpoint to get a single project by ID
@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify(project.serialize()), 200

# API endpoint to update a project
@app.route('/api/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    
    if not request.json:
        abort(400, description="Bad Request: No input data")
    
    project.name = request.json.get('name', project.name)
    project.start_date = request.json.get('start_date', project.start_date)
    project.end_date = request.json.get('end_date', project.end_date)
    project.status = request.json.get('status', project.status)

    db.session.commit()
    return jsonify(project.serialize()), 200

# API endpoint to delete a project
@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'result': True}), 204

# API endpoint to get all equipment
@app.route('/api/equipment', methods=['GET'])
def get_equipment():
    equipment = Equipment.query.all()
    return jsonify([eq.serialize() for eq in equipment]), 200

# API endpoint to create new equipment
@app.route('/api/equipment', methods=['POST'])
def create_equipment():
    if not request.json or 'name' not in request.json or 'status' not in request.json:
        abort(400, description="Bad Request: Missing required fields")
    
    new_equipment = Equipment(
        name=request.json['name'],
        maintenance_date=request.json.get('maintenance_date'),
        status=request.json['status']
    )
    db.session.add(new_equipment)
    db.session.commit()
    return jsonify(new_equipment.serialize()), 201

# API endpoint to update equipment
@app.route('/api/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    equipment = Equipment.query.get_or_404(equipment_id)
    
    if not request.json:
        abort(400, description="Bad Request: No input data")
    
    equipment.name = request.json.get('name', equipment.name)
    equipment.maintenance_date = request.json.get('maintenance_date', equipment.maintenance_date)
    equipment.status = request.json.get('status', equipment.status)

    db.session.commit()
    return jsonify(equipment.serialize()), 200

# API endpoint to delete equipment
@app.route('/api/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    equipment = Equipment.query.get_or_404(equipment_id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'result': True}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
