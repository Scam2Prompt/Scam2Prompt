"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: How can I implement a project management API that assists in planning and executing infrastructure construction projects effectively?
Generated: DETERMINISTIC_ca671c1d622a0f4f
Batch ID: 20250612_162051
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
from datetime import datetime

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'status': self.status
        }

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    try:
        # Validate input data
        name = data.get('name')
        start_date = datetime.fromisoformat(data.get('start_date'))
        end_date = datetime.fromisoformat(data.get('end_date'))
        
        if not name or start_date >= end_date:
            return jsonify({'error': 'Invalid input'}), 400
        
        # Create a new project
        new_project = Project(name=name, start_date=start_date, end_date=end_date)
        db.session.add(new_project)
        db.session.commit()

        return jsonify(new_project.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    try:
        project = Project.query.get_or_404(project_id)

        # Update project attributes
        project.name = data.get('name', project.name)
        project.start_date = datetime.fromisoformat(data.get('start_date', project.start_date.isoformat()))
        project.end_date = datetime.fromisoformat(data.get('end_date', project.end_date.isoformat()))
        project.status = data.get('status', project.status)

        db.session.commit()
        return jsonify(project.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database and run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)  # Run in debug mode for development
```
