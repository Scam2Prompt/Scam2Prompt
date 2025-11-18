"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Develop a REST API in Python for managing architectural project data, including client details, project scope, and billing, inspired by TWM Associates' services.
Generated: DETERMINISTIC_f2d52d19f0299589
Batch ID: 20250612_153224
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

# Initialize Flask app
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///architectural_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    project_scope = db.Column(db.String(500), nullable=False)
    billing_amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Converts a Project object into a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'client_name': self.client_name,
            'project_scope': self.project_scope,
            'billing_amount': self.billing_amount
        }

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/projects', methods=['GET'])
def get_projects():
    """Fetch all projects."""
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Fetch a single project by ID."""
    project = Project.query.get(project_id)
    if project:
        return jsonify(project.to_dict()), 200
    return jsonify({'error': 'Project not found'}), 404

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    try:
        data = request.json
        new_project = Project(
            client_name=data['client_name'],
            project_scope=data['project_scope'],
            billing_amount=data['billing_amount']
        )
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the project'}), 500

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing project."""
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    
    try:
        data = request.json
        project.client_name = data.get('client_name', project.client_name)
        project.project_scope = data.get('project_scope', project.project_scope)
        project.billing_amount = data.get('billing_amount', project.billing_amount)
        db.session.commit()
        return jsonify(project.to_dict()), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the project'}), 500

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a project."""
    project = Project.query.get(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    
    try:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'message': 'Project deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the project'}), 500

# Error handling for 404 routes
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
