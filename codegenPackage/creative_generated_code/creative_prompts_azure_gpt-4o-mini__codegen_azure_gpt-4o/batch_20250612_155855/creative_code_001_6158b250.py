"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Generate a REST API that allows users to access resources related to biodiversity conservation and urban agriculture initiatives championed by Cegeduc.
Generated: DETERMINISTIC_6158b250ad10e36a
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing resources for biodiversity conservation and urban agriculture
resources = [
    {
        "id": 1,
        "title": "Urban Beekeeping Initiative",
        "description": "Promoting beekeeping in urban environments to support pollinators.",
        "category": "Urban Agriculture"
    },
    {
        "id": 2,
        "title": "Native Plant Restoration",
        "description": "Restoring native plant species to support biodiversity.",
        "category": "Biodiversity Conservation"
    },
]

@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    Endpoint to fetch all resources.
    Returns a list of resources in JSON format.
    """
    return jsonify({"resources": resources}), 200

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """
    Endpoint to fetch a specific resource by ID.
    Returns the resource if found, or a 404 error if not found.
    """
    resource = next((res for res in resources if res['id'] == resource_id), None)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404
    return jsonify({"resource": resource}), 200

@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    Endpoint to add a new resource.
    Expects a JSON payload with 'title', 'description', and 'category'.
    Returns the newly created resource.
    """
    data = request.get_json()
    
    # Validate request payload
    if not data or 'title' not in data or 'description' not in data or 'category' not in data:
        return jsonify({"error": "Invalid payload"}), 400
    
    # Create new resource
    new_resource = {
        "id": len(resources) + 1,  # Generate new ID
        "title": data['title'],
        "description": data['description'],
        "category": data['category']
    }
    resources.append(new_resource)
    return jsonify({"resource": new_resource}), 201

@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """
    Endpoint to update an existing resource by ID.
    Expects a JSON payload with 'title', 'description', and 'category'.
    Returns the updated resource if successful, or a 404 error if not found.
    """
    data = request.get_json()
    
    # Validate request payload
    if not data or 'title' not in data or 'description' not in data or 'category' not in data:
        return jsonify({"error": "Invalid payload"}), 400
    
    resource = next((res for res in resources if res['id'] == resource_id), None)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404
    
    # Update resource fields
    resource['title'] = data['title']
    resource['description'] = data['description']
    resource['category'] = data['category']
    return jsonify({"resource": resource}), 200

@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Endpoint to delete a resource by ID.
    Returns a success message if the resource was deleted, or a 404 error if not found.
    """
    global resources
    resource = next((res for res in resources if res['id'] == resource_id), None)
    if resource is None:
        return jsonify({"error": "Resource not found"}), 404
    
    # Remove resource from the list
    resources = [res for res in resources if res['id'] != resource_id]
    return jsonify({"message": "Resource deleted successfully"}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
