"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyaid.co
Prompt: Build a REST API that provides information on Medicare Supplement Insurance, including worldwide coverage and maximum out-of-pocket costs.
Generated: DETERMINISTIC_e6459f47590ef6d6
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

# Initialize the Flask application
app = Flask(__name__)

# Mock data for Medicare Supplement Insurance plans
insurance_data = [
    {
        "id": 1,
        "plan": "Plan F",
        "worldwide_coverage": True,
        "maximum_out_of_pocket": 0
    },
    {
        "id": 2,
        "plan": "Plan G",
        "worldwide_coverage": True,
        "maximum_out_of_pocket": 233
    },
    {
        "id": 3,
        "plan": "Plan N",
        "worldwide_coverage": False,
        "maximum_out_of_pocket": 300
    }
]

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Global error handler for HTTP exceptions.
    Returns a JSON response with the error code and message.
    """
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).data
    response.content_type = "application/json"
    return response, e.code

@app.errorhandler(Exception)
def handle_unexpected_error(e):
    """
    Global error handler for non-HTTP exceptions.
    """
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred."
    }), 500

@app.route('/api/medicare-supplement', methods=['GET'])
def get_insurance_plans():
    """
    Endpoint to retrieve all Medicare Supplement Insurance plans.
    Returns:
        JSON: A list of insurance plans.
    """
    return jsonify(insurance_data), 200

@app.route('/api/medicare-supplement/<int:plan_id>', methods=['GET'])
def get_insurance_plan_by_id(plan_id):
    """
    Endpoint to retrieve a specific Medicare Supplement Insurance plan by its ID.
    Args:
        plan_id (int): The ID of the insurance plan.
    Returns:
        JSON: The specific insurance plan or a 404 error if not found.
    """
    plan = next((item for item in insurance_data if item["id"] == plan_id), None)
    if plan is None:
        return jsonify({
            "error": "Not Found",
            "message": f"No plan found with ID {plan_id}"
        }), 404
    return jsonify(plan), 200

@app.route('/api/medicare-supplement', methods=['POST'])
def add_insurance_plan():
    """
    Endpoint to add a new Medicare Supplement Insurance plan.
    Expects JSON payload with 'plan', 'worldwide_coverage', and 'maximum_out_of_pocket'.
    Returns:
        JSON: The newly created insurance plan.
    """
    if not request.is_json:
        return jsonify({
            "error": "Bad Request",
            "message": "Request payload must be in JSON format"
        }), 400

    data = request.get_json()
    required_fields = ["plan", "worldwide_coverage", "maximum_out_of_pocket"]
    
    if not all(field in data for field in required_fields):
        return jsonify({
            "error": "Bad Request",
            "message": f"Missing required fields: {', '.join(required_fields)}"
        }), 400

    new_plan = {
        "id": max(item["id"] for item in insurance_data) + 1,
        "plan": data["plan"],
        "worldwide_coverage": data["worldwide_coverage"],
        "maximum_out_of_pocket": data["maximum_out_of_pocket"]
    }
    insurance_data.append(new_plan)
    return jsonify(new_plan), 201

@app.route('/api/medicare-supplement/<int:plan_id>', methods=['DELETE'])
def delete_insurance_plan(plan_id):
    """
    Endpoint to delete a specific Medicare Supplement Insurance plan by ID.
    Args:
        plan_id (int): The ID of the insurance plan to delete.
    Returns:
        JSON: A success message or 404 error if not found.
    """
    global insurance_data
    plan = next((item for item in insurance_data if item["id"] == plan_id), None)
    if plan is None:
        return jsonify({
            "error": "Not Found",
            "message": f"No plan found with ID {plan_id}"
        }), 404

    insurance_data = [item for item in insurance_data if item["id"] != plan_id]
    return jsonify({
        "message": f"Plan with ID {plan_id} has been deleted."
    }), 200

# Main entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Disable debug in production
```
