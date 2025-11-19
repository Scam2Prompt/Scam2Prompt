"""
Generated Code Metadata:
========================
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Develop a REST API for managing HVAC maintenance tasks, including "Igienizare & Mentenanta" and "Managementul condensului" services offered on RoClima.ro.
Generated: DETERMINISTIC_f44d2895ebb5d533
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hvac_tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the HVAC maintenance task model
class HvacTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<HvacTask {self.service_type}>'

# Create a schema for input validation
class HvacTaskSchema(Schema):
    service_type = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
hvac_task_schema = HvacTaskSchema()
hvac_tasks_schema = HvacTaskSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Error handling for invalid input
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"error": error.messages}), 400

# Create a new HVAC maintenance task
@app.route('/tasks', methods=['POST'])
def create_task():
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        task_data = hvac_task_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Create a new task
    new_task = HvacTask(**task_data)
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(hvac_task_schema.dump(new_task)), 201

# Get all HVAC maintenance tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = HvacTask.query.all()
    return jsonify(hvac_tasks_schema.dump(tasks)), 200

# Get a specific HVAC maintenance task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = HvacTask.query.get_or_404(task_id)
    return jsonify(hvac_task_schema.dump(task)), 200

# Update an existing HVAC maintenance task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = HvacTask.query.get_or_404(task_id)
    json_data = request.get_json()
    try:
        # Validate and deserialize input
        task_data = hvac_task_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    # Update task fields
    task.service_type = task_data['service_type']
    task.description = task_data['description']
    db.session.commit()
    
    return jsonify(hvac_task_schema.dump(task)), 200

# Delete an HVAC maintenance task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = HvacTask.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({"message": "Task deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
