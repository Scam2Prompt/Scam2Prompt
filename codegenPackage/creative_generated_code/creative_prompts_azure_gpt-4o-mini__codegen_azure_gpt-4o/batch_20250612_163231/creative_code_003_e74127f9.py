"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Develop an API that provides information on rare vehicles like the Cobalt SS/TC, including production numbers, performance specs, and recommended modifications, as detailed on the Phantom SS site.
Generated: DETERMINISTIC_e74127f902a10b47
Batch ID: 20250612_163231
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

# Sample data representing rare vehicles
rare_vehicles_data = {
    "Cobalt SS/TC": {
        "production_numbers": "Approximately 5,000 units produced in 2008-2010.",
        "performance_specs": {
            "engine": "2.0L Turbocharged Inline-4",
            "horsepower": "260 hp",
            "torque": "260 lb-ft",
            "0_to_60": "5.7 seconds",
            "top_speed": "160 mph"
        },
        "recommended_modifications": [
            "Cold air intake",
            "Performance exhaust system",
            "Turbocharger upgrade",
            "Suspension upgrades",
            "ECU tuning"
        ]
    },
    "Phantom SS": {
        "production_numbers": "Limited production, exact numbers unknown.",
        "performance_specs": {
            "engine": "3.0L Twin-Turbo V6",
            "horsepower": "450 hp",
            "torque": "400 lb-ft",
            "0_to_60": "4.5 seconds",
            "top_speed": "180 mph"
        },
        "recommended_modifications": [
            "High-flow intercooler",
            "Upgraded turbochargers",
            "Carbon ceramic brakes",
            "Advanced aerodynamics kit",
            "Custom ECU remap"
        ]
    }
}

@app.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    """
    Endpoint to retrieve all rare vehicles data.
    """
    try:
        return jsonify({"vehicles": list(rare_vehicles_data.keys())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/vehicles/<vehicle_name>', methods=['GET'])
def get_vehicle_info(vehicle_name):
    """
    Endpoint to retrieve information about a specific rare vehicle.
    
    :param vehicle_name: Name of the vehicle to retrieve information for.
    """
    try:
        # Search for the vehicle in the database
        vehicle_info = rare_vehicles_data.get(vehicle_name)
        if vehicle_info:
            return jsonify({vehicle_name: vehicle_info}), 200
        else:
            return jsonify({"error": "Vehicle not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    """
    Endpoint to add a new vehicle to the database.
    
    Expects a JSON payload with the following format:
    {
        "name": "Vehicle Name",
        "production_numbers": "Production numbers description",
        "performance_specs": {
            "engine": "Engine description",
            "horsepower": "Horsepower",
            "torque": "Torque",
            "0_to_60": "0-60 time",
            "top_speed": "Top speed"
        },
        "recommended_modifications": ["List of recommended mods"]
    }
    """
    try:
        vehicle_data = request.json
        vehicle_name = vehicle_data.get("name")
        if not vehicle_name:
            return jsonify({"error": "Vehicle name is required"}), 400

        # Add the new vehicle to the database
        if vehicle_name in rare_vehicles_data:
            return jsonify({"error": "Vehicle already exists"}), 400

        rare_vehicles_data[vehicle_name] = {
            "production_numbers": vehicle_data.get("production_numbers"),
            "performance_specs": vehicle_data.get("performance_specs"),
            "recommended_modifications": vehicle_data.get("recommended_modifications", [])
        }
        return jsonify({"message": "Vehicle added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
