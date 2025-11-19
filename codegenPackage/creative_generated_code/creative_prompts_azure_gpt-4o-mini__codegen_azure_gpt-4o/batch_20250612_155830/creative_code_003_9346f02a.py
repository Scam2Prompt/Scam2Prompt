"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: What are the API endpoints available for managing Aethir Nodes and monitoring GPU performance?
Generated: DETERMINISTIC_9346f02a660ae68f
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Flask API for managing Aethir Nodes and monitoring GPU performance.

This code defines endpoints for:
1. Retrieving a list of nodes.
2. Adding a new node.
3. Monitoring GPU performance of a specific node.
4. Deleting a node.

Requirements:
- Flask (`pip install flask`)
- Install `psutil` if you want to simulate GPU monitoring (`pip install psutil`).

Run this script to start the server, and access the endpoints via HTTP.
"""

from flask import Flask, request, jsonify
import psutil

app = Flask(__name__)

# In-memory storage for nodes (for simplicity; replace with DB in production)
nodes = {}

@app.route('/nodes', methods=['GET'])
def get_nodes():
    """
    GET /nodes
    Retrieve the list of all nodes.
    """
    return jsonify(nodes), 200


@app.route('/nodes', methods=['POST'])
def add_node():
    """
    POST /nodes
    Add a new node.
    Request JSON Body:
    {
        "id": "unique_node_id",
        "name": "Node Name",
        "description": "Node Description"
    }
    """
    data = request.get_json()
    if not data or 'id' not in data or 'name' not in data:
        return jsonify({"error": "Invalid input. 'id' and 'name' are required."}), 400

    node_id = data['id']
    if node_id in nodes:
        return jsonify({"error": f"Node with id '{node_id}' already exists."}), 409

    nodes[node_id] = {
        "name": data['name'],
        "description": data.get('description', ""),
        "gpu": {"usage": "unknown"}  # Placeholder for GPU information
    }
    return jsonify({"message": f"Node '{node_id}' added successfully."}), 201


@app.route('/nodes/<node_id>/gpu', methods=['GET'])
def monitor_gpu(node_id):
    """
    GET /nodes/<node_id>/gpu
    Monitor GPU performance for a specific node.
    Response Example:
    {
        "node_id": "unique_node_id",
        "gpu_usage_percent": 45.3
    }
    """
    node = nodes.get(node_id)
    if not node:
        return jsonify({"error": f"Node '{node_id}' not found."}), 404

    # Simulate GPU usage monitoring using psutil (replace with actual logic for GPU stats)
    gpu_usage = psutil.cpu_percent()  # Replace with actual GPU usage monitoring logic
    return jsonify({
        "node_id": node_id,
        "gpu_usage_percent": gpu_usage
    }), 200


@app.route('/nodes/<node_id>', methods=['DELETE'])
def delete_node(node_id):
    """
    DELETE /nodes/<node_id>
    Delete a node by its ID.
    """
    if node_id not in nodes:
        return jsonify({"error": f"Node '{node_id}' not found."}), 404

    del nodes[node_id]
    return jsonify({"message": f"Node '{node_id}' deleted successfully."}), 200


# Error handling for unexpected issues
@app.errorhandler(500)
def internal_server_error(e):
    """
    Catch internal server errors and respond with a message.
    """
    return jsonify({"error": "An internal error occurred. Please try again later."}), 500


@app.errorhandler(404)
def not_found_error(e):
    """
    Catch 404 errors for undefined routes.
    """
    return jsonify({"error": "The requested resource could not be found."}), 404


if __name__ == '__main__':
    # Run the Flask development server (use a production server like Gunicorn for deployment)
    app.run(host='0.0.0.0', port=5000)
```
