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
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
api = Api(app)

# Sample data structure to hold vault information
vaults = {
    "1": {
        "id": "1",
        "name": "Omnichain Vault 1",
        "tokenized_rwa": "Tokenized Real World Asset 1",
        "balance": 1000,
        "owner": "user1"
    },
    "2": {
        "id": "2",
        "name": "Omnichain Vault 2",
        "tokenized_rwa": "Tokenized Real World Asset 2",
        "balance": 2000,
        "owner": "user2"
    }
}

class Vaults(Resource):
    """Resource for managing omnichain option vaults."""

    def get(self):
        """Get a list of all vaults."""
        return jsonify(vaults)

    def post(self):
        """Create a new vault."""
        try:
            data = request.get_json()
            vault_id = str(len(vaults) + 1)
            vaults[vault_id] = {
                "id": vault_id,
                "name": data["name"],
                "tokenized_rwa": data["tokenized_rwa"],
                "balance": data.get("balance", 0),
                "owner": data["owner"]
            }
            return jsonify(vaults[vault_id]), 201
        except KeyError as e:
            raise BadRequest(f"Missing required field: {str(e)}")
        except Exception as e:
            raise BadRequest(f"An error occurred: {str(e)}")

class Vault(Resource):
    """Resource for managing a specific vault."""

    def get(self, vault_id):
        """Get details of a specific vault by ID."""
        vault = vaults.get(vault_id)
        if vault is None:
            return jsonify({"error": "Vault not found"}), 404
        return jsonify(vault)

    def put(self, vault_id):
        """Update an existing vault."""
        if vault_id not in vaults:
            return jsonify({"error": "Vault not found"}), 404
        
        data = request.get_json()
        vaults[vault_id].update(data)
        return jsonify(vaults[vault_id])

    def delete(self, vault_id):
        """Delete a vault by ID."""
        if vault_id not in vaults:
            return jsonify({"error": "Vault not found"}), 404
        
        del vaults[vault_id]
        return jsonify({"message": "Vault deleted successfully"}), 204

# Define API endpoints
api.add_resource(Vaults, '/vaults')
api.add_resource(Vault, '/vaults/<string:vault_id>')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
