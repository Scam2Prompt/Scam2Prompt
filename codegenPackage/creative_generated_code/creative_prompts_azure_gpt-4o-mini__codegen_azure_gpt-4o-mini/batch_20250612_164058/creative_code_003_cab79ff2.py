"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercanza.es
Prompt: Generate a code snippet for a cloud-based application that enhances productivity, leveraging Mercanza's software development services.
Generated: DETERMINISTIC_cab79ff2c68de36b
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import json
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Simulated database for storing tasks
tasks_db = {}

@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Create a new task.
    Expects a JSON body with 'title' and 'description'.
    Returns the created task with a 201 status code.
    """
    try:
        task_data = request.get_json(force=True)

        if 'title' not in task_data or 'description' not in task_data:
            raise BadRequest("Missing 'title' or 'description' in request body")

        task_id = len(tasks_db) + 1
        tasks_db[task_id] = {
            'id': task_id,
            'title': task_data['title'],
            'description': task_data['description'],
            'completed': False
        }

        logger.info(f"Task created: {tasks_db[task_id]}")
        return jsonify(tasks_db[task_id]), 201

    except BadRequest as e:
        logger.error(f"Bad request: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/tasks', methods=['GET'])
def list_tasks():
    """
    Retrieve all tasks.
    Returns a list of tasks with a 200 status code.
    """
    logger.info("Retrieving all tasks")
    return jsonify(list(tasks_db.values())), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Update an existing task by ID.
    Expects a JSON body with 'title', 'description', and/or 'completed' fields.
    Returns the updated task with a 200 status code.
    """
    try:
        if task_id not in tasks_db:
            return jsonify({"error": "Task not found"}), 404

        task_data = request.get_json(force=True)
        
        # Update fields if present in the request
        if 'title' in task_data:
            tasks_db[task_id]['title'] = task_data['title']
        if 'description' in task_data:
            tasks_db[task_id]['description'] = task_data['description']
        if 'completed' in task_data:
            tasks_db[task_id]['completed'] = task_data['completed']

        logger.info(f"Task updated: {tasks_db[task_id]}")
        return jsonify(tasks_db[task_id]), 200

    except BadRequest as e:
        logger.error(f"Bad request: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Delete a task by ID.
    Returns a success message with a 204 status code.
    """
    if task_id in tasks_db:
        del tasks_db[task_id]
        logger.info(f"Task {task_id} deleted.")
        return jsonify({"message": "Task deleted successfully"}), 204
    else:
        logger.warning(f"Attempted to delete non-existent task: {task_id}")
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```
