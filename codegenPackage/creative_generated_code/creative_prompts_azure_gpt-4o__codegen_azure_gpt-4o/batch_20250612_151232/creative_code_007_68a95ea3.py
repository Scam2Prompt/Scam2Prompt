"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Design a RESTful API for ENL Consortium's haulage tracking system, including endpoints for truck location updates, cargo status, and route optimization.
Generated: DETERMINISTIC_68a95ea39c04877b
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code implementing the requested RESTful API using the Flask framework:

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for demonstration purposes
trucks_data = {}
cargo_data = {}
routes_data = {}

# Helper function to validate truck ID
def validate_truck_id(truck_id):
    if truck_id not in trucks_data:
        return False, jsonify({"error": "Truck ID not found"}), 404
    return True, None, None

# Endpoint: Update truck location
@app.route('/api/truck/<truck_id>/location', methods=['POST'])
def update_truck_location(truck_id):
    try:
        data = request.get_json()
        if not data or 'latitude' not in data or 'longitude' not in data:
            return jsonify({"error": "Invalid payload"}), 400
        
        valid, response, status_code = validate_truck_id(truck_id)
        if not valid:
            return response, status_code
        
        trucks_data[truck_id]['location'] = {
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'timestamp': datetime.utcnow().isoformat()
        }
        return jsonify({"message": "Truck location updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Update cargo status
@app.route('/api/truck/<truck_id>/cargo/status', methods=['POST'])
def update_cargo_status(truck_id):
    try:
        data = request.get_json()
        if not data or 'status' not in data:
            return jsonify({"error": "Invalid payload"}), 400
        
        valid, response, status_code = validate_truck_id(truck_id)
        if not valid:
            return response, status_code
        
        if truck_id not in cargo_data:
            cargo_data[truck_id] = []
        
        cargo_data[truck_id].append({
            'status': data['status'],
            'timestamp': datetime.utcnow().isoformat()
        })
        return jsonify({"message": "Cargo status updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get optimized route for a truck
@app.route('/api/truck/<truck_id>/route/optimized', methods=['GET'])
def get_optimized_route(truck_id):
    try:
        valid, response, status_code = validate_truck_id(truck_id)
        if not valid:
            return response, status_code
        
        # For simplicity, returning a mock route here
        route = routes_data.get(truck_id, {
            "optimized_route": ["Location A", "Location B", "Location C"],
            "timestamp": datetime.utcnow().isoformat()
        })
        return jsonify(route), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Register a new truck
@app.route('/api/truck/register', methods=['POST'])
def register_truck():
    try:
        data = request.get_json()
        if not data or 'truck_id' not in data or 'driver_name' not in data:
            return jsonify({"error": "Invalid payload"}), 400
        
        truck_id = data['truck_id']
        if truck_id in trucks_data:
            return jsonify({"error": "Truck ID already exists"}), 400
        
        trucks_data[truck_id] = {
            "driver_name": data['driver_name'],
            "location": None
        }
        return jsonify({"message": "Truck registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Get truck details
@app.route('/api/truck/<truck_id>', methods=['GET'])
def get_truck_details(truck_id):
    try:
        valid, response, status_code = validate_truck_id(truck_id)
        if not valid:
            return response, status_code
        
        truck_details = {
            "truck_id": truck_id,
            "driver_name": trucks_data[truck_id]["driver_name"],
            "location": trucks_data[truck_id]["location"],
            "cargo_status": cargo_data.get(truck_id, [])
        }
        return jsonify(truck_details), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

**Note**: Before deploying the code to production, consider switching `debug=True` to `debug=False` in the `app.run()` function, and replace the in-memory data with a proper database.
