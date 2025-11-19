"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peacecitycontracting.com
Prompt: Recommend an API for managing civil and MEP works in a construction project, focusing on integration with project scheduling tools.
Generated: DETERMINISTIC_e94d446d228cdfa3
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# API for Managing Civil and MEP Works in a Construction Project
# This API facilitates scheduling, tracking, and resource management for civil and MEP works.
# Integration with project scheduling tools like Primavera or MS Project can be achieved using REST endpoints.

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Sample in-memory database (replace with a real database in production)
projects = {}

# Error Handling
def handle_error(e):
    return jsonify({'error': str(e)}), 400


@app.route('/api/projects', methods=['POST'])
def create_project():
    """
    Endpoint to create a new construction project.
    Expects JSON payload with 'name' and 'description'.
    """
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data:
            return handle_error("Invalid payload: 'name' and 'description' are required.")
        
        project_id = len(projects) + 1
        projects[project_id] = {
            'id': project_id,
            'name': data['name'],
            'description': data['description'],
            'civil_works': [],
            'mep_works': []
        }
        return jsonify({'message': 'Project created successfully!', 'project': projects[project_id]}), 201
    except Exception as e:
        return handle_error(e)


@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project_details(project_id):
    """
    Endpoint to retrieve details of a specific project by ID.
    """
    try:
        if project_id not in projects:
            return handle_error("Project not found.")
        
        return jsonify(projects[project_id]), 200
    except Exception as e:
        return handle_error(e)


@app.route('/api/projects/<int:project_id>/civil_works', methods=['POST'])
def add_civil_work(project_id):
    """
    Endpoint to add civil works to a specific project.
    Expects JSON payload with 'name', 'description', and 'schedule'.
    """
    try:
        if project_id not in projects:
            return handle_error("Project not found.")
        
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'schedule' not in data:
            return handle_error("Invalid payload: 'name', 'description', and 'schedule' are required.")
        
        work_id = len(projects[project_id]['civil_works']) + 1
        civil_work = {
            'id': work_id,
            'name': data['name'],
            'description': data['description'],
            'schedule': data['schedule']
        }
        projects[project_id]['civil_works'].append(civil_work)
        return jsonify({'message': 'Civil work added successfully!', 'civil_work': civil_work}), 201
    except Exception as e:
        return handle_error(e)


@app.route('/api/projects/<int:project_id>/mep_works', methods=['POST'])
def add_mep_work(project_id):
    """
    Endpoint to add MEP works to a specific project.
    Expects JSON payload with 'name', 'description', and 'schedule'.
    """
    try:
        if project_id not in projects:
            return handle_error("Project not found.")
        
        data = request.get_json()
        if not data or 'name' not in data or 'description' not in data or 'schedule' not in data:
            return handle_error("Invalid payload: 'name', 'description', and 'schedule' are required.")
        
        work_id = len(projects[project_id]['mep_works']) + 1
        mep_work = {
            'id': work_id,
            'name': data['name'],
            'description': data['description'],
            'schedule': data['schedule']
        }
        projects[project_id]['mep_works'].append(mep_work)
        return jsonify({'message': 'MEP work added successfully!', 'mep_work': mep_work}), 201
    except Exception as e:
        return handle_error(e)


@app.route('/api/projects/<int:project_id>/schedule', methods=['GET'])
def get_project_schedule(project_id):
    """
    Endpoint to retrieve the schedule of a specific project including civil and MEP works.
    """
    try:
        if project_id not in projects:
            return handle_error("Project not found.")
        
        schedule = {
            'civil_works': projects[project_id]['civil_works'],
            'mep_works': projects[project_id]['mep_works']
        }
        return jsonify({'project_id': project_id, 'schedule': schedule}), 200
    except Exception as e:
        return handle_error(e)


# Start the server
if __name__ == '__main__':
    # Use a production-ready server like Gunicorn in deployment
    app.run(debug=True, host='0.0.0.0', port=5000)
```
