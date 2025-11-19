"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Create a RESTful API endpoint for a logistics service that handles ocean freight, including container sizes and types, inspired by the offerings of Fealty Worldwide.
Generated: DETERMINISTIC_984bb218ffb77adc
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data to simulate storage (could be replaced with a database in production)
containers = [
    {"id": 1, "type": "Standard", "size": "20ft", "max_payload_kg": 28000},
    {"id": 2, "type": "Standard", "size": "40ft", "max_payload_kg": 30000},
    {"id": 3, "type": "High Cube", "size": "40ft", "max_payload_kg": 29000},
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

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    response = jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    })
    response.status_code = 500
    return response

@app.route('/api/containers', methods=['GET'])
def get_containers():
    """
    Retrieve all container information.
    """
    return jsonify(containers), 200

@app.route('/api/containers/<int:container_id>', methods=['GET'])
def get_container_by_id(container_id):
    """
    Retrieve a specific container by its ID.
    """
    container = next((c for c in containers if c["id"] == container_id), None)
    if container:
        return jsonify(container), 200
    return jsonify({"error": "Container not found"}), 404

@app.route('/api/containers', methods=['POST'])
def add_container():
    """
    Add a new container to the collection.
    Expected JSON format:
    {
        "type": "High Cube",
        "size": "40ft",
        "max_payload_kg": 29000
    }
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["type", "size", "max_payload_kg"]):
            return jsonify({"error": "Invalid input data"}), 400

        new_container = {
            "id": len(containers) + 1,
            "type": data["type"],
            "size": data["size"],
            "max_payload_kg": data["max_payload_kg"]
        }
        containers.append(new_container)
        return jsonify(new_container), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/containers/<int:container_id>', methods=['PUT'])
def update_container(container_id):
    """
    Update an existing container's information.
    Expected JSON format:
    {
        "type": "updated type",
        "size": "updated size",
        "max_payload_kg": updated_value
    }
    """
    try:
        data = request.get_json()
        container = next((c for c in containers if c["id"] == container_id), None)
        if not container:
            return jsonify({"error": "Container not found"}), 404

        if not data or not all(key in data for key in ["type", "size", "max_payload_kg"]):
            return jsonify({"error": "Invalid input data"}), 400

        container.update({
            "type": data["type"],
            "size": data["size"],
            "max_payload_kg": data["max_payload_kg"]
        })
        return jsonify(container), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/containers/<int:container_id>', methods=['DELETE'])
def delete_container(container_id):
    """
    Delete a container by its ID.
    """
    try:
        container = next((c for c in containers if c["id"] == container_id), None)
        if not container:
            return jsonify({"error": "Container not found"}), 404

        containers.remove(container)
        return jsonify({"message": "Container deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
