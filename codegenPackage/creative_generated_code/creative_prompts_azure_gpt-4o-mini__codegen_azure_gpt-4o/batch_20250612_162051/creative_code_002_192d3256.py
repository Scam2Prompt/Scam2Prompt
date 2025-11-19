"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Create a REST API specification for a service that handles plumbing and electrical repairs, inspired by the offerings of Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_192d3256e6c8fa4c
Batch ID: 20250612_162051
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

# Mock database for demonstration purposes
repairs = []

# Error handler for 404 - Not Found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 400 - Bad Request
@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

# Root route
@app.route("/")
def welcome():
    return jsonify({"message": "Welcome to Felipe Muñoz Reparaciones API"}), 200

# Get a list of all repair requests
@app.route("/repairs", methods=["GET"])
def get_repairs():
    return jsonify({"repairs": repairs}), 200

# Create a new repair request
@app.route("/repairs", methods=["POST"])
def create_repair():
    try:
        data = request.get_json()
        # Validate payload
        if not data or "type" not in data or "description" not in data:
            raise ValueError("Missing or invalid data")
        new_repair = {
            "id": len(repairs) + 1,
            "type": data["type"],  # Type can be "plumbing" or "electrical"
            "description": data["description"],
            "status": "pending"  # Default status for new repairs
        }
        repairs.append(new_repair)
        return jsonify(new_repair), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Get a single repair request by ID
@app.route("/repairs/<int:repair_id>", methods=["GET"])
def get_repair(repair_id):
    repair = next((r for r in repairs if r["id"] == repair_id), None)
    if repair:
        return jsonify(repair), 200
    else:
        return jsonify({"error": "Repair not found"}), 404

# Update the status of a repair request
@app.route("/repairs/<int:repair_id>", methods=["PATCH"])
def update_repair(repair_id):
    try:
        data = request.get_json()
        repair = next((r for r in repairs if r["id"] == repair_id), None)
        if not repair:
            return jsonify({"error": "Repair not found"}), 404
        if "status" not in data:
            raise ValueError("Missing 'status' field")
        repair["status"] = data["status"]  # Update status, e.g., "completed" or "canceled"
        return jsonify(repair), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Delete a repair request
@app.route("/repairs/<int:repair_id>", methods=["DELETE"])
def delete_repair(repair_id):
    global repairs
    repair = next((r for r in repairs if r["id"] == repair_id), None)
    if repair:
        repairs = [r for r in repairs if r["id"] != repair_id]
        return jsonify({"message": "Repair deleted"}), 200
    else:
        return jsonify({"error": "Repair not found"}), 404

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)
```

### Instructions:
1. Install Flask: `pip install flask`.
2. Save this code in a file, e.g., `app.py`.
3. Run the application: `python app.py`.
4. Use an API testing tool like Postman or curl to interact with the endpoints.
