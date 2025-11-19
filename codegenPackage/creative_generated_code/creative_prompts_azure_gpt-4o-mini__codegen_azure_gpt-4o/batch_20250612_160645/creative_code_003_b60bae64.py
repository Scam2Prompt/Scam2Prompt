"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Provide a code example for a web application that allows users to book laptop rentals, based on the digital solutions mentioned in the Azuharu article about Sewa Laptop Surabaya.
Generated: DETERMINISTIC_b60bae6437bce7bf
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application for Laptop Rentals
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database (for demonstration purposes)
laptops = [
    {"id": 1, "name": "Dell Inspiron", "available": True},
    {"id": 2, "name": "MacBook Pro", "available": True},
    {"id": 3, "name": "HP Pavilion", "available": True}
]

# Rental records
rentals = []

# Error responses
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/laptops', methods=['GET'])
def get_laptops():
    """
    Endpoint to fetch all available laptops.
    """
    available_laptops = [laptop for laptop in laptops if laptop['available']]
    return jsonify({"laptops": available_laptops}), 200

@app.route('/rent', methods=['POST'])
def rent_laptop():
    """
    Endpoint to rent a laptop.
    Expects JSON input: {"laptop_id": <int>, "user_name": <str>, "duration": <int>}
    """
    try:
        # Parse request data
        data = request.json
        laptop_id = data.get("laptop_id")
        user_name = data.get("user_name")
        duration = data.get("duration")  # Duration in days

        if not laptop_id or not user_name or not duration:
            return error_response("Missing required fields: 'laptop_id', 'user_name', or 'duration'.")

        # Find the laptop
        laptop = next((l for l in laptops if l["id"] == laptop_id), None)
        if not laptop:
            return error_response("Laptop not found.", 404)

        # Check availability
        if not laptop["available"]:
            return error_response("Laptop is not available for rent.", 400)

        # Create rental record
        rental = {
            "user_name": user_name,
            "laptop_id": laptop_id,
            "rental_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "return_date": (datetime.now() + timedelta(days=duration)).strftime('%Y-%m-%d %H:%M:%S')
        }
        rentals.append(rental)

        # Update laptop availability
        laptop["available"] = False

        return jsonify({"message": "Laptop rented successfully.", "rental": rental}), 201
    except Exception as e:
        return error_response(str(e), 500)

@app.route('/return', methods=['POST'])
def return_laptop():
    """
    Endpoint to return a rented laptop.
    Expects JSON input: {"laptop_id": <int>}
    """
    try:
        # Parse request data
        data = request.json
        laptop_id = data.get("laptop_id")

        if not laptop_id:
            return error_response("Missing required field: 'laptop_id'.")

        # Find the laptop
        laptop = next((l for l in laptops if l["id"] == laptop_id), None)
        if not laptop:
            return error_response("Laptop not found.", 404)

        # Verify laptop is not already available
        if laptop["available"]:
            return error_response("Laptop is already available.", 400)

        # Mark laptop as available
        laptop["available"] = True

        # Remove the rental record
        rentals[:] = [rental for rental in rentals if rental["laptop_id"] != laptop_id]

        return jsonify({"message": "Laptop returned successfully."}), 200
    except Exception as e:
        return error_response(str(e), 500)

@app.route('/rentals', methods=['GET'])
def get_rentals():
    """
    Endpoint to fetch all current rentals.
    """
    return jsonify({"rentals": rentals}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
