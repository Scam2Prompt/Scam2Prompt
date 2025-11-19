"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Develop an API to support MIEC's empowerment initiatives for young entrepreneurs, including features for skill development and project management.
Generated: DETERMINISTIC_16f53e2289992775
Batch ID: 20250612_151934
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
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entrepreneurs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Model for Skill Development
class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Schema for Skill
class SkillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Skill

# Model for Project Management
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    skills_required = db.Column(db.String(255), nullable=True)

    def __init__(self, title, description, skills_required):
        self.title = title
        self.description = description
        self.skills_required = skills_required

# Schema for Project
class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new skill
@app.route('/skills', methods=['POST'])
def add_skill():
    try:
        name = request.json['name']
        description = request.json.get('description', '')
        new_skill = Skill(name, description)
        db.session.add(new_skill)
        db.session.commit()
        return SkillSchema().jsonify(new_skill), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all skills
@app.route('/skills', methods=['GET'])
def get_skills():
    skills = Skill.query.all()
    return SkillSchema(many=True).jsonify(skills)

# Route to create a new project
@app.route('/projects', methods=['POST'])
def add_project():
    try:
        title = request.json['title']
        description = request.json.get('description', '')
        skills_required = request.json.get('skills_required', '')
        new_project = Project(title, description, skills_required)
        db.session.add(new_project)
        db.session.commit()
        return ProjectSchema().jsonify(new_project), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return ProjectSchema(many=True).jsonify(projects)

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
