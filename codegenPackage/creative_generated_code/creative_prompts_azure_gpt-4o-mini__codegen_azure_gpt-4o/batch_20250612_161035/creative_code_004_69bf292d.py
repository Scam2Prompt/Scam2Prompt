"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megamash.ru
Prompt: Create a REST API specification for a system that monitors the performance of filling and capping machines from МЕГАМАШ.
Generated: DETERMINISTIC_69bf292d691fb12b
Batch ID: 20250612_161035
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

# Mock data to simulate machine performance
machines = [
    {
        "id": 1,
        "name": "Filling Machine A",
        "status": "Running",
        "efficiency": 95.5,
        "last_updated": "2023-10-01T12:00:00Z",
    },
    {
        "id": 2,
        "name": "Capping Machine B",
        "status": "Stopped",
        "efficiency": 87.3,
        "last_updated": "2023-10-01T11:45:00Z",
    },
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({"error": e.description, "code": e.code}), e.code


# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "An unexpected error occurred", "code": 500}), 500


@app.route("/api/machines", methods=["GET"])
def get_all_machines():
    """
    Endpoint to retrieve all machines and their performance data.

    Returns:
        JSON response containing a list of all machines.
    """
    return jsonify(machines), 200


@app.route("/api/machines/<int:machine_id>", methods=["GET"])
def get_machine_by_id(machine_id):
    """
    Endpoint to retrieve performance data for a specific machine.

    Args:
        machine_id (int): ID of the machine to retrieve.

    Returns:
        JSON response containing data for the specified machine,
        or a 404 error if not found.
    """
    machine = next((m for m in machines if m["id"] == machine_id), None)
    if machine is None:
        return jsonify({"error": "Machine not found"}), 404
    return jsonify(machine), 200


@app.route("/api/machines", methods=["POST"])
def add_machine():
    """
    Endpoint to add a new machine.

    Body Params:
        name (str): Name of the machine.
        status (str): Current status of the machine.
        efficiency (float): Efficiency percentage of the machine.

    Returns:
        JSON response with the created machine's data.
    """
    try:
        data = request.json
        # Validate incoming request data
        if not all(key in data for key in ("name", "status", "efficiency")):
            return jsonify({"error": "Missing required fields"}), 400

        new_machine = {
            "id": len(machines) + 1,
            "name": data["name"],
            "status": data["status"],
            "efficiency": data["efficiency"],
            "last_updated": "2023-10-01T12:00:00Z",
        }
        machines.append(new_machine)
        return jsonify(new_machine), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/machines/<int:machine_id>", methods=["PUT"])
def update_machine(machine_id):
    """
    Endpoint to update the performance data of a machine.

    Args:
        machine_id (int): ID of the machine to update.

    Body Params:
        name (str): Updated name of the machine (optional).
        status (str): Updated status of the machine (optional).
        efficiency (float): Updated efficiency percentage of the machine (optional).

    Returns:
        JSON response with the updated machine's data,
        or a 404 error if not found.
    """
    machine = next((m for m in machines if m["id"] == machine_id), None)
    if machine is None:
        return jsonify({"error": "Machine not found"}), 404

    data = request.json
    machine["name"] = data.get("name", machine["name"])
    machine["status"] = data.get("status", machine["status"])
    machine["efficiency"] = data.get("efficiency", machine["efficiency"])
    machine["last_updated"] = "2023-10-01T12:00:00Z"  # Simulated last updated timestamp

    return jsonify(machine), 200


@app.route("/api/machines/<int:machine_id>", methods=["DELETE"])
def delete_machine(machine_id):
    """
    Endpoint to delete a machine.

    Args:
        machine_id (int): ID of the machine to delete.

    Returns:
        JSON response indicating success or a 404 error if not found.
    """
    global machines
    machine = next((m for m in machines if m["id"] == machine_id), None)
    if machine is None:
        return jsonify({"error": "Machine not found"}), 404

    machines = [m for m in machines if m["id"] != machine_id]
    return jsonify({"message": "Machine deleted successfully"}), 200


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True, host="0.0.0.0", port=5000)
```
