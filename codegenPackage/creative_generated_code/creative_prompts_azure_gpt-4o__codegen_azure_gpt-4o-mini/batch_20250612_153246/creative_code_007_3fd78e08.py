"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Recommend tools or libraries to build a mobile app for NGOs, incorporating features like project updates, donation tracking, and volunteer registration, inspired by Youngistaan Foundation's initiatives.
Generated: DETERMINISTIC_3fd78e08b110823e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI and initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ngo_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Enable CORS for all routes
CORS(app)

# Database models
class Project(db.Model):
    """Model representing a project."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    updates = db.relationship('Update', backref='project', lazy=True)

class Update(db.Model):
    """Model representing project updates."""
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

class Donation(db.Model):
    """Model representing donations."""
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donor_name = db.Column(db.String(100), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

class Volunteer(db.Model):
    """Model representing volunteers."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    try:
        data = request.json
        new_project = Project(title=data['title'], description=data['description'])
        db.session.add(new_project)
        db.session.commit()
        return jsonify({'message': 'Project created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects."""
    try:
        projects = Project.query.all()
        return jsonify([{'id': p.id, 'title': p.title, 'description': p.description} for p in projects]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to add a project update
@app.route('/projects/<int:project_id>/updates', methods=['POST'])
def add_update(project_id):
    """Add an update to a specific project."""
    try:
        data = request.json
        new_update = Update(project_id=project_id, content=data['content'])
        db.session.add(new_update)
        db.session.commit()
        return jsonify({'message': 'Update added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to track donations
@app.route('/donations', methods=['POST'])
def add_donation():
    """Track a new donation."""
    try:
        data = request.json
        new_donation = Donation(amount=data['amount'], donor_name=data['donor_name'], project_id=data['project_id'])
        db.session.add(new_donation)
        db.session.commit()
        return jsonify({'message': 'Donation recorded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to register a volunteer
@app.route('/volunteers', methods=['POST'])
def register_volunteer():
    """Register a new volunteer."""
    try:
        data = request.json
        new_volunteer = Volunteer(name=data['name'], email=data['email'])
        db.session.add(new_volunteer)
        db.session.commit()
        return jsonify({'message': 'Volunteer registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Main execution point
if __name__ == '__main__':
    # Create database tables
    db.create_all()
    # Run the application
    app.run(debug=True)
```
