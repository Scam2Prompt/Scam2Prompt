"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nabberx.com
Prompt: Generate a project management tool prototype for construction firms using real-time collaboration features described in NabberX's IT solutions for the construction industry.
Generated: DETERMINISTIC_fac0f84b106f58f8
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management_tool.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from datetime import datetime
import os

# Create the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and socketio
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Model for the Project
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model for Messages (for real-time collaboration)
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Error handler for database errors
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": str(e)}), 500

# Endpoint to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    new_project = Project(name=data['name'], description=data.get('description'))
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"message": "Project created", "project_id": new_project.id}), 201

# Endpoint to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description} for p in projects]), 200

# Socket event for real-time messaging
@socketio.on('send_message')
def handle_send_message(data):
    project_id = data['project_id']
    content = data['content']
    new_message = Message(project_id=project_id, content=content)
    db.session.add(new_message)
    db.session.commit()
    emit('receive_message', {'content': content, 'timestamp': new_message.timestamp}, broadcast=True)

# Socket event for retrieving messages
@socketio.on('get_messages')
def handle_get_messages(data):
    project_id = data['project_id']
    messages = Message.query.filter_by(project_id=project_id).all()
    emit('receive_messages', [{'content': m.content, 'timestamp': m.timestamp} for m in messages])

# Main entry point to run the application
if __name__ == '__main__':
    # Create the database tables
    if not os.path.exists('projects.db'):
        db.create_all()
    socketio.run(app, debug=True)
```

### Requirements:
- Flask
- Flask-SQLAlchemy
- Flask-SocketIO

### Instructions to Run:
1. Install the required packages: `pip install Flask Flask-SQLAlchemy Flask-SocketIO`.
2. Run the script: `python project_management_tool.py`.
3. Use a WebSocket client to interact with the real-time features.
