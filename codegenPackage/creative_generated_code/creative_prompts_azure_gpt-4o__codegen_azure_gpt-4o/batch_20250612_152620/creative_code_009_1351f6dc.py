"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scimar.ca
Prompt: Generate code to integrate Scimar's hepatalin research into a web-based platform for outreach initiatives, ensuring collaboration features for non-profits and Indigenous communities.
Generated: DETERMINISTIC_1351f6dc60b91d5d
Batch ID: 20250612_152620
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
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hepatalin_research.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)  # Enable Cross-Origin Resource Sharing

# Initialize the database
db = SQLAlchemy(app)

# Define the database models
class Research(db.Model):
    """
    Model to store hepatalin research details.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    collaborators = db.Column(db.String(255), nullable=True)  # e.g., names of non-profits, communities
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


# Endpoint to retrieve all research projects
@app.route('/research', methods=['GET'])
def get_research_projects():
    """
    Endpoint to fetch all hepatalin research projects.
    """
    try:
        projects = Research.query.all()
        response = [{
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'collaborators': project.collaborators,
            'created_at': project.created_at,
            'updated_at': project.updated_at
        } for project in projects]
        return jsonify({'success': True, 'data': response}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# Endpoint to add a new research project
@app.route('/research', methods=['POST'])
def add_research_project():
    """
    Endpoint to add a new research project.
    """
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')
        collaborators = data.get('collaborators', None)

        # Validate input
        if not title or not description:
            return jsonify({'success': False, 'error': 'Title and description are required.'}), 400

        # Add new research project
        new_project = Research(title=title, description=description, collaborators=collaborators)
        db.session.add(new_project)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Research project added successfully.'}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# Endpoint to update an existing research project
@app.route('/research/<int:id>', methods=['PUT'])
def update_research_project(id):
    """
    Endpoint to update an existing research project.
    """
    try:
        data = request.json
        project = Research.query.get(id)

        if not project:
            return jsonify({'success': False, 'error': 'Research project not found.'}), 404

        # Update fields
        project.title = data.get('title', project.title)
        project.description = data.get('description', project.description)
        project.collaborators = data.get('collaborators', project.collaborators)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Research project updated successfully.'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# Endpoint to delete a research project
@app.route('/research/<int:id>', methods=['DELETE'])
def delete_research_project(id):
    """
    Endpoint to delete a research project.
    """
    try:
        project = Research.query.get(id)

        if not project:
            return jsonify({'success': False, 'error': 'Research project not found.'}), 404

        db.session.delete(project)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Research project deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# Main function to run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
```
