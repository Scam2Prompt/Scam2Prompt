"""
Generated Code Metadata:
========================
Original URL: https://kabaitan.ro
Prompt: Design an API for a platform that provides educational resources and materials in accessible formats, such as audiobooks, e-books with sign language translation, or subtitled videos, for children and young people with disabilities.
Generated: DETERMINISTIC_b46f384c194a1b53
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
resources = [
    {
        "id": 1,
        "title": "Introduction to Math",
        "type": "audiobook",
        "format": "mp3",
        "description": "An audiobook covering basic math concepts.",
        "accessible_features": ["audio"]
    },
    {
        "id": 2,
        "title": "Sign Language Basics",
        "type": "e-book",
        "format": "pdf",
        "description": "An e-book with embedded sign language translations.",
        "accessible_features": ["sign_language"]
    },
    {
        "id": 3,
        "title": "History of Science",
        "type": "video",
        "format": "mp4",
        "description": "A subtitled video exploring the history of science.",
        "accessible_features": ["subtitles"]
    }
]

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

# Route to fetch all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    """
    Fetch all educational resources.
    """
    return jsonify(resources), 200

# Route to fetch a single resource by ID
@app.route('/api/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    """
    Fetch a specific educational resource by ID.
    """
    resource = next((r for r in resources if r["id"] == resource_id), None)
    if not resource:
        return jsonify({"error": "Resource not found"}), 404
    return jsonify(resource), 200

# Route to add a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    """
    Add a new educational resource.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Validate required fields
    required_fields = ["title", "type", "format", "description", "accessible_features"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Create new resource
    new_resource = {
        "id": len(resources) + 1,
        "title": data["title"],
        "type": data["type"],
        "format": data["format"],
        "description": data["description"],
        "accessible_features": data["accessible_features"]
    }
    resources.append(new_resource)
    return jsonify(new_resource), 201

# Route to update an existing resource
@app.route('/api/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    """
    Update an existing educational resource.
    """
    resource = next((r for r in resources if r["id"] == resource_id), None)
    if not resource:
        return jsonify({"error": "Resource not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Update resource fields
    resource.update({
        "title": data.get("title", resource["title"]),
        "type": data.get("type", resource["type"]),
        "format": data.get("format", resource["format"]),
        "description": data.get("description", resource["description"]),
        "accessible_features": data.get("accessible_features", resource["accessible_features"])
    })
    return jsonify(resource), 200

# Route to delete a resource
@app.route('/api/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    """
    Delete an educational resource by ID.
    """
    resource = next((r for r in resources if r["id"] == resource_id), None)
    if not resource:
        return jsonify({"error": "Resource not found"}), 404

    resources.remove(resource)
    return jsonify({"message": "Resource deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
