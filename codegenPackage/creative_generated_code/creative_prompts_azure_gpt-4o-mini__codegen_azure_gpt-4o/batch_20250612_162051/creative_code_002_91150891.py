"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Create an API recommendation for managing mechanical installations in the oil and gas industry, referencing the expertise of C&M Pinnacle.
Generated: DETERMINISTIC_9115089170d47c96
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample data representing mechanical installations
mechanical_installations = [
    {"id": 1, "name": "Pipeline Installation", "description": "High-pressure pipeline system installation", "status": "Completed"},
    {"id": 2, "name": "Pump System Maintenance", "description": "Routine maintenance for oil pump system", "status": "In Progress"},
    {"id": 3, "name": "Tank Inspection", "description": "Inspection of storage tanks for integrity", "status": "Pending"},
]

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP errors globally."""
    response = jsonify({
        "error": e.name,
        "message": e.description,
        "status_code": e.code
    })
    response.status_code = e.code
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle generic exceptions globally."""
    response = jsonify({
        "error": "Internal Server Error",
        "message": str(e),
        "status_code": 500
    })
    response.status_code = 500
    return response

@app.route("/installations", methods=["GET"])
def get_installations():
    """Retrieve a list of all mechanical installations."""
    return jsonify(mechanical_installations), 200

@app.route("/installations/<int:installation_id>", methods=["GET"])
def get_installation(installation_id):
    """Retrieve details of a single mechanical installation by its ID."""
    installation = next((inst for inst in mechanical_installations if inst["id"] == installation_id), None)
    if not installation:
        return jsonify({"error": "Not Found", "message": "Installation not found"}), 404
    return jsonify(installation), 200

@app.route("/installations", methods=["POST"])
def add_installation():
    """Add a new mechanical installation."""
    try:
        data = request.get_json()
        if not data or "name" not in data or "description" not in data or "status" not in data:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        new_installation = {
            "id": len(mechanical_installations) + 1,
            "name": data["name"],
            "description": data["description"],
            "status": data["status"]
        }
        mechanical_installations.append(new_installation)
        return jsonify(new_installation), 201
    except Exception as e:
        return handle_exception(e)

@app.route("/installations/<int:installation_id>", methods=["PUT"])
def update_installation(installation_id):
    """Update an existing mechanical installation by its ID."""
    installation = next((inst for inst in mechanical_installations if inst["id"] == installation_id), None)
    if not installation:
        return jsonify({"error": "Not Found", "message": "Installation not found"}), 404

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Missing request body"}), 400

        installation["name"] = data.get("name", installation["name"])
        installation["description"] = data.get("description", installation["description"])
        installation["status"] = data.get("status", installation["status"])

        return jsonify(installation), 200
    except Exception as e:
        return handle_exception(e)

@app.route("/installations/<int:installation_id>", methods=["DELETE"])
def delete_installation(installation_id):
    """Delete a mechanical installation by its ID."""
    installation = next((inst for inst in mechanical_installations if inst["id"] == installation_id), None)
    if not installation:
        return jsonify({"error": "Not Found", "message": "Installation not found"}), 404

    mechanical_installations.remove(installation)
    return jsonify({"message": "Installation deleted successfully"}), 200

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
