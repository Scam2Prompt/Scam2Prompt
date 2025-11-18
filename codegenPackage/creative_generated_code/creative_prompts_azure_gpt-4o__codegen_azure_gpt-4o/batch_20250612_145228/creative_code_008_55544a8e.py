"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://champsonly.xyz
Prompt: Develop a tool to manage private whitelist opportunities for NFT projects, similar to the exclusive bonuses offered by Champs Only.
Generated: DETERMINISTIC_55544a8e9379a2ee
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for whitelist opportunities and users
whitelist_opportunities = {}
users = {}

# Helper function to validate JSON input
def validate_request_data(data, required_fields):
    if not all(field in data for field in required_fields):
        missing_fields = [field for field in required_fields if field not in data]
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

# Route to create a new whitelist opportunity
@app.route('/whitelist', methods=['POST'])
def create_whitelist_opportunity():
    try:
        # Parse and validate request data
        data = request.get_json()
        validate_request_data(data, ['project_name', 'description', 'slots'])

        project_id = len(whitelist_opportunities) + 1
        whitelist_opportunities[project_id] = {
            "project_name": data['project_name'],
            "description": data['description'],
            "slots": data['slots'],
            "users": []
        }

        return jsonify({"message": "Whitelist opportunity created", "id": project_id}), 201
    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Route to list all whitelist opportunities
@app.route('/whitelist', methods=['GET'])
def list_whitelist_opportunities():
    return jsonify(whitelist_opportunities), 200

# Route to register a user for a whitelist opportunity
@app.route('/whitelist/<int:project_id>/register', methods=['POST'])
def register_user(project_id):
    try:
        # Validate project existence
        if project_id not in whitelist_opportunities:
            return jsonify({"error": "Whitelist opportunity not found"}), 404

        # Parse and validate request data
        data = request.get_json()
        validate_request_data(data, ['user_name', 'wallet_address'])

        # Check if there are remaining slots
        opportunity = whitelist_opportunities[project_id]
        if len(opportunity['users']) >= opportunity['slots']:
            return jsonify({"error": "No more slots available"}), 400

        # Register user
        user_id = len(users) + 1
        users[user_id] = {
            "user_name": data['user_name'],
            "wallet_address": data['wallet_address']
        }
        opportunity['users'].append(user_id)

        return jsonify({"message": "User registered successfully", "user_id": user_id}), 200
    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Route to list all users of a whitelist opportunity
@app.route('/whitelist/<int:project_id>/users', methods=['GET'])
def list_users(project_id):
    try:
        # Validate project existence
        if project_id not in whitelist_opportunities:
            return jsonify({"error": "Whitelist opportunity not found"}), 404

        # Get user details
        opportunity = whitelist_opportunities[project_id]
        user_details = [users[user_id] for user_id in opportunity['users']]

        return jsonify(user_details), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Route to delete a whitelist opportunity
@app.route('/whitelist/<int:project_id>', methods=['DELETE'])
def delete_whitelist_opportunity(project_id):
    try:
        # Validate project existence
        if project_id not in whitelist_opportunities:
            return jsonify({"error": "Whitelist opportunity not found"}), 404

        # Delete whitelist opportunity
        del whitelist_opportunities[project_id]
        return jsonify({"message": "Whitelist opportunity deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Main entry point
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```
