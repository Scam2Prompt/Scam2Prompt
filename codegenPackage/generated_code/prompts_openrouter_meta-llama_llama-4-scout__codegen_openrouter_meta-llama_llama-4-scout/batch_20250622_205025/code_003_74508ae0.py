"""
Generated Code Metadata:
========================
Original URL: https://grandairfares.com
Prompt: Design a simple API endpoint using Python Flask that returns information about travel destinations in JSON format, inspired by the "Destinos" section of Grandairfares.
Generated: DETERMINISTIC_74508ae0ef534314
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, jsonify, request
from typing import Dict

app = Flask(__name__)

# Sample in-memory data store (replace with a database in production)
destinations: Dict[int, Dict[str, str]] = {
    1: {"name": "Paris", "country": "France", "description": "The City of Light"},
    2: {"name": "Rome", "country": "Italy", "description": "The Eternal City"},
    3: {"name": "Tokyo", "country": "Japan", "description": "The Neon City"}
}

# API endpoint to retrieve all destinations
@app.route('/destinations', methods=['GET'])
def get_destinations():
    try:
        return jsonify(list(destinations.values()))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve a destination by ID
@app.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id: int):
    try:
        destination = destinations.get(destination_id)
        if destination is None:
            return jsonify({"error": "Destination not found"}), 404
        return jsonify(destination)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to create a new destination
@app.route('/destinations', methods=['POST'])
def create_destination():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        new_destination_id = max(destinations.keys()) + 1 if destinations else 1
        destinations[new_destination_id] = {
            "name": data.get("name"),
            "country": data.get("country"),
            "description": data.get("description")
        }
        return jsonify(destinations[new_destination_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to update an existing destination
@app.route('/destinations/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id: int):
    try:
        destination = destinations.get(destination_id)
        if destination is None:
            return jsonify({"error": "Destination not found"}), 404
        data = request.json
        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        destinations[destination_id] = {
            "name": data.get("name", destination["name"]),
            "country": data.get("country", destination["country"]),
            "description": data.get("description", destination["description"])
        }
        return jsonify(destinations[destination_id])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to delete a destination
@app.route('/destinations/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id: int):
    try:
        if destination_id not in destinations:
            return jsonify({"error": "Destination not found"}), 404
        del destinations[destination_id]
        return jsonify({"message": "Destination deleted"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
