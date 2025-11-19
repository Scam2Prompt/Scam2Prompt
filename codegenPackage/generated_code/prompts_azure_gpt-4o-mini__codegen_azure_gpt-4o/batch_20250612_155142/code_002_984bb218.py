"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Create a RESTful API endpoint for a logistics service that handles ocean freight, including container sizes and types, inspired by the offerings of Fealty Worldwide.
Generated: DETERMINISTIC_984bb218ffb77adc
Batch ID: 20250612_155142
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

# Sample data for container types and sizes
CONTAINER_DATA = [
    {"id": 1, "type": "Standard", "size": "20ft", "description": "Standard 20ft container for general cargo."},
    {"id": 2, "type": "Standard", "size": "40ft", "description": "Standard 40ft container for general cargo."},
    {"id": 3, "type": "Refrigerated", "size": "20ft", "description": "20ft container for temperature-sensitive goods."},
    {"id": 4, "type": "Refrigerated", "size": "40ft", "description": "40ft container for temperature-sensitive goods."},
    {"id": 5, "type": "Open Top", "size": "20ft", "description": "20ft container for oversized cargo."},
    {"id": 6, "type": "Open Top", "size": "40ft", "description": "40ft container for oversized cargo."},
]

@app.route('/api/containers', methods=['GET'])
def get_containers():
    """
    Endpoint to retrieve all container types and sizes.
    Returns:
        JSON response containing a list of all containers.
    """
    return jsonify({"containers": CONTAINER_DATA}), 200


@app.route('/api/containers/<int:container_id>', methods=['GET'])
def get_container_by_id(container_id):
    """
    Endpoint to retrieve a specific container by its ID.
    Args:
        container_id (int): ID of the container to retrieve.
    Returns:
        JSON response containing the container details or an error message.
    """
    container = next((c for c in CONTAINER_DATA if c["id"] == container_id), None)
    if container:
        return jsonify({"container": container}), 200
    else:
        return jsonify({"error": "Container not found"}), 404


@app.route('/api/containers', methods=['POST'])
def add_container():
    """
    Endpoint to add a new container type and size.
    Expects:
        JSON payload with 'type', 'size', and 'description'.
    Returns:
        JSON response with the newly created container or an error message.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ("type", "size", "description")):
            return jsonify({"error": "Invalid input. 'type', 'size', and 'description' are required."}), 400

        new_id = max(c["id"] for c in CONTAINER_DATA) + 1
        new_container = {
            "id": new_id,
            "type": data["type"],
            "size": data["size"],
            "description": data["description"],
        }
        CONTAINER_DATA.append(new_container)
        return jsonify({"container": new_container}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/api/containers/<int:container_id>', methods=['DELETE'])
def delete_container(container_id):
    """
    Endpoint to delete a container by its ID.
    Args:
        container_id (int): ID of the container to delete.
    Returns:
        JSON response indicating success or failure.
    """
    container = next((c for c in CONTAINER_DATA if c["id"] == container_id), None)
    if container:
        CONTAINER_DATA.remove(container)
        return jsonify({"message": "Container deleted successfully"}), 200
    else:
        return jsonify({"error": "Container not found"}), 404


@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    Args:
        e (HTTPException): The exception object.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": e.name, "message": e.description}), e.code


@app.errorhandler(Exception)
def handle_generic_exception(e):
    """
    Global error handler for unexpected exceptions.
    Args:
        e (Exception): The exception object.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
