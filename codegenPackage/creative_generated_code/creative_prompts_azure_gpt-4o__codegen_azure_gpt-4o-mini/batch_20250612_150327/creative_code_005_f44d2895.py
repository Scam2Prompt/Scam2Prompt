"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Develop a REST API for managing HVAC maintenance tasks, including "Igienizare & Mentenanta" and "Managementul condensului" services offered on RoClima.ro.
Generated: DETERMINISTIC_f44d2895ebb5d533
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hvac_tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the HVAC Task model
class HvacTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a schema for input validation
class HvacTaskSchema(Schema):
    service_type = fields.Str(required=True)
    description = fields.Str(required=True)
    completed = fields.Bool(missing=False)

task_schema = HvacTaskSchema()
tasks_schema = HvacTaskSchema(many=True)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new HVAC maintenance task."""
    try:
        # Validate and deserialize input
        task_data = task_schema.load(request.json)
    except ValidationError as err:
        abort(400, description=err.messages)

    # Create a new task instance
    new_task = HvacTask(**task_data)
    db.session.add(new_task)
    db.session.commit()

    return jsonify(task_schema.dump(new_task)), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retrieve all HVAC maintenance tasks."""
    tasks = HvacTask.query.all()
    return jsonify(tasks_schema.dump(tasks)), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Retrieve a specific HVAC maintenance task by ID."""
    task = HvacTask.query.get_or_404(task_id)
    return jsonify(task_schema.dump(task)), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a specific HVAC maintenance task."""
    task = HvacTask.query.get_or_404(task_id)

    try:
        # Validate and deserialize input
        task_data = task_schema.load(request.json)
    except ValidationError as err:
        abort(400, description=err.messages)

    # Update task attributes
    for key, value in task_data.items():
        setattr(task, key, value)

    db.session.commit()
    return jsonify(task_schema.dump(task)), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a specific HVAC maintenance task."""
    task = HvacTask.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully."}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
