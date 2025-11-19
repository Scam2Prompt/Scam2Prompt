"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooltyme.app
Prompt: How can I implement a collaborative feature in a pool maintenance app similar to Pooltyme, allowing multiple users to log tasks?
Generated: DETERMINISTIC_1cdb6b155597edf3
Batch ID: 20250612_164238
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pool_maintenance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Define the Task Schema for validation and serialization
class TaskSchema(Schema):
    user_id = fields.Int(required=True)
    description = fields.Str(required=True)
    completed = fields.Bool()

# Initialize the schema
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Create a new task for pool maintenance.
    Expecting JSON with user_id and description fields.
    """
    try:
        # Validate and deserialize the input
        task_data = task_schema.load(request.json)
        # Create a new Task instance
        new_task = Task(**task_data)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Route to get all tasks for a user
@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    """
    Retrieve all tasks for a specific user.
    """
    try:
        tasks = Task.query.filter_by(user_id=user_id).all()
        return tasks_schema.dump(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a task's status
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Update the completion status of a specific task.
    Expecting JSON with completed field.
    """
    try:
        task = Task.query.get_or_404(task_id)  # Raise 404 if not found
        task.completed = request.json.get('completed', task.completed)
        db.session.commit()
        return task_schema.dump(task), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Route to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Delete a specific task.
    """
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully."}), 204
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements:
1. Flask
2. Flask-SQLAlchemy
3. Flask-Migrate
4. Marshmallow
5. Flask-CORS

Make sure to install the required libraries using:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow Flask-CORS
``` 

This code provides a basic structure for a collaborative feature in a pool maintenance app, allowing multiple users to log tasks with appropriate error handling and data validation.
