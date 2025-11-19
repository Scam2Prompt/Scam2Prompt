"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: How can I implement a car rental API for different vehicle models like Innova and Tempo Traveler as offered by Balaji Tours and Travels?
Generated: DETERMINISTIC_061250f7f0cf3c6c
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory database simulation
vehicles = [
    {"id": 1, "model": "Innova", "availability": True, "price_per_day": 1500},
    {"id": 2, "model": "Tempo Traveler", "availability": True, "price_per_day": 3000},
]

# Rentals information
rentals = []

# Endpoint: Get available vehicles
@app.route('/vehicles', methods=['GET'])
def get_available_vehicles():
    """
    Fetch all available vehicles for rental.
    """
    available_vehicles = [vehicle for vehicle in vehicles if vehicle["availability"]]
    return jsonify({"vehicles": available_vehicles})

# Endpoint: Rent a vehicle
@app.route('/rent', methods=['POST'])
def rent_vehicle():
    """
    Rent a vehicle based on provided vehicle ID and rental details.
    """
    try:
        data = request.json
        vehicle_id = data.get('vehicle_id')
        customer_name = data.get('customer_name')
        rental_days = data.get('rental_days')

        # Validate inputs
        if not vehicle_id or not customer_name or not rental_days:
            return jsonify({"error": "Missing required fields"}), 400

        # Find the vehicle
        vehicle = next((v for v in vehicles if v["id"] == vehicle_id and v["availability"]), None)
        if not vehicle:
            return jsonify({"error": "Vehicle not available"}), 404

        # Calculate total price
        total_price = vehicle["price_per_day"] * rental_days

        # Mark the vehicle as unavailable
        vehicle["availability"] = False

        # Save rental record
        rental_record = {
            "rental_id": len(rentals) + 1,
            "vehicle_id": vehicle_id,
            "customer_name": customer_name,
            "rental_days": rental_days,
            "total_price": total_price,
            "rental_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        rentals.append(rental_record)

        return jsonify({"message": "Vehicle rented successfully", "rental_details": rental_record}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Return a vehicle
@app.route('/return', methods=['POST'])
def return_vehicle():
    """
    Return a rented vehicle based on rental ID.
    """
    try:
        data = request.json
        rental_id = data.get('rental_id')

        # Validate input
        if not rental_id:
            return jsonify({"error": "Missing rental_id"}), 400

        # Find rental record
        rental_record = next((r for r in rentals if r["rental_id"] == rental_id), None)
        if not rental_record:
            return jsonify({"error": "Rental record not found"}), 404

        # Find the vehicle and mark it as available
        vehicle = next((v for v in vehicles if v["id"] == rental_record["vehicle_id"]), None)
        if vehicle:
            vehicle["availability"] = True

        # Remove rental record
        rentals.remove(rental_record)

        return jsonify({"message": "Vehicle returned successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: View rental history
@app.route('/rentals', methods=['GET'])
def get_rental_history():
    """
    Fetch all rental history records.
    """
    return jsonify({"rentals": rentals})

# Application startup
if __name__ == '__main__':
    app.run(debug=True)
```
