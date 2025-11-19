"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Create a REST API endpoint for a web application that facilitates collaborative management, similar to the frameworks Romain Rissoan uses in his training sessions.
Generated: DETERMINISTIC_563da3d310121821
Batch ID: 20250612_161745
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collab_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for collaborative tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the Task object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all tasks."""
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    new_task = Task(title=data['title'], description=data.get('description'))
    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Task could not be created'}), 500

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Retrieve a specific task by ID."""
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.to_dict()), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task."""
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'completed' in data:
        task.completed = data['completed']

    db.session.commit()
    return jsonify(task.to_dict()), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a specific task by ID."""
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
