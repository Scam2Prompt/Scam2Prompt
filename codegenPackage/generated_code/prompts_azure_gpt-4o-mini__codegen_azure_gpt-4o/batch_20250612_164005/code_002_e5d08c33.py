"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Create a REST API endpoint that allows for the management of independent contractor transitions to full-time employees, inspired by Connext's offerings.
Generated: DETERMINISTIC_e5d08c33cdcd9685
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
employees = []

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

@app.route('/contractor-to-fulltime', methods=['POST'])
def transition_contractor_to_fulltime():
    """
    Endpoint to transition a contractor to a full-time employee.
    Expects a JSON payload with contractor details.
    """
    try:
        # Parse the request data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Bad Request", "message": "Request body must be JSON"}), 400

        # Validate required fields
        required_fields = ['contractor_id', 'name', 'position', 'salary']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": "Bad Request", "message": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Check if contractor already exists in the database
        contractor_id = data['contractor_id']
        existing_employee = next((emp for emp in employees if emp['contractor_id'] == contractor_id), None)
        if existing_employee:
            return jsonify({"error": "Conflict", "message": "Contractor has already been transitioned to full-time"}), 409

        # Add contractor as a full-time employee
        new_employee = {
            "contractor_id": data['contractor_id'],
            "name": data['name'],
            "position": data['position'],
            "salary": data['salary'],
            "status": "full-time"
        }
        employees.append(new_employee)

        return jsonify({"message": "Contractor successfully transitioned to full-time", "employee": new_employee}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Endpoint to retrieve all employees.
    """
    return jsonify({"employees": employees}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
