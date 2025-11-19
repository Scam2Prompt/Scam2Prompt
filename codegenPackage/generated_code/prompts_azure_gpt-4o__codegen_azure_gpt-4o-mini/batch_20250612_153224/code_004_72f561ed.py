"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Suggest an API for managing green infrastructure projects, including plant selection and maintenance, as mentioned in the Ilmam Construction zelenih površin services.
Generated: DETERMINISTIC_72f561ed096dbe2c
Batch ID: 20250612_153224
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///green_infrastructure.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for Plant
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    maintenance_info = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'maintenance_info': self.maintenance_info
        }

# Model for Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    plants = db.relationship('Plant', backref='project', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'plants': [plant.to_dict() for plant in self.plants]
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new plant
@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.get_json()
    new_plant = Plant(name=data['name'], type=data['type'], maintenance_info=data.get('maintenance_info'))
    db.session.add(new_plant)
    try:
        db.session.commit()
        return jsonify(new_plant.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Plant already exists'}), 400

# API endpoint to get all plants
@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants]), 200

# API endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = Project(name=data['name'], description=data.get('description'))
    db.session.add(new_project)
    try:
        db.session.commit()
        return jsonify(new_project.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Project already exists'}), 400

# API endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

# API endpoint to add a plant to a project
@app.route('/projects/<int:project_id>/plants', methods=['POST'])
def add_plant_to_project(project_id):
    data = request.get_json()
    plant = Plant.query.get(data['plant_id'])
    project = Project.query.get(project_id)

    if not plant or not project:
        return jsonify({'error': 'Plant or Project not found'}), 404

    project.plants.append(plant)
    db.session.commit()
    return jsonify(project.to_dict()), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
