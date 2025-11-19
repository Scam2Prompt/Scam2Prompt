"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate a code snippet for a tool management API that includes functionalities for tracking inventory of tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_012f6651a8204dcb
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for tool inventory
tool_inventory = {
    "alicate": {"quantity": 10, "description": "Alicate for gripping and cutting."},
    "furadeira": {"quantity": 5, "description": "Electric drill for making holes."},
    "parafusadeira": {"quantity": 8, "description": "Screwdriver for tightening screws."}
}

@app.route('/tools', methods=['GET'])
def get_all_tools():
    """
    Endpoint to retrieve all tools in the inventory.
    """
    return jsonify(tool_inventory), 200

@app.route('/tools/<tool_name>', methods=['GET'])
def get_tool(tool_name):
    """
    Endpoint to retrieve details of a specific tool.
    :param tool_name: Name of the tool to retrieve.
    """
    tool = tool_inventory.get(tool_name)
    if tool:
        return jsonify({tool_name: tool}), 200
    else:
        return jsonify({"error": f"Tool '{tool_name}' not found."}), 404

@app.route('/tools/<tool_name>', methods=['POST'])
def add_tool(tool_name):
    """
    Endpoint to add a new tool to the inventory.
    :param tool_name: Name of the tool to add.
    """
    if tool_name in tool_inventory:
        return jsonify({"error": f"Tool '{tool_name}' already exists."}), 400

    data = request.json
    if not data or 'quantity' not in data or 'description' not in data:
        return jsonify({"error": "Invalid data. 'quantity' and 'description' are required."}), 400

    tool_inventory[tool_name] = {
        "quantity": data['quantity'],
        "description": data['description']
    }
    return jsonify({"message": f"Tool '{tool_name}' added successfully."}), 201

@app.route('/tools/<tool_name>', methods=['PUT'])
def update_tool(tool_name):
    """
    Endpoint to update the details of an existing tool.
    :param tool_name: Name of the tool to update.
    """
    tool = tool_inventory.get(tool_name)
    if not tool:
        return jsonify({"error": f"Tool '{tool_name}' not found."}), 404

    data = request.json
    if not data or ('quantity' not in data and 'description' not in data):
        return jsonify({"error": "Invalid data. At least 'quantity' or 'description' must be provided."}), 400

    if 'quantity' in data:
        tool['quantity'] = data['quantity']
    if 'description' in data:
        tool['description'] = data['description']

    return jsonify({"message": f"Tool '{tool_name}' updated successfully."}), 200

@app.route('/tools/<tool_name>', methods=['DELETE'])
def delete_tool(tool_name):
    """
    Endpoint to delete a tool from the inventory.
    :param tool_name: Name of the tool to delete.
    """
    if tool_name in tool_inventory:
        del tool_inventory[tool_name]
        return jsonify({"message": f"Tool '{tool_name}' deleted successfully."}), 200
    else:
        return jsonify({"error": f"Tool '{tool_name}' not found."}), 404

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
