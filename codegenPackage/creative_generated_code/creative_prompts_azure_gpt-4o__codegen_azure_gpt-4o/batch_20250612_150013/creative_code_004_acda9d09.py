"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyatoken.net
Prompt: Suggest an API for booking luxury travel packages and managing incentive programs for companies, inspired by the offerings on nyatoken.net.
Generated: DETERMINISTIC_acda9d0917096d98
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for travel packages and incentive programs
travel_packages = []
incentive_programs = []
bookings = []

# Helper function to generate unique IDs
def generate_id(prefix):
    return f"{prefix}_{int(datetime.utcnow().timestamp() * 1000)}"

# Route: Add a luxury travel package
@app.route('/api/travel-packages', methods=['POST'])
def add_travel_package():
    try:
        data = request.json
        package_id = generate_id("package")
        new_package = {
            "id": package_id,
            "name": data.get("name"),
            "description": data.get("description"),
            "price": data.get("price"),
            "availability": data.get("availability")
        }
        travel_packages.append(new_package)
        return jsonify({"message": "Travel package added successfully", "package_id": package_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Get all travel packages
@app.route('/api/travel-packages', methods=['GET'])
def get_travel_packages():
    return jsonify({"travel_packages": travel_packages}), 200

# Route: Book a travel package
@app.route('/api/bookings', methods=['POST'])
def book_travel_package():
    try:
        data = request.json
        package_id = data.get("package_id")
        customer_name = data.get("customer_name")
        
        # Verify package exists
        package = next((p for p in travel_packages if p["id"] == package_id), None)
        if not package:
            return jsonify({"error": "Travel package not found"}), 404
        
        # Create booking
        booking_id = generate_id("booking")
        booking = {
            "id": booking_id,
            "package_id": package_id,
            "customer_name": customer_name,
            "date": datetime.utcnow().isoformat()
        }
        bookings.append(booking)
        return jsonify({"message": "Booking completed successfully", "booking_id": booking_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Add an incentive program
@app.route('/api/incentive-programs', methods=['POST'])
def add_incentive_program():
    try:
        data = request.json
        program_id = generate_id("program")
        new_program = {
            "id": program_id,
            "name": data.get("name"),
            "description": data.get("description"),
            "reward": data.get("reward")
        }
        incentive_programs.append(new_program)
        return jsonify({"message": "Incentive program added successfully", "program_id": program_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Get all incentive programs
@app.route('/api/incentive-programs', methods=['GET'])
def get_incentive_programs():
    return jsonify({"incentive_programs": incentive_programs}), 200

# Route: Assign an incentive program to a company
@app.route('/api/assign-incentive', methods=['POST'])
def assign_incentive():
    try:
        data = request.json
        program_id = data.get("program_id")
        company_name = data.get("company_name")
        
        # Verify program exists
        program = next((p for p in incentive_programs if p["id"] == program_id), None)
        if not program:
            return jsonify({"error": "Incentive program not found"}), 404
        
        assignment_id = generate_id("assignment")
        assignment = {
            "id": assignment_id,
            "program_id": program_id,
            "company_name": company_name,
            "date": datetime.utcnow().isoformat()
        }
        return jsonify({"message": "Incentive program assigned successfully", "assignment_id": assignment_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Error handling for 404 - Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
