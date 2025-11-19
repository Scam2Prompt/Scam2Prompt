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
# pool_maintenance_app.py

from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
# In production, replace with a proper database (e.g., PostgreSQL, MongoDB)
tasks = []
users = []

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.json
        if not data or 'name' not in data:
            return error_response("Invalid request. 'name' is required.")
        
        user = {
            "id": generate_id(),
            "name": data['name'],
            "created_at": datetime.utcnow().isoformat()
        }
        users.append(user)
        return jsonify(user), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    try:
        data = request.json
        if not data or 'description' not in data or 'user_id' not in data:
            return error_response("Invalid request. 'description' and 'user_id' are required.")
        
        # Check if user exists
        user = next((u for u in users if u['id'] == data['user_id']), None)
        if not user:
            return error_response("User not found.")
        
        task = {
            "id": generate_id(),
            "description": data['description'],
            "user_id": data['user_id'],
            "created_at": datetime.utcnow().isoformat(),
            "completed": False
        }
        tasks.append(task)
        return jsonify(task), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to list all tasks
@app.route('/tasks', methods=['GET'])
def list_tasks():
    try:
        return jsonify(tasks), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to mark a task as completed
@app.route('/tasks/<task_id>/complete', methods=['PATCH'])
def complete_task(task_id):
    try:
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            return error_response("Task not found.")
        
        task['completed'] = True
        return jsonify(task), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to delete a task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        global tasks
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            return error_response("Task not found.")
        
        tasks = [t for t in tasks if t['id'] != task_id]
        return jsonify({"message": "Task deleted successfully."}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to list all users
@app.route('/users', methods=['GET'])
def list_users():
    try:
        return jsonify(users), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask to create a RESTful API for managing users and tasks collaboratively.
- Replace the in-memory `tasks` and `users` lists with a proper database in production.
- Error handling is implemented to ensure robustness.
- The code is well-commented and follows Python best practices.
