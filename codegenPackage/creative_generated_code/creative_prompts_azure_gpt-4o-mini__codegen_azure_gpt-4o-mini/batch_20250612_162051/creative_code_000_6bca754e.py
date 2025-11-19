"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Generate a code snippet for an Agile project management tool that incorporates interactive learning features as described on the CrestAgile website.
Generated: DETERMINISTIC_6bca754ef7c11569
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# agile_project_management_tool.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Set up the database URI (this is a sample URI; update according to your DB)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agile_project_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

# Define the Task schema for serialization
class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task

# Initialize the database
db.create_all()

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        title = request.json['title']
        description = request.json.get('description', '')
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        return TaskSchema().jsonify(new_task), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        return TaskSchema(many=True).jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        task.completed = request.json.get('completed', task.completed)
        db.session.commit()
        return TaskSchema().jsonify(task), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- The code implements a simple Flask-based RESTful API for managing tasks in an Agile project management tool.
- It uses SQLAlchemy as the ORM and Marshmallow for serializing the Task model.
- Error handling is included for database operations.
- Make sure to install Flask, SQLAlchemy, and Marshmallow to run this application (`pip install Flask Flask-SQLAlchemy Flask-Marshmallow`).
- Update the database URI as needed for your environment.
