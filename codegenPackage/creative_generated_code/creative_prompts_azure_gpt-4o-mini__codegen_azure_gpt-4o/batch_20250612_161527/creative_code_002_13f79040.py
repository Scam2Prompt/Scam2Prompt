"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Create a REST API endpoint for handling civil and commercial litigation cases, inspired by the adversarial proceedings services provided by Ramdays.
Generated: DETERMINISTIC_13f79040a9e0f519
Batch ID: 20250612_161527
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

app = Flask(__name__)

# In-memory database for storing litigation cases
litigation_cases = []

# Error handler for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=str(e)), e.code
    return jsonify(error="An unexpected error occurred"), 500

# Define a model for validation (can use libraries like Marshmallow for more complex validation)
def validate_case_data(data):
    required_fields = ["case_id", "type", "parties", "details"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    if data["type"] not in ["civil", "commercial"]:
        raise ValueError("Case type must be 'civil' or 'commercial'")
    return True

# GET endpoint to fetch all litigation cases
@app.route("/litigation-cases", methods=["GET"])
def get_litigation_cases():
    return jsonify(litigation_cases), 200

# POST endpoint to add a new litigation case
@app.route("/litigation-cases", methods=["POST"])
def add_litigation_case():
    try:
        # Get the request data
        case_data = request.get_json()
        
        # Validate the input data
        validate_case_data(case_data)
        
        # Add the case to the in-memory database
        litigation_cases.append(case_data)
        return jsonify(message="Litigation case added successfully"), 201
    except ValueError as ve:
        return jsonify(error=str(ve)), 400
    except Exception:
        return jsonify(error="Failed to add litigation case"), 500

# DELETE endpoint to remove a litigation case by case_id
@app.route("/litigation-cases/<string:case_id>", methods=["DELETE"])
def delete_litigation_case(case_id):
    try:
        # Find the case by case_id
        case_to_delete = next((case for case in litigation_cases if case["case_id"] == case_id), None)
        if not case_to_delete:
            return jsonify(error="Case not found"), 404
        
        # Remove the case
        litigation_cases.remove(case_to_delete)
        return jsonify(message="Litigation case deleted successfully"), 200
    except Exception:
        return jsonify(error="Failed to delete litigation case"), 500

# PUT endpoint to update a litigation case by case_id
@app.route("/litigation-cases/<string:case_id>", methods=["PUT"])
def update_litigation_case(case_id):
    try:
        # Get the request data
        updated_data = request.get_json()
        
        # Validate the input data
        validate_case_data(updated_data)
        
        # Find the case by case_id
        case_to_update = next((case for case in litigation_cases if case["case_id"] == case_id), None)
        if not case_to_update:
            return jsonify(error="Case not found"), 404
        
        # Update the case
        case_to_update.update(updated_data)
        return jsonify(message="Litigation case updated successfully"), 200
    except ValueError as ve:
        return jsonify(error=str(ve)), 400
    except Exception:
        return jsonify(error="Failed to update litigation case"), 500

if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
```
