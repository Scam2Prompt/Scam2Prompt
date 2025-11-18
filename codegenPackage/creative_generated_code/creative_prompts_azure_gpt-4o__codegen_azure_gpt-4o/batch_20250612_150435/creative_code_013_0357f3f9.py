"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Write code to implement a loyalty program API that enables gas stations to customize discounts and rewards for customers using CRUDO tokens.
Generated: DETERMINISTIC_0357f3f902357b01
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for simplicity (replace with a database in production)
gas_stations = {}
customers = {}
loyalty_programs = {}

# Custom Exception for Resource Not Found
class ResourceNotFound(Exception):
    pass

# Error Handlers
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": str(e)}).data
    response.content_type = "application/json"
    return response, e.code

@app.errorhandler(ResourceNotFound)
def handle_resource_not_found(e):
    return jsonify({"error": str(e)}), 404

@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "An unexpected error occurred."}), 500

# Routes for Gas Stations
@app.route('/gas_stations', methods=['POST'])
def create_gas_station():
    """Add a new gas station."""
    data = request.json
    station_id = data.get('station_id')
    if not station_id or station_id in gas_stations:
        return jsonify({"error": "Invalid or duplicate station_id"}), 400
    
    gas_stations[station_id] = {
        "name": data.get("name"),
        "location": data.get("location"),
        "loyalty_program_id": None
    }
    return jsonify({"message": "Gas station added successfully", "station_id": station_id}), 201

@app.route('/gas_stations/<station_id>', methods=['GET'])
def get_gas_station(station_id):
    """Retrieve details of a gas station."""
    if station_id not in gas_stations:
        raise ResourceNotFound(f"Gas station with id {station_id} not found.")
    return jsonify(gas_stations[station_id]), 200

# Routes for Loyalty Programs
@app.route('/loyalty_programs', methods=['POST'])
def create_loyalty_program():
    """Create a loyalty program."""
    data = request.json
    program_id = data.get('program_id')
    if not program_id or program_id in loyalty_programs:
        return jsonify({"error": "Invalid or duplicate program_id"}), 400
    
    loyalty_programs[program_id] = {
        "name": data.get("name"),
        "discount_percentage": data.get("discount_percentage", 0),
        "reward_points": data.get("reward_points", 0)
    }
    return jsonify({"message": "Loyalty program created successfully", "program_id": program_id}), 201

@app.route('/loyalty_programs/<program_id>', methods=['GET'])
def get_loyalty_program(program_id):
    """Retrieve details of a loyalty program."""
    if program_id not in loyalty_programs:
        raise ResourceNotFound(f"Loyalty program with id {program_id} not found.")
    return jsonify(loyalty_programs[program_id]), 200

@app.route('/gas_stations/<station_id>/assign_loyalty_program', methods=['PUT'])
def assign_loyalty_program_to_station(station_id):
    """Assign a loyalty program to a gas station."""
    data = request.json
    program_id = data.get('program_id')
    if station_id not in gas_stations:
        raise ResourceNotFound(f"Gas station with id {station_id} not found.")
    if program_id not in loyalty_programs:
        raise ResourceNotFound(f"Loyalty program with id {program_id} not found.")
    
    gas_stations[station_id]["loyalty_program_id"] = program_id
    return jsonify({"message": f"Loyalty program {program_id} assigned to gas station {station_id}"}), 200

# Routes for Customers
@app.route('/customers', methods=['POST'])
def create_customer():
    """Register a new customer."""
    data = request.json
    customer_id = data.get('customer_id')
    if not customer_id or customer_id in customers:
        return jsonify({"error": "Invalid or duplicate customer_id"}), 400
    
    customers[customer_id] = {
        "name": data.get("name"),
        "crudo_tokens": data.get("crudo_tokens", 0),
        "loyalty_rewards": 0
    }
    return jsonify({"message": "Customer added successfully", "customer_id": customer_id}), 201

@app.route('/customers/<customer_id>/redeem_rewards', methods=['POST'])
def redeem_rewards(customer_id):
    """Allow customers to redeem rewards using CRUDO tokens."""
    data = request.json
    station_id = data.get('station_id')
    if customer_id not in customers:
        raise ResourceNotFound(f"Customer with id {customer_id} not found.")
    if station_id not in gas_stations:
        raise ResourceNotFound(f"Gas station with id {station_id} not found.")
    
    customer = customers[customer_id]
    gas_station = gas_stations[station_id]
    program_id = gas_station["loyalty_program_id"]

    if not program_id:
        return jsonify({"error": "No loyalty program assigned to this gas station"}), 400
    
    loyalty_program = loyalty_programs[program_id]
    required_tokens = loyalty_program["reward_points"]
    
    if customer["crudo_tokens"] < required_tokens:
        return jsonify({"error": "Insufficient CRUDO tokens"}), 400
    
    customer["crudo_tokens"] -= required_tokens
    customer["loyalty_rewards"] += 1
    return jsonify({
        "message": "Rewards redeemed successfully",
        "remaining_tokens": customer["crudo_tokens"],
        "total_rewards": customer["loyalty_rewards"]
    }), 200

# Application Entry Point
if __name__ == '__main__':
    app.run(debug=True)
```
