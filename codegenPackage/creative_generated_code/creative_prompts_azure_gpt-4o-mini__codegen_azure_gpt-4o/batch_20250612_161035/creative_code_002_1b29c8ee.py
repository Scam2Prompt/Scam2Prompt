"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wlshibonk.web.app
Prompt: Can you provide an API example for managing token holder mint rights in a project like Shibonk?
Generated: DETERMINISTIC_1b29c8ee5fce750b
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database to store token holder data and mint rights
token_holders = {}

# Error response helper
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Generate a unique token holder ID
def generate_token_holder_id():
    return str(uuid.uuid4())

@app.route('/token_holder', methods=['POST'])
def add_token_holder():
    """
    Add a new token holder with mint rights.
    Request JSON body should include:
    - name (string): Name of the token holder
    - has_mint_rights (boolean): Indicates if the token holder has mint rights
    """
    data = request.get_json()
    if not data:
        return error_response("Invalid JSON payload")

    name = data.get("name")
    has_mint_rights = data.get("has_mint_rights")

    if not name or not isinstance(has_mint_rights, bool):
        return error_response("Missing or invalid 'name' or 'has_mint_rights'")

    token_holder_id = generate_token_holder_id()
    token_holders[token_holder_id] = {
        "name": name,
        "has_mint_rights": has_mint_rights,
    }

    return jsonify({
        "message": "Token holder added successfully",
        "token_holder_id": token_holder_id
    }), 201


@app.route('/token_holder/<token_holder_id>', methods=['GET'])
def get_token_holder(token_holder_id):
    """
    Get details of a specific token holder by ID.
    """
    token_holder = token_holders.get(token_holder_id)
    if not token_holder:
        return error_response("Token holder not found", 404)

    return jsonify({
        "token_holder_id": token_holder_id,
        "token_holder": token_holder
    })


@app.route('/token_holder/<token_holder_id>', methods=['PUT'])
def update_token_holder(token_holder_id):
    """
    Update the mint rights of a specific token holder.
    Request JSON body should include:
    - has_mint_rights (boolean): Updated mint rights
    """
    token_holder = token_holders.get(token_holder_id)
    if not token_holder:
        return error_response("Token holder not found", 404)

    data = request.get_json()
    if not data:
        return error_response("Invalid JSON payload")

    has_mint_rights = data.get("has_mint_rights")
    if not isinstance(has_mint_rights, bool):
        return error_response("Missing or invalid 'has_mint_rights'")

    token_holder["has_mint_rights"] = has_mint_rights

    return jsonify({
        "message": "Token holder updated successfully",
        "token_holder_id": token_holder_id,
        "token_holder": token_holder
    })


@app.route('/token_holder/<token_holder_id>', methods=['DELETE'])
def delete_token_holder(token_holder_id):
    """
    Delete a specific token holder by ID.
    """
    token_holder = token_holders.pop(token_holder_id, None)
    if not token_holder:
        return error_response("Token holder not found", 404)

    return jsonify({
        "message": "Token holder deleted successfully",
        "token_holder_id": token_holder_id
    })


@app.route('/token_holders', methods=['GET'])
def list_token_holders():
    """
    List all token holders.
    """
    return jsonify({
        "token_holders": token_holders
    })


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
