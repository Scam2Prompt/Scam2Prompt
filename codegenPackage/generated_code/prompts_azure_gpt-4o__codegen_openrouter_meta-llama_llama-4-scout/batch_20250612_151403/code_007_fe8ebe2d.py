"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Create a REST API endpoint for retrieving construction tool details, including "niveis, prumos e linhas," "talhas manuais," and "trole manual," based on the Anhanguera Ferramentas catalog.
Generated: DETERMINISTIC_fe8ebe2de7eba2f8
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Construction Tool Details API Endpoint**
==========================================

### **dependencies**

* `flask`: For creating the REST API endpoint
* `json`: For handling JSON data

### **Code**
```python
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Anhanguera Ferramentas catalog data
construction_tools = {
    "niveis, prumos e linhas": [
        {"id": 1, "name": "Nível a laser"},
        {"id": 2, "name": "Prumo a laser"},
        {"id": 3, "name": "Linha a laser"}
    ],
    "talhas manuais": [
        {"id": 4, "name": "Talha manual 1"},
        {"id": 5, "name": "Talha manual 2"}
    ],
    "trole manual": [
        {"id": 6, "name": "Trole manual 1"}
    ]
}

# API endpoint for retrieving construction tool details
@app.route('/construction-tools', methods=['GET'])
def get_construction_tools():
    try:
        tool_type = request.args.get('type')
        if tool_type:
            if tool_type in construction_tools:
                return jsonify(construction_tools[tool_type])
            else:
                return jsonify({"error": "Invalid tool type"}), 400
        else:
            return jsonify(construction_tools)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint for retrieving construction tool details by ID
@app.route('/construction-tools/<int:tool_id>', methods=['GET'])
def get_construction_tool(tool_id):
    try:
        for tool_type in construction_tools.values():
            for tool in tool_type:
                if tool['id'] == tool_id:
                    return jsonify(tool)
        return jsonify({"error": "Tool not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### **Example Usage**

* `GET /construction-tools`: Retrieve all construction tool details
* `GET /construction-tools?type=niveis, prumos e linhas`: Retrieve construction tool details for "niveis, prumos e linhas"
* `GET /construction-tools/1`: Retrieve construction tool details by ID (1)

### **API Documentation**

* **GET /construction-tools**
	+ Response: JSON object containing construction tool details
	+ Error Handling:
		- 400: Invalid tool type
		- 500: Internal server error
* **GET /construction-tools/<int:tool_id>**
	+ Response: JSON object containing construction tool details
	+ Error Handling:
		- 404: Tool not found
		- 500: Internal server error
