"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Create a RESTful API endpoint that allows users to add and retrieve tools from a collection, referencing specific tools like "caixa de ferramentas" and "ferramentas plumo."
Generated: DETERMINISTIC_0050a03139bf828b
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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory tool collection
tools = []

# Helper function to validate tool data
def validate_tool_data(data):
    if 'name' not in data or not isinstance(data['name'], str):
        return False, "Missing or invalid 'name' field."
    if 'description' not in data or not isinstance(data['description'], str):
        return False, "Missing or invalid 'description' field."
    return True, None

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = jsonify({
        'error': e.name,
        'message': e.description
    })
    response.status_code = e.code
    return response

# Error handler for non-HTTP exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    response = jsonify({
        'error': 'Internal Server Error',
        'message': str(e)
    })
    response.status_code = 500
    return response

# Endpoint to add a new tool
@app.route('/tools', methods=['POST'])
def add_tool():
    try:
        data = request.json
        is_valid, error_message = validate_tool_data(data)
        if not is_valid:
            return jsonify({'error': 'Invalid data', 'message': error_message}), 400

        # Add the tool to the collection
        tool = {
            'id': len(tools) + 1,
            'name': data['name'],
            'description': data['description']
        }
        tools.append(tool)
        return jsonify({'message': 'Tool added successfully', 'tool': tool}), 201
    except Exception as e:
        return handle_exception(e)

# Endpoint to retrieve all tools
@app.route('/tools', methods=['GET'])
def get_tools():
    try:
        return jsonify({'tools': tools}), 200
    except Exception as e:
        return handle_exception(e)

# Endpoint to retrieve a specific tool by ID
@app.route('/tools/<int:tool_id>', methods=['GET'])
def get_tool_by_id(tool_id):
    try:
        tool = next((tool for tool in tools if tool['id'] == tool_id), None)
        if not tool:
            return jsonify({'error': 'Not Found', 'message': f'Tool with ID {tool_id} not found.'}), 404
        return jsonify({'tool': tool}), 200
    except Exception as e:
        return handle_exception(e)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Sample Usage:
- POST `/tools` with JSON payload: `{"name": "caixa de ferramentas", "description": "A versatile toolbox."}`
- GET `/tools` to fetch all tools.
- GET `/tools/<tool_id>` to retrieve a specific tool by ID.

Make sure you have Flask installed in your environment (`pip install flask`) before running this code.
