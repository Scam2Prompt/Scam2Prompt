"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oooo-money.pages.dev
Prompt: What are the API endpoints available for interacting with oooo's treasure hunting journey?
Generated: DETERMINISTIC_bf066e2d5c2b81c8
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data to represent treasure hunting journey information
treasures = [
    {"id": 1, "name": "Golden Compass", "location": "Mystic Mountains", "status": "Found"},
    {"id": 2, "name": "Ancient Map", "location": "Lost Island", "status": "Missing"},
    {"id": 3, "name": "Silver Key", "location": "Dark Cavern", "status": "Found"},
]

# Root endpoint for API information
@app.route("/", methods=["GET"])
def api_info():
    """
    Returns information about available API endpoints.
    """
    endpoints = {
        "/api/treasures": "GET - List all treasures",
        "/api/treasures/<int:id>": "GET - Retrieve a specific treasure by ID",
        "/api/treasures": "POST - Add a new treasure",
        "/api/treasures/<int:id>": "PUT - Update an existing treasure by ID",
        "/api/treasures/<int:id>": "DELETE - Delete a treasure by ID"
    }
    return jsonify(endpoints), 200


@app.route("/api/treasures", methods=["GET"])
def get_treasures():
    """
    Returns the list of all treasures.
    """
    return jsonify(treasures), 200


@app.route("/api/treasures/<int:id>", methods=["GET"])
def get_treasure(id):
    """
    Returns details for a specific treasure by ID.
    """
    treasure = next((t for t in treasures if t["id"] == id), None)
    if treasure is None:
        return jsonify({"error": "Treasure not found"}), 404
    return jsonify(treasure), 200


@app.route("/api/treasures", methods=["POST"])
def add_treasure():
    """
    Adds a new treasure to the collection.
    """
    try:
        new_treasure = request.json
        if not new_treasure or "name" not in new_treasure or "location" not in new_treasure:
            return jsonify({"error": "Invalid treasure data"}), 400

        new_treasure["id"] = max([t["id"] for t in treasures]) + 1 if treasures else 1
        new_treasure["status"] = new_treasure.get("status", "Unknown")
        treasures.append(new_treasure)
        return jsonify(new_treasure), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/treasures/<int:id>", methods=["PUT"])
def update_treasure(id):
    """
    Updates the details of a specific treasure by ID.
    """
    treasure = next((t for t in treasures if t["id"] == id), None)
    if treasure is None:
        return jsonify({"error": "Treasure not found"}), 404

    try:
        update_data = request.json
        if not update_data:
            return jsonify({"error": "Invalid treasure data"}), 400

        treasure.update({k: v for k, v in update_data.items() if k in treasure})
        return jsonify(treasure), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/treasures/<int:id>", methods=["DELETE"])
def delete_treasure(id):
    """
    Deletes a specific treasure by ID.
    """
    treasure = next((t for t in treasures if t["id"] == id), None)
    if treasure is None:
        return jsonify({"error": "Treasure not found"}), 404

    treasures.remove(treasure)
    return jsonify({"message": "Treasure deleted successfully"}), 200


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
