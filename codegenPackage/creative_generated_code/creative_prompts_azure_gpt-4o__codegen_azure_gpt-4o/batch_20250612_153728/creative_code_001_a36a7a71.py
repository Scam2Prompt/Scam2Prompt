"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Recommend an API or library for showcasing architectural projects in a collaborative app, similar to the Études Architect App mentioned on Celestia's site.
Generated: DETERMINISTIC_a36a7a71710f9fe0
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses Flask and Flask-SocketIO to create a collaborative app showcasing architectural projects.
The app utilizes a simple REST API for data retrieval and Socket.IO for real-time collaboration.
Best practices are followed to ensure production readiness.

Dependencies:
- Flask: Web framework for Python.
- Flask-SocketIO: Real-time communication with Socket.IO.
- SQLAlchemy: ORM for database interactions.
- Marshmallow: Data serialization/deserialization and validation.

Install dependencies using pip install flask flask-socketio sqlalchemy marshmallow
"""

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)
socketio = SocketIO(app)

# Database configuration (SQLite for simplicity)
DATABASE_URL = "sqlite:///architect_projects.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()

# Define ArchitectureProject model
class ArchitectureProject(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    author = Column(String(255), nullable=False)

# Define Marshmallow schema for validation/serialization
class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    author = fields.Str(required=True)

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

# Create tables
Base.metadata.create_all(engine)

@app.route("/projects", methods=["GET"])
def get_projects():
    """
    Endpoint to retrieve all architectural projects.
    Returns a JSON list of projects.
    """
    projects = db_session.query(ArchitectureProject).all()
    return jsonify(projects_schema.dump(projects))

@app.route("/projects", methods=["POST"])
def create_project():
    """
    Endpoint to create a new architectural project.
    Expects JSON data with `title`, `description`, and `author`.
    """
    try:
        project_data = project_schema.load(request.json)
        new_project = ArchitectureProject(**project_data)
        db_session.add(new_project)
        db_session.commit()
        # Notify other users in real-time about the new project
        socketio.emit("new_project", project_schema.dump(new_project))
        return project_schema.dump(new_project), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found_error(error):
    """Custom error handler for 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom error handler for 500 errors."""
    return jsonify({"error": "Internal server error"}), 500

# Real-time collaboration events using Socket.IO
@socketio.on("join")
def on_join(data):
    """
    Event triggered when users join a project collaboration session.
    Expects `username` and `project_id` in the payload.
    """
    username = data.get("username")
    project_id = data.get("project_id")
    emit("user_joined", {"username": username, "project_id": project_id}, broadcast=True)

@socketio.on("message")
def handle_message(data):
    """
    Real-time messaging event. Expects `message` and `project_id`.
    Broadcasts the message to all connected users in the project session.
    """
    message = data.get("message")
    project_id = data.get("project_id")
    emit("message_received", {"message": message, "project_id": project_id}, broadcast=True)

if __name__ == "__main__":
    # Run the Flask app with Socket.IO support
    socketio.run(app, host="0.0.0.0", port=5000)
```
