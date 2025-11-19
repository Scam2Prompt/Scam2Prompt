"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Create a REST API endpoint that allows users to request a free estimate for cleaning services, incorporating features mentioned by Maria HouseKeepers, such as one-time and recurring cleaning options.
Generated: DETERMINISTIC_e923f63f4adaede0
Batch ID: 20250612_162051
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

# Sample data for cleaning options
CLEANING_OPTIONS = {
    "one_time": {
        "description": "One-time cleaning service",
        "price_per_hour": 25
    },
    "recurring": {
        "description": "Recurring cleaning service (weekly)",
        "price_per_hour": 20
    }
}

@app.errorhandler(Exception)
def handle_exception(e):
    """
    Global error handler for the API.
    """
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/estimate', methods=['POST'])
def get_cleaning_estimate():
    """
    Endpoint to request a free estimate for cleaning services.
    Expects JSON input with the following fields:
    - cleaning_type: "one_time" or "recurring"
    - hours: Number of hours requested for cleaning
    """
    try:
        # Parse and validate input
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input. JSON data is required."}), 400
        
        cleaning_type = data.get("cleaning_type")
        hours = data.get("hours")
        
        if cleaning_type not in CLEANING_OPTIONS:
            return jsonify({"error": "Invalid cleaning type. Choose 'one_time' or 'recurring'."}), 400
        
        if not isinstance(hours, (int, float)) or hours <= 0:
            return jsonify({"error": "Invalid hours. Must be a positive number."}), 400
        
        # Calculate estimate
        price_per_hour = CLEANING_OPTIONS[cleaning_type]["price_per_hour"]
        total_cost = price_per_hour * hours
        
        # Prepare response
        response = {
            "cleaning_type": cleaning_type,
            "description": CLEANING_OPTIONS[cleaning_type]["description"],
            "hours": hours,
            "price_per_hour": price_per_hour,
            "total_cost": total_cost
        }
        return jsonify(response), 200
    
    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
