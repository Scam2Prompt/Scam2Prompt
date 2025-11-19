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
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data structure to hold node information and GPU performance metrics
nodes = {}
gpu_performance = {}

@app.route('/api/nodes', methods=['GET'])
def get_nodes():
    """
    Retrieve a list of all Aethir nodes.
    Returns a JSON response with node details.
    """
    return jsonify(nodes), 200

@app.route('/api/nodes/<string:node_id>', methods=['GET'])
def get_node(node_id):
    """
    Retrieve details of a specific Aethir node by its ID.
    :param node_id: Unique identifier for the node.
    Returns a JSON response with node details or 404 if not found.
    """
    node = nodes.get(node_id)
    if not node:
        abort(404, description="Node not found")
    return jsonify(node), 200

@app.route('/api/nodes', methods=['POST'])
def create_node():
    """
    Create a new Aethir node.
    Expects JSON payload with node details.
    Returns the created node on success.
    """
    if not request.json or 'id' not in request.json:
        abort(400, description="Invalid input: 'id' is required")
    
    node_id = request.json['id']
    if node_id in nodes:
        abort(400, description="Node already exists")

    node = {
        'id': node_id,
        'data': request.json.get('data', {})
    }
    nodes[node_id] = node
    return jsonify(node), 201

@app.route('/api/nodes/<string:node_id>', methods=['DELETE'])
def delete_node(node_id):
    """
    Delete an Aethir node by its ID.
    :param node_id: Unique identifier for the node.
    Returns 204 on success or 404 if not found.
    """
    if node_id not in nodes:
        abort(404, description="Node not found")
    
    del nodes[node_id]
    return '', 204

@app.route('/api/gpu/performance', methods=['GET'])
def get_gpu_performance():
    """
    Retrieve GPU performance metrics.
    Returns a JSON response with GPU performance metrics.
    """
    return jsonify(gpu_performance), 200

@app.route('/api/gpu/performance/<string:node_id>', methods=['GET'])
def get_node_gpu_performance(node_id):
    """
    Retrieve GPU performance metrics for a specific node.
    :param node_id: Unique identifier for the node.
    Returns a JSON response with GPU performance metrics or 404 if not found.
    """
    performance = gpu_performance.get(node_id)
    if not performance:
        abort(404, description="GPU performance data not found for this node")
    return jsonify(performance), 200

@app.route('/api/gpu/performance/<string:node_id>', methods=['POST'])
def update_gpu_performance(node_id):
    """
    Update GPU performance metrics for a specific node.
    Expects JSON payload with performance data.
    Returns the updated performance data on success.
    """
    if not request.json:
        abort(400, description="Invalid input: JSON payload required")
    
    performance_data = {
        'usage': request.json.get('usage', None),
        'temperature': request.json.get('temperature', None),
        'memory_usage': request.json.get('memory_usage', None)
    }
    
    gpu_performance[node_id] = performance_data
    return jsonify(performance_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```
