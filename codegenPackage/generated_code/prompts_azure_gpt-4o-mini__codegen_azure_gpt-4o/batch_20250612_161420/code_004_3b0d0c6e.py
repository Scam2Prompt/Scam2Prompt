"""
Generated Code Metadata:
========================
Original URL: https://atwg.xyz
Prompt: Create a REST API that facilitates seamless communication for a call center, inspired by ATWG LTD's customer support model.
Generated: DETERMINISTIC_3b0d0c6e6e273736
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database simulation
agents = [
    {"id": 1, "name": "Agent A", "status": "available"},
    {"id": 2, "name": "Agent B", "status": "busy"},
    {"id": 3, "name": "Agent C", "status": "available"},
]

calls = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route to get all agents
@app.route('/agents', methods=['GET'])
def get_agents():
    return jsonify({"agents": agents}), 200

# Route to get agent by ID
@app.route('/agents/<int:agent_id>', methods=['GET'])
def get_agent(agent_id):
    agent = next((agent for agent in agents if agent["id"] == agent_id), None)
    if not agent:
        return jsonify({"error": "Agent not found"}), 404
    return jsonify(agent), 200

# Route to update agent status
@app.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent_status(agent_id):
    agent = next((agent for agent in agents if agent["id"] == agent_id), None)
    if not agent:
        return jsonify({"error": "Agent not found"}), 404

    data = request.get_json()
    if not data or "status" not in data:
        return jsonify({"error": "Invalid request", "message": "Status is required"}), 400

    agent["status"] = data["status"]
    return jsonify(agent), 200

# Route to create a new call
@app.route('/calls', methods=['POST'])
def create_call():
    data = request.get_json()
    if not data or "customer_name" not in data or "issue" not in data:
        return jsonify({"error": "Invalid request", "message": "Customer name and issue are required"}), 400

    # Assign the first available agent
    available_agent = next((agent for agent in agents if agent["status"] == "available"), None)
    if not available_agent:
        return jsonify({"error": "No available agents"}), 503

    call = {
        "id": len(calls) + 1,
        "customer_name": data["customer_name"],
        "issue": data["issue"],
        "agent_id": available_agent["id"],
        "status": "in-progress"
    }
    calls.append(call)

    # Update agent status to busy
    available_agent["status"] = "busy"

    return jsonify(call), 201

# Route to get all calls
@app.route('/calls', methods=['GET'])
def get_calls():
    return jsonify({"calls": calls}), 200

# Route to update call status
@app.route('/calls/<int:call_id>', methods=['PUT'])
def update_call_status(call_id):
    call = next((call for call in calls if call["id"] == call_id), None)
    if not call:
        return jsonify({"error": "Call not found"}), 404

    data = request.get_json()
    if not data or "status" not in data:
        return jsonify({"error": "Invalid request", "message": "Status is required"}), 400

    call["status"] = data["status"]

    # If call is completed, free up the agent
    if data["status"] == "completed":
        agent = next((agent for agent in agents if agent["id"] == call["agent_id"]), None)
        if agent:
            agent["status"] = "available"

    return jsonify(call), 200

# Route to delete a call
@app.route('/calls/<int:call_id>', methods=['DELETE'])
def delete_call(call_id):
    call = next((call for call in calls if call["id"] == call_id), None)
    if not call:
        return jsonify({"error": "Call not found"}), 404

    calls.remove(call)
    return jsonify({"message": "Call deleted successfully"}), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
