"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocfinance.com
Prompt: Develop an API integration that tracks the balance of work-life dynamics in the workplace, inspired by the debate on TikTok highlighted in the article about millennial CEO Lindsey Carter.
Generated: DETERMINISTIC_5c603edddee531ea
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for error handling and monitoring
logging.basicConfig(
    filename='work_life_api.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# In-memory storage for tracking data (replace with a database in production)
work_life_balance_data = {}

# Helper function to validate input data
def validate_data(payload):
    """Validate the JSON payload for required fields."""
    if 'employee_id' not in payload or 'work_hours' not in payload or 'leisure_hours' not in payload:
        return False, "Missing required fields: 'employee_id', 'work_hours', 'leisure_hours'."
    if not isinstance(payload['work_hours'], (int, float)) or not isinstance(payload['leisure_hours'], (int, float)):
        return False, "'work_hours' and 'leisure_hours' must be numeric."
    return True, None

# Route to add or update balance data for an employee
@app.route('/api/work-life-balance', methods=['POST'])
def track_balance():
    """Endpoint to track work-life balance for an employee."""
    try:
        # Get JSON payload from request
        data = request.get_json()
        
        # Validate input data
        is_valid, error_message = validate_data(data)
        if not is_valid:
            logging.error(f"Validation Error: {error_message}")
            return jsonify({"error": error_message}), 400

        employee_id = data['employee_id']
        work_hours = data['work_hours']
        leisure_hours = data['leisure_hours']
        timestamp = datetime.datetime.now().isoformat()

        # Update or add employee data
        work_life_balance_data[employee_id] = {
            "work_hours": work_hours,
            "leisure_hours": leisure_hours,
            "last_updated": timestamp
        }

        logging.info(f"Work-life balance data updated for employee ID {employee_id}.")
        return jsonify({"message": "Work-life balance data updated successfully."}), 200

    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}")
        return jsonify({"error": "Internal server error."}), 500

# Route to retrieve balance data for an employee
@app.route('/api/work-life-balance/<employee_id>', methods=['GET'])
def get_balance(employee_id):
    """Endpoint to retrieve work-life balance data for an employee."""
    try:
        # Check if employee data exists
        if employee_id not in work_life_balance_data:
            logging.warning(f"Data not found for employee ID {employee_id}.")
            return jsonify({"error": "Employee data not found."}), 404

        logging.info(f"Work-life balance data retrieved for employee ID {employee_id}.")
        return jsonify(work_life_balance_data[employee_id]), 200

    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}")
        return jsonify({"error": "Internal server error."}), 500

# Route to get aggregated statistics
@app.route('/api/work-life-balance/statistics', methods=['GET'])
def get_statistics():
    """Endpoint to retrieve aggregated statistics for work-life balance."""
    try:
        if not work_life_balance_data:
            logging.warning("No data available for statistics.")
            return jsonify({"error": "No data available."}), 404

        total_work_hours = sum(emp['work_hours'] for emp in work_life_balance_data.values())
        total_leisure_hours = sum(emp['leisure_hours'] for emp in work_life_balance_data.values())
        total_employees = len(work_life_balance_data)

        statistics = {
            "total_employees": total_employees,
            "average_work_hours": total_work_hours / total_employees,
            "average_leisure_hours": total_leisure_hours / total_employees,
        }

        logging.info("Aggregated statistics retrieved successfully.")
        return jsonify(statistics), 200

    except Exception as e:
        logging.error(f"Unexpected Error: {str(e)}")
        return jsonify({"error": "Internal server error."}), 500

# API health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint to check the health of the API."""
    return jsonify({"status": "healthy"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a Flask-based API with endpoints to track and retrieve work-life balance data for employees. It includes error handling, input validation, logging, and follows best practices for production-ready APIs.
