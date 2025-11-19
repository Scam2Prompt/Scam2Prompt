"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimusdtbox.in
Prompt: How can I integrate a task completion feature in a cryptocurrency platform similar to Claim USDT Box?
Generated: DETERMINISTIC_63a8acc5be1395fb
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Model for Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id} - User {self.user_id}>'

# Database setup
with app.app_context():
    db.create_all()

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    """Creates a new task for a user."""
    data = request.get_json()
    user_id = data.get('user_id')
    description = data.get('description')

    if not user_id or not description:
        return jsonify({'error': 'User ID and description are required'}), 400

    new_task = Task(user_id=user_id, description=description)

    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully', 'task_id': new_task.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create task'}), 500

# Endpoint to complete a task
@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    """Marks a task as completed."""
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'error': 'Task not found'}), 404

    task.completed = True

    try:
        db.session.commit()
        return jsonify({'message': 'Task marked as completed'}), 200
    except Exception as e:
        db.session.rollback()
        logging.error(f'Error completing task {task_id}: {e}')
        return jsonify({'error': 'Failed to complete task'}), 500

# Endpoint to list tasks for a user
@app.route('/tasks', methods=['GET'])
def list_tasks():
    """Lists all tasks for a user."""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    tasks = Task.query.filter_by(user_id=user_id).all()
    task_list = [{'id': task.id, 'description': task.description, 'completed': task.completed} for task in tasks]
    
    return jsonify(task_list), 200

if __name__ == '__main__':
    app.run(debug=True)
```
