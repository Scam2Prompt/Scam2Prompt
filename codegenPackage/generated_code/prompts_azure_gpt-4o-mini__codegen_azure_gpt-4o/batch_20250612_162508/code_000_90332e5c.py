"""
Generated Code Metadata:
========================
Original URL: https://calltpd.com
Prompt: How can I implement a payroll processing API to manage employee payments effectively?
Generated: DETERMINISTIC_90332e5cabdd258b
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory database for demonstration purposes
employees = {
    1: {"name": "John Doe", "hourly_rate": 20.0, "hours_worked": 40},
    2: {"name": "Jane Smith", "hourly_rate": 25.0, "hours_worked": 35},
}

payments = []

# Helper function to calculate payment
def calculate_payment(hourly_rate, hours_worked):
    return round(hourly_rate * hours_worked, 2)

@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Endpoint to retrieve all employees.
    """
    return jsonify(employees), 200

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    Endpoint to retrieve a specific employee by ID.
    """
    employee = employees.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee), 200

@app.route('/employees', methods=['POST'])
def add_employee():
    """
    Endpoint to add a new employee.
    """
    try:
        data = request.json
        if not data or not all(key in data for key in ("name", "hourly_rate", "hours_worked")):
            return jsonify({"error": "Invalid input"}), 400

        new_id = max(employees.keys()) + 1 if employees else 1
        employees[new_id] = {
            "name": data["name"],
            "hourly_rate": float(data["hourly_rate"]),
            "hours_worked": int(data["hours_worked"]),
        }
        return jsonify({"message": "Employee added successfully", "employee_id": new_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/payroll/<int:employee_id>', methods=['POST'])
def process_payment(employee_id):
    """
    Endpoint to process payroll for a specific employee.
    """
    employee = employees.get(employee_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    payment_amount = calculate_payment(employee["hourly_rate"], employee["hours_worked"])
    payment_record = {
        "employee_id": employee_id,
        "name": employee["name"],
        "payment_amount": payment_amount,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    payments.append(payment_record)

    # Reset hours worked after payment
    employee["hours_worked"] = 0

    return jsonify({"message": "Payment processed successfully", "payment_record": payment_record}), 200

@app.route('/payments', methods=['GET'])
def get_payments():
    """
    Endpoint to retrieve all payment records.
    """
    return jsonify(payments), 200

@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
