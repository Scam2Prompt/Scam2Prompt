"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://standrewsibanda.org
Prompt: Describe the target population for the St. Andrew’s School Project for The Young and suggest a suitable API for managing educational resources for these children.
Generated: DETERMINISTIC_28b16df49e398d25
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script defines a Flask API for managing educational resources for the 
St. Andrew’s School Project for The Young. The target population consists 
of children aged 5–12, particularly those from disadvantaged backgrounds 
who require access to quality educational materials.

The API includes endpoints for:
1. Adding new educational resources.
2. Retrieving all resources.
3. Updating specific resources.
4. Deleting resources.

The API follows REST principles and includes proper error handling.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to hold educational resources (for demonstration purposes)
# Format: [{'id': 1, 'title': 'Resource Title', 'description': 'Resource Description', 'age_group': '5-12'}]
resources = []
resource_id_counter = 1


@app.route('/resources', methods=['GET'])
def get_resources():
    """
    Retrieves all educational resources.
    """
    return jsonify(resources), 200


@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """
    Retrieves a specific educational resource by ID.
    """
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404
    return jsonify(resource), 200


@app.route('/resources', methods=['POST'])
def add_resource():
    """
    Adds a new educational resource. 
    Expects JSON payload with 'title', 'description', and 'age_group'.
    """
    global resource_id_counter
    data = request.get_json()

    # Validate input data
    if 'title' not in data or 'description' not in data or 'age_group' not in data:
        return jsonify({"error": "Missing required fields: title, description, age_group"}), 400

    new_resource = {
        'id': resource_id_counter,
        'title': data['title'],
        'description': data['description'],
        'age_group': data['age_group']
    }
    resources.append(new_resource)
    resource_id_counter += 1

    return jsonify(new_resource), 201


@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """
    Updates an existing educational resource by ID.
    Expects JSON payload with 'title', 'description', and/or 'age_group'.
    """
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404

    data = request.get_json()

    # Update resource fields if provided
    if 'title' in data:
        resource['title'] = data['title']
    if 'description' in data:
        resource['description'] = data['description']
    if 'age_group' in data:
        resource['age_group'] = data['age_group']

    return jsonify(resource), 200


@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Deletes an educational resource by ID.
    """
    global resources
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404

    resources = [r for r in resources if r['id'] != resource_id]
    return jsonify({"message": "Resource deleted successfully"}), 200


@app.errorhandler(404)
def not_found_error(error):
    """
    Handles 404 errors globally.
    """
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handles unexpected server errors globally.
    """
    return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
