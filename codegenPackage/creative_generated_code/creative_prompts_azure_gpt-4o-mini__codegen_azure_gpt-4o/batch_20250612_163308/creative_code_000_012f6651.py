"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate a code snippet for a tool management API that includes functionalities for tracking inventory of tools like "alicate," "furadeira," and "parafusadeira."
Generated: DETERMINISTIC_012f6651a8204dcb
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial tool inventory
inventory = {
    "alicate": {"quantity": 10, "description": "Alicate de pressão"},
    "furadeira": {"quantity": 5, "description": "Furadeira elétrica"},
    "parafusadeira": {"quantity": 8, "description": "Parafusadeira automática"}
}


@app.route('/tools', methods=['GET'])
def get_tools():
    """
    Endpoint to retrieve the full inventory of tools.
    """
    return jsonify({"inventory": inventory}), 200


@app.route('/tools/<tool_name>', methods=['GET'])
def get_tool(tool_name):
    """
    Endpoint to retrieve information about a specific tool.
    :param tool_name: Name of the tool to retrieve.
    """
    tool = inventory.get(tool_name)
    if not tool:
        return jsonify({"error": "Tool not found"}), 404
    return jsonify({tool_name: tool}), 200


@app.route('/tools', methods=['POST'])
def add_tool():
    """
    Endpoint to add a new tool to the inventory.
    Request Body Format:
    {
        "name": "tool_name",
        "quantity": int,
        "description": "tool_description"
    }
    """
    try:
        data = request.json
        name = data.get("name")
        quantity = data.get("quantity")
        description = data.get("description")

        if not name or not isinstance(quantity, int) or not description:
            return jsonify({"error": "Invalid input"}), 400

        if name in inventory:
            return jsonify({"error": "Tool already exists"}), 400

        inventory[name] = {"quantity": quantity, "description": description}
        return jsonify({"message": f"Tool {name} added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/tools/<tool_name>', methods=['PUT'])
def update_tool(tool_name):
    """
    Endpoint to update the quantity or description of a tool in the inventory.
    Request Body Format:
    {
        "quantity": int (optional),
        "description": "tool_description" (optional)
    }
    """
    try:
        data = request.json
        tool = inventory.get(tool_name)

        if not tool:
            return jsonify({"error": "Tool not found"}), 404

        quantity = data.get("quantity")
        description = data.get("description")

        if quantity is not None:
            if not isinstance(quantity, int):
                return jsonify({"error": "Invalid quantity"}), 400
            tool["quantity"] = quantity

        if description is not None:
            tool["description"] = description

        inventory[tool_name] = tool
        return jsonify({"message": f"Tool {tool_name} updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/tools/<tool_name>', methods=['DELETE'])
def delete_tool(tool_name):
    """
    Endpoint to delete a tool from the inventory.
    :param tool_name: Name of the tool to delete.
    """
    tool = inventory.pop(tool_name, None)
    if not tool:
        return jsonify({"error": "Tool not found"}), 404
    return jsonify({"message": f"Tool {tool_name} deleted successfully"}), 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
