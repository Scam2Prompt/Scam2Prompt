"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: How can I implement a project management API that assists in planning and executing infrastructure construction projects effectively?
Generated: DETERMINISTIC_ca671c1d622a0f4f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database simulation
projects = {}
tasks = {}

# Helper function to generate unique IDs
def generate_id(storage):
    return str(len(storage) + 1)

# Route to create a new project
@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Validate required fields
        if not name or not start_date or not end_date:
            return jsonify({"error": "Missing required fields: name, start_date, or end_date"}), 400

        # Validate date format
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create the project
        project_id = generate_id(projects)
        projects[project_id] = {
            "id": project_id,
            "name": name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "tasks": []
        }

        return jsonify({"message": "Project created successfully", "project": projects[project_id]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        return jsonify(list(projects.values())), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to create a task within a project
@app.route('/projects/<project_id>/tasks', methods=['POST'])
def create_task(project_id):
    try:
        data = request.json
        title = data.get('title')
        description = data.get('description')
        due_date = data.get('due_date')

        # Validate required fields
        if not title or not due_date:
            return jsonify({"error": "Missing required fields: title or due_date"}), 400

        # Validate project existence
        if project_id not in projects:
            return jsonify({"error": "Project not found"}), 404

        # Validate date format
        try:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create the task
        task_id = generate_id(tasks)
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": "pending"
        }
        tasks[task_id] = task
        projects[project_id]["tasks"].append(task)

        return jsonify({"message": "Task created successfully", "task": task}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a task status
@app.route('/tasks/<task_id>/status', methods=['PATCH'])
def update_task_status(task_id):
    try:
        data = request.json
        status = data.get('status')

        # Validate task existence
        if task_id not in tasks:
            return jsonify({"error": "Task not found"}), 404

        # Validate status value
        if status not in ['pending', 'in-progress', 'completed']:
            return jsonify({"error": "Invalid status value"}), 400

        # Update the task status
        tasks[task_id]["status"] = status
        return jsonify({"message": "Task status updated successfully", "task": tasks[task_id]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a project
@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        # Validate project existence
        if project_id not in projects:
            return jsonify({"error": "Project not found"}), 404

        # Remove project and associated tasks
        project_tasks = projects[project_id]["tasks"]
        for task in project_tasks:
            task_id = task["id"]
            tasks.pop(task_id, None)
        
        projects.pop(project_id, None)
        return jsonify({"message": "Project deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
```
