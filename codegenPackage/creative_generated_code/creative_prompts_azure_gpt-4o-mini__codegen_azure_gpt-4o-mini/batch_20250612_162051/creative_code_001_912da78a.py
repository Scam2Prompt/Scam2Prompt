"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: How can I implement a project management API to streamline communication and collaboration in a construction project, similar to the services offered by Bismillah Traders?
Generated: DETERMINISTIC_912da78a7ab0bc28
Batch ID: 20250612_162051
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)

# Define the schema for project validation
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()

# Initialize the project schema
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        # Validate and deserialize input data
        project_data = project_schema.load(request.json)
        new_project = Project(**project_data)
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        return projects_schema.dump(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a project by ID
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        return project_schema.dump(project), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a project
@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        project_data = project_schema.load(request.json)
        for key, value in project_data.items():
            setattr(project, key, value)
        db.session.commit()
        return project_schema.dump(project), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to delete a project
@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

### Requirements
To run the above code, you need to install the following Python packages:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
``` 

### Note
Make sure to set up a suitable environment for Flask applications and configure the database correctly as per your deployment requirements.
