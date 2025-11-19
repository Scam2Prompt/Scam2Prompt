"""
Generated Code Metadata:
========================
Original URL: https://parrotrans.com
Prompt: Create a RESTful API for managing translation projects, including endpoints for client registration, project submission, and translator assignment, inspired by Parrotrans' B2B service model.
Generated: DETERMINISTIC_f545e5499427cb6b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///translations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='submitted')

class Translator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    translator_id = db.Column(db.Integer, db.ForeignKey('translator.id'), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Client registration endpoint
@app.route('/clients', methods=['POST'])
def register_client():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing 'name' or 'email' in request data.")
    
    new_client = Client(name=data['name'], email=data['email'])
    db.session.add(new_client)
    db.session.commit()
    return jsonify({"id": new_client.id, "name": new_client.name, "email": new_client.email}), 201

# Project submission endpoint
@app.route('/projects', methods=['POST'])
def submit_project():
    data = request.get_json()
    if not data or 'client_id' not in data or 'title' not in data:
        raise BadRequest("Missing 'client_id' or 'title' in request data.")
    
    project = Project(client_id=data['client_id'], title=data['title'])
    db.session.add(project)
    db.session.commit()
    return jsonify({"id": project.id, "title": project.title, "status": project.status}), 201

# Translator assignment endpoint
@app.route('/assignments', methods=['POST'])
def assign_translator():
    data = request.get_json()
    if not data or 'project_id' not in data or 'translator_id' not in data:
        raise BadRequest("Missing 'project_id' or 'translator_id' in request data.")
    
    assignment = Assignment(project_id=data['project_id'], translator_id=data['translator_id'])
    db.session.add(assignment)
    db.session.commit()
    return jsonify({"id": assignment.id, "project_id": assignment.project_id, "translator_id": assignment.translator_id}), 201

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
