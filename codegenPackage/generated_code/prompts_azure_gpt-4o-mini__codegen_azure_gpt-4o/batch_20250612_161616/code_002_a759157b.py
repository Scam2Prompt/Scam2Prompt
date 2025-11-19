"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Create a RESTful API design for a construction management system that includes features for tracking civil engineering projects and equipment maintenance, inspired by the operations of Ntalo Investments.
Generated: DETERMINISTIC_a759157b6fbe7b1f
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data storage for demonstration purposes
projects = []
equipment = []

# Helper function to find a project by ID
def find_project(project_id):
    return next((project for project in projects if project['id'] == project_id), None)

# Helper function to find equipment by ID
def find_equipment(equipment_id):
    return next((item for item in equipment if item['id'] == equipment_id), None)

# Routes for Project Management
@app.route('/projects', methods=['GET'])
def get_projects():
    """
    Get all projects.
    """
    return jsonify({'projects': projects}), 200

@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """
    Get a specific project by ID.
    """
    project = find_project(project_id)
    if not project:
        abort(404, description="Project not found")
    return jsonify({'project': project}), 200

@app.route('/projects', methods=['POST'])
def create_project():
    """
    Create a new project.
    """
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request payload")
    new_project = {
        'id': len(projects) + 1,
        'name': request.json['name'],
        'description': request.json.get('description', ''),
        'status': request.json.get('status', 'Pending')
    }
    projects.append(new_project)
    return jsonify({'project': new_project}), 201

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    """
    Update an existing project.
    """
    project = find_project(project_id)
    if not project:
        abort(404, description="Project not found")
    if not request.json:
        abort(400, description="Invalid request payload")
    project['name'] = request.json.get('name', project['name'])
    project['description'] = request.json.get('description', project['description'])
    project['status'] = request.json.get('status', project['status'])
    return jsonify({'project': project}), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """
    Delete a project by ID.
    """
    project = find_project(project_id)
    if not project:
        abort(404, description="Project not found")
    projects.remove(project)
    return jsonify({'message': 'Project deleted successfully'}), 200

# Routes for Equipment Maintenance
@app.route('/equipment', methods=['GET'])
def get_equipment():
    """
    Get all equipment.
    """
    return jsonify({'equipment': equipment}), 200

@app.route('/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment_item(equipment_id):
    """
    Get a specific equipment item by ID.
    """
    item = find_equipment(equipment_id)
    if not item:
        abort(404, description="Equipment not found")
    return jsonify({'equipment': item}), 200

@app.route('/equipment', methods=['POST'])
def create_equipment():
    """
    Add a new equipment item.
    """
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request payload")
    new_item = {
        'id': len(equipment) + 1,
        'name': request.json['name'],
        'type': request.json.get('type', ''),
        'status': request.json.get('status', 'Operational'),
        'last_maintenance_date': request.json.get('last_maintenance_date', None)
    }
    equipment.append(new_item)
    return jsonify({'equipment': new_item}), 201

@app.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    """
    Update an existing equipment item.
    """
    item = find_equipment(equipment_id)
    if not item:
        abort(404, description="Equipment not found")
    if not request.json:
        abort(400, description="Invalid request payload")
    item['name'] = request.json.get('name', item['name'])
    item['type'] = request.json.get('type', item['type'])
    item['status'] = request.json.get('status', item['status'])
    item['last_maintenance_date'] = request.json.get('last_maintenance_date', item['last_maintenance_date'])
    return jsonify({'equipment': item}), 200

@app.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    """
    Delete an equipment item by ID.
    """
    item = find_equipment(equipment_id)
    if not item:
        abort(404, description="Equipment not found")
    equipment.remove(item)
    return jsonify({'message': 'Equipment deleted successfully'}), 200

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors.
    """
    return jsonify({'error': str(error)}), 404

@app.errorhandler(400)
def bad_request(error):
    """
    Handle 400 errors.
    """
    return jsonify({'error': str(error)}), 400

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
