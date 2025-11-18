"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polystack.tech
Prompt: Write code to simulate a cyber range environment for training and testing cybersecurity scenarios, inspired by Polystack Technologies' offerings.
Generated: DETERMINISTIC_e8f219f630d5e53f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a class to represent a Cyber Range Environment
class CyberRange:
    def __init__(self):
        self.scenarios = []
        self.active_scenarios = {}

    def create_scenario(self, name, description):
        """Create a new cybersecurity scenario."""
        scenario_id = self.generate_id()
        scenario = {
            "id": scenario_id,
            "name": name,
            "description": description,
            "status": "inactive"
        }
        self.scenarios.append(scenario)
        return scenario

    def start_scenario(self, scenario_id):
        """Start a specific scenario by its ID."""
        scenario = self.find_scenario(scenario_id)
        if scenario and scenario['status'] == 'inactive':
            scenario['status'] = 'active'
            self.active_scenarios[scenario_id] = scenario
            return scenario
        raise ValueError("Scenario is either active or does not exist.")

    def stop_scenario(self, scenario_id):
        """Stop a specific scenario by its ID."""
        if scenario_id in self.active_scenarios:
            scenario = self.active_scenarios[scenario_id]
            scenario['status'] = 'inactive'
            del self.active_scenarios[scenario_id]
            return scenario
        raise ValueError("Scenario not found in active scenarios.")

    def list_scenarios(self):
        """List all scenarios."""
        return self.scenarios

    def find_scenario(self, scenario_id):
        """Find a scenario by its ID."""
        return next((s for s in self.scenarios if s['id'] == scenario_id), None)

    @staticmethod
    def generate_id(length=8):
        """Generate a unique identifier for scenarios."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Initialize the cyber range environment
cyber_range = CyberRange()


@app.route('/scenarios', methods=['POST'])
def create_scenario():
    """Create a new cybersecurity training scenario."""
    data = request.json
    name = data.get('name')
    description = data.get('description')
    
    if not name or not description:
        return jsonify({"error": "Name and description are required."}), 400

    scenario = cyber_range.create_scenario(name, description)
    return jsonify(scenario), 201


@app.route('/scenarios/<scenario_id>/start', methods=['POST'])
def start_scenario(scenario_id):
    """Start a specified scenario."""
    try:
        scenario = cyber_range.start_scenario(scenario_id)
        return jsonify(scenario), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@app.route('/scenarios/<scenario_id>/stop', methods=['POST'])
def stop_scenario(scenario_id):
    """Stop a specified scenario."""
    try:
        scenario = cyber_range.stop_scenario(scenario_id)
        return jsonify(scenario), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@app.route('/scenarios', methods=['GET'])
def list_scenarios():
    """List all available scenarios."""
    return jsonify(cyber_range.list_scenarios()), 200


if __name__ == '__main__':
    # Ensure the environment is ready
    if not os.path.exists('cyber_range_data'):
        os.makedirs('cyber_range_data')
    
    app.run(debug=True)  # Set debug to False in production
```
