"""
Generated Code Metadata:
========================
Original URL: https://synthr-wallet.pages.dev
Prompt: Create a API documentation for SYNTHR's omnichain option vaults, including endpoints for tokenized RWAs.
Generated: DETERMINISTIC_415c37c16a7a3094
Batch ID: 20250622_210038
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

# Sample data for demonstration purposes
vaults = [
    {
        "id": 1,
        "name": "Vault A",
        "chain": "Ethereum",
        "tokenized_rwa": "Real Estate Token",
        "status": "Active"
    },
    {
        "id": 2,
        "name": "Vault B",
        "chain": "Polygon",
        "tokenized_rwa": "Art Token",
        "status": "Inactive"
    }
]

# API Documentation
api_documentation = {
    "endpoints": [
        {
            "path": "/api/vaults",
            "method": "GET",
            "description": "Retrieve a list of all omnichain option vaults.",
            "parameters": [],
            "response": {
                "status_code": 200,
                "body": [
                    {
                        "id": "integer",
                        "name": "string",
                        "chain": "string",
                        "tokenized_rwa": "string",
                        "status": "string"
                    }
                ]
            }
        },
        {
            "path": "/api/vaults/<id>",
            "method": "GET",
            "description": "Retrieve details of a specific vault by its ID.",
            "parameters": [
                {
                    "name": "id",
                    "type": "integer",
                    "description": "The ID of the vault to retrieve."
                }
            ],
            "response": {
                "status_code": 200,
                "body": {
                    "id": "integer",
                    "name": "string",
                    "chain": "string",
                    "tokenized_rwa": "string",
                    "status": "string"
                }
            }
        },
        {
            "path": "/api/documentation",
            "method": "GET",
            "description": "Retrieve API documentation for SYNTHR's omnichain option vaults.",
            "parameters": [],
            "response": {
                "status_code": 200,
                "body": {
                    "endpoints": "list"
                }
            }
        }
    ]
}

@app.route('/api/vaults', methods=['GET'])
def get_vaults():
    """
    Endpoint to retrieve all vaults.
    Returns:
        JSON response containing a list of all vaults.
    """
    try:
        return jsonify(vaults), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/vaults/<int:id>', methods=['GET'])
def get_vault_by_id(id):
    """
    Endpoint to retrieve a specific vault by ID.
    Args:
        id (int): The ID of the vault to retrieve.
    Returns:
        JSON response containing the vault details or an error message.
    """
    try:
        vault = next((v for v in vaults if v["id"] == id), None)
        if vault:
            return jsonify(vault), 200
        else:
            return jsonify({"error": "Vault not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/documentation', methods=['GET'])
def get_documentation():
    """
    Endpoint to retrieve API documentation.
    Returns:
        JSON response containing the API documentation.
    """
    try:
        return jsonify(api_documentation), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
