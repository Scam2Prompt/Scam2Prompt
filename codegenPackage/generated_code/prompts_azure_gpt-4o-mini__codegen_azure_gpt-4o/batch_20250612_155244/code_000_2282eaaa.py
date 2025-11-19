"""
Generated Code Metadata:
========================
Original URL: https://anshsofttech.com
Prompt: Generate a code snippet that demonstrates how to implement modern digital solutions using creative problem-solving techniques as described by Ansh Soft Tech.
Generated: DETERMINISTIC_2282eaaa19b3b324
Batch ID: 20250612_155244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This Python script demonstrates a modern digital solution using creative problem-solving techniques.
The example implements a simple RESTful API for task management using Flask, showcasing modular design,
error handling, and scalability principles.
"""

from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# In-memory database for tasks (for demonstration purposes)
tasks = []

# Error handling: Custom error response for 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling: Custom error response for 400
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad request"}), 400

# Route: Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Fetch all tasks.
    Returns:
        JSON response containing the list of tasks.
    """
    return jsonify({"tasks": tasks}), 200

# Route: Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Add a new task to the list.
    Expects:
        JSON payload with 'title' and optional 'description'.
    Returns:
        JSON response with the added task.
    """
    data = request.get_json()
    if not data or 'title' not in data:
        return bad_request_error("Missing 'title' in request payload")
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "description": data.get('description', ""),
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Route: Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Update an existing task.
    Expects:
        JSON payload with 'title', 'description', or 'completed'.
    Returns:
        JSON response with the updated task.
    """
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return not_found_error("Task not found")
    
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['completed'] = data.get('completed', task['completed'])
    return jsonify(task), 200

# Route: Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Delete a task by ID.
    Returns:
        JSON response confirming deletion.
    """
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return not_found_error("Task not found")
    
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted successfully"}), 200

# Main entry point: Run the application
if __name__ == '__main__':
    """
    Start the Flask application.
    The server will run on localhost:5000 by default.
    """
    app.run(debug=True)
```
