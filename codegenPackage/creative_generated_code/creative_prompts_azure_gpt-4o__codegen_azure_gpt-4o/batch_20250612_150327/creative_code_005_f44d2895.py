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
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for HVAC tasks
hvac_tasks = [
    {"id": 1, "name": "Igienizare & Mentenanta", "description": "Sanitation and maintenance for HVAC systems."},
    {"id": 2, "name": "Managementul condensului", "description": "Condensate management services for HVAC systems."}
]

# Utility function for generating unique IDs
def generate_id():
    if hvac_tasks:
        return max(task['id'] for task in hvac_tasks) + 1
    return 1

# Generic error handler
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({"error": e.description}).data
        response.content_type = "application/json"
        return response
    return jsonify({"error": "An unexpected error occurred"}), 500

# Route: Get all HVAC tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(hvac_tasks), 200

# Route: Get a single HVAC task by ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in hvac_tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

# Route: Add a new HVAC task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    # Input validation
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    new_task = {
        "id": generate_id(),
        "name": data['name'],
        "description": data['description']
    }
    hvac_tasks.append(new_task)
    return jsonify(new_task), 201

# Route: Update an HVAC task by ID
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in hvac_tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    # Input validation
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({"error": "Invalid input"}), 400

    task['name'] = data['name']
    task['description'] = data['description']
    return jsonify(task), 200

# Route: Delete an HVAC task by ID
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global hvac_tasks
    task = next((task for task in hvac_tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    hvac_tasks = [t for t in hvac_tasks if t['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
```
