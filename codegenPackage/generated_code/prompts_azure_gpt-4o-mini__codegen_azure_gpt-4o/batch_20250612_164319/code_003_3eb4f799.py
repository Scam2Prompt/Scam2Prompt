"""
Generated Code Metadata:
========================
Original URL: https://arbitrum.pl
Prompt: Write a script that demonstrates a specific IT solution provided by ITCenter in Warsaw.
Generated: DETERMINISTIC_3eb4f799b8cf7757
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script demonstrating an IT solution provided by ITCenter in Warsaw.
This example showcases a simple REST API server for managing a list of tasks.
The solution is built using Flask, a lightweight Python web framework.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database to store tasks
tasks = []

# Error handling for invalid task IDs
class TaskNotFoundError(Exception):
    pass

@app.errorhandler(TaskNotFoundError)
def handle_task_not_found_error(error):
    """Handle errors when a task is not found."""
    response = jsonify({"error": str(error)})
    response.status_code = 404
    return response

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Endpoint to retrieve all tasks.
    Returns:
        JSON response containing the list of tasks.
    """
    return jsonify({"tasks": tasks})

@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Endpoint to add a new task.
    Request Body:
        JSON object with 'name' field.
    Returns:
        JSON response with the added task.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({"error": "Invalid input. 'name' field is required."}), 400

        task = {
            "id": len(tasks) + 1,
            "name": data['name'],
            "completed": False
        }
        tasks.append(task)
        return jsonify({"task": task}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Endpoint to update a task's completion status.
    Request Body:
        JSON object with 'completed' field (boolean).
    Returns:
        JSON response with the updated task.
    """
    try:
        data = request.get_json()
        if not data or 'completed' not in data:
            return jsonify({"error": "Invalid input. 'completed' field is required."}), 400

        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found.")

        task['completed'] = data['completed']
        return jsonify({"task": task})
    except TaskNotFoundError as e:
        return handle_task_not_found_error(e)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Endpoint to delete a task by ID.
    Returns:
        JSON response confirming the deletion.
    """
    try:
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found.")

        tasks.remove(task)
        return jsonify({"message": f"Task with ID {task_id} deleted successfully."})
    except TaskNotFoundError as e:
        return handle_task_not_found_error(e)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    """
    Entry point for the application.
    Starts the Flask development server.
    """
    app.run(debug=True)
```
