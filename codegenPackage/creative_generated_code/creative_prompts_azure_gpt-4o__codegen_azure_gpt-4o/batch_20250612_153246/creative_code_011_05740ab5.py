"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spmepl.com
Prompt: Suggest an API for designing and simulating the functionality of pipeline rollers with adjustable rigging stands, similar to the products offered by SPM Equipment.
Generated: DETERMINISTIC_05740ab5b9e0185e
Batch ID: 20250612_153246
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

# Sample in-memory database to store pipeline roller configurations
pipeline_rollers = {}

@app.route('/rollers', methods=['GET'])
def list_rollers():
    """
    API endpoint to list all pipeline rollers.
    """
    return jsonify({"rollers": pipeline_rollers}), 200

@app.route('/rollers', methods=['POST'])
def add_roller():
    """
    API endpoint to add a new pipeline roller configuration.
    Expected JSON payload:
    {
        "roller_id": "unique_id",
        "material": "steel",
        "diameter": 25.0,
        "adjustable_stand_height": 100.0,
        "load_capacity": 200.0
    }
    """
    data = request.json
    try:
        # Validate payload
        required_fields = ["roller_id", "material", "diameter", "adjustable_stand_height", "load_capacity"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"'{field}' field is required"}), 400

        roller_id = data['roller_id']
        if roller_id in pipeline_rollers:
            return jsonify({"error": "Roller ID already exists"}), 400

        # Add roller to the database
        pipeline_rollers[roller_id] = {
            "material": data["material"],
            "diameter": data["diameter"],
            "adjustable_stand_height": data["adjustable_stand_height"],
            "load_capacity": data["load_capacity"]
        }
        return jsonify({"message": "Roller added successfully"}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/rollers/<roller_id>', methods=['GET'])
def get_roller(roller_id):
    """
    API endpoint to retrieve details of a specific roller by ID.
    """
    roller = pipeline_rollers.get(roller_id)
    if not roller:
        return jsonify({"error": "Roller not found"}), 404
    return jsonify({"roller": roller}), 200

@app.route('/rollers/<roller_id>', methods=['PUT'])
def update_roller(roller_id):
    """
    API endpoint to update an existing roller configuration.
    Expected JSON payload:
    {
        "material": "steel",
        "diameter": 30.0,
        "adjustable_stand_height": 120.0,
        "load_capacity": 250.0
    }
    """
    data = request.json
    roller = pipeline_rollers.get(roller_id)
    if not roller:
        return jsonify({"error": "Roller not found"}), 404

    try:
        # Update roller details
        roller.update({
            "material": data.get("material", roller["material"]),
            "diameter": data.get("diameter", roller["diameter"]),
            "adjustable_stand_height": data.get("adjustable_stand_height", roller["adjustable_stand_height"]),
            "load_capacity": data.get("load_capacity", roller["load_capacity"])
        })
        return jsonify({"message": "Roller updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/rollers/<roller_id>', methods=['DELETE'])
def delete_roller(roller_id):
    """
    API endpoint to delete a roller by ID.
    """
    if roller_id not in pipeline_rollers:
        return jsonify({"error": "Roller not found"}), 404

    try:
        del pipeline_rollers[roller_id]
        return jsonify({"message": "Roller deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
