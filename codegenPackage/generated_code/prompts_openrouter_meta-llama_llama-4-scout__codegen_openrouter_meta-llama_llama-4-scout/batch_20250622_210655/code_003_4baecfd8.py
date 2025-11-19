"""
Generated Code Metadata:
========================
Original URL: https://sharawatch.org
Prompt: Develop a plan for a mobile app to engage volunteers in environmental conservation projects, such as the ones undertaken by Čuvari Šare, and suggest features like project catalogs, volunteer registration, and impact tracking.
Generated: DETERMINISTIC_4baecfd83a45f05c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_conservation_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conservation.db'
db = SQLAlchemy(app)

class Project(db.Model):
    """Environmental conservation project model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Project('{self.name}', '{self.location}')"

class Volunteer(db.Model):
    """Volunteer model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Volunteer('{self.name}', '{self.email}')"

class ProjectVolunteer(db.Model):
    """Many-to-many relationship between projects and volunteers"""
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteer.id'), primary_key=True)

    def __repr__(self):
        return f"ProjectVolunteer('{self.project_id}', '{self.volunteer_id}')"

@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve a list of all conservation projects"""
    projects = Project.query.all()
    output = []
    for project in projects:
        project_data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'location': project.location
        }
        output.append(project_data)
    return jsonify({'projects': output})

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new conservation project"""
    try:
        data = request.get_json()
        new_project = Project(
            name=data['name'],
            description=data['description'],
            location=data['location']
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Failed to create project'}), 400

@app.route('/volunteers', methods=['GET'])
def get_volunteers():
    """Retrieve a list of all volunteers"""
    volunteers = Volunteer.query.all()
    output = []
    for volunteer in volunteers:
        volunteer_data = {
            'id': volunteer.id,
            'name': volunteer.name,
            'email': volunteer.email
        }
        output.append(volunteer_data)
    return jsonify({'volunteers': output})

@app.route('/volunteers', methods=['POST'])
def create_volunteer():
    """Create a new volunteer account"""
    try:
        data = request.get_json()
        new_volunteer = Volunteer(
            name=data['name'],
            email=data['email']
        )
        new_volunteer.set_password(data['password'])
        db.session.add(new_volunteer)
        db.session.commit()
        return jsonify({'message': 'Volunteer account created successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Failed to create volunteer account'}), 400

@app.route('/projects/<id>/volunteers', methods=['POST'])
def assign_volunteer_to_project(id):
    """Assign a volunteer to a conservation project"""
    try:
        project = Project.query.get(id)
        if project is None:
            return jsonify({'message': 'Project not found'}), 404
        data = request.get_json()
        volunteer = Volunteer.query.get(data['volunteer_id'])
        if volunteer is None:
            return jsonify({'message': 'Volunteer not found'}), 404
        project_volunteer = ProjectVolunteer(
            project_id=project.id,
            volunteer_id=volunteer.id
        )
        db.session.add(project_volunteer)
        db.session.commit()
        return jsonify({'message': 'Volunteer assigned to project successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Failed to assign volunteer to project'}), 400

@app.route('/impact', methods=['GET'])
def get_impact():
    """Retrieve impact data for all conservation projects"""
    projects = Project.query.all()
    impact_data = []
    for project in projects:
        volunteers = ProjectVolunteer.query.filter_by(project_id=project.id).all()
        impact_data.append({
            'project_id': project.id,
            'project_name': project.name,
            'num_volunteers': len(volunteers)
        })
    return jsonify({'impact': impact_data})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
