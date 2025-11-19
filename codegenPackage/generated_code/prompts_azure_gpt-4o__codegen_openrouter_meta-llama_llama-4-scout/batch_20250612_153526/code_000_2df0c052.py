"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Write Python code for a web application that allows users to donate to projects like "Adopt me help my education" and "Feed me a simple lunch" described on the Kibera Hamlets website. Include functionality for tracking donations by project.
Generated: DETERMINISTIC_2df0c052946bb793
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///donations.db"
db = SQLAlchemy(app)


class Project(db.Model):
    """Represents a project for donations."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    total_donations = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f"Project('{self.name}', '{self.description}')"


class Donation(db.Model):
    """Represents a donation to a project."""
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref('donations', lazy=True))
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Donation('{self.project.name}', '{self.amount}')"


@app.route('/projects', methods=['GET'])
def get_projects():
    """Returns a list of all projects."""
    projects = Project.query.all()
    output = []
    for project in projects:
        project_data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'total_donations': project.total_donations
        }
        output.append(project_data)
    return jsonify({'projects': output})


@app.route('/projects', methods=['POST'])
def create_project():
    """Creates a new project."""
    try:
        data = request.get_json()
        new_project = Project(name=data['name'], description=data['description'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Failed to create project', 'error': str(e)}), 400


@app.route('/donate', methods=['POST'])
def make_donation():
    """Makes a donation to a project."""
    try:
        data = request.get_json()
        project_id = data['project_id']
        amount = data['amount']
        project = Project.query.get(project_id)
        if project is None:
            return jsonify({'message': 'Project not found'}), 404
        new_donation = Donation(project_id=project_id, amount=amount)
        project.total_donations += amount
        db.session.add(new_donation)
        db.session.commit()
        return jsonify({'message': 'Donation made successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to make donation', 'error': str(e)}), 400


@app.route('/projects/<id>', methods=['GET'])
def get_project(id):
    """Returns a project by ID."""
    project = Project.query.get(id)
    if project is None:
        return jsonify({'message': 'Project not found'}), 404
    project_data = {
        'id': project.id,
        'name': project.name,
        'description': project.description,
        'total_donations': project.total_donations
    }
    return jsonify({'project': project_data})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```python
# run.sh
#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```
