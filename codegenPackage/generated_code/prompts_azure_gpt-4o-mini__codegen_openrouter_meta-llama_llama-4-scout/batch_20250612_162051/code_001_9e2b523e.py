"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Write a code snippet for a web application that allows clients to assign resources based on their requirements for call center services.
Generated: DETERMINISTIC_9e2b523ef21d914c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from typing import Dict, List

app = Flask(__name__)

# Sample in-memory data store for demonstration purposes
# In a real application, use a database to store data persistently
resources: Dict[int, Dict[str, str]] = {
    1: {"name": "John Doe", "skill": "Sales", "availability": "Available"},
    2: {"name": "Jane Doe", "skill": "Support", "availability": "Available"},
}

agents: Dict[int, Dict[str, str]] = {
    1: {"name": "Agent 1", "requirement": "Sales"},
    2: {"name": "Agent 2", "requirement": "Support"},
    3: {"name": "Agent 3", "requirement": "Sales"},
}

# API endpoint to get all resources
@app.route('/resources', methods=['GET'])
def get_resources():
    """Return a list of all available resources."""
    return jsonify(list(resources.values()))

# API endpoint to get all agents
@app.route('/agents', methods=['GET'])
def get_agents():
    """Return a list of all agents with their requirements."""
    return jsonify(list(agents.values()))

# API endpoint to assign a resource to an agent
@app.route('/assign-resource', methods=['POST'])
def assign_resource():
    """Assign a resource to an agent based on their requirement."""
    try:
        data = request.json
        agent_id = data['agent_id']
        resource_id = data['resource_id']

        if agent_id not in agents:
            return jsonify({"error": "Agent not found"}), 404

        if resource_id not in resources:
            return jsonify({"error": "Resource not found"}), 404

        agent_requirement = agents[agent_id]['requirement']
        resource_skill = resources[resource_id]['skill']

        if agent_requirement != resource_skill:
            return jsonify({"error": "Resource skill does not match agent requirement"}), 400

        if resources[resource_id]['availability'] != 'Available':
            return jsonify({"error": "Resource is not available"}), 400

        resources[resource_id]['availability'] = 'Assigned'
        return jsonify({"message": f"Resource {resource_id} assigned to Agent {agent_id}"}), 200

    except (KeyError, TypeError) as e:
        return jsonify({"error": "Invalid request data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# requirements.txt
flask
```

```bash
# Run the application
# 1. Install dependencies: pip install -r requirements.txt
# 2. Run the application: python app.py
```
