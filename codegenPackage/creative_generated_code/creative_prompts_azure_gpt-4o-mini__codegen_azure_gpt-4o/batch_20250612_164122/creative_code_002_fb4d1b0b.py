"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Create an API endpoint for a virtual library system that supports student access to educational resources, similar to the Biblioteca Virtual at Trentino.
Generated: DETERMINISTIC_fb4d1b0be14ce5bd
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing educational resources
resources = [
    {"id": 1, "title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "category": "Computer Science"},
    {"id": 2, "title": "Physics for Scientists and Engineers", "author": "Raymond A. Serway", "category": "Physics"},
    {"id": 3, "title": "Organic Chemistry", "author": "Paula Yurkanis Bruice", "category": "Chemistry"}
]

@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    GET endpoint to retrieve all educational resources.
    """
    return jsonify(resources), 200

@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource_by_id(resource_id):
    """
    GET endpoint to retrieve a specific resource by ID.
    """
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if resource:
        return jsonify(resource), 200
    else:
        # Return 404 if resource is not found
        return jsonify({"error": "Resource not found"}), 404

@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    POST endpoint to add a new educational resource.
    """
    try:
        new_resource = request.json
        # Validate required fields
        if not new_resource.get("title") or not new_resource.get("author") or not new_resource.get("category"):
            return jsonify({"error": "Missing required fields"}), 400

        # Generate the next ID
        new_resource_id = max([r["id"] for r in resources]) + 1
        new_resource["id"] = new_resource_id
        resources.append(new_resource)

        return jsonify(new_resource), 201
    except Exception as e:
        logging.error(f"Error while adding resource: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    DELETE endpoint to remove a resource by ID.
    """
    global resources
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if resource:
        resources = [r for r in resources if r['id'] != resource_id]
        return jsonify({"message": "Resource deleted successfully"}), 200
    else:
        return jsonify({"error": "Resource not found"}), 404

@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """
    PUT endpoint to update a resource by ID.
    """
    try:
        updated_data = request.json
        resource = next((r for r in resources if r['id'] == resource_id), None)
        if resource:
            # Update resource fields (only if provided in the request)
            resource["title"] = updated_data.get("title", resource["title"])
            resource["author"] = updated_data.get("author", resource["author"])
            resource["category"] = updated_data.get("category", resource["category"])
            return jsonify(resource), 200
        else:
            return jsonify({"error": "Resource not found"}), 404
    except Exception as e:
        logging.error(f"Error while updating resource: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
```
