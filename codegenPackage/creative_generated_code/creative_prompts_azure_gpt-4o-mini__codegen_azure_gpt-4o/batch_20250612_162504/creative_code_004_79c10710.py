"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokugroup.com
Prompt: Create a sample code snippet for a feature that allows users to interact with an intelligent platform for built environments.
Generated: DETERMINISTIC_79c10710d090d27f
Batch ID: 20250612_162504
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

# Simulating Intelligent Platform for Built Environments
class IntelligentPlatform:
    def __init__(self):
        # Sample data for built environments
        self.data = {
            "building_1": {"temperature": 22, "lights_on": True},
            "building_2": {"temperature": 25, "lights_on": False},
        }

    def get_status(self, building_id):
        # Retrieve the status of the specified building
        return self.data.get(building_id, None)

    def update_status(self, building_id, updates):
        # Update the status of the specified building
        if building_id in self.data:
            self.data[building_id].update(updates)
            return self.data[building_id]
        return None


# Instantiate the Intelligent Platform
platform = IntelligentPlatform()

@app.route('/status/<building_id>', methods=['GET'])
def get_building_status(building_id):
    """
    Endpoint to retrieve the status of a specific building.
    Request type: GET
    URL example: /status/building_1
    """
    try:
        status = platform.get_status(building_id)
        if status is None:
            return jsonify({"error": "Building not found"}), 404
        return jsonify(status), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/status/<building_id>', methods=['PUT'])
def update_building_status(building_id):
    """
    Endpoint to update the status of a specific building.
    Request type: PUT
    URL example: /status/building_1
    Request body example: {"temperature": 24, "lights_on": false}
    """
    try:
        updates = request.get_json()
        if not updates:
            return jsonify({"error": "Invalid request body"}), 400

        updated_status = platform.update_status(building_id, updates)
        if updated_status is None:
            return jsonify({"error": "Building not found"}), 404
        return jsonify(updated_status), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Set debug=False for production use
```
