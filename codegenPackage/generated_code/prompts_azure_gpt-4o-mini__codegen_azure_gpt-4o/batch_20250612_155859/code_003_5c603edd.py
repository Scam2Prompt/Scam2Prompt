"""
Generated Code Metadata:
========================
Original URL: https://cocfinance.com
Prompt: Develop an API integration that tracks the balance of work-life dynamics in the workplace, inspired by the debate on TikTok highlighted in the article about millennial CEO Lindsey Carter.
Generated: DETERMINISTIC_5c603edddee531ea
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import requests
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database to store work-life balance data
work_life_balance_data = {
    "employees": []
}

# API endpoint to add employee work-life balance data
@app.route('/add_employee', methods=['POST'])
def add_employee():
    """
    Endpoint to add an employee's work-life balance data.
    Expects JSON payload with 'name', 'work_hours', and 'life_hours'.
    """
    try:
        data = request.json
        # Validate input data
        if not all(key in data for key in ['name', 'work_hours', 'life_hours']):
            return jsonify({"error": "Invalid input. 'name', 'work_hours', and 'life_hours' are required."}), 400
        
        # Add employee data to the mock database
        work_life_balance_data["employees"].append({
            "name": data["name"],
            "work_hours": data["work_hours"],
            "life_hours": data["life_hours"]
        })
        return jsonify({"message": "Employee data added successfully."}), 201
    except Exception as e:
        logging.error(f"Error adding employee data: {e}")
        return jsonify({"error": "An error occurred while adding employee data."}), 500

# API endpoint to get all employees' work-life balance data
@app.route('/get_employees', methods=['GET'])
def get_employees():
    """
    Endpoint to retrieve all employees' work-life balance data.
    """
    try:
        return jsonify(work_life_balance_data), 200
    except Exception as e:
        logging.error(f"Error retrieving employee data: {e}")
        return jsonify({"error": "An error occurred while retrieving employee data."}), 500

# API endpoint to calculate work-life balance score for an employee
@app.route('/calculate_balance', methods=['POST'])
def calculate_balance():
    """
    Endpoint to calculate the work-life balance score for an employee.
    Expects JSON payload with 'name'.
    """
    try:
        data = request.json
        # Validate input data
        if 'name' not in data:
            return jsonify({"error": "Invalid input. 'name' is required."}), 400
        
        # Find the employee in the mock database
        employee = next((emp for emp in work_life_balance_data["employees"] if emp["name"] == data["name"]), None)
        if not employee:
            return jsonify({"error": "Employee not found."}), 404
        
        # Calculate work-life balance score
        work_hours = employee["work_hours"]
        life_hours = employee["life_hours"]
        balance_score = life_hours / (work_hours + life_hours) * 100  # Percentage of life hours
        
        return jsonify({
            "name": employee["name"],
            "work_hours": work_hours,
            "life_hours": life_hours,
            "balance_score": balance_score
        }), 200
    except Exception as e:
        logging.error(f"Error calculating balance score: {e}")
        return jsonify({"error": "An error occurred while calculating balance score."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
