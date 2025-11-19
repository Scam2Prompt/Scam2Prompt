"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Create a REST API specification for a service that handles plumbing and electrical repairs, inspired by the offerings of Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_192d3256e6c8fa4c
Batch ID: 20250612_162051
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

# In-memory database for demonstration purposes
repairs = []

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Felipe Muñoz Reparaciones API"}), 200

# Get all repair requests
@app.route("/repairs", methods=["GET"])
def get_repairs():
    return jsonify({"repairs": repairs}), 200

# Create a new repair request
@app.route("/repairs", methods=["POST"])
def create_repair():
    try:
        data = request.get_json()
        if not data or "type" not in data or "description" not in data:
            return jsonify({"error": "Invalid input"}), 400

        repair = {
            "id": len(repairs) + 1,
            "type": data["type"],  # Type of repair: plumbing or electrical
            "description": data["description"],  # Description of the issue
            "status": "pending"  # Default status
        }
        repairs.append(repair)
        return jsonify(repair), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get a specific repair request by ID
@app.route("/repairs/<int:repair_id>", methods=["GET"])
def get_repair(repair_id):
    repair = next((r for r in repairs if r["id"] == repair_id), None)
    if not repair:
        return jsonify({"error": "Repair not found"}), 404
    return jsonify(repair), 200

# Update the status of a repair request
@app.route("/repairs/<int:repair_id>", methods=["PUT"])
def update_repair(repair_id):
    try:
        repair = next((r for r in repairs if r["id"] == repair_id), None)
        if not repair:
            return jsonify({"error": "Repair not found"}), 404

        data = request.get_json()
        if not data or "status" not in data:
            return jsonify({"error": "Invalid input"}), 400

        repair["status"] = data["status"]  # Update the status
        return jsonify(repair), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a repair request
@app.route("/repairs/<int:repair_id>", methods=["DELETE"])
def delete_repair(repair_id):
    global repairs
    repair = next((r for r in repairs if r["id"] == repair_id), None)
    if not repair:
        return jsonify({"error": "Repair not found"}), 404

    repairs = [r for r in repairs if r["id"] != repair_id]
    return jsonify({"message": "Repair deleted successfully"}), 200

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```
