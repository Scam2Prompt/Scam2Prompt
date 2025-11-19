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
import uuid

app = Flask(__name__)

# In-memory database (for demonstration purposes)
tasks = {}

# Helper function to validate task input
def validate_task_input(data):
    if not data.get("title") or not isinstance(data["title"], str):
        return "Invalid title. Title must be a non-empty string."
    if not data.get("description") or not isinstance(data["description"], str):
        return "Invalid description. Description must be a non-empty string."
    return None

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.json
        # Input validation
        error = validate_task_input(data)
        if error:
            return jsonify({"error": error}), 400

        task_id = str(uuid.uuid4())  # Generate unique task ID
        tasks[task_id] = {
            "id": task_id,
            "title": data["title"],
            "description": data["description"],
            "status": "Pending"
        }
        return jsonify({"message": "Task created successfully", "task": tasks[task_id]}), 201
    except Exception as e:
        # General error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Endpoint to retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        return jsonify({"tasks": list(tasks.values())}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Endpoint to update a task's status
@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task_status(task_id):
    try:
        data = request.json
        # Ensure task exists
        if task_id not in tasks:
            return jsonify({"error": "Task not found"}), 404

        # Validate status update
        if not data.get("status") or data["status"] not in ["Pending", "In Progress", "Completed"]:
            return jsonify({"error": "Invalid status. Must be one of: 'Pending', 'In Progress', 'Completed'"}), 400

        tasks[task_id]["status"] = data["status"]
        return jsonify({"message": "Task status updated successfully", "task": tasks[task_id]}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Endpoint to delete a task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        # Ensure task exists
        if task_id not in tasks:
            return jsonify({"error": "Task not found"}), 404

        # Remove task from database
        deleted_task = tasks.pop(task_id)
        return jsonify({"message": "Task deleted successfully", "task": deleted_task}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
