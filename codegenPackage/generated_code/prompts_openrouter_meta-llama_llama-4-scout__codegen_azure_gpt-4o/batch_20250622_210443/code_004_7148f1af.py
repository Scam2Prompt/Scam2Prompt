"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Create a RESTful API using Flask to handle CRUD operations for museum resources, such as articles, videos, and podcasts, as seen on the Mêtis website.
Generated: DETERMINISTIC_7148f1af78844073
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
museum_resources = {
    "articles": [],
    "videos": [],
    "podcasts": []
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Helper function to validate resource type
def validate_resource_type(resource_type):
    if resource_type not in museum_resources:
        raise ValueError(f"Invalid resource type: {resource_type}. Must be one of {list(museum_resources.keys())}.")

# Create a new resource
@app.route('/api/<resource_type>', methods=['POST'])
def create_resource(resource_type):
    try:
        validate_resource_type(resource_type)
        data = request.json
        if not data or 'id' not in data or 'title' not in data:
            return jsonify({"error": "Invalid data", "message": "Resource must include 'id' and 'title'."}), 400
        museum_resources[resource_type].append(data)
        return jsonify({"message": f"{resource_type.capitalize()} resource created successfully.", "resource": data}), 201
    except ValueError as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Read all resources of a specific type
@app.route('/api/<resource_type>', methods=['GET'])
def get_resources(resource_type):
    try:
        validate_resource_type(resource_type)
        return jsonify(museum_resources[resource_type]), 200
    except ValueError as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Read a specific resource by ID
@app.route('/api/<resource_type>/<int:resource_id>', methods=['GET'])
def get_resource(resource_type, resource_id):
    try:
        validate_resource_type(resource_type)
        resource = next((res for res in museum_resources[resource_type] if res['id'] == resource_id), None)
        if not resource:
            return jsonify({"error": "Not Found", "message": f"Resource with ID {resource_id} not found."}), 404
        return jsonify(resource), 200
    except ValueError as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Update a specific resource by ID
@app.route('/api/<resource_type>/<int:resource_id>', methods=['PUT'])
def update_resource(resource_type, resource_id):
    try:
        validate_resource_type(resource_type)
        data = request.json
        if not data or 'title' not in data:
            return jsonify({"error": "Invalid data", "message": "Resource must include 'title'."}), 400
        resource = next((res for res in museum_resources[resource_type] if res['id'] == resource_id), None)
        if not resource:
            return jsonify({"error": "Not Found", "message": f"Resource with ID {resource_id} not found."}), 404
        resource.update(data)
        return jsonify({"message": f"{resource_type.capitalize()} resource updated successfully.", "resource": resource}), 200
    except ValueError as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Delete a specific resource by ID
@app.route('/api/<resource_type>/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_type, resource_id):
    try:
        validate_resource_type(resource_type)
        resource = next((res for res in museum_resources[resource_type] if res['id'] == resource_id), None)
        if not resource:
            return jsonify({"error": "Not Found", "message": f"Resource with ID {resource_id} not found."}), 404
        museum_resources[resource_type].remove(resource)
        return jsonify({"message": f"{resource_type.capitalize()} resource deleted successfully."}), 200
    except ValueError as e:
        return jsonify({"error": "Bad Request", "message": str(e)}), 400

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
