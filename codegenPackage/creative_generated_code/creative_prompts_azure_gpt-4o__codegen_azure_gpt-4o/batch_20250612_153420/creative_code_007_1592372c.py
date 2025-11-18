"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fusionjiujitsu.com.br
Prompt: Using Flask, create an API endpoint that retrieves and serves data about the Fusion Jiu Jitsu School's class schedules and pricing plans.
Generated: DETERMINISTIC_1592372c221f806d
Batch ID: 20250612_153420
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

app = Flask(__name__)

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO)

# Mock data for Fusion Jiu Jitsu School
class_schedules = [
    {"day": "Monday", "time": "6:00 PM - 7:30 PM", "class": "Beginner"},
    {"day": "Tuesday", "time": "6:00 PM - 7:30 PM", "class": "Intermediate"},
    {"day": "Wednesday", "time": "6:00 PM - 7:30 PM", "class": "Advanced"},
    {"day": "Thursday", "time": "6:00 PM - 7:30 PM", "class": "Open Mat"},
    {"day": "Friday", "time": "6:00 PM - 7:30 PM", "class": "Beginner"},
    {"day": "Saturday", "time": "10:00 AM - 12:00 PM", "class": "All Levels"},
]

pricing_plans = [
    {"plan": "Monthly", "price": 100, "description": "Unlimited classes for one month."},
    {"plan": "Drop-In", "price": 15, "description": "Single class session."},
    {"plan": "Yearly", "price": 1000, "description": "Unlimited classes for one year."},
]

@app.route('/fusion-jiu-jitsu/class-schedules', methods=['GET'])
def get_class_schedules():
    """
    Endpoint to retrieve class schedules for Fusion Jiu Jitsu School.
    Returns a JSON response containing all class schedules.
    """
    try:
        # Return class schedules as JSON
        return jsonify({"success": True, "data": class_schedules}), 200
    except Exception as e:
        # Log error and return failure response
        logging.error(f"Error retrieving class schedules: {e}")
        return jsonify({"success": False, "error": "Unable to retrieve class schedules"}), 500


@app.route('/fusion-jiu-jitsu/pricing-plans', methods=['GET'])
def get_pricing_plans():
    """
    Endpoint to retrieve pricing plans for Fusion Jiu Jitsu School.
    Returns a JSON response containing all pricing plans.
    """
    try:
        # Return pricing plans as JSON
        return jsonify({"success": True, "data": pricing_plans}), 200
    except Exception as e:
        # Log error and return failure response
        logging.error(f"Error retrieving pricing plans: {e}")
        return jsonify({"success": False, "error": "Unable to retrieve pricing plans"}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors (route not found).
    """
    return jsonify({"success": False, "error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors (internal server error).
    """
    return jsonify({"success": False, "error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask app in debug mode for development purposes
    app.run(debug=True)
```
