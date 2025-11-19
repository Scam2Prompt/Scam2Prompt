"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Create a RESTful API endpoint for a construction management system that handles data related to mining and road construction projects.
Generated: DETERMINISTIC_6676918e0818a1f1
Batch ID: 20250612_155223
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
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construction_projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and schema
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., 'mining', 'road construction'
    budget = db.Column(db.Float, nullable=False)

    def __init__(self, name, type, budget):
        self.name = name
        self.type = type
        self.budget = budget

# Define the Project schema
class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

# Initialize the schema
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def add_project():
    """Add a new construction project."""
    try:
        name = request.json['name']
        type = request.json['type']
        budget = request.json['budget']
        new_project = Project(name=name, type=type, budget=budget)

        db.session.add(new_project)
        db.session.commit()

        return project_schema.jsonify(new_project), 201
    except KeyError as e:
        return jsonify({"error": f"Missing parameter: {str(e)}"}), 400
    except IntegrityError:
        return jsonify({"error": "Project with this name already exists."}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all construction projects."""
    try:
        all_projects = Project.query.all()
        return projects_schema.jsonify(all_projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a project by ID
@app.route('/projects/<int:id>', methods=['GET'])
def get_project(id):
    """Retrieve a project by its ID."""
    try:
        project = Project.query.get_or_404(id)
        return project_schema.jsonify(project), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a project by ID
@app.route('/projects/<int:id>', methods=['PUT'])
def update_project(id):
    """Update a project by its ID."""
    try:
        project = Project.query.get_or_404(id)
        name = request.json.get('name', project.name)
        type = request.json.get('type', project.type)
        budget = request.json.get('budget', project.budget)

        project.name = name
        project.type = type
        project.budget = budget

        db.session.commit()
        return project_schema.jsonify(project), 200
    except KeyError as e:
        return jsonify({"error": f"Missing parameter: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a project by ID
@app.route('/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    """Delete a project by its ID."""
    try:
        project = Project.query.get_or_404(id)
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Project deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
