"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: How can I implement a collaborative feature in a pool maintenance app similar to Pooltyme, allowing multiple users to log tasks?
Generated: DETERMINISTIC_1cdb6b155597edf3
Batch ID: 20250612_164238
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///pooltyme.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Define the Task schema for serialization
class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    description = fields.Str(required=True)
    completed = fields.Bool()

# Initialize the schema
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        # Validate and deserialize input
        task_data = task_schema.load(request.json)
        new_task = Task(**task_data)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all tasks for a user
@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    try:
        tasks = Task.query.filter_by(user_id=user_id).all()
        return tasks_schema.dump(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        task_data = task_schema.load(request.json)
        for key, value in task_data.items():
            setattr(task, key, value)
        db.session.commit()
        return task_schema.dump(task), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to set the `DATABASE_URL` environment variable to your database connection string before running the application.
