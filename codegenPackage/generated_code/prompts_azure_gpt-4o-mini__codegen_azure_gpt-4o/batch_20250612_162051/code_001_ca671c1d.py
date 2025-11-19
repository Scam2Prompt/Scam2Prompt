"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: How can I implement a project management API that assists in planning and executing infrastructure construction projects effectively?
Generated: DETERMINISTIC_ca671c1d622a0f4f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for simplicity (use a real database in production)
projects = {}
tasks = {}

# Helper function to generate unique IDs
def generate_id(collection):
    return str(len(collection) + 1)

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route: Create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Validate input
        if not name or not start_date or not end_date:
            return error_response("Missing required fields: name, start_date, end_date")

        # Parse dates
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return error_response("Invalid date format. Use YYYY-MM-DD.")

        if end_date <= start_date:
            return error_response("End date must be after start date.")

        # Create project
        project_id = generate_id(projects)
        projects[project_id] = {
            "id": project_id,
            "name": name,
            "description": description,
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d'),
            "tasks": []
        }

        return jsonify(projects[project_id]), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route: Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(list(projects.values())), 200

# Route: Get a single project by ID
@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    project = projects.get(project_id)
    if not project:
        return error_response("Project not found", 404)
    return jsonify(project), 200

# Route: Add a task to a project
@app.route('/projects/<project_id>/tasks', methods=['POST'])
def add_task_to_project(project_id):
    try:
        project = projects.get(project_id)
        if not project:
            return error_response("Project not found", 404)

        data = request.json
        name = data.get('name')
        description = data.get('description')
        due_date = data.get('due_date')

        # Validate input
        if not name or not due_date:
            return error_response("Missing required fields: name, due_date")

        # Parse due date
        try:
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            return error_response("Invalid date format. Use YYYY-MM-DD.")

        # Ensure task due date is within project timeline
        project_start_date = datetime.strptime(project['start_date'], '%Y-%m-%d')
        project_end_date = datetime.strptime(project['end_date'], '%Y-%m-%d')
        if not (project_start_date <= due_date <= project_end_date):
            return error_response("Task due date must be within project timeline.")

        # Create task
        task_id = generate_id(tasks)
        task = {
            "id": task_id,
            "name": name,
            "description": description,
            "due_date": due_date.strftime('%Y-%m-%d'),
            "status": "pending"
        }
        tasks[task_id] = task
        project['tasks'].append(task)

        return jsonify(task), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route: Update task status
@app.route('/tasks/<task_id>', methods=['PATCH'])
def update_task_status(task_id):
    try:
        task = tasks.get(task_id)
        if not task:
            return error_response("Task not found", 404)

        data = request.json
        status = data.get('status')

        # Validate status
        if status not in ['pending', 'in-progress', 'completed']:
            return error_response("Invalid status. Allowed values: pending, in-progress, completed")

        task['status'] = status
        return jsonify(task), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route: Delete a project
@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        project = projects.pop(project_id, None)
        if not project:
            return error_response("Project not found", 404)

        # Remove associated tasks
        for task in project['tasks']:
            tasks.pop(task['id'], None)

        return jsonify({"message": "Project deleted successfully"}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route: Delete a task
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = tasks.pop(task_id, None)
        if not task:
            return error_response("Task not found", 404)

        # Remove task from associated project
        for project in projects.values():
            project['tasks'] = [t for t in project['tasks'] if t['id'] != task_id]

        return jsonify({"message": "Task deleted successfully"}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
