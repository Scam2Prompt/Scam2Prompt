"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Suggest an API for managing employee appreciation programs, referencing PDC Brush's initiative to celebrate staff contributions with gifts.
Generated: DETERMINISTIC_941dd470b9e7c773
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py - Flask application for managing employee appreciation programs

from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory database simulation
# In production, this should be replaced with a real database
employees = {
    1: {"name": "Alice", "contributions": ["Designed new product logo"], "gifts": []},
    2: {"name": "Bob", "contributions": ["Implemented new feature"], "gifts": []},
}

gifts_catalogue = {
    "gift_card": "Amazon Gift Card",
    "bonus": "Performance Bonus",
    "holiday_voucher": "Holiday Travel Voucher",
}

# Error handling for missing or invalid data
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Endpoint to list employees
@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Fetch details of all employees
    """
    return jsonify(employees), 200

# Endpoint to get specific employee details
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    Fetch details of a specific employee by ID
    """
    employee = employees.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee), 200

# Endpoint to add employee contributions
@app.route('/employees/<int:employee_id>/contributions', methods=['POST'])
def add_contribution(employee_id):
    """
    Add a new contribution for an employee
    """
    employee = employees.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.json
    contribution = data.get('contribution')
    if not contribution:
        return jsonify({"error": "Contribution is required"}), 400

    employee['contributions'].append(contribution)
    return jsonify({"message": "Contribution added successfully", "employee": employee}), 201

# Endpoint to assign a gift to an employee
@app.route('/employees/<int:employee_id>/gifts', methods=['POST'])
def assign_gift(employee_id):
    """
    Assign a gift from the catalogue to an employee
    """
    employee = employees.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.json
    gift_key = data.get('gift_key')
    if gift_key not in gifts_catalogue:
        return jsonify({"error": "Invalid gift key"}), 400

    gift_details = {
        "gift": gifts_catalogue[gift_key],
        "date_awarded": datetime.datetime.utcnow().isoformat()
    }
    employee['gifts'].append(gift_details)
    return jsonify({"message": "Gift assigned successfully", "employee": employee}), 201

# Endpoint to list available gifts
@app.route('/gifts', methods=['GET'])
def list_gifts():
    """
    Fetch the list of available gifts
    """
    return jsonify(gifts_catalogue), 200

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```

Note:
- This implementation uses Flask as the web framework.
- Replace the in-memory database with a persistent database (e.g., MySQL, PostgreSQL) for production use.
- Secure inputs and endpoints to prevent injection attacks in production environments.
