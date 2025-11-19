"""
Generated Code Metadata:
========================
Original URL: https://tokugroup.com
Prompt: Create a sample code snippet for a feature that allows users to interact with an intelligent platform for built environments.
Generated: DETERMINISTIC_79c10710d090d27f
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample data representing built environments
built_environments = {
    "office_1": {
        "name": "Office Building 1",
        "location": "Downtown",
        "features": ["WiFi", "Conference Rooms", "Parking"]
    },
    "mall_1": {
        "name": "Shopping Mall 1",
        "location": "Suburbs",
        "features": ["Food Court", "Cinema", "Parking"]
    }
}

@app.route('/environments', methods=['GET'])
def get_environments():
    """
    Endpoint to retrieve all built environments.
    """
    try:
        return jsonify(built_environments), 200
    except Exception as e:
        logging.error(f"Error retrieving environments: {e}")
        return jsonify({"error": "Unable to fetch environments"}), 500

@app.route('/environments/<env_id>', methods=['GET'])
def get_environment_details(env_id):
    """
    Endpoint to retrieve details of a specific built environment.
    :param env_id: ID of the environment to retrieve
    """
    try:
        environment = built_environments.get(env_id)
        if not environment:
            return jsonify({"error": "Environment not found"}), 404
        return jsonify(environment), 200
    except Exception as e:
        logging.error(f"Error retrieving environment details: {e}")
        return jsonify({"error": "Unable to fetch environment details"}), 500

@app.route('/environments', methods=['POST'])
def add_environment():
    """
    Endpoint to add a new built environment.
    Expects JSON payload with 'id', 'name', 'location', and 'features'.
    """
    try:
        data = request.get_json()
        if not data or 'id' not in data or 'name' not in data or 'location' not in data or 'features' not in data:
            return jsonify({"error": "Invalid input"}), 400

        env_id = data['id']
        if env_id in built_environments:
            return jsonify({"error": "Environment ID already exists"}), 400

        built_environments[env_id] = {
            "name": data['name'],
            "location": data['location'],
            "features": data['features']
        }
        return jsonify({"message": "Environment added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding environment: {e}")
        return jsonify({"error": "Unable to add environment"}), 500

@app.route('/environments/<env_id>', methods=['DELETE'])
def delete_environment(env_id):
    """
    Endpoint to delete a built environment.
    :param env_id: ID of the environment to delete
    """
    try:
        if env_id not in built_environments:
            return jsonify({"error": "Environment not found"}), 404

        del built_environments[env_id]
        return jsonify({"message": "Environment deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting environment: {e}")
        return jsonify({"error": "Unable to delete environment"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
