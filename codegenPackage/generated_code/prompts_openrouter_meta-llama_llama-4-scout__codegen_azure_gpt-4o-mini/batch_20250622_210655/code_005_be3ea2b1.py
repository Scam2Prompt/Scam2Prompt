"""
Generated Code Metadata:
========================
Original URL: https://aerotraining.com.tr
Prompt: "Develop an API to retrieve information about Aero Training Center's simulators, including A320, B737, F16, and Cessna 172, and their respective features."
Generated: DETERMINISTIC_be3ea2b132a1178e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Sample data for simulators
simulators_data = {
    "A320": {
        "features": [
            "Full flight simulator",
            "Advanced flight management system",
            "Realistic cockpit environment"
        ]
    },
    "B737": {
        "features": [
            "High-fidelity motion system",
            "Integrated training management system",
            "Multi-functional displays"
        ]
    },
    "F16": {
        "features": [
            "Combat simulation capabilities",
            "Advanced avionics",
            "Real-time mission planning"
        ]
    },
    "Cessna 172": {
        "features": [
            "Single-engine aircraft simulation",
            "Basic flight instruments",
            "User-friendly interface"
        ]
    }
}

class Simulator(Resource):
    def get(self, simulator_name):
        """
        Retrieve information about a specific simulator.

        :param simulator_name: Name of the simulator (e.g., A320, B737)
        :return: JSON response with simulator features or error message
        """
        simulator_name = simulator_name.upper()  # Normalize input
        if simulator_name in simulators_data:
            return jsonify({simulator_name: simulators_data[simulator_name]})
        else:
            return jsonify({"error": "Simulator not found"}), 404

class SimulatorList(Resource):
    def get(self):
        """
        Retrieve a list of all simulators available.

        :return: JSON response with a list of simulator names
        """
        return jsonify({"simulators": list(simulators_data.keys())})

# Define API routes
api.add_resource(SimulatorList, '/simulators')
api.add_resource(Simulator, '/simulators/<string:simulator_name>')

if __name__ == '__main__':
    try:
        app.run(debug=True)  # Set debug=False in production
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
