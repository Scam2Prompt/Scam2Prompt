"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teleperformance-amplifai.com
Prompt: Generate a REST API endpoint for retrieving employee engagement data, inspired by AmplifAI's platform capabilities.
Generated: DETERMINISTIC_9cea2f013c372b88
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Mock data representing employee engagement metrics
# Normally, this data would come from a database or external service
employee_engagement_data = [
    {"employee_id": 1, "name": "Alice", "engagement_score": 89, "last_updated": "2023-10-11"},
    {"employee_id": 2, "name": "Bob", "engagement_score": 76, "last_updated": "2023-10-12"},
    {"employee_id": 3, "name": "Charlie", "engagement_score": 95, "last_updated": "2023-10-13"},
]

@app.route('/api/employee-engagement', methods=['GET'])
def get_employee_engagement():
    """
    REST API endpoint to retrieve employee engagement data.

    Query Parameters:
    - employee_id (optional): Filter results by specific employee ID.

    Returns:
        JSON response containing engagement data.
    """
    try:
        employee_id = request.args.get('employee_id')  # Retrieve employee_id from query parameters
        if employee_id:
            # Filter data by employee_id, return a single record if it exists
            filtered_data = [
                employee for employee in employee_engagement_data
                if employee['employee_id'] == int(employee_id)
            ]
            if not filtered_data:
                return jsonify({"error": "Employee not found"}), 404
            return jsonify(filtered_data[0]), 200
        
        # Return all employee engagement data if no employee_id is provided
        return jsonify(employee_engagement_data), 200
    except ValueError:
        # Handle invalid employee_id format (e.g., non-integer values)
        logging.error("Invalid employee_id format provided")
        return jsonify({"error": "Invalid employee_id format"}), 400
    except Exception as e:
        # Catch-all for unexpected errors
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

# Run the Flask application (for development purposes)
if __name__ == '__main__':
    app.run(debug=True)
```
