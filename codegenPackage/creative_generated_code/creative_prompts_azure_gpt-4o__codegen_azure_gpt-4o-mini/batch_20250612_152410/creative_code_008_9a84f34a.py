"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neotokyo.pages.dev
Prompt: Generate code to display and manage citizen-run projects within the Neo Tokyo community, highlighting contributions to the gaming/metaverse space as described on the webpage.
Generated: DETERMINISTIC_9a84f34a264001c7
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neotokyo_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    """Model representing a citizen-run project in Neo Tokyo."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    contributions = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert Project instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'contributions': self.contributions
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    """Create database tables if they do not exist."""
    db.create_all()

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all citizen-run projects."""
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects]), 200

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new citizen-run project."""
    if not request.json or not 'name' in request.json:
        abort(400, description="Invalid input: Project must have a name.")
    
    new_project = Project(
        name=request.json['name'],
        description=request.json.get('description', ''),
        contributions=request.json.get('contributions', '')
    )
    
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify(new_project.to_dict()), 201

# Route to update an existing project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """Update an existing citizen-run project."""
    project = Project.query.get_or_404(project_id)

    if not request.json:
        abort(400, description="Invalid input: Request must contain JSON data.")

    project.name = request.json.get('name', project.name)
    project.description = request.json.get('description', project.description)
    project.contributions = request.json.get('contributions', project.contributions)

    db.session.commit()
    return jsonify(project.to_dict()), 200

# Route to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a citizen-run project."""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'result': True}), 204

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    """Return a custom 404 error message."""
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    """Return a custom 400 error message."""
    return jsonify({'error': str(error)}), 400

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
