"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Create a REST API endpoint for a web application that facilitates collaborative management, similar to the frameworks Romain Rissoan uses in his training sessions.
Generated: DETERMINISTIC_563da3d310121821
Batch ID: 20250612_161745
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collab_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json()
    try:
        new_task = Task(
            title=data['title'],
            description=data.get('description', ''),
            completed=data.get('completed', False)
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"task": {"id": new_task.id, "title": new_task.title}}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred."}), 500

# Endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all tasks."""
    tasks = Task.query.all()
    return jsonify([{"id": task.id, "title": task.title, "description": task.description, "completed": task.completed} for task in tasks]), 200

# Endpoint to update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task."""
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    try:
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.completed = data.get('completed', task.completed)
        db.session.commit()
        return jsonify({"task": {"id": task.id, "title": task.title}}), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred."}), 500

# Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task."""
    task = Task.query.get_or_404(task_id)
    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully."}), 204
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
