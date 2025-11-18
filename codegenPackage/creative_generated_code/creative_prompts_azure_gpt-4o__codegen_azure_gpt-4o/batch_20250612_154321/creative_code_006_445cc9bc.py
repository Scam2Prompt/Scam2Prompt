"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethermall.pages.dev
Prompt: Create code to manage aliases in a Web3 email system, allowing users to customize their email address for easy sharing and recall, inspired by EtherMail's alias settings.
Generated: DETERMINISTIC_445cc9bc9fcf380f
Batch ID: 20250612_154321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code in Python, using the Flask framework for the web application and MongoDB for storing alias data:

```python
from flask import Flask, request, jsonify
from pymongo import MongoClient
import re

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client.web3_email_system
aliases_collection = db.aliases

# Function to validate email alias format
def is_valid_alias(alias):
    # Alias can only contain alphanumeric characters, underscores, and periods
    return re.match(r'^[a-zA-Z0-9_.]+$', alias)

# Endpoint to create or update an alias
@app.route('/alias', methods=['POST'])
def manage_alias():
    try:
        # Parse input data
        data = request.json
        if not data or 'address' not in data or 'alias' not in data:
            return jsonify({"error": "Missing required fields"}), 400

        web3_address = data['address']
        alias = data['alias']

        # Validate Web3 address (basic check for length)
        if not isinstance(web3_address, str) or len(web3_address) != 42 or not web3_address.startswith('0x'):
            return jsonify({"error": "Invalid Web3 address"}), 400

        # Validate alias format
        if not is_valid_alias(alias):
            return jsonify({"error": "Alias contains invalid characters"}), 400

        # Check if the alias is already taken
        existing_alias = aliases_collection.find_one({"alias": alias})
        if existing_alias and existing_alias["address"] != web3_address:
            return jsonify({"error": "Alias is already in use"}), 409

        # Create or update alias in the database
        aliases_collection.update_one(
            {"address": web3_address},
            {"$set": {"alias": alias}},
            upsert=True
        )

        return jsonify({"message": "Alias successfully created/updated"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected server error occurred", "details": str(e)}), 500

# Endpoint to retrieve an alias by Web3 address
@app.route('/alias/<web3_address>', methods=['GET'])
def get_alias(web3_address):
    try:
        # Validate Web3 address format
        if not isinstance(web3_address, str) or len(web3_address) != 42 or not web3_address.startswith('0x'):
            return jsonify({"error": "Invalid Web3 address"}), 400

        # Retrieve the alias from the database
        alias_data = aliases_collection.find_one({"address": web3_address})
        if not alias_data:
            return jsonify({"error": "Alias not found"}), 404

        return jsonify({"address": web3_address, "alias": alias_data["alias"]}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected server error occurred", "details": str(e)}), 500

# Endpoint to delete an alias
@app.route('/alias/<web3_address>', methods=['DELETE'])
def delete_alias(web3_address):
    try:
        # Validate Web3 address format
        if not isinstance(web3_address, str) or len(web3_address) != 42 or not web3_address.startswith('0x'):
            return jsonify({"error": "Invalid Web3 address"}), 400

        # Delete the alias from the database
        result = aliases_collection.delete_one({"address": web3_address})
        if result.deleted_count == 0:
            return jsonify({"error": "Alias not found"}), 404

        return jsonify({"message": "Alias successfully deleted"}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected server error occurred", "details": str(e)}), 500

# Entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
1. Install required Python packages before running:
   ```
   pip install flask pymongo
   ```

2. Make sure MongoDB is running locally, or update the connection string to point to your MongoDB server.

3. Replace `debug=True` with `debug=False` for production deployment.
